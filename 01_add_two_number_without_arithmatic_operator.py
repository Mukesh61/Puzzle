'''
we are going to add using logic gate. xor and and
'''
num_1 = 5
num_2 = 3

total_without_carry = num_1 ^ num_2 # xor operation
carry = (num_1 & num_2) << 1

# print(f"total_without_carry: {total_without_carry}")
# print(f"carry: {carry}")

'''
if we will add total_without_carry + carry then we will get the total, however 
we are not allowed to use + operator, now think about below scenario when carry is 0

total_without_carry = 8
carry = 0

since carry is 0, so total_without_carry will be answer.
so use loop and keep adding until carry is 0
'''
# set 2
num_1 = 55
num_2 = 45

while num_2:
    total_without_carry = num_1 ^ num_2  # xor operation
    carry = (num_1 & num_2) << 1
    num_1 = total_without_carry
    num_2 = carry

print(f"Total: {num_1}")
