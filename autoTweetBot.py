import tweetBot
import tkinter as tk
from tkinter import messagebox
import threading
from tkinter import END
import os, datetime
from tkinter import *
#BUG: Emojis dont work. 
"""TODO: 

Media attachments
    Create function to upload attachme
Include quote tweets/tweet replies.
    Fetch most recent tweet, and select it to quote / tweet 

Include selective tweeting (everyone, et c). 

Caching to load browser faster. 
    No easy solutions

GPT Suggestions - Future Scope: 
Hashtag suggestions via autocomplete
"""

#GUI initialiser
def send_tweet_gui():
    global tweet_message 
    tweet_message = message.get("1.0", tk.END).strip()
    if tweet_message:
        try:
            tweet_message_thread = threading.Thread(target=send_tweet, args=(tweet_message,))
            tweet_message_thread.start()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to post tweet: {e}")
    else:
        messagebox.showwarning("Input Error", "Please enter a message to tweet.")

def send_tweet(*args): 
    global tweet_message
    tweetBot.login_send_tweet(args)
    message.delete('1.0', END)

#Func to write drafts to local file
def write_drafts():
    try: 
        content = message.get('1.0', END).strip()
        if content: 
            with open('C:/Users/Vaibhav/Desktop/python/Projects_AutomateBoringStuff/tweet_drafts.txt', 'a') as text_file:
                text_file.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n{content}\n\n")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to write to file: {e}")

#Counting num chars
def char_count(event=None):
    tweet_counter = message.get('1.0', tk.END)
    if tweet_counter.endswith('\n'):
        tweet_counter = tweet_counter[:-1]
    chars = len(tweet_counter)
    char_count_label.config(text=f'Character count: {chars}')
    if chars >= 280:
        char_count_label.config(text=f'You are {chars-280} characters over the limit.')
        submit_button.config(state='disabled')
    else:
        submit_button.config(state='active')
    message.edit_modified(False)  # Clear the modified flag

#Saves drafts and destroys root
def on_closing():
    root.after(0, write_drafts())
    root.destroy()

#Opens drafts that are saved locally 
def open_drafts():
    try: 
        with open('C:/Users/Vaibhav/Desktop/python/Projects_AutomateBoringStuff/tweet_drafts.txt', 'r') as text_file:
            content = text_file.read()
        message.delete('1.0', END)
        message.insert(tk.END, content)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open file: {e}")

# Main UI 
root = tk.Tk()
root.title("Tweet Poster")
root.attributes('-topmost', True)
root.update()
root.attributes('-topmost', False)
# Create a frame for the Text widget and scrollbar
frame = tk.Frame(root)
frame.pack(expand=True, fill='both')

# Create a label
label = tk.Label(root, text="Enter your tweet:")
label.pack(pady=10)

# Create a text entry widget
message = tk.Text(frame, width=55, height=20, wrap=tk.WORD, font=('Microsoft YaHei', 12), undo=True)
message.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

# Create a scrollbar widget
scrollbar = tk.Scrollbar(frame, orient='vertical', command=message.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Link the Text widget to the Scrollbar
message.config(yscrollcommand=scrollbar.set)

# Create buttons
submit_button = tk.Button(root, text="Tweet", command=send_tweet_gui)
submit_button.pack(side=LEFT, padx= 15)
draft_button = tk.Button(root, text='Drafts', command=open_drafts)
draft_button.pack(side=LEFT, padx= 5, pady=10)

# Create a label to display the character count
char_count_label = tk.Label(root, text="Character count: 0", anchor='e')
char_count_label.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)

# Bind the <<Modified>> event to the char_count function
message.bind("<<Modified>>", char_count)

# Initial call to update character count
char_count()

root.protocol("WM_DELETE_WINDOW", on_closing)
# Run the Tkinter event loop
root.mainloop()
