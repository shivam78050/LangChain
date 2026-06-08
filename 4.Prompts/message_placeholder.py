from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

template = ChatPromptTemplate([
    ('system', 'You are a helpful assistant.'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])
chat_history = []
with open('/Users/shivam/LangChain-1/4.Prompts/chat_history.txt', 'r') as f:
    chat_history.extend(f.readlines())
prompt = template.invoke({
    'chat_history': chat_history,
    'query': 'What is the capital of France?'
})

print(prompt)