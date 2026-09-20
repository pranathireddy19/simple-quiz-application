def run_quiz():
    questions = [
        {
            "question": "Which language is used for Python programming?",
            "options": ["Java", "Python", "C++", "HTML"],
            "answer": "Python"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["func", "define", "def", "function"],
            "answer": "def"
        },
        {
            "question": "Which data type stores multiple values in Python?",
            "options": ["List", "Integer", "Boolean", "Float"],
            "answer": "List"
        },
        {
            "question": "Which symbol is used for comments in Python?",
            "options": ["//", "#", "/*", "--"],
            "answer": "#"
        },
        {
            "question": "Which function is used to display output in Python?",
            "options": ["display()", "show()", "print()", "output()"],
            "answer": "print()"
        }
    ]

    score = 0

    print("===== SIMPLE QUIZ APPLICATION =====")

    for i, q in enumerate(questions, 1):
        print("\nQuestion", i)
        print(q["question"])

        for j, option in enumerate(q["options"], 1):
            print(j, ".", option)

        choice = int(input("Enter your answer (1-4): "))

        if q["options"][choice - 1] == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    print("\n===== QUIZ RESULT =====")
    print("Your score:", score, "/", len(questions))


run_quiz()
