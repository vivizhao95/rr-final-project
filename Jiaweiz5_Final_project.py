import csv
import re
"""
firstly, the file should be imported.
"""
open_file = open("Jiaweiz5_Final_text_file", "r")

"""
next step is to tidy the text file.
1. format all the sentences to '1. word; POS tagging - meaning; sentence of example.'
"""
read_file = open_file.read()
"""add new lines after full stop to format all the sections."""
new_line_before_num = read_file.replace(". ", ". \n").replace(".", ". \n")

#print(new_line_before_num)

"""delete all the new lines"""
lists_of_lines = new_line_before_num.split("\n")

clean_line_list = []

for line in lists_of_lines:
    clean_line = line.replace('\n', '')
    clean_line_list.append(clean_line)

for line in clean_line_list:
    if line == '' or line == ' ':
        del clean_line_list[clean_line_list.index(line)]

for title in clean_line_list:
    if "SAT" in title or "Sat" in title or "Vocabulary" in title:
        del clean_line_list[clean_line_list.index(title)]

#print(clean_line_list)

"""forming a regex to match a number and word"""

numRegex = re.compile(r'(\d)(\d*)?(\.)(\s*)?(\w*)')

matched_word_list = []

for groups in numRegex.findall(new_line_before_num):
    item = ''.join(groups)
    clean_string = item.replace('\n', '')
    matched_word_list.append(clean_string)

open_file.close()
#print(matched_word_list)

"""there are several \xa0\xa0\xa0 in the string generated, so next step is to delete them."""

clean_word = ""

for str_word in matched_word_list:
    new_matched_word = "".join(str_word.split())
    clean_word = clean_word+","+new_matched_word

clean_word_new = clean_word[1:]
#print(clean_word_new)

"""
since i want to get a whole list of words, i have to sequence all the numbers.
"""

count = 1
sequence_word = ""
split_word = clean_word_new.split(",")

for pair in split_word:
    word = pair[2:].replace(".", "")
    num_and_word = str(count)+'.' + word
    count = count + 1
    sequence_word = sequence_word + num_and_word + "\n"

sequence_word_list = sequence_word.split("\n")

for word in sequence_word_list:
    if word == '':
        del sequence_word_list[sequence_word_list.index(word)]


"""then, slicing different parts out."""

word_list = sequence_word_list
#print(len(word_list))
part_of_speech_list = []
meaning_list = []
eg_sentence_list = []

"""
define a new function using Regex to find all the digits with a single dot followed
because a line without '-' could also be the serial number.
"""


def has_numbers_or_not(input_string):
    return bool(re.search(r'\d+\.', input_string))


"""slicing different parts out."""


for lines in clean_line_list:

    if "-" in lines:
        index_end = lines.index("-")
        index_start = lines.index(";")
        part_of_speech = lines[index_start+1:index_end]
        meaning = lines[index_end + 1:]
        part_of_speech_list.append(part_of_speech)
        meaning_list.append(meaning)

    elif "-" not in lines and has_numbers_or_not(lines) == False and lines != '' and lines != '\u2028\xa0' and lines != '\xa0':
        eg_sentence_list.append(lines)

"""next step is to assign the keys"""

zipped = list(zip(part_of_speech_list, meaning_list, eg_sentence_list))
zipped_list = []

for tuples in zipped:
    list_up = list(tuples)
    zipped_list.append(list_up)

dict_of_whole = {}

for key in word_list:
    for value in zipped_list:
        dict_of_whole[key] = value
        zipped_list.remove(value)
        break

print(dict_of_whole)

out_file = csv.writer(open('Jiaweiz5_Final.csv', 'w', newline=""))

for key, val in dict_of_whole.items():
    for value in val:
        out_file.writerow([key, value])

