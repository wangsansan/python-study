from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate(
 template="你是{name},你最喜欢{lover}",
    input_variables=["name", "lover"]
)

prompt_template1 = PromptTemplate.from_template(
    template="你是{name},你最喜欢{lover}"
)

prompt = prompt_template1.format(name="wcs",lover="nys")

print(prompt)