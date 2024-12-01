
f = open('input.txt', 'r')

col1 = []
col2 = []
total = 0

for i in f.readlines():

    row = i.strip('\n').split("   ")
    col1.append(int(row[0]))
    col2.append(int(row[1]))


def part1():

    col1.sort()
    col2.sort()

    for i in range(len(col1)):
        diff = 0
        diff = abs(col1[i] - col2[i])
        total += diff

    print(f"total: {total}")


def part2():
    col1.sort()
    tot = 0
    for target in col1:
        occurance = 0
        for num in col2:
            if target == num:
                occurance += 1
        tot += (target * occurance)
    return tot


print(part2())
