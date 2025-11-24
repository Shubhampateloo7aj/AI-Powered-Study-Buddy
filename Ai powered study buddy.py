import time

# Sample flashcards (question: answer)
flashcards = {
    "What is the capital of India?": "New Delhi",
    "What is 2 + 2?": "4",
    "Who wrote 'Hamlet'?": "Shakespeare",
    "What is Python?": "Programming language"
}

# Spaced repetition intervals in seconds (for demo, normally in days)
intervals = [5, 10, 20]  # times to wait before repeating a question

# Track flashcard states: 0 means new/incorrect, index in intervals means repetition step
flashcard_states = {q: 0 for q in flashcards}

def quiz():
    while True:
        for question, answer in flashcards.items():
            state = flashcard_states[question]
            # Ask question based on state (0=ask immediately, else check time)
            print(f"Question: {question}")
            user_answer = input("Your answer: ").strip()
            if user_answer.lower() == answer.lower():
                print("Correct! Well done.")
                if state < len(intervals):
                    flashcard_states[question] = state + 1  # move to next interval
                else:
                    flashcard_states[question] = state
            else:
                print(f"Wrong! The correct answer is '{answer}'. Let's try again later.")
                flashcard_states[question] = 0  # reset repetition on wrong answer
            print()
            time.sleep(1)
        
        # Check if all flashcards are learned (max interval reached)
        all_done = all(state == len(intervals) for state in flashcard_states.values())
        if all_done:
            print("Congratulations! You have mastered all flashcards.")
            break

if __name__ == "__main__":
    print("Welcome to the AI-Powered Study Buddy!")
    print("Try to answer the questions. Let's start!\n")
    quiz()
