branch_1 = {"sangsokea", "khounlaxe", "mesasila", "Koukimhai"}
branch_2 = {"sangsokea", "khounlaxe", "pol alisa", "raksmey"}

branch_center = branch_1.union(branch_2)
# print(branch_1)



# use intersention() method for return new  set
old_username = branch_1.intersection(branch_2)
print(old_username)
# use symmetric_difference() method for return new set
new_client = branch_1.symmetric_difference(branch_2)
print("New client:", new_client)



