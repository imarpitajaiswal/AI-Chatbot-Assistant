# A simple AI Chatbot structure
def get_bot_response(user_input):
    # This is a placeholder for your AI logic (e.g., calling an OpenAI API)
    response = f"I received your message: {user_input}. How can I assist you further?"
    return response

if __name__ == "__main__":
    print("Chatbot initialized. Type 'exit' to quit.")
    while True:
        user_msg = input("You: ")
        if user_msg.lower() == 'exit':
            break
        print("Bot:", get_bot_response(user_msg))
