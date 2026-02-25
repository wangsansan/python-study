from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder, \
    FewShotChatMessagePromptTemplate
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

# 定义一个example
examples = [
    {"input":"x喜欢y", "output":"y喜欢x"},
    {"input":"a喜欢b", "output":"b喜欢a"}
]

# 定义example的提示词
examples_template = ChatPromptTemplate.from_messages([
    ("human","{input}"),
    ("ai","{output}")
])

# 根据example和example的提示词构建FewShotChatMessagePromptTemplate，也就是让ai学习的东西
examples_prompt = FewShotChatMessagePromptTemplate(
    examples = examples,
    example_prompt=examples_template
)

final_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是一个逻辑奇才"),
        examples_prompt,
        ("human","{input}")
    ]
)

response = chat_model.invoke(final_template.invoke(input={"input","王春生喜欢宁雅姝"}))

print(response.content)

