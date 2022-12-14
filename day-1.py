# begin of day 1

# setting up all variables and lists
text = open('day-1-input.txt', 'r')
setup = text.readlines()
inp = []
out = []
answer = 0

# string to int conversion for all the numbers 
for line in setup:
        try:
            int_value = int(line)
        except ValueError:
            if line[-1] == '\n':
                inp.append(line[:-1])
            else:
                inp.append(line)
        else:
            if line[-1] == '\n':
                inp.append(int(line[:-1]))
            else:
                inp.append(int(line))

# the math part, if it detexts a string in the list it means that that elf is not carrying anymore calories and so the total amount is stored and the math starts over
def math(inp, out, answer):
    counter = 0

    for i, value in enumerate(inp):
        end = len(inp)-1
        try:
            int_value = int(value)
        except ValueError:
            out.append(answer)
            answer = 0
            counter = 0
        else:
            counter = counter+1
            answer = answer+value
        if(i == end):
            out.append(answer)
            answer = 0
            counter = 0
    
    #answer for day 1 part 1
    final = max(out)
    print("the answer day 1, part 1 = ", final)  

math(inp, out, answer)


# begin part 2

# getting the top 3 by sorting the list in ascending order and pulling the last 3 out
out.sort()
first = max(out)
second = max(out[:-1])
third = max(out[:-2])

# standard math to get the answer of part 2
final = first+second+third
print("the answer day 1, part 2 = ", final)  