
games = open("054.txt", "r")

def best_hand(hand):
    translation = {"T":10, "J": 11, "Q":12,"K":13, 'A':14 }
    values = [translation[x[0]] if x[0] in list(translation.keys()) else int(x[0]) for x in hand]
    suits = [x[1] for x in hand]
    set_val = set(values)
    set_suits = set(suits)
    sort_val = sorted(values)
    
    if sort_val == [10,11,12,13,14] and len(set_suits) == 1: return [0]
    if [sort_val[i+1]-sort_val[i] for i in range(len(sort_val)-1)] == [1,1,1,1] and len(set_suits) == 1: return [1, sort_val]
    if len(set_val) == 2 and values.count(values[0]) in [1,4]: return [2, sort_val]
    if len(set_val) == 2: return 3, sort_val
    if len(set_suits) == 1: return 4, sort_val
    if [sort_val[i+1]-sort_val[i] for i in range(len(sort_val)-1)] == [1,1,1,1]: return 5, sort_val
    if len(set_val) == 3 and values.count(values[0]) in [1,3]: return 6, sort_val
    if len(set_val) == 3: return 7, sort_val
    if len(set_val) == 4: return 8, sort_val
    return 9, sort_val

p1_wins = 0
for i in games:  
    break
    hands = i.split(" ")
    hands[-1] = hands[-1][0:2]   
    p1 = hands[:5]
    p2 = hands[5:]

    score1 = best_hand(p1)
    score2 = best_hand(p2)

    if score1[0] < score2[0]:
        p1_wins += 1
    elif p1 == p2:
        s1 = score1[1]
        s2 = score2[1]
        if score1[0] == 1 and s1[0]>s2[0]: 
            p1_wins += 1
        elif score1[0] == 2: 
            ls1 = list(set(s1))
            ls2 = list(set(s2))
            count4_1 = ls1[0] if s1.count(ls1[0]) == 4 else ls1[1]
            count4_2 = ls2[0] if s2.count(ls12[0]) == 4 else ls2[1]
            if count4_1 > count4_2: 
                p1_wins += 1
            elif count4_1 == count4_2:
                for j in range(5):
                    if s1[j] > s2[j]:
                        p1_wins += 1
                        break
        elif score1[0] == 3:
            for 
        



