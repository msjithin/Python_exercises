def my_product(*iterables):
    pools = [tuple(iterable) for iterable in iterables]
    result = [[]]

    for pool in pools:
        print('pool', pool)
        result = [x + [y] for x in result for y in pool]

    for prod in result:
        yield tuple(prod)


def recursive_product(*iterables, current=[]):
    if not iterables:
        yield tuple(current)
    else:
        for item in iterables[0]:
            yield from recursive_product(*iterables[1:], current=current + [item])

# Example usage:
list1 = [1, 2]
list2 = ['a', 'b']
list3 = ['x', 'y']

recursive_cartesian_product = list(recursive_product(list1, list2, list3))
print(recursive_cartesian_product)

# Example usage:
list1 = [1, 2]
list2 = ['a', 'b']
list3 = ['x', 'y']

my_cartesian_product = list(my_product(list1, list2, list3))
print(my_cartesian_product)
