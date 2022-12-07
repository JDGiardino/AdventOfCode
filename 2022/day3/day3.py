from string import ascii_lowercase, ascii_uppercase


def get_dict_key(character_numbers_dictionary: dict[int, str], character: str) -> int:
    for key, value in character_numbers_dictionary.items():
        if character == value:
            return key


def same_character_in_string(string1: str, string2: str) -> str:
    for character in string1:
        if character in string2:
            return character


def string_into_two(string: str) -> tuple[str, str]:
    string1 = string[:len(string) // 2]
    string2 = string[len(string) // 2:]
    return string1, string2


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
    total_numbers = 0
    for string in input_data:
        string1, string2 = string_into_two(string)
        character = same_character_in_string(string1, string2)
        number = get_dict_key(character_numbers_dictionary, character)
        total_numbers += number
    print(f"The sum of the priorities of items that appear in both compartments of each ruksack is {total_numbers}")


if __name__ == "__main__":
    main()
