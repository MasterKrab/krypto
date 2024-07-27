import itertools

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
    "(n_n)_n_n",
]


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


def format_expression(cards, expression, operations):

    for operation in operations:
        expression = expression.replace("_", operation, 1)

    for card in cards:
        expression = expression.replace("n", str(card), 1)

    return expression


def search_solution(cards, target):
    all_operations, solutions = [], []

    compute_all_operations(all_operations)

    cards.sort()

    for permuted_cards in itertools.permutations(cards):
        for current_operations in all_operations:
            for combination in COMBINATIONS:
                formatted = format_expression(
                    permuted_cards, combination, current_operations
                )

                try:
                    if eval(formatted) == target:
                        return format_answer(formatted)
                except ZeroDivisionError:
                    pass

    return solutions


def main():
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

    print(solution + " = " + str(target))


if __name__ == "__main__":
    main()
