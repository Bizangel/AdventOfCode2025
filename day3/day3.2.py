
with open('input.txt', 'r') as fhandle:
    input = fhandle.read()

splitted = [x.strip() for x in input.split('\n') if x.strip() != "" ]


n_batteries = 12

def max_joltage_rec(last_picked: int, picked_batteries: int, bankline: str) -> str:

    remaining_to_pick = n_batteries - picked_batteries
    if remaining_to_pick == 0:
        return ""

    idx2battery = [(i, int(bankline[i])) for i in range(last_picked+1, len(bankline) - remaining_to_pick + 1)]
    max_battery = max([x[1] for x in idx2battery])
    possibilities = [x for x in idx2battery if x[1] == max_battery]

    best_poss = -1
    for idx, digit in possibilities:
        best_poss = max(best_poss,
                        int(
                             str(digit) + max_joltage_rec(idx, picked_batteries + 1, bankline)
                            )
                        )
    return str(best_poss)



def max_joltage(bankline: str):
    return int(max_joltage_rec(-1, 0, bankline))



res = 0
for bank in splitted:
    res += max_joltage(bank)


print(res)

