import re


def print_final_stacks(master_list):
    first_boxes = ""
    for stack in master_list:
        first_boxes += stack[0]
    print(first_boxes)


def move_crates(master_list, numbers):
    stack1 = master_list[(numbers[1]-1)]
    stack2 = master_list[(numbers[2]-1)]
    stack1.reverse()
    stack2.reverse()
    counter = 1
    while counter <= numbers[0]:
        stack2.append(stack1.pop())
        counter += 1
    stack1.reverse()
    stack2.reverse()
    return master_list


def create_given_stacks(input_data) -> list[list]:
    counter = 1
    master_list = [[], [], [], [], [], [], [], [], []]
    for line in input_data:
        if counter < 9:
            position1 = 1
            position2 = 2
            for stack in master_list:
                if line[position1:position2] != " " and line[position1:position2] != "":
                    stack.append(line[position1:position2])
                position1 += 4
                position2 += 4
            counter += 1
    input_data.seek(0)  # Return to the beginning of the input data file for future reads
    return master_list


def main():
    input_data = open("input.txt", "r")
    master_list = create_given_stacks(input_data)
    for line in input_data:
        if re.compile(r'move').search(line):
            numbers = re.findall(r"\d+", line)
            numbers = [eval(number) for number in numbers]
            master_list = move_crates(master_list, numbers)
    print_final_stacks(master_list)


if __name__ == "__main__":
    main()
