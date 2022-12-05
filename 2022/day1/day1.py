input_data = open("input.txt", "r")

sum_list = []
group_sum = 0
for line in input_data:
    if line.strip():  # Line is not empty
        line = int(line)
        group_sum += line
    else:  # Line is empty
        sum_list.append(group_sum)
        group_sum = 0

first_max_number = max(sum_list)
print(f"The Elf carrying the most Calories has {first_max_number} total Calories!")

sum_list.sort()
print(f"The top three Elves carrying the most Calories have a total of {sum(sum_list[-3:])} Calories!")
