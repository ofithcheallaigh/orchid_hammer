import tkinter as tk
from tkinter import scrolledtext
from transformers import pipeline

"""
if there are torch issues, pip install torch==2.3.0 torchvision transformers seems to work,
after uninstalling torch
"""

# text = """America has changed dramatically during recent years. Not only has the number of 
#         graduates in traditional engineering disciplines such as mechanical, civil, 
#         electrical, chemical, and aeronautical engineering declined, but in most of 
#         the premier American universities engineering curricula now concentrate on 
#         and encourage largely the study of engineering science. As a result, there 
#         are declining offerings in engineering subjects dealing with infrastructure, 
#         the environment, and related issues, and greater concentration on high 
#         technology subjects, largely supporting increasingly complex scientific 
#         developments. While the latter is important, it should not be at the expense 
#         of more traditional engineering.

#         Rapidly developing economies such as China and India, as well as other 
#         industrial countries in Europe and Asia, continue to encourage and advance 
#         the teaching of engineering. Both China and India, respectively, graduate 
#         six and eight times as many traditional engineers as does the United States. 
#         Other industrial countries at minimum maintain their output, while America 
#         suffers an increasingly serious decline in the number of engineering graduates 
#         and a lack of well-educated engineers."""

# Assuming summerise_this is defined elsewhere in your code
def summerise_this(text):
    # BERT model pre-trained on English langaue and fine tuned on CNN/Daily Mail articles
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn") 
    result = summarizer(text,max_length=130, min_length=30, do_sample=False)
    # result = "This is a summary of: " + text
    return result

def on_summerise_click():
    input_text_content = input_text.get(1.0, tk.END).strip()
    result = summerise_this(input_text_content)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, result)

# Create the main application window
root = tk.Tk()
root.title("Orchid Hammer") # GUI window name

# Configure the grid layout
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)

# Create a scrolled text widget for text input
input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
input_text.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Create a button to trigger the summerise_this function
summerise_button = tk.Button(root, text="Summarize", command=on_summerise_click)
summerise_button.grid(row=1, column=0, pady=10)

# Create a scrolled text widget to display the output
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
output_text.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

# Run the main event loop
root.mainloop()