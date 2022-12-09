def compare_elf_ranges(elf_range1, elf_range2):
    if elf_range1[0] <= elf_range2[0] and elf_range1[1] >= elf_range2[1]:
        return 1
    elif elf_range2[0] <= elf_range1[0] and elf_range2[1] >= elf_range1[1]:
        return 1
    else:
        return 0


def create_elf_ranges(line: str) -> tuple[list, list]:
    elf_ranges = line.replace("-", " ").replace(",", " ").split()
    elf_range1 = [int(elf_ranges[0]), int(elf_ranges[1])]
    elf_range2 = [int(elf_ranges[2]), int(elf_ranges[3])]
    return elf_range1, elf_range2


def main():
    input_data = open("input.txt", "r")
    total_count = 0
    for line in input_data:
        elf_range1, elf_range2 = create_elf_ranges(line)
        total_count += compare_elf_ranges(elf_range1, elf_range2)
    print(f"There are a total of {total_count} assignment pairs where one range fully contain the other!")


if __name__ == "__main__":
    main()
