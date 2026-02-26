def get_response(user_input):
    if user_input.lower() == "bye":
        return "Goodbye! :wave:"
    return "I'm Branch 2 AI bot."

def main():
    print("ChatBot v2 - Branch 2 AI")
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()