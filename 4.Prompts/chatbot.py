from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
chat_history = [
    SystemMessage(content='You are a helpful assistant')
]
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Exiting the chatbot. Goodbye!")
        break
    chat_history.append(HumanMessage(content=user_input))
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print(f"Chatbot: {result.content}")
print("Chat history:")
for msg in chat_history:
    print(f"{msg.__class__.__name__}: {msg.content}")