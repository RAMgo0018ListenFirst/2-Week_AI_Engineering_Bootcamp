from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1" #This is the HuggingFace model repository ID 
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("who are you ? ")

print(response.content)#
#This uses the api key from the environment variable HUGGINGFACEHUB_API_TOKEN, you can set it in your .env file or export it in your terminal.