
# Open and format the input a little bit
nums = open('arith.txt').read().split('\n')

# Store the working input here
rows = []

# Fill a new list with sublists, finish creating the working variable
for i in nums:
    rows.append(i.split(' '))

# Feed this a list of 3 part lists
def progression(n):
    # Build list in this variable
    ans = []
    for i in n:
        # One part for each variable
        a = int(i[0])
        d = int(i[1])
        n = int(i[2])

        s_n = (n/2)*(2*a + (n-1)*d)
        # Fill the returning list while the loop runs
        ans.append(int(s_n))
    # Return when the loop completes
    return ans


print(progression(rows))
