# Домашнее задание к лекции «Открытие и чтение файла, запись в файл»
# Задача 3

from pprint import pprint
import os
from glob import glob


def sorted_files():
    list_of_files = list(glob(os.path.join(os.getcwd(), '*.txt')))
    total_file = []
    for file in (list_of_files):
        file_name = os.path.basename(file)
        with open(file_name) as file_obj:
            lines = file_obj.readlines()
            list_for_file_name = [file_name, len(lines), lines]
            total_file.append(list_for_file_name)
    sorted_total_file = sorted(total_file, key = lambda total_file: total_file[1])
    return sorted_total_file

pprint(sorted_files())