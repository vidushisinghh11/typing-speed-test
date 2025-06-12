import tkinter as tk
import time
import random

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


class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("700x450")
        self.root.configure(bg="#f0f0f0")

        self.sentence = ""
        self.start_time = 0

        self.label_title = tk.Label(root, text="Typing Speed Test", font=("Helvetica", 20, "bold"), bg="#f0f0f0")
        self.label_title.pack(pady=10)

        self.label_sentence = tk.Label(root, text="", wraplength=600, font=("Helvetica", 14), bg="#f0f0f0")
        self.label_sentence.pack(pady=10)

        self.text_entry = tk.Text(root, height=6, width=80, font=("Courier", 12))
        self.text_entry.pack(pady=10)
        self.text_entry.bind("<FocusIn>", self.start_timer)

        self.button_submit = tk.Button(root, text="Finish", command=self.calculate_result, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        self.button_submit.pack(pady=5)

        self.button_restart = tk.Button(root, text="Restart", command=self.restart_test, bg="#f44336", fg="white", font=("Helvetica", 12, "bold"))
        self.button_restart.pack(pady=5)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#f0f0f0")
        self.result_label.pack(pady=5)

        self.load_new_sentence()

    def load_new_sentence(self):
        self.sentence = random.choice(sentences)
        self.label_sentence.config(text=self.sentence)
        self.text_entry.delete("1.0", tk.END)
        self.result_label.config(text="")
        self.start_time = 0

    def start_timer(self, event):
        if self.start_time == 0:
            self.start_time = time.time()

    def calculate_result(self):
        end_time = time.time()
        time_taken = end_time - self.start_time
        typed_text = self.text_entry.get("1.0", tk.END).strip()

        word_count = len(typed_text.split())
        wpm = (word_count / time_taken) * 60 if time_taken > 0 else 0

        correct_chars = sum(1 for o, t in zip(self.sentence, typed_text) if o == t)
        accuracy = (correct_chars / len(self.sentence)) * 100 if self.sentence else 0

        self.result_label.config(
            text=f"Typing Speed: {round(wpm, 2)} WPM\nAccuracy: {round(accuracy, 2)}%"
        )

    def restart_test(self):
        self.load_new_sentence()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
