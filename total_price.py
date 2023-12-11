""" Task

 Ragu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.

Your task is to compute how much money  earned.

Input Format

The first line contains , the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains , the number of customers.
The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.

Output Format

Print the amount of money earned by Ragu.

Sample Input
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

Sample Output
200
"""



from collections import Counter
no=eval(input())
size=Counter([eval(i) for i in input().split(" ")])
users=eval(input())
profit=[j for i in range(users) for j in input().split(" ")]
s=0
for i in range(0,len(profit),2):
    lists=int(profit[i])
    prize=int(profit[i+1])
    if size[lists]: 
        # print(f"size is {lists} and no is {size[lists]}")                                              
        size[lists]-=1
        s=s+prize
    else:
        continue
print(s)


