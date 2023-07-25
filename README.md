# PDF Chatbot

PDF Chatbot allows users to upload PDF files and use natural language processing (NLP) to train the chatbot with those files and answer users´ question or requests about the uploaded files.

## Description

PDF Chatbot works by receiving one or more PDF files by the user and train itself from those files to answer questions or requests from the user. When the user uploads 

The chatbot usesOpenAI NLP capabilities to train the chatbot with the PDF files that the user uploads. Therefore, the user must provide a OpenAI API to use the chatbot. 

## Use the chatbot on the website (no downloads, dependencies or installations needed)

In order to use the chatbot on the website, the user can go to the following link:

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




