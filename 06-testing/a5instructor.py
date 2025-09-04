import random

'''
1. Complete the function `compute_matching`, which takes two lists of equal
length and returns a list of the same length where the `i`th element is True if
the `i`th elements of the two lists are equal.
'''

def compute_matching(lst1, lst2):
    '''
    Given two lists of equal length, compute a list
    that where the ith element is True if the lists
    match at index i.

    Input: lst1, lst2 (lists)

    Returns: list of bools
    '''
    rv = []
    for i, val in enumerate(lst1):
        rv.append(val == lst2[i])
    return rv

'''
2. Complete the function `compute_matching_indices`, which takes two lists of
equal length and returns a list of the indices where the elements of the two
lists are equal.
'''

def compute_matching_indices(lst1, lst2):
    '''
    Given two lists of equal length, computed a list of
    the indices where the elements of the two lists
    are equal

    Input: lst1, lst2 (lists)

    Returns: list of ints
    '''
    matches = compute_matching(lst1, lst2)
    #rv = [i for i, match in enumerate(matches) if match] # alt solution
    rv = []
    for i, match in enumerate(matches):
        if match:
            rv.append(i)
    return rv

'''
3. Write a python function `lowest_temperature(data, date)` that takes as an
argument a list of lists (of weather data -- as in the prompt on Canvas) and
returns the name of the city with the lowest temperature for the specified date.
'''

DATE = 0
CITY = 1
LOW = 3

def lowest_temperature(data, date):
    '''
    Finds the city with lowest temperature for a specified date

    Input: data (list of lists of strings), date (str of form "YYYYMMDD")
    Output: (str) city with lowest temp for `date`
    '''
    minCity = ""
    minTemp = float('inf') # or implausibly high value, e.g. 9999 or 9999.0

    for line in data:
        if line[DATE] == date and float(line[LOW]) < minTemp:
            minCity = line[CITY]
            minTemp = float(line[LOW])
    
    return minCity

'''
4. Generalize the coin flip prompt covered in class
'''

def run_trial(target, head_probability):
    total_flips = 0
    consecutive_heads = 0

    while consecutive_heads < target:
        # 1. Flip a coin
        flip = random.random()

        # 2a. If it's heads: increment consecutive_heads
        if flip < head_probability:
            consecutive_heads += 1

        # 2b. If it's tails: reset consecutive_heads to 0
        else:
            consecutive_heads = 0

        # 3. Increment the total_flips after coin is flipped
        total_flips += 1
    
    return total_flips

def compute_list_average(lst):
    avg = sum(lst) / len(lst)
    return avg

def compute_simulated_average(target=5, 
                              n_trials=1000, 
                              seed=0, 
                              head_probability=0.5):
    sim_results = []
    random.seed(seed)

    for i in range(n_trials):
        total_flips = run_trial(target, head_probability)
        sim_results.append(total_flips)

    avg = compute_list_average(sim_results)
    return avg

if __name__ == '__main__':
    print("This program simulates the number of times you need to flip a coin before you get a certain number of heads")
    target = int(input("Target number of heads: "))
    n_trials = int(input("Number of trials to simulate: "))
    head_probability = float(input("Probability of heads: "))

    r = compute_simulated_average(target=target, 
                                  n_trials=n_trials,
                                  seed=0,
                                  head_probability=head_probability
                                  )
    print(r,
          " average number of coin flips in order to get ",
          target,
          " heads in a row")