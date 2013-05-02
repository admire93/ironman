import itertools

def map_reduce(data, map_reducer):
    mapped = map_reducer.mapper(data)
    def collector(mapped_data):
        for x in itertools.groupby(sorted(mapped_data), lambda x: x[0]):
            yield (x[0], map(lambda y: y[1], x[1]))

    collected = collector(mapped)
    return map_reducer.reducer(collected)

def get_set_from_keys(d):
    try:
        return list(map(lambda x: eval(x), d.keys()))
    except SyntaxError:
        print("Something goes wrong when evaluate set.")
        print(d)
        return []

def get_next_length_set(curr_sets, except_sets):
    curr_sets = list(curr_sets)
    curr_all_set = set()
    result_sets = []
    for x in curr_sets:
        for y in x:
            curr_all_set.add(y)

    for x in curr_sets:
        for y in list(curr_all_set):
            curr = set(x)
            curr.add(y)
            if not curr in curr_sets and not curr in result_sets:
                is_include_except_set = False
                for except_set in except_sets:
                    is_include_except_set = is_include_except_set or curr.issuperset(except_set)

                if not is_include_except_set:
                    result_sets.append(curr) 

    return result_sets

def seperate_frequency_items_by_support(d, min_supp):
    high = []
    low = []
    for k, v in d.items():
        if v >= min_supp:
            high.append((k, v))
        else:
            low.append((k, v))
    return (dict(high), dict(low))
