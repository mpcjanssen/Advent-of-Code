import numpy as np

import aoc_helper
from aoc_helper.utils import extract_ints

RAW = aoc_helper.day(4)

def parse_raw():
    numbers, *boards = RAW.split("\n\n")

    return (
        tuple(extract_ints(numbers)),
        np.array(
            [np.fromiter(extract_ints(board), dtype=int) for board in boards]
        ).reshape(-1, 5, 5),
    )

NUMBERS, BOARDS = parse_raw()

def part_one():
    boards = BOARDS.copy()

    for number in NUMBERS:
        boards[boards == number] = -1

        for i in range(10):
            winners = np.all(boards[:, i//2] == -1, axis=1)

            if winners.any():
                boards[boards == -1] = 0
                return boards[winners.argmax()].sum() * number

            boards = np.swapaxes(boards, 1, 2)

def part_two():
    boards = BOARDS.copy()

    for number in NUMBERS:
        boards[boards == number] = -1

        for i in range(10):
            winners = np.all(boards[:, i//2] == -1, axis=1)

            if len(boards) > 1:
                boards = boards[~winners]
            elif winners[0]:
                boards[boards == -1] = 0
                return boards.sum() * number

            boards = np.swapaxes(boards, 1, 2)

aoc_helper.submit(4, part_one)
aoc_helper.submit(4, part_two)
