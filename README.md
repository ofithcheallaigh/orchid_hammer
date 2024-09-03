# Introduction
## Updates

**Update 6: 2 September 2024**
- Running 750 words into the app did produce an output, but also a lot of errors. This is done on the fix-text-size-issue branch

**Update 5: 31 August 2024**
- Updated GUI to use threading to try and stop it freezing
- Found and issue where too much text can be added to the GUI, this causes an error. I have added an issue to the project to investigate this (Issue [#2](https://github.com/ofithcheallaigh/orchid_hammer/issues/2)).

**Update 4: 28 August 2024**
- Initial GUI developed, which will take text and summerise it. Text can be placed in a text box within the GUI.
- Some tests showed the on smaller amounts of text, the summerisation was essentially just a repeat of the text provided -- this needs inbestigated
- Update the summerisation pipleline to `summarizer = pipeline("summarization", model="facebook/bart-large-cnn")`, this is an English-language dataset containing just over 300k unique news articles as written by journalists at CNN and the Daily Mail

**Update 3: 20 August 2024**
- Updated information and code related to the zero-shot classification.
- Created and updated text generation section, added text generation code.

**Update 2: 19 August 2024**
- More information added to the [Wiki](https://github.com/ofithcheallaigh/orchid_hammer/wiki).
- Code folder added, with a small `main.py` file which includes a very simple pipeline for zero-shot classification.

**Update 1: 30 July 2024**     
- Please see the [Wiki](https://github.com/ofithcheallaigh/orchid_hammer/wiki) section of this Repo for some information on this project.



