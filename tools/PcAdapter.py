import os
import time
from datetime import datetime
import mss
import threading
from pyautogui import screenshot
from screeninfo import get_monitors
from log_util import log_method_call


class PcAdapter:
        monitors_info = None
        screenshotFlag = True

        '''
        撮影準備データ生成
        引数：なし
        戻り値：成功/失敗
        '''
        @log_method_call
        def screenshotPrepare(self):
                PcAdapter.monitors_info = get_monitors()
                if PcAdapter.monitors_info is None:
                        print("screenshotPrepare() error : monitors_info is null")
                        return False
                else:
                        print(PcAdapter.monitors_info)
                        return True

        '''
        撮影
        引数：なし
        戻り値：成功/失敗
        '''
        @log_method_call
        def takeScreenshot(self):
                thread = threading.Thread(target=self.startTakeScreenshot)
                thread.start()
                #self.startTakeScreenshot()

        '''
        撮影開始
        引数：なし
        戻り値：なし
        '''
        @log_method_call
        def startTakeScreenshot(self):
                with mss.mss() as sct:
                        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
                        for i, monitor in enumerate(PcAdapter.monitors_info, start=0):
                                monitor_dict = {
                                        "left": monitor.x,
                                        "top": monitor.y,
                                        "width": monitor.width,
                                        "height": monitor.height
                                }
                                # スクリーンショット撮影
                                screenshot = sct.grab(monitor_dict)
                                screenshot_filename = f"screenshot_monitor_{i+1}_{current_time}.png"
                                # スクリーンショット保存
                                mss.tools.to_png(screenshot.rgb, screenshot.size, output=screenshot_filename)
                                print(f"Screenshot of monitor {i+1} saved as {screenshot_filename}")
                        # 900秒待機
                        time.sleep(900)

