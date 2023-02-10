def all_numbers_form_0ne_to_thousand_divisible_by_seven():
    original_list = list(range(1, 1001))
    return [number for number in original_list if number % 7 == 0]
