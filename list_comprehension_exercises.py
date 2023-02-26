from typing import List


def all_numbers_form_one_to_thousand_divisible_by_seven() -> List[int]:
    original_list = list(range(1, 1001))
    return [number for number in original_list if number % 7 == 0]


def all_numbers_form_one_to_thousand_with_three_in_them() -> List[int]:
    original_list = list(range(1, 1001))
    return [number for number in original_list if "3" in str(number)]


def count_the_number_of_spaces_in_string(sentence: str) -> int:
    return len([character for character in sentence if character == " "])


def list_all_consonants_in_sentence(sentence: str) -> List[chr]:
    return list([letter for letter in sentence if letter not in "aeiouAEIOU "])
