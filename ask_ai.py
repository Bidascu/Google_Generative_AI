# ---------------------------------------------------------------------------
#
# Title: Ask AI
# Date: 05/03/2025
# Version: 2.0
# Author: Bidascu Denis
#
# Purpose: This script is used to interact with the Google Generative AI API
#         to generate content based on user input.
#
# ---------------------------------------------------------------------------
import google.generativeai as genai

# Open the file
with open('./definitely_not_the_api_key.txt', 'r') as file:
    get_api = file.read()

# Configure the API key
genai.configure(api_key = get_api)

# Load the model
model = genai.GenerativeModel("gemini-2.0-flash-thinking-exp-1219")

# Start the chat
chat = model.start_chat()

# Print the welcome message
print("Welcome to the AI chat! Type 'exit' to quit the chat.\n")

# Start the chat loop
while True:
    # Get user input
    user_input = input("Write a message: ")

    # Generate content based on the user input
    response = chat.send_message(user_input)

    # Print the response
    print(response.text)

    # Break the loop if the response is empty
    if user_input.lower() == 'exit':
        print("Goodbye, Old Friend. May the Force Be With You.")
        break
