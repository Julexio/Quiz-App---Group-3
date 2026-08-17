questions = [
    {
    "question": "What is 2 + 2?",
    "A": "3",
    "B": "4",
    "C": "5",
    "D": "HMM",
    "answer": "D"
    },
    {
    "question": "What is 2 + 2?",
    "A": "3",
    "B": "4",
    "C": "5",
    "D": "depende kung 3 yan",
    "answer": "D"
    },
    {
    "question": "What is 2 + 2?",
    "A": "3",
    "B": "4",
    "C": "5",
    "D": "kase kung 3 yan edi ",
    "answer": "D"
    },
    {
    "question": "What is 2 + 2?",
    "A": "3",
    "B": "4",
    "C": "5",
    "D": "FIVE",
    "answer": "B"
    },
    {
    "question": "What is 2 + 2?",
    "A": "3",
    "B": "4",
    "C": "5",
    "D": "SYEMPRE",
    "answer": "B"
    }
]

#test question lang nasa taas 


def start_quiz():
    if len(questions) == 0:
        print("\nYou need to create at least one question first.")
        return
    
    print("          QUIZ START")

    score = 0

    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        print(f"A. {q['A']}")
        print(f"B. {q['B']}")
        print(f"C. {q['C']}")
        print(f"D. {q['D']}")

        while True:
            answer = input("Your answer: ").upper()

            if answer in ["A", "B", "C", "D"]:
                break

            print("Please enter A, B, C, or D.")

        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer: {q['answer']}")

    percentage = (score / len(questions)) * 100

    print("          QUIZ RESULT")
    print(f"Score: {score}/{len(questions)}")
    print(f"Percentage: {percentage:.1f}%")

    if percentage == 100:
        print("Perfect score!")
    elif percentage >= 80:
        print("Excellent!")
    elif percentage >= 60:
        print("Good job!")
    elif percentage >= 50:
        print("You passed!")
    else:
        print("Keep practicing!")

#test call out lang den to

start_quiz()