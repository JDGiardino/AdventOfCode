from string import ascii_lowercase, ascii_uppercase


def get_dict_key(character_numbers_dictionary: dict[int, str], character: str) -> int:
    for key, value in character_numbers_dictionary.items():
        if character == value:
            return key


def same_character_in_strings(string1: str, string2: str, string3: str) -> str:
    for character in string1:
        if character in string2 and character in string3:  # Nested loops are bad.
            return character


def string_list_into_3(list_of_strings: list) -> tuple[str, str, str]:
    return list_of_strings[0], list_of_strings[1], list_of_strings[2]


def character_numbers() -> dict[int, str]:
    character_numbers_dictionary = {}
    number = 1
    all_characters = ascii_lowercase + ascii_uppercase  # These are special strings that include every character
    for character in all_characters:
        character_numbers_dictionary.update({number: character})
        number += 1
    return character_numbers_dictionary


def main():
    input_data = open("input.txt", "r")
    character_numbers_dictionary = character_numbers()
    string_groups_of_3 = []
    temp_group = []
    for line in input_data:
        temp_group.append(line)
        if len(temp_group) >= 3:
            string_groups_of_3.append(temp_group)
            temp_group = []

    total_numbers = 0
    for list_of_strings in string_groups_of_3:
        string1, string2, string3 = string_list_into_3(list_of_strings)
        string = same_character_in_strings(string1, string2, string3)
        number = get_dict_key(character_numbers_dictionary, string)
        total_numbers += number

    print(f"{total_numbers}")


if __name__ == "__main__":
    main()
