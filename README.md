# rr-final-project
this page is for the readme file of final project of IS452
author: Jiaweiz5

I would like to guide you to read through my final project, which is a project to convert a text file to a csv file.

Firstly, I would like to provide a brief description of my project. This project is to convert a text file, which contains 300 words for SAT exam, to a csv file with a clear format. The general idea is structured as follows: 1) clean the data and re-organize it so that I can process it easily, 2) extract different parts (in this text file, they are: words, part of speech, meaning and example sentences), 3) assign them to keys and values in dictionary, and 4) convert the dictionary to a csv file.

The breakdown interpretation will be given as follows.

1)	Import the text file.
Here, we use open() function to read the file into Python.

2)	Tidy the text file.
a.	Format all the sentences to '1. Word; POS tagging – meaning. sentence of example.'
b.	My purpose was to extract different parts out and combine them, so I chose to add new lines before all the full stops. (each part was separated by a ‘.’)
c.	In the list of lines that I got, there are still some empty lines. Therefore, I used for loop to delete all the empty lines. First step was to replace the newlines with empty strings. Next was to use if statement to check if the line is empty or not. Also, the title with string ‘SAT’ or ‘vocabulary’ should also be deleted, since I want a whole list of words instead of several lists of words.
3)	Extract the key, which is the serial number and the words follows, by using Regex to compile a word and number.
4)	Delete some redundant characters in the word list.
5)	Re-organize all the words by giving them new serial numbers.
6)	Slice different parts out.
a.	For the par of speech, we can first check whether character ‘-‘ is in lines or not. If the line has ‘-‘, then the part of speech would be start from ‘;’ and ends before the first appearance of a single dot. Although the indexed line may have two dots, the index function will return the position of the character’s first appearance. Also, the meaning part would be start from the first appearance of a single dot to the end of the line.
b.	For the example sentence, we can first select those lines without the appearance of a ‘-‘. However, as I add new lines before each single dot, the serial number would also be selected out. Hence, we can check the membership of numbers. Also, as numbers can also exist in example sentences, we use Regex again to only match ‘a digit and a single dot’, which is the format of the serial number.
7)	Assign key and value
a.	Zip all the values. This step is to make all the corresponding elements in three lists (part_of_speech_list, meaning_list and eg_sentence_list) into tuples.
8)	Write the dictionary out to a csv file.
