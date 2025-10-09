import time
from PcAdapter import PcAdapter
from log_util import log_method_call

from data.CoponaviInputData import CoponaviInputData
from data.AiAnswerData import AiAnswerData

class main:
    #コンストラクタ
    def __init__(self):
        self.mPcAdapter = PcAdapter()

        self.startTime = None

# メイン処理
@log_method_call
def main():
    # 初期化処理
    mPcAdapter = PcAdapter()
    # 撮影データ生成
    result = mPcAdapter.screenshotPrepare()
    if result is False:
        print("screenshotPrepare() error")
        return
    
    coponaviInputData = CoponaviInputData()
    aiAnwerData = AiAnswerData()
    startTime = time.time()
    print(startTime)
    # 撮影開始
    mPcAdapter.takeScreenshot()
    mPcAdapter.screenshotFlag = False

if __name__ == "__main__":
    main()

