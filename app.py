import os
from typing import Any
from llama_index.query_engine import RetrieverQueryEngine
import openai
import streamlit as st
from llama_index import StorageContext, load_index_from_storage
from llama_index.embeddings import resolve_embed_model
from llama_index.llms import OpenAI
from llama_index import ServiceContext


openai.api_key = "sk-Ibjy7xLl6mUjx04YF0097b2496Ac4384B56f04014903557f"
openai.api_base = "https://openkey.cloud/v1"

@st.cache_resource(show_spinner=False)  # type: ignore[misc]
def load_index() -> Any:
    """从磁盘加载持久化索引,构建查询引擎"""

    print("Loading index...")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    index_path = os.path.join(base_dir, "vector_index")
    # 指定本地嵌入模型路径
    local_embed_model_path = "./embed_model"
    # 解析本地嵌入模型
    embed_model = resolve_embed_model(f"local:{local_embed_model_path}")
    llm = OpenAI(model="gpt-3.5-turbo")
    service_context = ServiceContext.from_defaults(
        llm=llm, embed_model=embed_model
    )
    # 构建 storage context
    storage_context = StorageContext.from_defaults(persist_dir=index_path)
    # 从磁盘加载 index
    index = load_index_from_storage(storage_context,service_context=service_context)
    print("Index loading completed!")
    #构建查询引擎
    base_retriever = index.as_retriever(similarity_top_k=3)
    query_engine = RetrieverQueryEngine.from_args(base_retriever, service_context=service_context)
    print("The query engine has been built!")
    return query_engine


def main() -> None:
    """运行 GastroBot"""
    
    if "query_engine" not in st.session_state:
        st.session_state.query_engine = load_index()

    st.title("GastroBot")
    if "messages" not in st.session_state:
        system_prompt = (
            "Your purpose is to answer questions about specific documents only. "
            "Please answer the user's questions based on what you know about the document. "
            "If the question is outside scope of the document, please politely decline. "
            "If you don't know the answer, say `I don't know`. "
        )
        st.session_state.messages = [{"role": "system", "content": system_prompt}]

    for message in st.session_state.messages:
        if message["role"] not in ["user", "assistant"]:
            continue
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            print("正在调用查询引擎API...")
            response = st.session_state.query_engine.query(prompt)
            full_response = f"{response}"
            print(full_response)
            message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})


if __name__ == "__main__":
    main()