'''
Chef and Instant Noodles

Chef has invented 11-minute Instant Noodles. As the name suggests, each packet takes exactly 11 minute to cook.

Chef's restaurant has XX stoves and only 11 packet can be cooked in a single stove at any minute.

How many customers can Chef serve in YY minutes if each customer orders exactly 11 packet of noodles?
Input Format

    The first and only line of input contains two space-separated integers XX and YY — the number of stoves and the number of minutes, respectively.

Output Format

    Print a single integer, the maximum number of customers Chef can serve in YY minutes

Constraints

    1≤X≤Y≤1000

Sample 1:
Input:
3 7
Output:
21
'''
a,b = input().split()
a=int(a)
b=int(b)
print(a*b)
