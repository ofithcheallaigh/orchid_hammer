import torch
import torchvision
from transformers import pipeline

print(f"torch version: {torch.__version__}")
print(f"torchvision version: {torchvision.__version__}")

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
print(summarizer("This is a test summary."))

