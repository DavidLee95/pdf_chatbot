import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI

# Function to read the PDF´s text
def get_pdf_text(pdf_docs):
    text = ''
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Function split the PDF text into small groups
def split_text(raw_text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
        )
    chunks = text_splitter.split_text(raw_text)
    return chunks

# Function to embed the text
def get_vectorstore(text_chunks, api_key):
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    vectorstore = FAISS.from_texts(text_chunks, embedding=embeddings)
    return vectorstore

# Train the bot with the PDF information
def get_conversation_chain(vectorstore, api_key):
    llm = ChatOpenAI(openai_api_key=api_key)
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm = llm,
        retriever = vectorstore.as_retriever(),
        memory = memory
    )
    return conversation_chain

# Input question and receive output
def handle_userinput(question):
    response = st.session_state.information({'question': f"According to the provided context, {question}"})
    st.session_state.chat_history = response['chat_history']
    return st.session_state.chat_history

# Disable chat box
def disable_chat():
    st.session_state["chat_box"] = True

# Enable chat box
def enable_chat():
    st.session_state["chat_box"] = False

# Main function
def main():

    #Setup page
    st.set_page_config(page_title="PDF Chatbot", page_icon=":robot_face:")

    # Initialize session states
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    if "information" not in st.session_state:
        st.session_state.information = None
    if "conversations" not in st.session_state:
        st.session_state["conversations"] = [{"role": "assistant", "content": "What questions do you have regarding your PDF documents?"}]
    if "chat_box" not in st.session_state:
        st.session_state["chat_box"] = True

    # Setup sidebar
    with st.sidebar:
        # Brief instructions
        space = st.container()
        space.write('<p style="font-weight:bold;">Instructions:<br>1. Place your OPEN AI API key below<br>2. Upload your PDFs and click on "Process"<br>3. You are ready, enjoy the bot :)</p>', unsafe_allow_html=True)
        
        # Add OPENAI API key
        openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
        
        # Add PDF files
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload your PDFs here and click on Process", type="pdf", accept_multiple_files=True)

        if st.button("Process"):
            
            # Stop if the user did not add the OPENAI API key
            if not openai_api_key:
                st.warning('Please add your OpenAI API key to continue.', icon="⚠️")
                st.stop()
            elif not pdf_docs:
                st.warning('Please add upload a PDF document to continue.', icon="⚠️")
                st.stop()
            else:
                with st.spinner("Processing"):
                    # Get the pdf text
                    raw_text = get_pdf_text(pdf_docs)

                    # Get the text chunks
                    text_chunks = split_text(raw_text)

                    # Create vector store
                    vectorstore = get_vectorstore(text_chunks, openai_api_key)

                    # Create conversation chain
                    st.session_state.information = get_conversation_chain(vectorstore, openai_api_key) 

                    # Enable chat
                    enable_chat()

    # Setup streamlit main/center screen
    st.title("PDF Chatbot 💬")
    
    # Display the first message
    for msg in st.session_state.conversations:
        st.chat_message(msg["role"]).write(msg["content"])
    
    # Action to perform after asking the question
    if question := st.chat_input("Write your question or comments here", disabled=st.session_state.chat_box, on_submit=disable_chat):
        
        # Display a warning message if OpenAI's API key is not registered
        if not openai_api_key:
            st.warning('Please add your OpenAI API key to continue.', icon="⚠️")
            st.stop()
        
        # Display a warning message if the PDF file was not processed
        if st.session_state.information is None:
            st.warning('Please process the PDF file to continue.', icon="⚠️")
            st.stop()
        
        # Append the user's question to the conversation
        st.session_state.conversations.append({"role": "user", "content": question})
        # Display the user's question
        st.chat_message("user").write(question)
        # Wait for the bot's response
        with st.spinner("Processing"):
            # Ask for the question's answer
            response = handle_userinput(question)
            # Always get the most recent result
            msg = response[-1].content
            # Append the chatbot's reply to the conversation
            st.session_state.conversations.append({"role": "assistant", "content": msg})
            # Display the chatbot's reply
            st.chat_message("assistant").write(msg)
        
        # Enable chat
        enable_chat()
        st.experimental_rerun()
    
if __name__ == '__main__':
    main()