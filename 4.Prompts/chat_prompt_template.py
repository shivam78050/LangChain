from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} assistant.'),
    ('human', 'Can you explain {topic} to me?'),
])

prompt = template.invoke({
    'domain': 'math',
    'topic': 'calculus'})

print(prompt)