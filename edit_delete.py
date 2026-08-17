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

def view_questions():
    print("          YOUR QUESTIONS")

    if len(questions) == 0:
        print("No questions created yet.")
        return

    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        print(f"  A. {q['A']}")
        print(f"  B. {q['B']}")
        print(f"  C. {q['C']}")
        print(f"  D. {q['D']}")
        print(f"  Correct Answer: {q['answer']}")

def edit_question():
    if len(questions) == 0:
        print("\nThere are no questions to edit.")
        return

    view_questions()

    while True:
        try:
            number = int(input("\nEnter the question number to edit: "))

            if 1 <= number <= len(questions):
                break

            print("Invalid question number.")

        except ValueError:
            print("Please enter a number.")

    q = questions[number - 1]

    print("\n--- Edit Question ---")
    print("Press ENTER if you want to keep the current value.")

    new_question = input(f"Question [{q['question']}]: ")
    if new_question:
        q["question"] = new_question

    new_a = input(f"A [{q['A']}]: ")
    if new_a:
        q["A"] = new_a

    new_b = input(f"B [{q['B']}]: ")
    if new_b:
        q["B"] = new_b

    new_c = input(f"C [{q['C']}]: ")
    if new_c:
        q["C"] = new_c

    new_d = input(f"D [{q['D']}]: ")
    if new_d:
        q["D"] = new_d

    while True:
        new_answer = input(
            f"Correct answer [{q['answer']}] (A/B/C/D): "
        ).upper()

        if new_answer == "":
            break

        if new_answer in ["A", "B", "C", "D"]:
            q["answer"] = new_answer
            break

        print("Invalid answer.")

    print("Question updated successfully!")

def delete_question():
    if len(questions) == 0:
        print("\nThere are no questions to delete.")
        return

    view_questions()

    while True:
        try:
            number = int(input("\nEnter the question number to delete: "))

            if 1 <= number <= len(questions):
                break

            print("Invalid question number.")

        except ValueError:
            print("Please enter a number.")

    deleted = questions.pop(number - 1)

    print(f"Deleted: {deleted['question']}")


edit_question()
delete_question()