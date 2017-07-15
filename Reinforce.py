import random
import operator

items=['pumpkin', 'sugar', 'egg', 'egg', 'red_mushroom', 'planks','planks']

food_recipes = {'pumpkin_pie': ['pumpkin', 'egg', 'sugar'],
                'pumpkin_seeds': ['pumpkin'],
                'bowl':['planks','planks'],
                'mushroom_stew':['bowl','red_mushroom']}

rewards_map = {'pumpkin': -5, 'egg': -25, 'sugar': -10,
               'pumpkin_pie': 100, 'pumpkin_seeds': -50,'red_mushroom': 5,
               'planks': -5, 'bowl': -1, 'mushroom_stew': 100}

def is_solution(reward):
    #return reward == -10
    return reward == 75

def get_curr_state(items):
    #print("item: ",items)
    state = []
    for item, amount in items:
        if amount == 1:
            state.append(item)
        if amount == 2:
            state.append(item)
            state.append(item)
        if amount == 3:
            state.append(item)
            state.append(item)
            state.append(item)
    #print ("\nstate: ",state)
    #print (tuple(sorted(state)))
    return tuple(sorted(state))

def choose_action(curr_state, possible_actions, eps, q_table):
    rnd = random.random()
##    print("")
##    print("____________________________________________________________")
##    print("Current State: {}".format(curr_state))
##    print("Possible Actionas: {}".format(possible_actions))
##    print("Q-Table: {}".format(q_table))
##    print("List of actions and the Q=-values: {}".format(q_table[curr_state].items()))
##    print("The max : {}".format(max(q_table[curr_state].items())))
##    print("Random: {}".format(rnd))
##    print("_____________________________________________________________")
##    print ("")
##    print max([1,2,3,4,5,5,5,5])
    d = dict()
    counter = 0
    index_list = []
    new_possible = []
   
    for i, j in q_table[curr_state].items():
        new_possible.append(i)
        d[i] = float(j)

            
##
    #print("This is the dictionary: {}".format(d))

    if rnd < eps:
        a = random.randint(0, len(new_possible) - 1)
    else:
        #print(d)
        maxi = max(d.iteritems(), key=operator.itemgetter(1))[1]
        #print("maxi: {}".format(maxi))
        for i, j in q_table[curr_state].items():
            #i is the item
            if j == maxi:
                index_list.append(counter)
                counter += 1
            else:
                counter += 1
        #print("new possibles : {}".format(new_possible))
        #print("This is index_list: {}".format(index_list ))
        if len(index_list)== 1:
            a = index_list[0]
        else:
            a = random.randint(index_list[0], index_list[-1])
            #print("Random_index = {}".format(a))
    #print(a)
    #print("The real max : {}".format(new_possible[a]))

    return new_possible[a]

