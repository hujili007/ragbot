# GastroBot

This is the official codebase for **GastroBot**.

## Introduction

GastroBot is a RAG framework Chinese gastric disease chatbot. It uses 25 gastric disease-related guideline documents as a corpus, fine-tuned the embedding model, and is developed based on llama-index.
An overview of GastroBot architecture can be seen below:

<p align="center">
  <img src="https://github.com/hujili007/ragbot/blob/7424152b37ced2c0136dade4fa7d0e3a8a5463c8/Architecture.png" alt="GastroBot architecture diagram" border="0" width=70%>
</p>

## Getting Started

### Step 1 Installation

Set up conda environment and clone the github repo

```
# create a new environment
$ conda create --name rag python=3.10.13 -y
$ conda activate rag
# install requirements
$ pip install -r requirements.txt
```

### Step 2 Create index


Executing the code in the build_index.ipynb file will build the index locally. The built index is saved in the vector_index folder.


### Step 3 Run app.py

```
$ streamlit run app.py
```

### Step 4 Navigate to browser

Open the browser and enter the address http://127.0.0.1:port/ 
Start Q&A with it！

<p align="center">
  <img src="https://github.com/hujili007/ragbot/blob/7424152b37ced2c0136dade4fa7d0e3a8a5463c8/GastroBot.png" alt="GastroBot Q&A" border="0" width=40%>
</p>

## Acknowledgement

- llamaindex: [https://www.llamaindex.ai/](https://www.llamaindex.ai/)