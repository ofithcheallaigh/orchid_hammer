from transformers import pipeline

classifier = pipeline("zero-shot-classification")
result = classifier("Keir Starmer is the PM in the UK",
                candidate_labels=["education", "politics", "business"])

print(result)