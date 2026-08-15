questions = []

def add_questions():
    global questions
    questions = input("Enter question:")
    choice_a = input("Choice A:")
    choice_b = input("Choice B:")
    choice_c = input("Choice C:")
    choice_d = input("Choice D:")
    answer = input("Correct answer (A/B/C/D):").upper()

    questions.append({
        "question":questions,
        "choices": {
            "A": choice_a,
            "B": choice_b,
            "C": choice_c,
            "D": choice_d
        },
        "answer":answer
    })

    print("Question added succesfully!")


add_questions()