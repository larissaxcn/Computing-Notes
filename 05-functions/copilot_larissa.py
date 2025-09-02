# loop over a list of integers [1, 2, 3] and print out each integer's square
for i in [1, 2, 3]:
    print(i ** 2)

def compute_matching_indices(lst1, lst2):
    return [i for i, (a, b) in enumerate(zip(lst1, lst2)) if a == b]

