import tkinter as tk
from tkinter import scrolledtext, messagebox
from transformers import pipeline, BartTokenizer
import threading

class SummarizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Orchid Hammer")  # GUI window name
        
        self.create_widgets()
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        self.tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")

    def create_widgets(self):
        # Configure the grid layout
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=0)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Create a scrolled text widget for text input
        self.input_text = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=50, height=10)
        self.input_text.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Create a button to trigger the summarize function
        self.summarize_button = tk.Button(self.root, text="Summarize", command=self.on_summarize_click)
        self.summarize_button.grid(row=1, column=0, pady=10)

        # Create a scrolled text widget to display the output
        self.output_text = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=50, height=10)
        self.output_text.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

    def on_summarize_click(self):
        input_text = self.input_text.get("1.0", tk.END).strip()
        if not input_text:
            messagebox.showwarning("Input Error", "Please enter some text to summarize.")
            return

        self.summarize_button.config(state=tk.DISABLED) # Disable the button to prevent multiple clicks
        threading.Thread(target=self.summarize_text, args=(input_text,)).start() # Run the summarization in a separate thread

    def summarize_text(self, text):
        try:
            chunks = self.split_text_into_chunks(text, max_length=1024)
            summaries = [self.summarizer(chunks, max_length=130, min_length=30, do_sample=False)[0]['summary_text'] for chunk in chunks]
            summary = " ".join(summaries)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, summary)
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            self.summarize_button.config(state=tk.NORMAL) # Reenable the button after summerisation finished

    def split_text_into_chunks(self, text, max_length=1024):
        tokens = self.tokenizer.encode(text)
        chunks = []
        for i in range(0, len(tokens), max_length):
            chunk = tokens[i:i+max_length]
            chunks.append(self.tokenizer.decode(chunk))
        return chunks

if __name__ == "__main__":
    root = tk.Tk()
    app = SummarizerApp(root)
    root.mainloop()