
with open('input.txt', 'r') as fhandle:
    input = fhandle.read()

splitted = [x.strip() for x in input.split('\n') if x.strip() != "" ]


def max_joltage(bankline: str):
    best_joltage = 0
    for i in range(len(bankline)):
        for j in range(i+1, len(bankline)):
            combo = int(bankline[i] + bankline[j])
            best_joltage = max(best_joltage, combo)

    # print(bankline, '-->', best_joltage)
    return best_joltage


res = 0
for bank in splitted:
    res += max_joltage(bank)


print(res)

