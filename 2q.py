
BETA = 0.9

def isConverged(prev, curr):
    for i in range(len(prev)):
        if (prev[i] - curr[i])**2 > 0.01:
            print(i)
            print("prev is: " + str(prev[i]))
            print("curr is: " + str(curr[i]))
            print((prev[i] - curr[i])**2)
            return False

    return True

def main():
    U_star = [1 for i in range(10)] #init utilities to random values
    action_dict = {}

    """
    #the format of action_dict is {<stateNum>:{"<ACTION>": (reward, [(trans. to x prob, x)...]), ...}}
    """

    action_dict[0] = { "USE":(100, [(1,1)])}#0 corresponds with New

    for i in range(1,9):
        action_dict[i] = {"USE": (100-10*i, [(0.1*i, i+1), (1 - 0.1*i, i)]), 
                          "REPLACE": (-250, [(1,0)])}

    action_dict[9] = {"REPLACE": (-250, [(1,0)])}

    prev_U_star = [0 for i in range(10)]

    while not isConverged(prev_U_star, U_star):
        for i in range(len(U_star)):
            prev_U_star[i] = U_star[i]

        for i in range(len(U_star)):
            #for each a in A(s), perform the calculation
            action_keys = action_dict[i].keys()
            calcs = []
            for key in action_keys:
                r_sa = action_dict[i][key][0]
                other_term = 0
                for transition in action_dict[i][key][1]:
                    other_term += (transition[0] * prev_U_star[transition[1]])
                other_term *= BETA
                add = r_sa + other_term
                calcs.append(add)
            U_star[i] = max(calcs)
            
            #if difference is less than a certain amount, then break
    print("converged!")
    print(U_star)
        


if __name__ == "__main__":
    main()
