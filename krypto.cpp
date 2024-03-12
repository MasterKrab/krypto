#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const char PLUS = '+';
const char MINUS = '-';
const char DIVIDE = '/';
const char MULTIPLY = '*';

string formatAnswer(vector<short> cards, string operations)
{
    string answer = "((";

    for (short i = 0; i < 4; i++)
    {
        answer += to_string(cards[i]);

        if (i >= 1 && i < 3)
            answer += ')';

        if (i < 3)
            answer += ' ';

        answer += operations[i];
        answer += ' ';
    }

    return answer;
}

void computeAllOperations(vector<string> &result, string operations = "")
{
    if (operations.size() == 3)
    {
        result.push_back(operations);
        return;
    }

    operations.push_back(PLUS);
    computeAllOperations(result, operations);

    *operations.rbegin() = MINUS;
    computeAllOperations(result, operations);

    *operations.rbegin() = MULTIPLY;
    computeAllOperations(result, operations);

    *operations.rbegin() = DIVIDE;
    computeAllOperations(result, operations);
}

int calculate(vector<short> cards, string operations)
{
    int result = cards[0];

    for (short i = 1; i < 4; i++)
    {
        char operation = operations[i - 1];
        int card = cards[i];

        if (operation == DIVIDE)
        {
            if (card == 0 || result % card != 0)
                return -1;

            result /= card;
        }

        if (operation == MULTIPLY)
            result *= card;
        else if (operation == PLUS)
            result += card;
        else if (operation == MINUS)
            result -= card;
    }

    return result;
}

vector<string> allOperations;
string searchSolution(vector<short> &cards, int target)
{
    if (allOperations.empty())
        computeAllOperations(allOperations);

    sort(cards.begin(), cards.end());

    do
    {
        for (string currentOperations : allOperations)
            if (calculate(cards, currentOperations) == target)
                return formatAnswer(cards, currentOperations);

    } while (next_permutation(cards.begin(), cards.end()));

    return "";
}

int main()
{
    vector<short> cards(4);
    int target;

    for (short &card : cards)
        cin >> card;

    cin >> target;

    string result = searchSolution(cards, target);

    if (result == "")
    {
        cout << "No solution\n";
        return 0;
    }

    cout << result << "= " << target << '\n';
}
