# ---------------------------------------------------------------------------
#
# Title: Chat with Gemini
# Date: 07/03/2025
# Version: 1.0
# Author: Bidascu Denis
#
# Purpose: This script is used to interact with the Google Generative AI API
#         using a GUI to ask questions to the AI model.
#
# Command to run: python: path/to/ChatWithGemini.py
#
# ---------------------------------------------------------------------------
from tkinter import *
from tkinter import filedialog
import pandas as pd
import google.generativeai as genai

# ==================== Initialize chat with Gemini ===========================
# Open the file
with open('./definitely_not_the_api_key.txt', 'r') as file:
    get_api = file.read()

# Configure the API key
genai.configure(api_key = get_api)

# Load the model
model = genai.GenerativeModel("gemini-2.0-flash-thinking-exp-1219")

# Start the chat
chat = model.start_chat()
# ============================================================================


# ==================== GUI for Chat with Gemini ===============================
# Create window
window = Tk()
window.title('Chat with Gemini')
window.geometry("1000x300")
window.config(background="#FFFFFF")

# Function to print Input Text
def askGemini():
    inp = inputtext.get(1.0, "end-1c")
    if inp != "":
        response = chat.send_message(inp)
        print(response.text)
        respondText.insert(END, response.text)

# Create Label "Start chatting with Gemini!"
textBoxLabel = Label(window, text = "Start chatting with Gemini!",
                     font = ("Arial", 20),
                     bg = "white")

# Create Label "Gemini's Response"
textBoxLabel_response = Label(window, text = "Gemini's Response:",
                     font = ("Arial", 20),
                     bg = "white")

# Creating Text Box for Input
inputtext = Text(window,
                height = 5,
                width = 100,
                bg = "white")

# Creating Button
askButton = Button(window,
                     text = 'Ask Gemini',
                     command = askGemini)

# Text Box for Response
respondText = Text(window,
                height = 5,
                width = 100,
                bg = "white")

# Pack all elements
textBoxLabel.pack()
inputtext.pack()
askButton.pack()
textBoxLabel_response.pack()
respondText.pack()

# ============================================================================

# Run GUI
window.mainloop()



