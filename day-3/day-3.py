text = open('day-3-input.txt', 'r')
setup = text.readlines()

# temp info holders
part1 = []
part2 = []

answer = []
score = 0

# storage arrays
inp = []
out = []
lowerCase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
upperCase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lowerScores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
upperScores = [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]

for line in setup:
    try:
        if line[-1] == '\n':
            inp.append(line[:-1])
        else:
            inp.append(line)
    finally:
        pass

def main(inp, answer, score):

        for i, value in enumerate(inp):
            end = len(inp)-1
            if(i != end):
                string1 = value[:len(value)//2]
                string2 = value[len(value)//2:]
                
                compare(string1, string2, answer)
            else:
                pass
            if(i == end):
                string1 = value[:len(value)//2]
                string2 = value[len(value)//2:]
                
                compare(string1, string2, answer)
        points(answer, lowerCase, upperCase, lowerScores, upperScores, score)

def compare(string1, string2, answer):

        a_len = len(string1)
        b_len = len(string2)

        for a in string1:
            for b in string2:

                if a == b:
                    answer.append(b)
                    return

def points(answer, lowerCase, upperCase, lowerScores, upperScores, score):

        for i, value in enumerate(answer):
            if value.islower() == True:
                for u, value2 in enumerate(lowerCase):
                    if answer[i] == value2:
                        score = score+lowerScores[u]
            elif value.islower() == False:
                for u, value2 in enumerate(upperCase):
                    if answer[i] == value2:
                        score = score+upperScores[u]
            else:
                print(i, "error")
        print(score)

main(inp, answer, score)
