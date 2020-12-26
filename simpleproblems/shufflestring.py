'''
string related problems
'''
def shuffle_string(input_str, input_indices):
    '''
    inputs - one string and 2nd one is list of indices of string
    shuffle input string in order to given indices
    '''
    output_list = list(i for i in range(0, len(input_str)))
    output_str = ''
    input_str = list(input_str)
    for key, value in enumerate(input_indices):
        output_list[value] = input_str[key]
    return output_str.join(output_list)
if __name__ == "__main__":
    TEST1 = shuffle_string('codeleet', [4, 5, 6, 7, 0, 2, 1, 3])
    print(f'test {TEST1}')
    if TEST1 == "leetcode":
        print("testcases passed")
    