import threading      # スレッド（並列処理）を使うためのモジュール
import time           # 時間管理（現在時刻、スリープなど）用モジュール

ALWAYS_TIMER = "ALWAYS_TIMER"   # タイマーID（定数）

class TimerProcess:             # タイマー処理をまとめたクラス
    def __init__(self):
        self.mStartTime = None          # タイマー開始時刻を保存する変数
        self.timer_thread = None        # サブスレッド用の変数
        self.running = False            # タイマーが動作中かどうかのフラグ

    def initTimer(self):
        self.mStartTime = time.time()   # 現在時刻を取得して保存（タイマー初期化）

    def startTimer(self, timer_id=ALWAYS_TIMER):
        if timer_id == ALWAYS_TIMER:    # 指定IDが常時タイマーなら
            self.running = True         # 動作フラグON
            self.timer_thread = threading.Thread(target=self.run_timer)  # サブスレッド生成
            self.timer_thread.start()   # サブスレッド開始

    def run_timer(self):
        while self.running:                     # フラグがTrueの間、繰り返す
            current_time = time.time()          # 現在時刻取得
            elapsed = current_time - self.mStartTime  # 経過時間計算
            print(f"[{ALWAYS_TIMER}] 経過時間: {elapsed:.2f}秒")  # 経過時間表示
            time.sleep(1)                       # 1秒待機（周期的に動作）

    def stopTimer(self):
        self.running = False                    # 動作フラグOFFでループ終了
        if self.timer_thread is not None:       # サブスレッドがあれば
            self.timer_thread.join()            # サブスレッド終了まで待つ