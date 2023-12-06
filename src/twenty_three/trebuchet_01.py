from pprint import pprint


def parse(line: str) -> int:
    """Concatenate the first and last number from a string to form a two digit number."""

    digits = [str(n) for n in range(0, 10)]
    nums = [s for s in line if s in digits]
    first, last = nums[0], nums[-1]
    return int(f"{first}{last}")


def solution_one(txt: str) -> int:
    """Sum the array of two digit numbers parsed from the text."""

    nums = [parse(line) for line in txt.split("\n")]
    return sum(nums)


def parse_two(line: str) -> int:
    """
    Concatenate the first and last number from a string to form a two digit number.

    one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
    """

    def first_num(line: str, reverse: bool = False) -> int:
        # Find the first single digit number (numeral or written) and convert to an int
        # When reverse is False, chunk from left -> right
        # Otherwise, chunk from right -> left
        # Note: The order of characters in string is still read left -> right
        # Example
        # >>> first_num("7pqrstsixteen", reverse=True)
        # >>> 6

        numerals = range(1, 10)
        names = [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
        ]
        digit_map = dict(
            zip(
                names,
                numerals,
            )
        )

        start = min(len(n) for n in names)
        stop = len(line)

        # Would it be better to use queues?
        rng = range(stop)
        if reverse:
            rng = rng[::-1]
        for i in rng:
            try:
                return int(line[i])
            except ValueError:
                if reverse:
                    substring = line[i:]
                else:
                    substring = line[: i + 1]
                if len(substring) >= start:
                    # TODO: Only check for names <= len(substring)
                    for name, numeral in digit_map.items():
                        if name in substring:
                            return numeral

    first = first_num(line)
    last = first_num(line, reverse=True)
    return int(f"{first}{last}")


def solution_two(txt: str) -> int:
    nums = [parse_two(line) for line in txt.split("\n")]
    return sum(nums)


def main():
    def read(path):
        with open(path) as f:
            txt = f.read().strip()
        return txt

    stem = "2023_01"

    input_text = dict(
        example=read(f"inputs/{stem}_example.txt"),
        actual=read(f"inputs/{stem}.txt"),
    )

    answers = {
        "part_one": {k: solution_one(v) for k, v in input_text.items()},
        "part_two": {k: solution_two(v) for k, v in input_text.items()},
    }

    pprint(answers)


if __name__ == "__main__":
    main()
