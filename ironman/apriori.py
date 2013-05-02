import itertools

import ironman.functions

class MapReducer:

    def reducer(self, grouped_data):
        for k, v in grouped_data:
            yield (k, sum(v))

    

class FrequentItemMapReducer(MapReducer):
    
    def mapper(self, data):
        for t_set in data:
            for item in t_set:
                yield (set(item).__str__(), 1)
 
class FrequencyForItemMapReducer(MapReducer):
    
    def __init__(self, for_):
        self.for_ = for_

    def mapper(self, data):
        for d in data:
            for x in self.for_:
                if x.issubset(d):
                    yield (x.__str__(), 1)

def get_frequency(transaction, minimum_support):
    r = ironman.functions.map_reduce(transaction, FrequentItemMapReducer())
    return dict(filter(lambda item: item[1] >= minimum_support, r))

def get_frequency_for(for_, transaction, level, minimum_support):
    subset = []
    for x in itertools.combinations(for_, level):
        subset.append(set(x))

    r = ironman.functions.map_reduce(
      transaction,
      FrequencyForItemMapReducer(subset)
    )
    return dict(filter(lambda item: item[1] >= minimum_support, r))

def get_association_rules(data):
    pass
