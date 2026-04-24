import random
import time

def play_game():
    words = ["python", "apple", "river", "student", "teacher"]
    secret_word = random.choice(words)
    guessed = set()
    errors = 0
    max_errors = 5
    start_time = time.time()
    
    while errors < max_errors:
        display = "".join([c if c in guessed else "-" for c in secret_word])
        print(f"Từ: {display} (Sai: {errors}/{max_errors})")
        
        if "-" not in display:
            print("Thắng cuộc!")
            break
            
        char = input("Đoán chữ cái: ").strip().lower()
        if len(char) != 1 or not char.isalpha():
            continue
            
        if char in secret_word:
            guessed.add(char)
        else:
            errors += 1
    else:
        print(f"Thua! Đáp án: {secret_word}")
        
    duration = round(time.time() - start_time, 2)
    with open("game_stats.txt", "a", encoding="utf-8") as f:
        f.write(f"Time: {duration}s | Errors left: {max_errors - errors}\n")

if __name__ == "__main__":
    play_game()