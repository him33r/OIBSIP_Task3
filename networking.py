# Add the networking part in chat_app.py
import socket
import threading
import tkinter as tk
from cryptography import cipher

class ChatApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Advanced Chat Application")

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(("127.0.0.1", 9999))

        # Login/Register screen
        self.login_screen()

    # Add this method to handle incoming messages
    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                self.display_message(message)
            except:
                print("An error occurred!")
                self.client_socket.close()
                break

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

        threading.Thread(target=self.receive_messages).start()

    def send_message(self):
        message = self.message_entry.get()
        if message:
            self.display_message("You: " + message)
            encrypted_message = cipher.encrypt(message.encode('utf-8'))
            self.client_socket.send(encrypted_message)
            self.message_entry.delete(0, tk.END)
