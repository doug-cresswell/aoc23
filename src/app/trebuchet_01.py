def parse(line: str) -> int:
    """Concatenate the first and last number from a string to form a two digit number."""

    digits = [str(n) for n in range(0, 10)]
    nums = [s for s in line if s in digits]
    first, last = nums[0], nums[-1]
    return int(f"{first}{last}")


def solution(text: str) -> int:
    """Sum the array of two digit numbers parsed from the text."""

    nums = [parse(line) for line in text.split("\n")]
    return sum(nums)
