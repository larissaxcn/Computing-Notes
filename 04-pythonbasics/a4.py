'''
1. Given an integer variable `x`, write a conditional statement that will assign
to a variable `s` the string value `"POSITIVE"`, `"NEGATIVE"`, or `"ZERO"`
(depending on whether `x` is positive, negative, or zero, respectively). Assume
`x` has the value 2 for the purposes of this prompt (but also try plugging
in the values 0 and -1 for x, to ensure that your conditional statements are
written correctly).
'''

# YOUR CODE HERE

# Solution 1
if x == 0:
    s = "ZERO"
elif x > 0:
    s = "POSITIVE"
else:
    s = "NEGATIVE"
print(s)

# Solution 2
# x is a list containing three integers
# x = [2, 0, -1]
for x in [2, 0, -1]: 
    if x > 0:
        s = "POSITIVE"
    elif x < 0:
        s = "NEGATIVE"
    else:
        s = "ZERO"
    print(s)
# my_list = [1, 2, 3]
# my_list = list(range(1, 4)) 
# list: this converts the range object into a list.




'''
2. Given integer variables `lb`, `ub`, `p`, and `q`, write a loop that will
count how many numbers between `lb` and `ub` (inclusive) are divisible by both
`p` and `q`. For the purposes of this prompt, assume that `p` is 2 and `q` is 3.
Also assume that `lb` is 1 and `ub` is 20. Thus, your result should be 3
(because only 6, 12, and 18 are divisible by both 2 and 3).
'''
# YOUR CODE HERE
lb = 1
ub = 20
p = 2
q = 3
count = 0 # base condition before we iterate the condition

# lb, ub, p, q = 1, 20, 2, 3
for i in range (lb, ub + 1): # range(a, b) => [a, b)
    if (i % p ==0 and i % q == 0):
        count += 1 # count=count+1
        # print(count)
print(count)


'''
3. Given a list of integers `lst`, write a loop to count the number of negative
numbers in the list. Assume `lst` has the value `[-1, 2, -3, 4, 0]` for the
purposes of this prompt. Thus, your result should be 2 (because only -1 and -3
are negative numbers).
'''
# YOUR CODE HERE
count = 0
lst = [-1, 2, -3, 4, 0]
for i in lst:
    if i < 0:
        count +=1
        # print(i，count) # if not i < 0 -> skip
print(count)

'''
4. Write a loop to compute a variable `all_pos` that has the value `True` if
all of the elements in a list of integers `lst` are positive and `False`
otherwise. Again, assume `lst` has the value `[-1, 2, -3, 4, 0]` for the
purposes of this prompt.
'''
# YOUR CODE HERE
lst = [-1, 2, -3, 4, 0]
all_pos = True # starting point (assuming all integers are positive)
# base condition
# as I loop thhrough, it will see if all_pos = True
for i in lst:
    if i <= 0:
        all_pos = False # use == when comparing two values; = is for assigning values
        # print(i) # if do this and without adding break, it will gave us -1, -3, false
        break
    # When break is hit and executed within a for loop, 
    # the loop stops iterating through the remaining elements, 
    # and the program continues after the loop.    
    # As soon as the loop finds one number that is <= 0, all_pos = False and quit loop
print(all_pos)



'''
lst = [-1, 2, -3, 4, 0]
all_pos = True 
for i in lst:
    if i <= 0:
        all_pos = False
        print(all_pos) # pring out three Falses
'''
# different print positions in for loop, serving different purposes
# always need to set a beginning point?? still find it somehow conceptually confusing



'''
5. Given a list of keys and a list of values, use a loop to construct a
dictionary that maps the ith key in the list of keys to the ith value in the
list of values. For the purposes of this prompt, assume that the list of keys
is `["x", "y", "z"]` and the list of values is `[10, 20, 30]`.
'''
# YOUR CODE HERE
dic={}
print({f"keys": f"keys" ""})
# dic = {"x": 10, "y": 20, "z": 30}
# for key, value in dic.items():
#    print(key, value)

keys = ["x", "y", "z"]
values = [10, 20, 30]
dic = {}

for i in range(len(keys)):
    dic[keys[i]] = values[i]
print(dic)

# len(list): check how long the list is
# rv = {}
# for i in range(n):
#    print(keys[i], values[i])



'''
6. Compute the most frequently occuring categorical label for the region
depicted in the satellite images provided (see description in prompt on Canvas).
'''

band_red = [[1, 10, 255],
            [200, 155, 20],
            [30, 20, 10]]
band_nir = [[1, 20, 255],
            [10, 20, 30],
            [200, 155, 20]]

# YOUR CODE HERE
# create a dictionary
counts = {"barren": 0, "vegetation-rich": 0, "flood": 0}
# counts["barren"]
# retrieve an item from the dic - use key to get the value


# len(band_red) -> how many rows 
# range(len(band_red[0]))) -> how many colomns
# band_red[0] -> 1st row
# len(band_red[0]) -> how many colomns
for i in range(len(band_red)):
    for j in range(len(band_red[0])):
        red = band_red[i][j] # use the coordinate of the item to extract the tiem
        nir = band_nir[i][j]
        
        ndvi = (nir - red) / (nir + red)
        
        if -0.25 < ndvi <= 0.25:
            counts["barren"] += 1 
        # call the dic
        # retrieve an item from the dic - use key to get the value
        elif 0.25 < ndvi <= 1.0:
            counts["vegetation-rich"] += 1
        else:
            counts["flood"] += 1

most_freq = max(counts, key = counts.get)
# suppose have the following counts in the dic:
# counts = {"barren": 3, "vegetation-rich": 4, "flooded": 2}
# counts["barren"] -> 3
# counts.get("barren")
# counts.get("barren") and counts["barren"] return the same value mostly
# but counts["barren"] raises an error if the key does not exist
# counts.get("barren") returns None (or a default value if being provided)

# max
# max(dic key=))
# key tells python how to compare the items
# e.g. print(max(words, key=len)) 
# compare the values of counts for each key(item) in the dic

print("Label counts: ", counts)
print("Most likely: ", most_freq)

'''
# 1. how to represent the coordinate of an item in a list
# 2. how to extract the i-th list j-st value for this list

band_red[i][j]
band_nir[i][j]

# 0th list 1st value for this list

band_red = [[1, 10, 255],
            [200, 155, 20],
            [30, 20, 10]]

# 0th list:
band_red[0]        # → [1, 10, 255]
# 1st value in the 0th list:
band_red[0][1]     # → 10

i = 2
j = 1
red = band_red[i][j] # put in loop
red

len(band_red) # how many rows
3
range(3)
# go through each row of the list
'''



7. Read in any files named `band_nir.csv` and `band_red.csv` as lists of lists
and print out the highest frequency label for the corresponding region.

# YOUR CODE HERE
import csv

'''
with open ("band_nir.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
'''



band_red = []
with open("band_red.csv") as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        band_red.append(row)
        print(row) # will show every list


band_nir = []
with open ("band_nir.csv") as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        band_nir.append(row)
        print(row)

counts = {"barren": 0, "vegetation-rich": 0, "flood": 0}

for i in range(len(band_red)):
    for j in range(len(band_red[0])):
        red = band_red[i][j] 
        nir = band_nir[i][j]

        ndvi = (nir - red) / (nir + red)

        if -0.25 < ndvi <= 0.25:
            counts["barren"] += 1 
        elif 0.25 < ndvi <= 1.0:
            counts["vegetation-rich"] += 1
        else:
            counts["flood"] += 1

most_freq = max(counts, key = counts.get)
print("Label counts: ", counts)
print("Most likely: ", most_freq)
