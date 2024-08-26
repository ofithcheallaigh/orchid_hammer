from transformers import pipeline
# import torch

# def print_torch():
#     print(torch.__version__)

def main():
    classifier = pipeline("zero-shot-classification")
    result = classifier("Keir Starmer is the PM in the UK",
                    candidate_labels=["education", "politics", "business"])

    print(result)
    # return result


def generator():
    generator = pipeline("text-generation", model="gpt2")
    result = generator("In this course, we will teach you how to")

    print(result)
    # return result

def generator_distilpgt2():
    generator = pipeline("text-generation", model="distilgpt2")
    result = generator("In this course, we will teach you how to", 
              max_length=30,
              num_return_sequences=2
              )
    
    print(result)
    # return result

def mask_fill():
    unmasker = pipeline("fill-mask")
    result = unmasker("This course will teach you all about <mask> models.", top_k=2) # top_k controls the number of sequences to be displayed

    print(result)
    return result

def name_entity_recognition():
    ner = pipeline("ner", grouped_entities=True)
    result = ner("My name is Seán Ó Fithcheallaigh and I work at Sensata in Antrim and Belfast.")
    print(result)

    return result

def question_and_answer():
    question_answerer = pipeline("question-answering")
    result = question_answerer(
        question="Am I old?",
        context="My name is Seán and I work at Sensata in Antrim. I am very old, and very sore.",
        )
    print(result)
    return result

def summerise_this():
    summarizer = pipeline("summarization")
    result = summarizer(
        """
        America has changed dramatically during recent years. Not only has the number of 
        graduates in traditional engineering disciplines such as mechanical, civil, 
        electrical, chemical, and aeronautical engineering declined, but in most of 
        the premier American universities engineering curricula now concentrate on 
        and encourage largely the study of engineering science. As a result, there 
        are declining offerings in engineering subjects dealing with infrastructure, 
        the environment, and related issues, and greater concentration on high 
        technology subjects, largely supporting increasingly complex scientific 
        developments. While the latter is important, it should not be at the expense 
        of more traditional engineering.

        Rapidly developing economies such as China and India, as well as other 
        industrial countries in Europe and Asia, continue to encourage and advance 
        the teaching of engineering. Both China and India, respectively, graduate 
        six and eight times as many traditional engineers as does the United States. 
        Other industrial countries at minimum maintain their output, while America 
        suffers an increasingly serious decline in the number of engineering graduates 
        and a lack of well-educated engineers.
    """
    )
    print(result)
    return result

if __name__ == "__main__":
    # main()
    # generator()
    # generator_distilpgt2()
    # mask_fill()
    # print_torch()
    # name_entity_recognition()
    # question_and_answer()
    summerise_this()