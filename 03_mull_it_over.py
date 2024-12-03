import re

with open("03_input.txt", "r") as file:
    memory = file.read()


def get_mul_total(memory):
    pattern = r"mul\((\d+),(\d+)\)"

    matches = re.findall(pattern, memory)

    mul_total = 0
    for match in matches:
        mul_total += int(match[0]) * int(match[1])

    return mul_total

print(get_mul_total(memory=memory))

do_pattern = r"do()"
dont_pattern = r"don't()"

do_matches = re.findall(do_pattern, memory)
dont_matches = re.findall(dont_pattern, memory)

print(len(do_matches))
print(len(dont_matches))



splitted_memory = memory.split("don't()")
p2_total = get_mul_total(splitted_memory[0])

for m in splitted_memory:
    do_split = m.split("do()")
    if len(do_split) > 1:
        for d in range(1, len(do_split)):
            p2_total += get_mul_total(do_split[d])

print(p2_total)

# part 2 Correct