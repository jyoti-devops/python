list1 = [1,2,3,4,5]
def find_2nd_smallest(list1):
    largest = list1[0]
    lowest =  list1[0]
    largest2 = None
    lowest2 = None
    for item in list1[1:]:
        if item > largest:
            largest2 = largest
            largest = item
        elif largest2 == None or item > largest2:
             largest2 = item
        elif item < lowest:
             lowest2 = lowest
             lowest  = item
        elif lowest2 == None or item < lowest2:
             lowest2 = item

    print(largest, largest2, lowest , lowest2)
#print(find_2nd_smallest([1,2,3,4,5]))


def find2nd_largest(list1):
    lg = list1[0]
    lg2 = list1[0]
    for item in list1[1:]:
        if item > lg:
            lg = item
    for item in list1[1:]:
        if item != lg and item > lg2:
            lg2 = item

    print('largest-{},largest2-{}'.format(lg,lg2))

print(find2nd_largest([-1,-2,-3,-4.5,6.0]))

def find2nd_smallest(list1):
    sm = list1[0]
    sm2 = None
    print(len(list1))
    for item in list1[1:]:
        if item < sm:
            sm = item
            #print(sm)
    for item in list1:
        if item < sm2 or  sm2==None and sm != item:
            sm2 = item
    print('smallest {}, 2nd smallest{}'.format(sm,sm2))

#print(find2nd_smallest([2,4.8,3,4,5,]))
#print(find2nd_smallest([1]))
def find_1stnonchar(s):
    orders = []
    counts = {}
    for x in s:
        if x in counts:
            counts[x]=counts[x]+1
            #print('2nd',x)
            #print(counts,'counts')
        else:
            counts[x]=1
            orders.append(x)
            #print('1st',x)
            #print('counts','counts')
    print(orders,'orders')
    i = 0
    for x in orders:
        if counts[x] == 1:
            i+=1
        if i ==2:
            return x
            print('x',x)


##print(find_1stnonchar('abcabcde'))

def apache_log(logs1):

    #print(logs1, "logs1")
    iplist = {}
    for line in logs1:
        #print(line,"line")
        #print("st",st)
        ip =  line.split()[0]
        print(ip, "ip")
        if ip in iplist :
            iplist[ip]  += 1
        else:
            iplist[ip] = 1
    ip_count = iplist.values()
    ips = iplist.keys()
    print(iplist.values())
    print(iplist.keys())
    print(max(ip_count))
    #print(ips.index(max(ip_count)))

    return ips[ip_count.index(max(ip_count))]

lines= ["10.10.10.10 - testing1 testing3 testing4 testing5",
                 "10.10.10.10 - TESTING",
                 "10.10.10.9 ---- LAST ONE"]
print(apache_log(lines))




