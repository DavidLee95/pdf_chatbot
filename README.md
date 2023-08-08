<a>
    <img src="images/logo.png" alt="PDF Chatbot Logo" title="Logo" align="right" height="40" />
</a>

# PDF Chatbot

## Introduction

PDF Chatbot is a Python application that seeks to facilitate the interaction between humans and PDF files by allowing users to upload the PDF files and to ask question or requests about them to a chatbot. The application uses the PDFs provided by the user to train a chatbot that will answer the users´s queries using natural language processing (NLP).

<div align="center">
    <img src="images/main_page.png" alt="PDF Chatbot Logo" width="900" />
</div>

## Description

First of all, PDF Chatbot makes use of the "Streamlit" library to design the user interface. Streamlit´s simple yet powerful tools were very helpful for this specific task. The user can easily locate the places where he or she would place the OpenAI Key, upload the PDF files, and ask and receive questions with the chatbot.

As to the logic of the application, the following are the steps taken by the application:

<div align="center">
    <img src="images/description.png" alt="PDF Chatbot Logo" width="900" />
</div>

1. The user uploads one or more PDF files.

2. The contents of the uploaded PDF files are extracted into one single huge text and later divided into smaller chunks of text that will be analyzed in the next step. The main reasons why smaller chunks of text are preferred over one single huge text is due to computational efficiency, memory limitations, and batch processing.

3. The chunks of text are then converted to embeddings, which are numerical representations of words in the form of vectors or arrays that contain the meaning and context of the words. Through these embeddings, the program can identify which words are the most relevant to a particular query that the user writes. Therefore, the process of converting the chunks of text to embeddings allows the bot to generate quick and coherent answers to a particular question or comment, and all these embeddings are stored in a vector store that is a type of database. In this particular application, the embeddings and the vector store in use are **OpenAI´s embeddings** and **FAISS**.

4. Once the embeddings are stored, the Langchain framework will be used to build the chatbot. In simple terms, Langchain allows users to add different components such as prompts, data, agents or memory in order to create more robust and personalized Large Language Models (LLMs) from existing ones. In this particular application, the base LLM will be **OpenAI´s LLM**, the data will be the PDFs that were embedded in vector stores, and the memory will save the "chat history". 

5. The chatbot is now ready! Whenever the user writes a query, the chatbot will search in the vector store the embeddings that relate the most to the user´s query, and the LLM will do the job of answering the user in the most coherent manner possible based on the results. As stated on step 4, the chatbot will remember the conversation to give answers based on previous queries and results as well.

## Use the chatbot on the website (no downloads, dependencies, or installations needed, but can be slower tha running it locally)

In order to use the chatbot on the website, the user can go to the following link: 
[CLICK HERE TO GO TO THE CHATBOT WEBSITE!](https://pdf-chatbot-iowz.onrender.com)

The steps to use it are the following:

1. Provide a OpenAI API
2. Upload the PDF files to be analyzed and click on "PROCESS"
3. You are ready to go! You can now ask questions or request information about the PDF files to the chatbot.

## Use the chatbot locally by running the program

In order to use the chatbot locally, you can do the following: 

1. Clone this repository to your local machine.
2. Install the required libraries through the following command:

```bash
pip install -r requirements.txt
```

3. Run the program through the command: "streamlit run app.py"
4. Wait for the program to open locally on your web browser.
5. Provide a OpenAI API
6. Upload the PDF files to be analyzed and click on "PROCESS"
7. You are ready to go! You can now ask questions or request information about the PDF files to the chatbot.

## License

This project under the terms of the [MIT license](https://opensource.org/license/mit/)



