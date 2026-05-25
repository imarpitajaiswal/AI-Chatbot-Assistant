import time

# --- CHATBOT LOGIC ---
def get_response(user_input):
    user_input = user_input.lower()
    
    # Simple Intent-Classification Pipeline
    if "hello" in user_input or "hi" in user_input:
        return "Hello! I am your AI assistant. How can I help you today?"
    elif "how are you" in user_input:
        return "I'm functioning at optimal capacity. Ready to assist you!"
    elif "help" in user_input:
        return "I can assist with task automation, data processing, and general queries."
    elif "bye" in user_input:
        return "Goodbye! Have a productive day."
    else:
        return "I'm still learning. Could you rephrase your query?"

# --- MAIN INTERFACE ---
def main():
    print("AI Chatbot Initialized. (Type 'bye' to exit)")
    
    while True:
        user_input = input("You: ")
        
        # Simulate processing time for a "smart" feel
        print("Processing...", end="\r")
        time.sleep(0.5) 
        
        response = get_response(user_input)
        print(f"Bot: {response}")
        
        if "bye" in user_input.lower():
            break

if __name__ == "__main__":
    main()
