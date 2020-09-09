'''
    - for any given string , find longest uniform substring
    - return starting index and length
'''
def find_longest_substring(input_str):
    '''
        find longest substring
        pylnit result - Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
    '''
    temp_list = []
    full_list = []
    input1 = enumerate(input_str)
    print(list(input1))
    for i, value in enumerate(input_str):
        if i == 0:
            temp_list = [0, 1]
        if i >= 1 and input_str[i] == input_str[i-1]:
            temp_list = [temp_list[0], temp_list[1]+1]
        elif i >= 1 and input_str[i] != input_str[i-1]:
            full_list = [temp_list]
            temp_list = [i, 1]
            longest_substring = []
    enumlist = enumerate(full_list)
    print(list(enumlist))
    for key, value in enumerate(full_list):

        print(full_list)
        print(key)
        if key == 0:
            longest_substring = value
        elif longest_substring[1] > value[1]:
            longest_substring = value
        elif longest_substring[1] >= value[1]:
            longest_substring = longest_substring.append(value)
    print(longest_substring)
    return longest_substring

if __name__ == "__main__":
    if find_longest_substring("aabbbcc") == [2, 3]:
        print("testpassed")
