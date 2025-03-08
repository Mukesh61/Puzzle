'''
People should join a line where less numbers of people are there.
input_1: n m
         3 4
    means there are n lines and m new people just arrived.
input_2: 3 2 5

output: number of people in the queue when they joined.
2
3
3
4
'''

input_1 = '3 4'
input_2 = '3 2 5'

num_of_lines, num_of_new_people = map(int, input_1.split())
people_in_queue = sorted(list(map(int, input_2.split())))


for _ in range(num_of_new_people):
    min_value = people_in_queue[0]
    print(min_value)
    min_value += 1
    people_in_queue[0] = min_value

    for i in range(num_of_lines):
        if min_value > people_in_queue[i+1]:
            people_in_queue[i] = people_in_queue[i+1]
            people_in_queue[i+1] = min_value
        else:
            break
