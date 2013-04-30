import itertools

def get_frequency(transaction, minimum_support):
    return dict(filter(lambda item: item[1] >= minimum_support, 
                       reduce_(map_(transaction))))

def map_(list_of_set):
    for column_set in list_of_set:
        for item in column_set:
            yield [item, 1]

def reduce_(t):
    for k, v in collect_(t).items():
        yield [k, sum(v)]

def collect_(transaction_iter):
    res = {}
    for item in transaction_iter:
        if(res.has_key(item[0])):
          res[item[0]].append(item[1])
        else:
          res[item[0]] = [item[1]]
    return res
