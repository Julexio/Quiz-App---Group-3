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


def add_question():
    question = input("Enter question: ")
    choice_a = input("Choice A: ")
    choice_b = input("Choice B: ")
    choice_c = input("Choice C: ")
    choice_d = input("Choice D: ")
    answer = input("Correct answer (A/B/C/D): ").upper()

    questions.append({
        "question": question,
        "A": choice_a,
        "B": choice_b,
        "C": choice_c,
        "D": choice_d,
        "answer": answer
    })

    print("\nQuestion added successfully!\n")


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


def show_result(score, total):
    if total == 0:
        return

    print("\n" + "=" * 30)
    print("          QUIZ RESULT")
    print("=" * 30)
    print(f"You got {score} out of {total} correct!")

    percentage = (score / total) * 100
    print(f"Score Percentage: {percentage:.2f}%")

    if percentage >= 50:
        print("Awesome job! You passed!")
    else:
        print("Keep practicing! You'll get it next time.")
    print("=" * 30)


def start_quiz():
    if len(questions) == 0:
        print("\nYou need to create at least one question first.")
        return

    print("\n          QUIZ START")

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

    show_result(score, len(questions))


def main_menu():
    while True:
        print("\n===== QUIZ APP MENU =====")
        print("1. Add Question")
        print("2. View Questions")
        print("3. Edit Question")
        print("4. Delete Question")
        print("5. Start Quiz")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_question()
        elif choice == "2":
            view_questions()
        elif choice == "3":
            edit_question()
        elif choice == "4":
            delete_question()
        elif choice == "5":
            start_quiz()
        elif choice == "6":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()