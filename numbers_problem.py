'''
list of all number related problems
'''
def is_power_of_10(input_number):
    '''
    function is check that given number is power of 10.
    '''
    if input_number >= 10:
        while True:
            return bool(input_number % 2)
        input_number = input_number/10
    return False

def is_palindrome(input_number):
    '''
    to check if given number is palindrome
    '''
    if str(input_number) == str(input_number)[::-1]:
        return True
    return False

def medians_of_two_sortedarray(arr1, arr2):
    '''
    return median of two sorted arrays
    '''
    sorted_arr = arr1 + arr2
    sorted_arr.sort()
    print(sorted_arr)
    len_arr = int(len(sorted_arr))
    if len_arr <= 1:
        median = sorted_arr[0]
    elif len_arr %2 == 0:
        print("insideif")
        median = (sorted_arr[int(len_arr/2)-1] + sorted_arr[int(len_arr/2)])/2
    else:
        median = sorted_arr[len_arr-1/2]
    print(median)
    return median



if __name__ == '__main__':
    #test cases for power 10
    TEST1 = is_power_of_10(100)
    TEST2 = is_power_of_10(10000)
    TEST3 = is_power_of_10(101)
    if TEST1  and TEST2 and not TEST3:
        print("All test cases passed for is power of 10")
    else:
        print("test cases failed for is power of 10")
    #test case of palindrome number
    TEST1 = is_palindrome(100)
    TEST2 = is_palindrome(10000)
    TEST3 = is_palindrome(101)
    if not TEST1 and not TEST2 and TEST3:
        print("All test cases passed for palindrome")
    else:
        print("test cases failed for palindrome")
    #Test cases for median for two sorted array
    TEST1 = medians_of_two_sortedarray([1, 2, 3], [1, 4, 5])
    TEST2 = medians_of_two_sortedarray([0, 0, 0], [0, 0, 0])
    TEST3 = medians_of_two_sortedarray([2], [])
    if TEST1 == 2.5 and TEST2 == 0 and TEST3 == 2:
        print("test cases passed for median")
    else:
        print("test cases failed for median")
