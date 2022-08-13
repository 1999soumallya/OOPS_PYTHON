def recur_sum(ll):
    if len(ll)==0:
        return 0
    else:
        return(ll[-1]+recur_odd_sum(ll[:-1]))

ll=[11,22,33,44,55]
print(recur_sum(ll))

def recur_odd_sum(ll):
    if len(ll)==2 or len(ll)==1:
        return(ll[0])
    else:
        return(ll[0]+recur_odd_sum(ll[2:]))

ll=[11,22,33,44,55]
print(recur_odd_sum(ll))

