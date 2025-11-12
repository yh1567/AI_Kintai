import tkinter as tk
import threading
import time

ALWAYS_TIMER = "ALWAYS_TIMER"

class TimerProcess:
    def __init__(self, label, button):
        self.mStartTime = None
        self.running = False
        self.timer_thread = None
        self.label = label  # 経過時間表示用ラベル
        self.button = button  # ボタン（開始⇔終了）

    def initTimer(self):
        self.mStartTime = time.time()

    def startTimer(self):
        if not self.running:
            self.initTimer()
            self.running = True
            # ボタンのテキストと動作を「終了」に変更
            self.button.config(text="終了", command=self.stopTimer)
            self.timer_thread = threading.Thread(target=self.run_timer, daemon=True)
            self.timer_thread.start()

    def run_timer(self):
        while self.running:
            current_time = time.time()
            elapsed_seconds = int(current_time - self.mStartTime)
            hours = elapsed_seconds // 3600
            minutes = (elapsed_seconds % 3600) // 60
            seconds = elapsed_seconds % 60
            display_text = f"経過時間：{hours}時間{minutes}分{seconds}秒"
            # GUIのラベルを更新（スレッドセーフにafterで呼び出し）
            self.label.after(0, lambda text=display_text: self.label.config(text=text))
            time.sleep(1)

    def stopTimer(self):
        if self.running:
            self.running = False
            # ボタンのテキストと動作を「開始」に戻す（停止後すぐ切替）
            self.button.config(text="開始", command=self.startTimer)

# --- GUI部分 ---
def main():
    root = tk.Tk()
    root.title("タイマー画面")
    root.geometry("400x200")

    # 経過時間表示ラベル（packで中央下）
    timer_label = tk.Label(root, text="経過時間：0時間0分0秒", font=("Arial", 32))
    timer_label.pack(pady=30)

    # 中央に開始ボタン（packで中央配置）
    start_btn = tk.Button(root, text="開始", font=("Arial", 16))
    start_btn.pack(pady=10)

    # タイマー処理インスタンス生成（ラベルとボタンを渡す）
    timer_proc = TimerProcess(timer_label, start_btn)

    # 開始ボタン押下時の動作を設定
    start_btn.config(command=timer_proc.startTimer)

    root.mainloop()

if __name__ == "__main__":
    main()