'''
lengthOfLongestSubstring without any duplicate char
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
'''
def length_of_longest_substring(input_str):
    '''
    input - string
    output - length of longest substring
    '''
    tmp_list = []
    key_list = []
    for key, value in enumerate(input_str):
        if key == 0:
            longest_word = value
            longest_length = 1
        elif value in longest_word:
            key_list.append(longest_length)
            tmp_list.append(longest_word)
            longest_word = value
            longest_length = 1
        else:
            longest_length += 1
            longest_word += value
    key_list.sort()
    return key_list[-1]
if __name__ == "__main__":
    test1 = length_of_longest_substring('bbbbbb') # 1, b
    test2 = length_of_longest_substring('abcabcbb') #abc , 3
    test4 = length_of_longest_substring('pwwkew') #wke, 3
    if test1 == 1 and test2 == 3 and test4 == 3:
        print("all test cases pased")
    else:
        print("test cases failed")
