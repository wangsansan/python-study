import os

import langchain
from langchain_openai import ChatOpenAI
import dotenv

#加载配置文件.env，在gitignore里忽略掉
dotenv.load_dotenv()
print(langchain.__version__)

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

# 调用模型
response = chat_model.invoke("宁雅姝喜欢王春生，那么宁雅姝喜欢谁呢？")

#执行时间较长
print(response.content)