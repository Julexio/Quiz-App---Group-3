questions = []


def add_question():
    question = input("Enter question: ")
    choice_a = input("Choice A: ")
    choice_b = input("Choice B: ")
    choice_c = input("Choice C: ")
    choice_d = input("Choice D: ")
    answer = input("Correct answer (A/B/C/D): ").upper()

    questions.append({
        "question": question,
        "choices": {
            "A": choice_a,
            "B": choice_b,
            "C": choice_c,
            "D": choice_d
        },
        "answer": answer
    })

    print("\nQuestion added successfully!\n")


def show_questions():
    if not questions:
        print("\nNo questions added yet.\n")
        return

    print("\n===== QUESTIONS =====")

    for number, q in enumerate(questions, start=1):
        print(f"\nQuestion {number}: {q['question']}")
        print(f"A. {q['choices']['A']}")
        print(f"B. {q['choices']['B']}")
        print(f"C. {q['choices']['C']}")
        print(f"D. {q['choices']['D']}")
        print(f"Correct Answer: {q['answer']}")

    print()


while True:
    print("===== QUESTIONNAIRE MENU =====")
    print("1. Add Question")
    print("2. Stop Adding Questions")
    print("3. Show Questions and Answers")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_question()

    elif choice == "2":
        print("\nStopped adding questions.\n")

    elif choice == "3":
        show_questions()

    elif choice == "4":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice. Please try again.\n")