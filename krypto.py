import itertools, re, sys

PLUS = "+"
MINUS = "-"
DIVIDE = "/"
MULTIPLY = "*"

COMBINATIONS = [
    "((n_n)_n)_n",
    "n_((n_n)_n)",
    "(n_(n_n))_n",
    "n_(n_(n_n))",
    "(n_n)_(n_n)",
]

show_all = False


def format_answer(expression):
    answer = ""

    for character in expression:
        if character in "+-*/":
            answer += " " + character + " "
        else:
            answer += character

    return answer


def compute_all_operations(result, operations=""):
    if len(operations) == 3:
        result.append(operations)
        return

    operations += PLUS
    compute_all_operations(result, operations)

    operations = operations[:-1] + MINUS
    compute_all_operations(result, operations)

    operations = operations[:-1] + MULTIPLY
    compute_all_operations(result, operations)

    operations = operations[:-1] + DIVIDE
    compute_all_operations(result, operations)


def compute_all_combinations(result):
    all_operations = []
    compute_all_operations(all_operations)

    for current_operations in all_operations:
        for combination in COMBINATIONS:
            for operation in current_operations:
                combination = combination.replace("_", operation, 1)

            result.add(combination)


def format_expression(cards, expression, operations):

    for operation in operations:
        expression = expression.replace("_", operation, 1)

    for card in cards:
        expression = expression.replace("n", str(card), 1)

    return expression


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError

    if a % b == 0:
        return a // b

    raise ValueError("Division is not an integer")


def replace_division_expression(expr):
    def replacement(match):
        num1 = match.group(1)
        num2 = match.group(2)
        return f"divide({num1}, {num2})"

    pattern = r"(\d+)/(\d+)"
    return re.sub(pattern, replacement, expr)


def search_solution(cards, target):
    all_combinations, solutions = set(), set()

    compute_all_combinations(all_combinations)

    cards.sort()

    for permuted_cards in itertools.permutations(cards):
        for combination in all_combinations:

            for card in permuted_cards:
                combination = combination.replace("n", str(card), 1)

            try:
                if eval(replace_division_expression(combination)) == target:
                    if not show_all:
                        return [format_answer(combination)]

                    solutions.add(format_answer(combination))
            except ZeroDivisionError:
                pass
            except ValueError:
                pass

    return solutions


def main():
    global show_all
    show_all = "--all" in sys.argv

    cards = [0] * 4
    target = 0

    numbers = input().split()

    for i in range(4):
        cards[i] = int(numbers[i])

    target = int(numbers[4])

    solution = search_solution(cards, target)

    if not solution:
        print("No solution")
        return

    if not show_all:
        print(solution[0] + " = " + str(target))
        return

    for solution in solution:
        print(solution + " = " + str(target))


if __name__ == "__main__":
    main()
