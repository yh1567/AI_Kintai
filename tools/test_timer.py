# test_timer.py

from TimerManager import TimerProcess
import time

# TimerProcessのインスタンス生成
timer = TimerProcess()

# タイマー開始
timer.start()

# 5回カウントアップしてみる
for _ in range(5):
    timer.tick()
    time.sleep(1)  # 1秒待つ（タイマー感覚を出すため）

print(f"最終カウント値: {timer.get_count()}")