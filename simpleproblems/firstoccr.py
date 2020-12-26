def firstoccr(s,x):
    startstr = 0
    substr = ''
    notsubstr = ''
    for str1 in x:
        if str1 in s and str1 != '*':
            substr += str1
        elif str1 == '*':
            startstr +=1
        else:
            notsubstr += str1

    print(f'substr = {substr} startstr {startstr} notsubstr {notsubstr}')
    if len(substr) + startstr == len(x):
        print("yes")

if __name__=="__main__":
    firstoccr('xabcdey','ab*de')