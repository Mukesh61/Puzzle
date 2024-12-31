"""
If there are 50 trees,
round 1: apply sticker to all the trees.
round 2: remove if already sticker or apply sticker from 2, 4, 6,...,50
round 3: remove if already sticker or apply sticker from 3, 6, 9, ...

----------------
let's check the final output of brute force.

1,4,9,16,25,36,49

output is nothing but 
1 * 1 = 1
2 * 2 = 4
..
7 * 7 = 49

now 8 * 8 = 64 and 64 > 50, so we can break the loop.

"""

number_of_tree = 50

for i in range(1, number_of_tree//2):
    output = i * i

    if output > number_of_tree:
        break

    print(output, end=',')
