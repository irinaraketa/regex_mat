import os
import re

DIR = os.path.dirname(os.path.abspath(__file__))
PATH_DATA = f"{DIR}/data/mat.txt"

def replace_word(word):
# Замена мата на *    
    return word[0] +re.sub('[а-яА-Я]', '*', word[1:len(word)-1]) + \
           word[-1]

def move_punctuation_marks(result, start_search):
# Убираем знаки пунктуации    
    while message_for_search[start_search] == ' ':
        result += message[start_search]
        start_search +=1
    return [start_search, result]

message = input('Введите сообщение: ')
message_for_search = re.sub(r"[,.!?:;-]", " ", message) + ' '
with open(PATH_DATA, "r", encoding='utf-8') as file_mat:
    mat = [letter for letter in file_mat]  # массив матерных слов
start_search = 0  # начало поиска
result = ''  # сообщение после цензуры
while start_search < len(message):
    array_temp = move_punctuation_marks(result, start_search)
    start_search = array_temp[0]
    result = array_temp[1]
    end_word = message_for_search.index(' ', start_search)  # конечный символ слова
    word = message_for_search[start_search:end_word]
    for letter in mat:
        if letter.strip() in word.lower():
            word = replace_word(word)
            break
    result += word
    start_search = end_word
print(result)
