import logging
from functools import wraps

# ログ設定
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s"
)

# 関数・メソッド呼び出し時にログ出力するデコレーター
def log_method_call(func):
    @wraps(func)
    def wrapper(*args):
        logging.info(f"[IN]{func.__name__}() 引数={args}")
        return func(*args)
    return wrapper

# 使用例
'''
①
from log_util import log_method_callをファイルの頭に付ける
②
メソッドの上に@log_method_callを付ける

例：
from log_util import log_method_call

class PcAdapter:
        monitors_info = None
        screenshotFlag = True
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