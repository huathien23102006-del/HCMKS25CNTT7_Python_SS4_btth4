lucky_number = 79
check = 0
for i in range (5):
    number = int(input("Nhập vào số bạn đoán: "))
    if(number == lucky_number):
        print("Chúc mừng! Bạn đã đoán chính xác mã số may mắn!")
        check = 1
        print("--- TRÒ CHƠI KẾT THÚC ---")
        break

    if (number > lucky_number):
        print("Gợi ý: Số của bạn lớn hơn mã số may mắn!")
    else:
        print("Gợi ý: Số của bạn nhỏ hơn mã số may mắn!")

if check == 0:
    print("Trò chơi kết thúc! Bạn đã hết lượt đoán")