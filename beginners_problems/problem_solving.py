'''
In the new CodeChef Learn module, under the "Learn Problem Solving" section, there are two courses for each language. For eg. "Python Beginner - Part 1" and "Python Beginner - Part 2". These courses help you get started with CodeChef contests.

Currently there are courses for 4 languages, and hence there are 8 courses in this section. But suppose there are courses for NN languages, what will be the total number of courses in this section?
Input Format

The only line of input will contain a single integer NN, denoting the number of languages for which there are courses.
Output Format

Output on a single line the total number of courses in the section.
Constraints

    1≤N≤100

Input : 
4
Output :
8

Input : 
9
Output :
18
'''
# c = input()
# print(int(c)*2)


'''
Chef has recently started learning from the new CodeChef SQL course.

He has a table which initially has RR rows and CC columns. He then adds EE extra rows to it. How many total cells does he have finally?
Input Format

The only line in the input contains three space-separated integers RR, CC, and EE — the number of initial rows, the number of columns, and the number of extra rows added, respectively.
Output Format

Output on a new line, a single integer, which should be the final total number of cells in the table.
Constraints

    1≤R≤100
    1≤E≤100
    1≤C≤100

Sample 1:
Input
5 2 1
Output
12

Explanation:

There are initially 55 rows, and 22 columns. So the initial number of cells was 5∗2=105∗2=10. Then, 11 extra row was added. So now the table has 66 rows, and 22 columns. So the total number of cells is now 6∗2=126∗2=12, which is the answer.
Sample 2:
Input
6 10 3
Output
90

Explanation:

There are initially 66 rows, and 1010 columns. So the initial number of cells was 6∗10=606∗10=60. Then, 33 extra rows were added. So now the table has 99 rows, and 1010 columns. So the total number of cells is now 9∗10=909∗10=90, which is the answer.
Sample 3:
Input
1 1 1 
Output
2

Explanation:

There are initially 11 rows, and 11 columns. So the initial number of cells was 1∗1=11∗1=1. Then, 11 extra row was added. So now the table has 22 rows, and 11 columns. So the total number of cells is now 2∗1=22∗1=2, which is the answer.
Sample 4:
Input
100 100 100
Output
20000

Explanation:

There are initially 100100 rows, and 100100 columns. So the initial number of cells was 100∗100=10000100∗100=10000. Then, 100100 extra rows were added. So now the table has 200200 rows, and 100100 columns. So the total number of cells is now 200∗100=20000200∗100=20000, which is the answer.
'''
'''
r = NUMBER OF INITIAL ROWS IN A TABLE
c = NUMBER OF COLUMNS IN A TABLE
e = nUMBER OF ROWS ADDED IN A TABLE
'''
r,c,e = input().split(" ")
r = int(r)
c = int(c)
e = int(e)
if (r <=100 and r>0) and (c <=100 and c>0) and (e <=100 and e>0):
    total_number_of_rows_in_a_table = (r * c) + (e * c)
    print(total_number_of_rows_in_a_table)
else:
    print("")
