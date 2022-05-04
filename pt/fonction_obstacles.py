def obstacle_avant (message) : 
    qualite_min = 8
    distance_min = 150
    ret = False
    for tuple in message:
        if tuple[0]>=qualite_min:
            if tuple[1] < 51 or tuple[1]>311: ## entre 312° et 52°
                if tuple[2]<= distance_min:
                    ret = True
    return ret


def obstacle_droite (message) :
    qualite_min = 8
    distance_min_1 = 300
    distance_min_2 = 550
    ret = False
    for t in message:
        if t[0]>=qualite_min:
            if t[1] <= 150 and t[1]>=100: ## entre 100° et 150°
                if t[2]<= distance_min_2:
                    ret = True
            elif t[1] < 100 and t[1]> 50: ## entre 51° et 101°
                if t[2]<= distance_min_1:
                    ret = True
    return ret


def obstacle_gauche (message) : 
    qualite_min = 8
    distance_min_1 = 300
    distance_min_2 = 550
    ret = False
    for t in message:
        if t[0]>=qualite_min:
            if t[1] < 310 and t[1]>260: ## entre 261° et 311°
                if t[2]<= distance_min_1:
                    ret = True
            elif t[1] <= 260 and t[1]>= 210: ## entre 210° et 260°
                if t[2]<= distance_min_2:
                    ret = True
    return ret