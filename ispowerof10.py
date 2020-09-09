def ispowerof10(x):
    '''
    function is check that given number is power of 10.
    '''
    if x >=10:
        while(True):
            if x % 10 == 0:
                print(f"power of 10 {x}")
                return True
            else:
                print(f"power of 10 {x}")
                return False
        x = x/10

if __name__=='__main__':
    ispowerof10(100)