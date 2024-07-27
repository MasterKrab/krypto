# Krypto Game Solver

The game consist of 5 cards from 1 to 13 where the player must find a sequence of operations using the first 4 cards to get the value of the 5th card.

## Rules

- The allowed operations are: sum, substraction, multiplication and division.
- Cannot divide by 0.
- Only use integer division.

## Example

Cards: `9 9 10 2 5`, the player must obtain 5 using cards 9, 9, 10 and 2. A solution for this is `((9 - 9) + 10) / 2 = 5`.

## Build

You can use Python Interpreter. The used version for this program was `3.12.2`.

## Usage

```bash
./krypto
1 1 1 1 4
```

And the output is:

```
((1 + 1) + 1) + 1 = 4
```
