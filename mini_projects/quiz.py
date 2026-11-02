# using lists
questions = [
    "What is the capital of India?",
    "How many days are there in a week?",
    "What is 5 multiplied by 6?",
    "Which planet is known as the Red Planet?"
]

answers = [
    "delhi",
    "7",
    "30",
    "mars"
]

score = 0

for i in range(len(questions)):
    print(questions[i])
    user_answer = input("Your answer: ").strip().lower()

    if user_answer == answers[i]:
        print("Correct!")
        score = score + 1
    else:
        print("Incorrect! The answer is", answers[i])

print("Final score:", score, "out of", len(questions))


#using dictionaries
questions = [
    {
        "question": "What is the capital of India?",
        "answer": "delhi"
    },
    {
        "question": "How many days are there in a week?",
        "answer": "7"
    },
    {
        "question": "What is 5 multiplied by 6?",
        "answer": "30"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "answer": "mars"
    }
]

score = 0

for item in questions:
    print(item["question"])

    user_answer = input("Your answer: ").strip().lower()

    if user_answer == item["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The answer is", item["answer"])

print("Final score:", score, "out of", len(questions))

# Challenges
# 1. Add five questions of the student's choice.
# 2. Award two points for a difficult question.
# 3. Display the percentage score.
# 4. Give a message based on the score.
# 5. Add a category field, such as "Science" or "Maths".
# 6. Count the number of correct and incorrect answers separately.