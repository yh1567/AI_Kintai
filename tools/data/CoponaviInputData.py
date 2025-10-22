import sys
sys.path.append('d:/AI_Kintai/AI_Kintai/tools')

#data/CoponaviInputData.py

class CoponaviInputData:
    def __init__(self):
        #プロジェクト名
        self.pj = None
        #プロセスコード
        self.process = None
        #プロセス明細
        self.details = None
        #備考
        self.note = None
        #作業時間
        self.time = None