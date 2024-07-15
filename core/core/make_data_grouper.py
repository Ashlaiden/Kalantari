import itertools


# make date grouper
def make_data_grouper(group_count, iterable):
    args = [iter(iterable)] * group_count
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


