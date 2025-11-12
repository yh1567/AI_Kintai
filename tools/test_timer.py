from TimerManager import TimerProcess

if __name__ == "__main__":
    # TimerProcessインスタンス生成
    timer = TimerProcess()
    
    # タイマー初期化（開始時刻をセット）
    timer.initTimer()
    
    # タイマー開始（サブスレッドで経過時間を表示し続ける）
    timer.startTimer()
    
    # メインスレッドで5秒待つ（その間サブスレッドが動く）
    time.sleep(5)
    
    # タイマー停止（サブスレッド終了まで待つ）
    timer.stopTimer()
    
    print("タイマー終了")