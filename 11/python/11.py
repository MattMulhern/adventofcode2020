#!/usr/bin/env python
def part_one(rows):
    print("*** PART 1 ***")
    num_seatings = 0
    while True:
        newrows = seat(rows)
        if newrows == rows:
            break
        num_seatings += 1
        rows = newrows

    occupied = count_occupied(rows)
    print(f"It took {num_seatings} seatings to reach a stable pattern, at which {occupied} seats were occupied!")

    return occupied


def count_occupied(rows):
    total = 0
    for row in rows:
        total += row.count('#')
    return total


def get_surrounding_seats(rows, r, c):
    surrounding_seats = []
    for pos in [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c+1), (r+1, c+1), (r+1, c), (r+1, c-1), (r, c-1)]:

        if (pos[0] < 0) or (pos[0] >= len(rows)) or (pos[1] < 0) or (pos[1] >= len(rows[0])):
            surrounding_seats.append('.')
        else:
            surrounding_seats.append(rows[pos[0]][pos[1]])
    return surrounding_seats


def seat(rows):
    newrows = []
    for x, row in enumerate(rows):
        newrows.append([])
        for y, space in enumerate(row):
            if space == '.':
                newrows[x].append('.')
                continue   # floor spaces don't change
            surrounding_seats = get_surrounding_seats(rows, x, y)
            if (space == 'L') and (surrounding_seats.count('#') == 0):
                newrows[x].append('#')
            elif (space == '#') and (surrounding_seats.count('#') >= 4):
                newrows[x].append('L')
            else:
                newrows[x].append(space)

    return newrows


def print_rows(rows):
    for row in rows:
        print(f"{''.join(row)}, [{len(row)}]")


def print_three_rowsets(itera, iterb, iterc):
    print()
    for i, row in enumerate(itera):
        print(f"{''.join(itera[i])} -> {''.join(iterb[i])} ?? {''.join(iterc[i])}")


def test_example_input():
    print("*** EXAMPLE ***")
    with open("../11.example.input.txt", "r") as fp:
        lines = [list(x.strip()) for x in fp.readlines()]
        iterations = [[]]
        i = 0
        for line in lines:
            if len(line) == 0:
                iterations.append([])
                i += 1
                continue
            iterations[i].append(line)
        assert seat(iterations[0]) == iterations[1]
        assert seat(iterations[1]) == iterations[2]
        assert seat(iterations[2]) == iterations[3]
        assert seat(iterations[3]) == iterations[4]
        assert part_one(iterations[0]) == 37


def test_my_input():
    print("*** MY INPUT ***")
    with open("../11.input.txt", "r") as fp:
        lines = [list(x.strip()) for x in fp.readlines()]
        assert part_one(lines) == 2344


if __name__ == "__main__":
    test_example_input()
    test_my_input()
