def is_free(free_list, char):
    for n in free_list:
        if char in n:
            return False
    return True

def select_preference(man, proposed, woman,woman_list):
    engaged_index = -1
    proposed_index = -1
    index = -1
    # get engaged index
    for n in proposed:
        if woman in n:
            if n[0] in woman_list:
                engaged_index = woman_list.index(n[0])
                index = proposed.index(n)

    # get proposed index
    if man in woman_list:
        proposed_index = woman_list.index(man)
    
    #if man is prefered over m'
    if proposed_index!= -1 and proposed_index < engaged_index:
        #remove the current (m', w) pairing from the list and append the new pairing
        proposed.pop(index)
        proposed.append([man,woman])

def gale_shapely(men, women):
    if not men or not women:
        return []
    
    women_list = list(women.keys())
    men_list = list(men.keys())
    # use to monitor woman who man has propsed to
    proposed = []
    # use to monitor man who has proposed and been accepted
    wait_list = []
    while len(wait_list) < len(men_list):
        for man in men_list: # O(men)
            #first free man (i.e. not engaged and not in waiting list?)
            if is_free(wait_list,man):
                # need to get the man's preference list
                man_preference = men[man]
                # iterate through preference to find the first free (haven't acccepted any proposal) woman
                # woman is in man's preference and woman has not been proposed to by said man
                for woman in man_preference: #O(women)
                    # if woman is not engaged then engage man and woman
                    if is_free(proposed, woman):
                        proposed.append([man,woman]) 
                        wait_list += [man]
                        break
                    # some pair of (m', w) exist
                    else:
                        #let woman choose between her preference  
                        woman_preference = women[woman]
                        select_preference(man, proposed, woman,woman_preference) #O(men)
    return proposed
