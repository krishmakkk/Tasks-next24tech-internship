import nltk
from nltk.chat.util import Chat, reflections
import tkinter as tk
from tkinter import scrolledtext, END

# Download the necessary NLTK data
nltk.download('punkt')

# Define patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", "Hi! How can I help you today?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by you. You can call me Chatbot!. What is your name?",]
    ],
    [
        r"how are you?",
        ["I'm doing good. How about you?", "I'm great! How can I assist you today?"]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "No problem", "Don't worry about it"]
    ],
    [
        r"I am fine|I am good|I am alright",
        ["Great to hear that!", "Awesome! How can I help you today?"]
    ],
    [
        r"what can you do?",
        ["I can chat with you and respond to your queries. Try asking me something!",]
    ],
    [
        r"how old are you?",
        ["I am just a few lines of code, so I don't have an age.",]
    ],
    [
        r"who created you?",
        ["I was created by a developer who loves coding!",]
    ],
    [
        r"quit|bye|sayonara",
        ["Bye! Take care.", "Goodbye! Have a great day!"]
    ],
]

# Reflections for better conversation
reflections = {
    "i am"       : "you are",
    "i was"      : "you were",
    "i"          : "you",
    "i'd"        : "you would",
    "i've"       : "you have",
    "i'll"       : "you will",
    "my"         : "your",
    "you are"    : "I am",
    "you were"   : "I was",
    "you've"     : "I have",
    "you'll"     : "I will",
    "your"       : "my",
    "yours"      : "mine",
    "you"        : "me",
    "me"         : "you"
}

class CustomChat(Chat):
    def respond(self, str):
        response = super().respond(str)
        if response:
            return response
        else:
            return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Create the chatbot
chat = CustomChat(pairs, reflections)

# GUI Application
class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        self.root.geometry("600x700")
        self.root.config(bg="#A1D8E6")

        self.create_widgets()

    def create_widgets(self):
        self.chat_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, bg="white", fg="black", font=("Helvetica", 12))
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.chat_area.config(state=tk.DISABLED)

        self.entry_frame = tk.Frame(self.root, bg="#ADD8E6")
        self.entry_frame.pack(padx=10, pady=10, fill=tk.X, expand=True)

        self.entry_box = tk.Entry(self.entry_frame, font=("Helvetica", 12), bg="white", fg="black")
        self.entry_box.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.entry_box.bind("<Return>", self.get_response)

        self.send_button = tk.Button(self.entry_frame, text="Send", command=self.get_response, font=("Helvetica", 12), bg="#4632B4", fg="white", activebackground="#4682B4", activeforeground="white", relief=tk.FLAT)
        self.send_button.pack(side=tk.RIGHT, padx=5)

        # Define text tags for alignment
        self.chat_area.tag_configure("user", justify='left', foreground="#0000FF")
        self.chat_area.tag_configure("bot", justify='right', foreground="#008000")

    def get_response(self, event=None):
        user_input = self.entry_box.get()
        self.display_message("You: " + user_input, "user")
        self.entry_box.delete(0, END)

        if user_input.lower() in ['quit', 'bye', 'sayonara']:
            self.root.quit()
        else:
            response = chat.respond(user_input)
            self.display_message("Chatbot: " + response, "bot")

    def display_message(self, message, tag):
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(END, message + "\n", tag)
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.yview(END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()
