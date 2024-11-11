'''
Parking Charges

Chef needs to park her car while she watches a movie. The parking charges at the theater are as follows:

    Rs. XX for the first 1 hour
    Rs. YY for every extra hour after the first hour

If Chef parks her car for HH hours, what is the total parking charges that she should pay?
Input Format

The only line of the input will contain three space separated integers - XX, YY, and HH.
Output Format

Output a single integer, which should be the total amount that Chef pays as parking charge.
Constraints

    1≤X≤100
    1≤Y≤100
    1≤H≤100

Sample 1:
Input
10 1 5
Output
14

Explanation:

X=10X=10, which means that for the first hour, Chef has to pay Rs. 10.
Y=1Y=1, which means that for every extra hour, Chef has to pay Rs. 1.
Chef needs to park for H=5H=5 hours.

So, for the first hour, she will pay Rs. 1010. And for the 5−1=45−1=4 hours extra, she will pay 4∗1=4∗1=Rs. 44. So in total, she has to pay 10+4=10+4= Rs. 1414.
Sample 2:
Input
1 10 100
Output
991

Explanation:

X=1X=1, which means that for the first hour, Chef has to pay Rs. 1.
Y=10Y=10, which means that for every extra hour, Chef has to pay Rs. 10.
Chef needs to park for H=100H=100 hours.

So, for the first hour, she will pay Rs. 11. And for the 100−1=99100−1=99 hours extra, she will pay 99∗10=99∗10=Rs. 990990. So in total, she has to pay 1+990=1+990= Rs. 991991.
Sample 3:
Input
10 15 1
Output
10

Explanation:

X=10X=10, which means that for the first hour, Chef has to pay Rs. 10.
Y=15Y=15, which means that for every extra hour, Chef has to pay Rs. 15.
Chef needs to park for H=1H=1 hours.

So, for the first hour, she will pay Rs. 1010. And she does not have to pay any more. So in total, she has to pay Rs. 1010.

'''

money_for_first_hour,money_for_every_extra_hour,time = input().split(" ")
time = int(time)
money_for_first_hour = int(money_for_first_hour)
money_for_every_extra_hour = int(money_for_every_extra_hour)
every_extra_hour = money_for_every_extra_hour * (time-1)
total = money_for_first_hour + every_extra_hour
print (f"Price for parking  = {total}")