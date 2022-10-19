"""
Refactoring for homework 3
"""

import re  # Import module re for regular expressions use

text_sample = """homEwork:

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each 
  existING SENtence and add it to the END OF this Paragraph. 

 

  it iZ misspeLLing here. fix “iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I 
  got 87."""


def splitting_sentences(input_text: str) -> list:
    """Split string into separate sentences, using regex"""
    split_sentences = re.findall(r'([A-Za-z][^.!?:]*[.!?:]\s*)', input_text)
    return split_sentences


def create_new_sentence(input_text: str, sentences_list: list) -> list:
    """Find the last word of each sentence and create new sentence"""
    last_words = re.findall(r'[^\s]*[.]', input_text)
    new_sentence = [x[:-1] for x in last_words]
    sentences_list.append(' ')
    sentences_list.append(f"I've got last words from each sentence: {', '.join(new_sentence)}.")
    return sentences_list


def normalize_text(list_of_sentences: list) -> str:
    """Normalize text from letters point of view and join all sentences in one text"""
    normalized_text = [i.capitalize() for i in list_of_sentences]
    joined_text = ''.join(normalized_text)
    return joined_text


def replace_text(input_text: str, wrong_text: str, correct_text: str) -> str:
    """Replace misspelled text"""
    fixed_text = input_text.replace(wrong_text, correct_text)
    return fixed_text


def total_spaces(final_text: str):
    """Count whitespaces in final text"""
    num_spaces = 0
    for items in final_text:
        if items.isspace():
            num_spaces = num_spaces + 1
    return num_spaces


def main(text: str) -> str:
    """Call all previous functions"""
    split_step = splitting_sentences(text)
    new_sentence_step = create_new_sentence(text, split_step)
    normalize_step = normalize_text(new_sentence_step)
    fix_text_step = replace_text(normalize_step, ' iz ', ' is ')
    final_step = f'{fix_text_step} Total amount of spaces - {total_spaces(fix_text_step)}.'
    return final_step

