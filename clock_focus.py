import time

def countdown(minutes):
    total_seconds = minutes * 60
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1

def focus_timer():
    print("专注开始！你有25分钟时间。")
    countdown(25)
    print("时间到！休息5分钟吧。")
    countdown(5)
    print("休息结束！准备好进入下一轮专注了吗？")

if __name__ == "__main__":
    focus_timer()
