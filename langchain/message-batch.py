import os

import langchain
from langchain_core.messages import SystemMessage, HumanMessage
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
    base_url=os.getenv("OPEN_BASE_URL"),
    streaming=True
)

messages = [SystemMessage(content="wcs喜欢nys"), HumanMessage(content="那么，推测一下，nys喜欢谁?")]

# 调用模型
response = chat_model.batch([messages])

print(response)