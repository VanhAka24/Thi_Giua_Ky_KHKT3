import string
from collections import Counter

def analyze_text(text):
    translator = str.maketrans('', '', string.punctuation)
    words = text.translate(translator).lower().split()
    
    if not words:
        return
        
    total_words = len(words)
    most_common = Counter(words).most_common(1)[0][0]
    
    print(f"Tổng số từ: {total_words}")
    print(f"Từ xuất hiện nhiều nhất: {most_common}")

if __name__ == "__main__":
    user_input = input("Nhập văn bản: ")
    analyze_text(user_input)