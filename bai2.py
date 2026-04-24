import re
from collections import Counter

def analyze_text(text):
    clean_text = re.sub(r'[^\w\s]', '', text).lower()
    words = clean_text.split()
    
    if not words:
        return
        
    total_words = len(words)
    most_common_word, frequency = Counter(words).most_common(1)[0]
    
    print(f"Tổng số từ: {total_words}")
    print(f"Từ xuất hiện nhiều nhất: {most_common_word} ({frequency} lần)")

if __name__ == "__main__":
    user_input = input("Nhập văn bản: ")
    analyze_text(user_input)