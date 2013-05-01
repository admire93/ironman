import ironman.functions

class FrequentItemMapReducer:
    
    def mapper(self, data):
        for t_set in data:
            for item in t_set:
                yield (set(item).__str__(), 1)

    def reducer(self, grouped_data):
        for k, v in grouped_data:
            yield (k, sum(v))

def get_frequency(transaction, minimum_support):
    r = ironman.functions.map_reduce(transaction, FrequentItemMapReducer())
    return dict(filter(lambda item: item[1] >= minimum_support, r))

def get_frequency_for(for_, transaction, minimum_support):
    r = ironman.functions.map_reduce(transaction, FrequentItemMapReducer())
    return dict(filter(lambda item: item[1] >= minimum_support, r))

def get_association_rules(data):
    pass
