import re


def arithmetic_arranger(problems, solve=False):
   
    if (len(problems) > 5):
        return "Error: Too many problems."
    firstline = ""
    secondline = ""
    dashes = ""
    answer = ""
    arranged_problems = ""

    for problem in problems:
        if (re.search("[^\s0-9.+-]", problem)):
            if (re.search("[/]", problem) or re.search("[*]", problem)):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."

        firstnum = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        secondnum = problem.split(" ")[2]

        if (len(firstnum) >= 5 or len(secondnum) >= 5):
            return "Error: Numbers cannot be more than four digits."

        sum = ""
        if (operator == "+"):
            sum = str(int(firstnum) + int(secondnum))
        elif (operator == "-"):
            sum = str(int(firstnum) - int(secondnum))

        length = (max(len(firstnum), len(secondnum))) + 2
        first = str(firstnum).rjust(length)
        second = operator + str(secondnum).rjust(length - 1)
        dash = ""
        total = str(sum).rjust(length)

        for num in range(length):
            dash += "-"

        if problem != problems[-1]:
            firstline += first + "    "
            secondline += second + "    "
            dashes += dash + "    "
            answer += total + "    "
        else:
            firstline += first
            secondline += second
            dashes += dash
            answer += total

    if solve == True:
        arranged_problems = firstline + "\n" + secondline + "\n" + dashes + "\n" + answer
    else:
        arranged_problems = firstline + "\n" + secondline + "\n" + dashes
    return arranged_problems
