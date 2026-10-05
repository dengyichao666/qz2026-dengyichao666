import json
def analyze_log(filepath):
  """初始化"""
  result = {
            "total":0,
            "by_level":{},
            "by_user":{},
            "last_error":" "
           }
