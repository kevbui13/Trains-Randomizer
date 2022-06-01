import random

with open("randomizer.txt") as f:
    randomizer = f.read().splitlines()

error = 1
card_cost = []
card_type = []
card_name = []

if __name__ == '__main__':

    ## Randomizers - Random Mechanic
    while error != 0:
        error = 0
        pool = random.sample(randomizer, k=8)

        ## Define three lists
        card_cost = []
        card_type = []
        card_name = []

        ## String Manipulations - to indicate card cost, card type, and card name
        for i in range(0,8):
            data = str(pool[i])
            card_cost.append((int(data[0])))
            card_type.append(data[1])
            card_name.append(data[2:])

        ## Checks for Balanced Randomizers
        
        ## Checks the supply cost sum
        check_sum = sum(card_cost)
        if check_sum > 44 or check_sum < 34:
            error = error + 1

        ## Checks the card type distribution
        check_type = card_type.count("r")
        if check_type > 5 or check_type < 1:
            error = error + 1

        check_type = card_type.count("b")
        if check_type > 4 or check_type < 1:
            error = error + 1

        check_type = card_type.count("p")
        if check_type > 3 or check_type < 1:
            error = error + 1

        check_type = card_type.count("g")
        if check_type > 3 or check_type < 1:
            error = error + 1

        ## Check for too many of one cost level.
        for i in [2,3,4,5,6,7]:
            check_cost = card_cost.count(i)
            if check_cost > 3:
                error = error + 1

    ## Output to Terminal
    for i in range(0,8):
        print("Cost: ",card_cost[i],"       Type: ",card_type[i],"      Name: ",card_name[i])
