import os

# Import a text file filled with a paragraph of your choosing.
first_paragraph_txt = "raw_data/paragraph_1.txt"
second_paragraph_txt = "raw_data/paragraph_2.txt"

# Assess the passage for each of the following:
with open(first_paragraph_txt, 'r'):

#   Approximate word count
    firstparagraph_word_count = 0
    for row in first_paragraph_txt:
        firstparagraph_word_count += 1
    
#   Approximate sentence count
    firstparagraph_sentence_count = 0

#   Approximate letter count (per word)

#   Average sentence length (in words)

