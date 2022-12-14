inp = [int(x) for x in input("insert your int: ").split()]
print(inp)
elf = 1
answer = 0
"""
for i, value in enumerate(inp):
    end = len(inp)-19 
    try:
        int_value = int(value)
    except ValueError:
        print("elf ", elf," is carrying ->", answer, " calories")
        elf = elf+1
        answer = 0
    else:
        answer = answer+value
    if(i == end):
        print("elf ", elf," is carrying ->", answer, " calories")
        elf = elf+1
        answer = 0
"""