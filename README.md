# GastroBot

This is the official codebase for **GastroBot**.

## Introduction

GastroBot is a RAG framework Chinese gastric disease chatbot. It uses 25 gastric disease-related guideline documents as a corpus, fine-tuned the embedding model, and is developed based on llama-index.

## Getting Started

### step 1 Installation

Set up conda environment and clone the github repo

```
# create a new environment
$ conda create --name rag python=3.10.13 -y
$ conda activate rag
# install requirements
$ pip install -r requirements.txt
```

### step 2 Create index


Executing the code in the build_index.ipynb file will build the index locally. The built index is saved in the vector_index folder.


### step 3 Run app.py

```
$ streamlit run app.py
```

## Acknowledgement

- llamaindex: [https://www.llamaindex.ai/](https://www.llamaindex.ai/)