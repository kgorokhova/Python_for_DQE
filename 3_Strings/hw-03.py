import re  # Import module re for regular expressions use

initial_text = """homEwork:

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each 
  existING SENtence and add it to the END OF this Paragraph. 

 

  it iZ misspeLLing here. fix “iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I 
  got 87."""

# Split string into separate sentences, using regex
split_sentences = re.findall(r'([A-Za-z][^.!?:]*[.!?:]\s*)', initial_text)

#  Find the last word of each sentence
last_words = re.findall(r'[^\s]*[.]', initial_text)

# Create new sentence and put it after third index
new_sentence = [x[:-1] for x in last_words]
split_sentences.insert(4, f"I've got 8 last words from each sentence: {', '.join(new_sentence)}. \n\n \n\n  ")

# Normalize text from letters point of view
normalized_text = [i[0:].capitalize() for i in split_sentences]

# Join all sentences in one text
joined_text = ''.join(normalized_text)

# Replace misspelled "iz" with correct "is" and check the final result
final_text = joined_text.replace(' iz ', ' is ')
print(final_text)

# Count whitespaces in initial and final text, print the results
initial_spaces = 0
for a in initial_text:
    if a.isspace():
        initial_spaces = initial_spaces+1

final_spaces = 0
for b in final_text:
    if b.isspace():
        final_spaces = final_spaces+1
print(f' \n\n\n  Initial text spaces - {initial_spaces}, final text spaces - {final_spaces}')
