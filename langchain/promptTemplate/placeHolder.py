from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
import os

import langchain
from langchain_openai import ChatOpenAI
import dotenv

#加载配置文件.env，在gitignore里忽略掉
dotenv.load_dotenv()
print(langchain.__version__)

# 这些key配置在.env文件中
print(os.getenv("ALI_BASE_URL"))
print(os.getenv("ALI_API_KEY"))
os.environ["OPEN_BASE_URL"] = os.getenv("ALI_BASE_URL")
os.environ["OPENAI_API_KEY"] = os.getenv("ALI_API_KEY")

# 调用对话模型
# 阿里云百炼开发手册：https://help.aliyun.com/zh/model-studio/what-is-model-studio
chat_model = ChatOpenAI(
    model="qwen3.5-plus-2026-02-15",
    base_url=os.getenv("OPEN_BASE_URL")
)

template = ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant"),
        MessagesPlaceholder("history"),
        ("human","{question}")
    ]
)

prompt = template.format_messages(
    history=[HumanMessage("宁雅姝喜欢谁？"), AIMessage("宁雅姝喜欢王春生")],
    question="再问你一次，宁雅姝喜欢谁？"
)

print(prompt)

response = chat_model.invoke(prompt)
print(response)