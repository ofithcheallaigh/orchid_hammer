import transformers
from transformers import pipeline

def split_text(text, max_length):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        if len(' '.join(current_chunk + [word])) <= max_length:
            current_chunk.append(word)
        else:
            chunks.append(' '.join(current_chunk))
            current_chunk = [word]

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks

# Loading summarization pipeline and model
summarizer = pipeline('summarization', model = 'luisotorres/bart-finetuned-samsum')

# Example input text
text = """Research and Development (R&D) Tax Relief: Enhanced R&D intensive support for loss-making SMEs based in Northern Ireland

Find out if you can claim Enhanced R&D intensive support (ERIS) as a loss-making, small and medium enterprise (SME) based in Northern Ireland.

The Research and Development (R&D) Relief (Chapter 2 Relief) Regulations 2024 (‘the regulations’) make provision for loss-making, R&D intensive, small and medium enterprises (SMEs), with a registered office in Northern Ireland.

SMEs registered in Northern Ireland whose business activities involve no element of trade in goods, and no relevant activities in relation to electricity, can choose to opt out of these provisions by notifying HMRC.

Affected companies are not subject to the restrictions for relief on payments to overseas contractors or providers of externally provided workers, and will be able to claim enhanced R&D intensive support (ERIS), subject to a rolling 3-year limit. Above this limit, relief is available under the new merged scheme.

This guidance applies to you if:

you are a small and medium enterprise (SME) claiming ERIS
your registered office is in Northern Ireland
you have either:
a trade in goods, or a trade which involves relevant activities in relation to electricity
no trade in goods, and your trade does not involve relevant activities in relation to electricity, but you have not decided to opt out by notifying HMRC under paragraph (3)(b) of regulation 2
Who can opt out
If your business activities involve no element of trade in goods, and no relevant activities in relation to electricity, you can opt out by notifying HMRC in writing under paragraph (3)(b) of regulation 2. You can do this when you provide additional information to support your R&D claim. If you do this, the overseas restrictions will apply, but the limit on the amount of relief obtainable in a rolling 3-year period will not apply.

Overseas restrictions
For affected companies, the restrictions on relief for overseas spend on contracted out R&D and externally provided workers do not apply for the purposes of any claim under ERIS. The restrictions will apply for any residual amounts claimed under the merged scheme.

What a trade in goods is
You have a trade in goods if any of your business activities involves any element of trading in goods.

If you are not sure, you should proceed on the basis that you are trading in goods.

Relevant activities in relation to electricity
Relevant activities are the generation, transmission, distribution, supply, wholesale trading and cross-border exchange of electricity.

How much you can claim under ERIS
The limit applies to the net benefit of all claims made under ERIS over any period of 3 years, on a rolling basis (‘the relevant net benefit’). This must not exceed £250,000.

The net benefit amount for a given ERIS claim is the amount by which the benefit of the claim under ERIS exceeds the benefit of an equivalent claim for R&D expenditure credit (RDEC) under the merged scheme.

The net benefit for a given claim under ERIS for an accounting period is calculated using the following formula:

N = (A + B + C) – D

Where:

N is the net benefit amount
A is the amount by which the liability of the company to pay corporation tax (in any accounting period) is reduced as a result of the Chapter 2 relief obtained by the company for the period, for example by the use of losses arising as a result of the claim for a period against profits of another period
B is the sum of any amounts by which the liability of any other company to pay corporation tax (in any accounting period) is reduced by virtue of a loss that both:
(a) arises as a result of the Chapter 2 relief obtained by the company for the period
(b) is surrendered by the company to the other company under Part 5 or 5A of the Corporation Tax Act 2010 (surrender of relief between members of groups and consortia)
C is the amount of R&D tax credit to which the company is entitled, and which it claims, for the period
D is the net value of the RDEC that the company would have been entitled to had the expenditure in respect of which the company claims Chapter 2 relief instead been the subject of a claim for relief under Chapter 1A of Part 13 of CTA 2009 — this is defined as the third amount referred to in section 1042K of CTA 2009 (the initial amount of expenditure credit, minus the notional tax deduction)
To work out the relevant net benefit, add together:

the net benefit for the claim in the current accounting period
the net benefit amounts for ERIS claims, made in any previous accounting period of the company that began on or after 1 April 2024, and ended within the period of 3 years ending with the final day of the accounting period in question
The relevant net benefit must not exceed £250,000. Claims for ERIS that go over this limit are not allowed, and HMRC has the power to address any inaccuracies in tax returns. If you submit an inaccurate claim, you may become liable for tax-geared penalties.

Relief you can get for expenditure that that you cannot claim for under ERIS
You can claim RDEC for any additional qualifying R&D expenditure under the new merged scheme. Read more information about Research and Development (R&D) tax relief: the merged scheme and enhanced R&D intensive support.
"""

try:
    # Loading summarization pipeline and model
    summarizer = pipeline('summarization', model='luisotorres/bart-finetuned-samsum')
    print("Model loaded successfully.")

    # Split the text into chunks
    max_length = 1024  # Maximum sequence length for the model
    chunks = split_text(text, max_length)

    # Process each chunk with the model and concatenate the results
    generated_short_summary = []
    generated_medium_summary = []
    generated_long_summary = []

    for chunk in chunks:
        input_length = len(chunk.split())
        short_summary_chunk = summarizer(chunk, max_length=min(45, input_length))[0]['summary_text']
        medium_summary_chunk = summarizer(chunk, min_length=min(50, input_length), max_length=min(150, input_length))[0]['summary_text']
        long_summary_chunk = summarizer(chunk, min_length=min(100, input_length), max_length=min(200, input_length))[0]['summary_text']

        generated_short_summary.append(short_summary_chunk)
        generated_medium_summary.append(medium_summary_chunk)
        generated_long_summary.append(long_summary_chunk)

    # Join the summaries
    short_summary = " ".join(generated_short_summary)
    medium_summary = " ".join(generated_medium_summary)
    long_summary = " ".join(generated_long_summary)

    print(f"Short Summary:\n\n{short_summary}")
    print(f"Medium Summary:\n\n{medium_summary}")
    print(f"Long Summary:\n\n{long_summary}")

except Exception as e:
    print(f"An error occurred: {e}")