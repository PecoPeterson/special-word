def get_unique_string(original_list):
    return ''.join(''.join(set(string)) for string, value in original_list)


def get_sorted_list(original_list):
    new_string = get_unique_string(original_list)
    char_count = Counter(new_string)
    return sorted(new_string, key=lambda x: char_count[x], reverse=True)

