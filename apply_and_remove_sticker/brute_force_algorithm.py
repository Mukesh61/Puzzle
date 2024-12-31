"""
If there are 50 trees,
round 1: apply sticker to all the trees.
round 2: remove if already sticker or apply sticker from 2, 4, 6,...,50
round 3: remove if already sticker or apply sticker from 3, 6, 9, ...
"""

sticker_in_tree = [False] * 51

for i in range(1, 51):
    for j in range(i,51,i):
        sticker_in_tree[j] = not sticker_in_tree[j]

for i, item in enumerate(sticker_in_tree):
    if item:
        print(i)
