import time
import random

# Sample sentences
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a great language for beginners.",
    "Typing fast is a useful skill to develop.",
    "Practice daily to improve your coding skills.",
    "Code in Place is an amazing learning platform.",
    "Artificial intelligence is transforming the future.",
    "Debugging is twice as hard as writing the code in the first place.",
    "Stay curious, keep learning, and never stop exploring.",
    "The more you practice, the better you become.",
    "Simple code is often the best code.",
    "Reading books can expand your imagination.",
    "Consistency is the key to mastery in any field.",
    "Computers are incredibly fast, accurate, and stupid.",
    "Typing without looking at the keyboard is a superpower.",
    "You can build amazing things with just a few lines of code.",
    "Every programmer was once a beginner.",
    "Errors are opportunities to learn and improve.",
    "The function of good software is to make the complex appear simple.",
    "Coding is not just about syntax, it’s about solving problems.",
    "Never give up — great things take time to build."
]


def calculate_wpm(start_time, end_time, user_input):
    time_taken = end_time - start_time  # in seconds
    word_count = len(user_input.split())
    wpm = (word_count / time_taken) * 60
    return round(wpm, 2)

def calculate_accuracy(original, typed):
    correct = 0
    for o, t in zip(original, typed):
        if o == t:
            correct += 1
    accuracy = (correct / len(original)) * 100
    return round(accuracy, 2)

def typing_test():
    print("----- Typing Speed Test -----\n")
    sentence = random.choice(sentences)
    print("Type the following sentence:\n")
    print("👉", sentence)
    input("\nPress Enter when you are ready to start...")

    start_time = time.time()
    user_input = input("\nStart typing:\n")
    end_time = time.time()

    print("\n--- Results ---")
    wpm = calculate_wpm(start_time, end_time, user_input)
    accuracy = calculate_accuracy(sentence, user_input)

    print(f"Your Typing Speed: {wpm} WPM")
    print(f"Your Accuracy: {accuracy}%")

if __name__ == "__main__":
    typing_test()
