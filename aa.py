def flatten_and_set(original_list):
    result = [set(x[0]) for x in original_list]
    return "".join([str(elem) for sublist in result for elem in sublist])

original_list = [("head", 4), ("dead", 4), ("lead", 4)]
result = flatten_and_set(original_list)
print(result)