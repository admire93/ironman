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

def get_frequency_for(for_, transaction, level):
    if level == 1:
        return dict(ironman.functions.map_reduce(
          transaction, FrequentItemMapReducer()
        ))
    else:
        return dict(ironman.functions.map_reduce(
          transaction,
          FrequencyForItemMapReducer(for_)
        ))

def get_association_rules(data, min_supp=3):
    level = 1 
    next_sets = []
    start_frequency, except_frequency = ironman.functions.seperate_frequency_items_by_support(
                                            get_frequency_for([], data, level),
                                            min_supp
                                        )
    while len(start_frequency) > 0:
        next_sets = ironman.functions.get_next_length_set(
                        ironman.functions.get_set_from_keys(start_frequency),
                        ironman.functions.get_set_from_keys(except_frequency)
                    )
        data = list(filter(lambda x: len(x) >= level, data))
        start_frequency, except_frequency = ironman.functions.seperate_frequency_items_by_support(
                                                get_frequency_for(next_sets, data, level),
                                                min_supp
                                            )
        level += 1

    return next_sets
