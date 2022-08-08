def enter_data():
    """
    Kiểm tra số dương hay không và kiểm tra có phải là số nguyên hay không
    """
    while True:
        n = input("Nhập 1 số nguyên: ")
        if n.isnumeric():
            n = int(n)
            if n > 0:
                print("Đã nhập số dương")
                return n
            print("Đã nhập số không dương. Chương trình sẽ tiếp tục!")
        else:
            print("Dữ liệu đã nhập không phải số nguyên")


enter_data()
