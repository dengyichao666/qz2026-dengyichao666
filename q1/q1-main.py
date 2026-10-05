import json
def analyze_log(filepath):
  """初始化"""
  result = {
            "total":0,
            "by_level":{},
            "by_user":{},
            "last_error":" "
           }
  try:
    with open(filepath,"r",encoding = "utf-8") as f:
      for line in f:
        if not line:
          continue
        try:
          log_data = json.load(line)
          result["total"] +=1
          level = log_data["level"]
          user = log_data["user"]
          if level in result["by_level"]:
            result["by_level"][level] = 1
