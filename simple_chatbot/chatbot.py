def chatbot_with_if_elif():
    """
    A simple chatbot implementation using an if-elif-else structure.
    """
    print("Chatbot: Hello! I am a simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print("Chatbot: Hi!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: I don't understand that.")
if __name__ == "__main__":
    chatbot_with_if_elif()
    
    
    
    # def chatbot():
#     """
#     A simple, rule-based chatbot that responds to user input.
#     """
#     print("Chatbot: Hello! I am a simple chatbot. Type 'bye' to exit.")

#     # Use a dictionary for responses for better scalability
#     responses = {
#         "hello": "Chatbot: Hi!",
#         "how are you": "Chatbot: I'm fine, thanks!",
#         "default": "Chatbot: I don't understand that."
#     }

#     while True:
#         # Get user input and clean it up by converting to lowercase and removing whitespace
#         user_input = input("You: ").lower().strip()

#         if user_input == "bye":
#             print("Chatbot: Goodbye!")
#             break  # exit the loop

#         # Use dict.get() to provide a response, falling back to the default
#         response = responses.get(user_input, responses["default"])
#         print(response)

# # Run the chatbot only when the script is executed directly
# if __name__ == "__main__":
#     chatbot()

