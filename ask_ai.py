# ---------------------------------------------------------------------------
#
# Title: Ask AI
# Date: 05/03/2025
# Version: 1.0
# Author: Bidascu Denis
#
# Purpose: This script is used to interact with the Google Generative AI API
#         to generate content based on user input.
#
# ---------------------------------------------------------------------------
import google.generativeai as genai

# Open the file
with open('./definetly_not_the_api_key.txt', 'r') as file:
    get_api = file.read()

# Configure the API key
genai.configure(api_key = get_api)

# Get user input
user_input = input("Write a message: ")

# Load the model
model = genai.GenerativeModel("gemini-2.0-flash-thinking-exp-1219")

# Generate content based on the user input
response = model.generate_content(user_input)

# Print the response
print(response.text)
