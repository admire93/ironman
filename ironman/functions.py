import itertools

def map_reduce(data, map_reducer):
    mapped = map_reducer.mapper(data)
    def collector(mapped_data):
        for x in itertools.groupby(sorted(mapped_data), lambda x: x[0]):
            yield (x[0], map(lambda y: y[1], x[1]))

    collected = collector(mapped)
    return map_reducer.reducer(collected)

def get_set_from_keys(d):
    result_set = set()
    try:
        set_list = map(lambda x: eval(x), d.keys())
    except SyntaxError:
        print("Something goes wrong when evaluate set.")
        print(d)
        return {}
    else:
        for s in set_list:
            result_set |= s

        return result_set
