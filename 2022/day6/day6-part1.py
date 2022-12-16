input_data = open("input.txt").read()

for position in range(len(input_data)):  # len gives length of string.  range gives each number between 1 and given num
    unique_group = set(input_data[position:position+4])  # set makes a list into a unique list of elements
    if len(unique_group) == 4:
        print(position+4)
        break
