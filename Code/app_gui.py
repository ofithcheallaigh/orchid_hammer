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

        # Disable the button to prevent multiple clicks
        self.summarize_button.config(state=tk.DISABLED)
        # Run the summarization in a separate thread
        threading.Thread(target=self.summarize_text, args=(input_text,)).start()

    def summarize_text(self, text):
        try:
            chunks = self.split_text_into_chunks(text, max_length=1024)
            summaries = []
            for i, chunk in enumerate(chunks):
                try:
                    print(f"Processing chunk {i+1}/{len(chunks)}: {chunk[:50]}...")  # Debugging statement
                    # Adjust max_length based on the input length
                    input_length = len(self.tokenizer.encode(chunk))
                    max_length = min(130, input_length - 1)
                    if input_length < 30:  # Skip very short chunks
                        print(f"Skipping chunk {i+1} due to short length: {input_length} tokens")
                        continue
                    result = self.summarizer(chunk, max_length=max_length, min_length=30, do_sample=False)
                    print(f"Result for chunk {i+1}: {result}")  # Debugging statement
                    if result and len(result) > 0:
                        summaries.append(result[0]['summary_text'])
                    else:
                        messagebox.showwarning("Summarization Error", f"No summary could be generated from chunk {i+1}.")
                except Exception as e:
                    print(f"Error processing chunk {i+1}: {e}")  # Debugging statement
                    messagebox.showerror("Summarization Error", f"Error processing chunk {i+1}: {e}")
            summary = " ".join(summaries)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, summary)
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            self.summarize_button.config(state=tk.NORMAL)  # Re-enable the button after summarization is finished

    def split_text_into_chunks(self, text, max_length=1024):
        tokens = self.tokenizer.encode(text)
        chunks = []
        for i in range(0, len(tokens), max_length):
            chunk = tokens[i:i + max_length]
            decoded_chunk = self.tokenizer.decode(chunk)
            print(f"Chunk {len(chunks)+1} length: {len(chunk)} tokens")  # Debugging statement
            print(f"Chunk {len(chunks)+1} content: {decoded_chunk[:50]}...")  # Debugging statement
            chunks.append(decoded_chunk)
        print(f"Total chunks created: {len(chunks)}")  # Debugging statement
        return chunks

if __name__ == "__main__":
    root = tk.Tk()
    app = SummarizerApp(root)
    root.mainloop()