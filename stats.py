def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    # Create an empty dictionary to store the character counts
    char_counts = {}

    # Iterate through each character in the input text
    for char in text:

        # Convert the character to lowercase to avoid duplicates (e.g., 'A' and 'a')
        lower_char = char.lower()

        # If the character is already in our dictionary, increment its count
        if lower_char in char_counts:
            char_counts[lower_char] += 1

        # If it's a new character, add it to the dictionary with a count of 1
        else:
            char_counts[lower_char] = 1

    # Return the dictionary containing all the character counts
    return char_counts

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for char in num_chars_dict:
        sorted_list.append({"char": char, "num": num_chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
