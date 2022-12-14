
# setting up everything
text = open('day-2-input.txt', 'r')
setup = text.readlines()
inp = []
out = []
points = 0


for line in setup:
    try:
    
        if line[-1] == '\n':
            inp.append(line[:-1])
        else:
            inp.append(line)
    finally:
        pass

# math for day 2 part 1
def math(inp, points):
    
    for i, value in enumerate(inp):
        end = len(inp)-1
        if(i != end):
                if value.__contains__("A"):
                    if value.__contains__("X"): # draw:3 + 1(rock)
                        points = points+4
                    elif value.__contains__("Y"): # win:6 + 2(paper)
                        points = points+8
                    elif value.__contains__("Z"): # loss:0 + 3(sissors)
                        points = points+3
                elif value.__contains__("B"):
                    if value.__contains__("X"): # loss:0 + 1(rock)
                        points = points+1
                    elif value.__contains__("Y"): # draw:3 + 2(paper)
                        points = points+5
                    elif value.__contains__("Z"): # win:6 + 3(sissors)
                        points = points+9
                elif value.__contains__("C"):
                    if value.__contains__("X"): # win:6 + 1(rock)
                        points = points+7
                    elif value.__contains__("Y"): # loss:0 + 2(paper)
                        points = points+2
                    elif value.__contains__("Z"): # draw:3 + 3(sissors)
                        points = points+6
        else:
            pass
        if(i == end):
            if value.__contains__("A"):
                if value.__contains__("X"): # draw:3 + 1(rock)
                    points = points+4
                elif value.__contains__("Y"): # win:6 + 2(paper)
                    points = points+8
                elif value.__contains__("Z"): # loss:0 + 3(sissors)
                    points = points+3
            elif value.__contains__("B"):
                if value.__contains__("X"): # loss:0 + 1(rock)
                    points = points+1
                elif value.__contains__("Y"): # draw:3 + 2(paper)
                    points = points+5
                elif value.__contains__("Z"): # win:6 + 3(sissors)
                    points = points+9
            elif value.__contains__("C"):
                if value.__contains__("X"): # win:6 + 1(rock)
                    points = points+7
                elif value.__contains__("Y"): # loss:0 + 2(paper)
                    points = points+2
                elif value.__contains__("Z"): # draw:3 + 3(sissors)
                    points = points+6
        #print(i,points)
    print(points)
math(inp, points)
print("____________________________________________")
def math2(inp, points):

    # rules
    #
    # if the round ends in a X, you need to lose
    #
    # if the round ends in a Y, it needs to be a draw
    #
    # if the round end in a Z, you need to win
    #
    # rock      is    1 point
    # paper     is    2 points
    # sissors   is    3 points

    for i, value in enumerate(inp):
        end = len(inp)-1
        if(i != end):
            if value.__contains__("A"): # rock
                if value.__contains__("X"):  # lose + sissors(3)
                    points = points+3
                elif value.__contains__("Y"): # draw + rock(1) 
                    points = points+4
                elif value.__contains__("Z"): # win + paper(2)
                    points = points+8
            elif value.__contains__("B"): # paper
                if value.__contains__("X"): # lose + rock(1)
                    points = points+1
                elif value.__contains__("Y"): # draw + paper(2)
                    points = points+5
                elif value.__contains__("Z"): # win + sissors(3)
                    points = points+9
            elif value.__contains__("C"): # sissors
                if value.__contains__("X"): # lose + paper(2)
                    points = points+2
                elif value.__contains__("Y"): # draw + sissors 3
                    points = points+6
                elif value.__contains__("Z"): # win + rock(1)
                    points = points+7
        else:
            pass
        if(i == end):
            if value.__contains__("A"): # rock
                if value.__contains__("X"):  # lose + sissors(3)
                    points = points+3
                elif value.__contains__("Y"): # draw + rock(1) 
                    points = points+4
                elif value.__contains__("Z"): # win + paper(2)
                    points = points+8
            elif value.__contains__("B"): # paper
                if value.__contains__("X"): # lose + rock(1)
                    points = points+1
                elif value.__contains__("Y"): # draw + paper(2)
                    points = points+5
                elif value.__contains__("Z"): # win + sissors(3)
                    points = points+9
            elif value.__contains__("C"): # sissors
                if value.__contains__("X"): # lose + paper(2)
                    points = points+2
                elif value.__contains__("Y"): # draw + sissors 3
                    points = points+6
                elif value.__contains__("Z"): # win + rock(1)
                    points = points+7
        #print(i,points)
    print(points)
math2(inp, points)