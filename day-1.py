text = open('day-1-input.txt', 'r')
setup = text.readlines()
answer = 0
inp = []
out = []

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



for i, value in enumerate(inp):
    end = len(inp)-1
    try:
        int_value = int(value)
    except ValueError:
        out.append(answer)
        answer = 0
    else:
        answer = answer+value
    if(i == end):
        out.append(answer)
        answer = 0

answer = max(out)
print(answer)