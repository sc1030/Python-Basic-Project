'''qestions= {
    "What is 25*25?": "625",
    "what is the capital of the France?": "Paris",
    "What is Python?": "Programming Language"
}

score = 0

for q , a in questions.items():
    user_answer = input(q + " ")
    if user_answer.lower() == a.lower():
        print("Correct")
        score += 1
    else:
        print("Wrong, the correct answer is " + a)
        print("Your score is: " + str(score) + "/" + str(len(questions)))
       '''   

import random
import time

# Dictionary with questions and multiple-choice answers
questions = {
    "What is 2+2?": {"options": ["3", "4", "5", "6"], "answer": "4"},
    "What is the capital of France?": {"options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": "Paris"},
    "What is Python?": {"options": ["Snake", "Car", "Programming Language", "Fruit"], "answer": "Programming Language"},
    "Who wrote 'Hamlet'?": {"options": ["Shakespeare", "Dickens", "Hemingway", "Austen"], "answer": "Shakespeare"},
    "What is the square root of 16?": {"options": ["2", "4", "8", "16"], "answer": "4"}
}

score = 0
total_questions = len(questions)

# Randomize question order
shuffled_questions = list(questions.items())
random.shuffle(shuffled_questions)

# Start quiz
for q, data in shuffled_questions:
    print("\n" + q)
    
    # Shuffle options
    options = data["options"]
    random.shuffle(options)
    
    # Display multiple-choice options
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    # Timer starts
    start_time = time.time()
    
    # Get user answer
    try:
        user_choice = int(input("Enter the option number: "))
        user_answer = options[user_choice - 1]
    except (ValueError, IndexError):
        print("Invalid choice! Moving to next question.")
        continue
    
    # Check if the answer is correct
    if user_answer.lower() == data["answer"].lower():
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was: {data['answer']}")
    
    # Timer ends
    elapsed_time = round(time.time() - start_time, 2)
    print(f"⏳ Time taken: {elapsed_time} seconds")

# Final score
percentage = (score / total_questions) * 100
print(f"\n🎯 Your final score: {score}/{total_questions} ({percentage:.2f}%)")

# Feedback based on performance
if percentage == 100:
    print("🏆 Excellent! You got all answers right!")
elif percentage >= 70:
    print("👏 Good job! You have a strong grasp of the material.")
elif percentage >= 50:
    print("🙂 Not bad! A little more practice and you'll ace it!")
else:
    print("😕 Keep practicing! You'll get better with time.")

