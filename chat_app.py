# file: chat_app.py

import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
from cryptography.fernet import Fernet
import socket
import threading
import os

# Generate a key for encryption
key = Fernet.generate_key()
cipher = Fernet(key)

class ChatApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Advanced Chat Application")

        # Login/Register screen
        self.login_screen()

    def login_screen(self):
        self.clear_screen()
        self.username_label = tk.Label(self.master, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.master)
        self.username_entry.pack()

        self.password_label = tk.Label(self.master, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.master, text="Login", command=self.login)
        self.login_button.pack()

        self.register_button = tk.Button(self.master, text="Register", command=self.register)
        self.register_button.pack()

    def clear_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            # Implement actual authentication logic here
            self.chat_screen()
        else:
            messagebox.showwarning("Login Failed", "Please enter both username and password")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            # Implement actual registration logic here
            self.chat_screen()
        else:
            messagebox.showwarning("Registration Failed", "Please enter both username and password")

    def chat_screen(self):
        self.clear_screen()
        self.chat_frame = tk.Frame(self.master)
        self.chat_frame.pack()

        self.chat_display = tk.Text(self.chat_frame, state='disabled', width=50, height=15)
        self.chat_display.pack()

        self.message_entry = tk.Entry(self.chat_frame, width=40)
        self.message_entry.pack(side='left')

        self.send_button = tk.Button(self.chat_frame, text="Send", command=self.send_message)
        self.send_button.pack(side='left')

        self.file_button = tk.Button(self.chat_frame, text="File", command=self.send_file)
        self.file_button.pack(side='left')

        self.emoji_button = tk.Button(self.chat_frame, text="Emoji", command=self.send_emoji)
        self.emoji_button.pack(side='left')

    def send_message(self):
        message = self.message_entry.get()
        if message:
            self.display_message("You: " + message)
            # Send the message to the server here
            self.message_entry.delete(0, tk.END)

    def send_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            # Implement file sending logic here
            self.display_message("You sent a file: " + os.path.basename(file_path))

    def send_emoji(self):
        # Implement emoji sending logic here
        self.display_message("You sent an emoji")

    def display_message(self, message):
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, message + "\n")
        self.chat_display.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
