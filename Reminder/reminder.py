"""" Nhắc nhở uống nước:
    - Chạy trên macOS mà không cần cải đặt thêm gì.
    - Với windows thì tham khảo thêm package: win10toast
    - Lấy code của emoji tại: https://unicode.org/emoji/charts/emoji-list.html
"""

from win10toast import ToastNotifier
import time

notifier = ToastNotifier()

# Setting notify
def gen_notify(titles, texts, sounds="default"):
    notifier.show_toast(f"{titles}", f"{texts}")


# nhập giờ phút giây
def input_time():
    hours = int(input("Giờ: "))
    minutes = int(input("Phút: "))
    seconds = int(input("Giây: "))
    interval = seconds + (minutes * 60) + (hours * 3600)
    print(f"Khoảng thời gian bạn chọn là: {interval} giây")
    return interval


# Lặp lại thông báo
def start_time(interval):
    while True:
        gen_notify(
            "\N{alarm clock} Uống nước đeeeeeeê!",
            "\U0001F595 \U0001F449 Đã đến lúc uống nước \U0001F964 rồi đó mày ơi!\n\U0001F60E Không đừng trách tao \U0001F5E1",
        )
        time.sleep(interval)


if __name__ == "__main__":
    time_interval = input_time()
    start_time(time_interval)
