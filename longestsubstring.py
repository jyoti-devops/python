def FindLongestSubstring(input_str):
    temp_list = []
    full_list = []
    for i in range(len(input_str)):
        if i == 0:
           temp_list = [0,1]
        if i >= 1 and input_str[i] == input_str[i-1]:
            temp_list = [temp_list[0],temp_list[1]+1]
        elif i >=1 and input_str[i] != input_str[i-1]:
            full_list = [temp_list]
            temp_list = [i,1]
    find_longest_substring = []
    for i in range(len(full_list)):
        print(full_list)
        print(i)
        if i == 0:
            find_longest_substring = full_list[i]
        elif find_longest_substring[1] > full_list[i][1]:
            find_longest_substring = full_list[i]
        elif find_longest_substring[1] >= full_list[i][1]:
            find_longest_substring = find_longest_substring.append(full_list[i])


    print(find_longest_substring)
    return find_longest_substring

if __name__=="__main__":
    if FindLongestSubstring("aabbbcc") == [2,3]:
         print("testpassed")    
