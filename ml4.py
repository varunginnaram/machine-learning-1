def highest_alphabet_occurrence(input_string):
    char_count_dict = {}
    for character in input_string:
        if character.isalpha():
            char_count_dict[character] = char_count_dict.get(character, 0) + 1
    max_character = max(char_count_dict, key=char_count_dict.get)
    max_occurrence = char_count_dict[max_character]
 
    return max_character, max_occurrence
 
input_string = "hippopotamus"
result_char, result_count = highest_alphabet_occurrence(input_string)
print(f"The highest occurring character is '{result_char}' with occurrence count {result_count}.")
