AI Study Buddy — Chat with your own notes/PDFs
Upload any PDF — a textbook chapter, lecture notes, anything — and ask it questions in plain English. It reads the document and answers from it. This is called a RAG (Retrieval Augmented Generation) app and it's the most hired-for LLM skill right now.



How you'll build it
1
Learn Python basics + install libraries using pip (you're doing this now)
2
Get a free OpenAI API key — they give free credits to start
3
Use LangChain to load a PDF and split it into small chunks
4
Store chunks in FAISS — a free vector database that runs on your laptop
5
When user asks a question, find the relevant chunks and send them to GPT
6
Build a simple chat UI with Streamlit — takes about 10 lines of code
7
Deploy free on Streamlit Cloud and share the live link on your resume
Why this gets you hired: RAG is the dominant pattern for real production LLM apps right now. Very few beginner candidates have built one end-to-end — having it on your resume is a genuine differentiator that hiring managers notice.