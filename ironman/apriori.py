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

def get_frequency(transaction):
    return dict(ironman.functions.map_reduce(transaction, FrequentItemMapReducer()))

def get_frequency_for(for_, transaction, level):
    return dict(ironman.functions.map_reduce(
      transaction,
      FrequencyForItemMapReducer(for_)
    ))

def get_association_rules(data):
    level = 2
    min_supp = 3
    frequency = get_frequency(data)
    def foo(d, min_supp):
        high = []
        low = []
        for k, v in d.items():
            if v >= min_supp:
                high.append((k, v))
            else:
                low.append((k, v))
        return (dict(high), dict(low))

    start_frequency, except_frequency = foo(frequency, min_supp)
    next_sets = []
    while len(start_frequency) > 0:
        start_sets = ironman.functions.get_set_from_keys(start_frequency)
        except_sets = ironman.functions.get_set_from_keys(except_frequency)
        next_sets = ironman.functions.get_next_length_set(start_sets, except_sets)
        data = list(filter(lambda x: len(x) >= level, data))
        level += 1
        start_frequency, except_frequency = foo(get_frequency_for(next_sets, data, level), min_supp)
        print("Start sets", start_sets)
        print("Next sets", next_sets)
        print("Except sets", except_sets)

    return next_sets
