# part 1
left_list, right_list = [], []

with open("01_input.txt", "r") as file:
    for line in file:
        formatted_line = line.strip().split()
        left_list.append(int(formatted_line[0]))
        right_list.append(int(formatted_line[1]))

left_list.sort()
right_list.sort()

distance = 0

for i in range(len(left_list)):
    distance += abs(left_list[i] - right_list[i])

print(f"distance = {distance}")

# part 2

right_list_entries_count = {}
for n in right_list:
    if n in right_list_entries_count:
        right_list_entries_count[n] += 1
    else:
        right_list_entries_count[n] = 1

similarty_score = 0
for n in left_list:
    if n in right_list_entries_count:
        similarty_score += n * right_list_entries_count[n]
    else:
        pass

print(f"similarty score = {similarty_score}")

# both correct!