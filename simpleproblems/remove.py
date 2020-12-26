
'''
Task
You have a non-empty set , and you have to execute  commands given in  lines.
The commands will be pop, remove and discard.
Input Format
The first line contains integer , the number of elements in the set . 
The second line contains  space separated elements of set . All of the elements are non-negative integers, less than or equal to 9. 
The third line contains integer , the number of commands.
The next  lines contains either pop, remove and/or discard commands followed by their associated value.
Constraints
 

Output Format
Print the sum of the elements of set  on a single line.
Sample Input
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5
Sample Output
4
'''

n = int(input())
s = set(map(int,input().split()))

cmd_count = int(input())

for i in range(1,cmd_count+1):
    eval('s.{0}({1})'.format(*input().split()+[' ']))
print("{}".format(sum(s)))
