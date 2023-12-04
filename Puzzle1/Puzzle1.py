# %%
with open('./input1.txt') as file:
    input_lines = [line.strip() for line in file]

myvals = int(0)

for line in input_lines:
    tempval = [x for x in line if x.isdigit()]
    firstVal = tempval[0]
    lastVal = tempval[-1]
    concat = firstVal+lastVal
    retval = int(concat)
    myvals = myvals + retval
    # myvals.append(retval)


# %%
