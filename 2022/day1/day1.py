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
sum_list.remove(max(sum_list))

second_max_number = max(sum_list)
sum_list.remove(max(sum_list))

third_max_number = max(sum_list)

top_three_sum = first_max_number + second_max_number + third_max_number
print(f"The top three Elves carrying the most Calories have a total of {top_three_sum} Calories!")
