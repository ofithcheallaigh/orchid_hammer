from transformers import pipeline

def main():
    classifier = pipeline("zero-shot-classification")
    result = classifier("Keir Starmer is the PM in the UK",
                    candidate_labels=["education", "politics", "business"])

    print(result)


def generator():
    generator = pipeline("text-generation", model="gpt2")
    result = generator("In this course, we will teach you how to")

    print(result)


if __name__ == "__main__":
    # main()
    generator()