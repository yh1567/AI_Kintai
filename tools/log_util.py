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