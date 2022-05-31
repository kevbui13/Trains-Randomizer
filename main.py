import random

randomizer = ["7rControl Room", "4bNovelty Train", "3gLay Rail", "3pStation Expansion", "7gViaduct", "3bLimited Train", "3rPolitician", "7bMaglev"]
error = 1
card_cost = []
card_type = []
card_name = []

if __name__ == '__main__':

    ## Randomizers Random Mechanic
    while error != 0:
        error = 0
        pool = random.sample(randomizer, k=8)

        card_cost = []
        card_type = []
        card_name = []

        ## String Manipulations
        for i in range(0,8):
            data = str(pool[i])
            card_cost.append((int(data[0])))
            card_type.append(data[1])
            card_name.append(data[2:])

        ## Checks for Balanced Randomizers
        check_sum = sum(card_cost)
        if check_sum > 46 or check_sum < 34:
            error = error + 1

        check_type = card_type.count("r")
        if check_type > 4 or check_type < 1:
            error = error + 1

        check_type = card_type.count("b")
        if check_type > 4 or check_type < 1:
            error = error + 1

        check_type = card_type.count("p")
        if check_type > 4 or check_type < 1:
            error = error + 1

        check_type = card_type.count("g")
        if check_type > 4 or check_type < 1:
            error = error + 1

        ## Check for too many of one cost level.
        for i in [2,3,4,5,6,7]:
            check_cost = card_type.count(i)
            if check_cost > 4:
                error = error + 1

    ## Output to Terminal
    for i in range(0,8):
        print("Cost: ",card_cost[i],"       Type: ",card_type[i],"      Name: ",card_name[i])
