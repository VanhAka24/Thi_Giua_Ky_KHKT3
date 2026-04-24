import matplotlib.pyplot as plt

def manage_inventory():
    inventory = {
        'Balo': 150,
        'Áo khoác': 85,
        'Giày': 120,
        'Mũ': 45
    }
    
    while True:
        print("\n=== MENU QUẢN LÝ KHO ===")
        print("0. Dừng lại")
        print("1. Cập nhật thêm 1 mặt hàng mới")
        print("2. Cập nhật số lượng")
        print("3. Hiển thị biểu đồ")
        
        choice = input("Chọn chức năng: ").strip()
        
        if choice == '0':
            break
            
        elif choice == '1':
            item = input("Nhập tên mặt hàng mới: ").strip()
            if item in inventory:
                print("Mặt hàng đã tồn tại.")
            else:
                try:
                    quantity = int(input("Nhập số lượng: "))
                    inventory[item] = max(0, quantity)
                except ValueError:
                    print("Lỗi định dạng. Vui lòng nhập số nguyên.")
                    
        elif choice == '2':
            item = input("Bạn muốn cập nhật số lượng cho mặt hàng nào?: ").strip()
            if item in inventory:
                try:
                    change = int(input("Cập nhật bao nhiêu?: "))
                    inventory[item] = max(0, inventory[item] + change)
                except ValueError:
                    print("Lỗi định dạng. Vui lòng nhập số nguyên.")
            else:
                print("Mặt hàng không tồn tại.")
                
        elif choice == '3':
            if sum(inventory.values()) == 0:
                print("Kho hàng đang trống hoặc tất cả mặt hàng đều có số lượng 0.")
                continue
                
            labels = list(inventory.keys())
            values = list(inventory.values())
            
            plt.figure(figsize=(7, 7))
            plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
            plt.title("Tỷ trọng hàng hóa trong kho")
            plt.axis('equal')
            plt.show()
            
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn từ 0 đến 3.")

if __name__ == "__main__":
    manage_inventory()