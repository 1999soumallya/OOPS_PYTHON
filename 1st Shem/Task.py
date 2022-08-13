from collections import defaultdict

def maxaverage(l):
    data_dict = defaultdict(list)

    for k, v in l:
        data_dict[k].append(v)

    data_dict = dict(data_dict)

    for k, v in data_dict.items():
        data_dict[k] = sum(v) / len(v)

    dl = [i for i,j in data_dict.items() if j == max(data_dict.values())]
    return dl 

print(maxaverage([('Kohli',73),('Ashwin',33),('Kohli',7),('Pujara',122),('Ashwin',90)]))
