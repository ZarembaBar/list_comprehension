def all_numbers_form_one_to_thousand_divisible_by_seven():
    original_list = list(range(1, 1001))
    return [number for number in original_list if number % 7 == 0]


def all_numbers_form_one_to_thousand_with_three_in_them():
    original_list = list(range(1, 1001))
    return [number for number in original_list if "3" in str(number)]


def count_the_number_of_spaces_in_string(sentence: str) -> int:
    return len([space for space in sentence if space == " "])


