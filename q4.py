START_CURLY = '{'
START_BOX = '['
START_ROUND = '('
END_CURLY = '}'
END_BOX = ']'
END_ROUND = ')'

PAIR = {
    START_ROUND: END_ROUND,
    END_ROUND: START_ROUND,
    START_BOX: END_BOX,
    END_BOX: START_BOX,
    START_CURLY: END_CURLY,
    END_CURLY: START_CURLY
}

ALL_BRACKETS = [START_ROUND, START_BOX, START_CURLY, END_ROUND, END_CURLY, END_BOX]
START_BRACKETS = [START_ROUND, START_BOX, START_CURLY]
END_BRACKETS = [END_ROUND, END_BOX, END_CURLY]


def brackets_ok(string_brackets: str) -> bool:
    state = []
    for i, char in enumerate(string_brackets):
        if i == 0 and char not in START_BRACKETS:
            return False
        if char in START_BRACKETS:
            state.append(char)
        if char in END_BRACKETS:
            if PAIR[state[-1]] == char:
                state.pop()
            else:
                return False
    return len(state) == 0


print(brackets_ok("{(])}"))
print(brackets_ok("{([)]}"))
print(brackets_ok("{[]}"))
