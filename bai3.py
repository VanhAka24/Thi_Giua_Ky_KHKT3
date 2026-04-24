def calculate_bmi():
    try:
        weight = float(input("Nhập cân nặng (kg): "))
        height = float(input("Nhập chiều cao (m): "))
        
        bmi = weight / (height ** 2)
        
        if bmi < 18.5:
            status = "Gầy"
        elif 18.5 <= bmi <= 24.9:
            status = "Bình thường"
        else:
            status = "Thừa cân"
            
        print(f"BMI: {bmi:.2f} - Kết quả: {status}")
        
    except ValueError:
        print("Lỗi: Dữ liệu nhập vào phải là số.")
    except ZeroDivisionError:
        print("Lỗi: Chiều cao phải lớn hơn 0.")

if __name__ == "__main__":
    calculate_bmi()