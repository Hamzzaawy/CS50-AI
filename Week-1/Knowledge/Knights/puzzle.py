from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # data from the problem description
    Or(AKnight, AKnave),
    Not(And(AKnave, AKnight)),
    # data from the puzzle 0 description
    Implication(And(AKnight, AKnave) , AKnight),
    Implication(Not(And(AKnight, AKnave)) , AKnave)

)
# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # data from the problem description
    Or(AKnight, AKnave),
    Not(And(AKnave, AKnight)),
    Or(BKnight, BKnave), 
    Not(And(BKnave, BKnight)),

    # data from the puzzle 1 description
    Biconditional(AKnight, And(AKnave, BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # data from the problem description
    Or(AKnight, AKnave),
    Not(And(AKnave, AKnight)),
    Or(BKnight, BKnave), 
    Not(And(BKnave, BKnight)),

    # data from the puzzle 2 description
    Biconditional(AKnight, Or(And(AKnave, BKnave), And(AKnight, BKnight))),
    Biconditional(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight)))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # data from the problem description
    Or(AKnight, AKnave),
    Not(And(AKnave, AKnight)),
    Or(BKnight, BKnave), 
    Not(And(BKnave, BKnight)),
    Or(CKnight, CKnave), 
    Not(And(CKnave, CKnight)),

    # data from the puzzle 3 description
    Biconditional(Or(AKnight, AKnight), Or(AKnight, AKnave)),
    Biconditional(BKnight, AKnave),
    Biconditional(BKnight, CKnave), 
    Biconditional(CKnight, AKnight)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
