from pathlib import Path
import json

#json.dumps()
#将数据转换为json格式
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
path = Path('nums.json')
contents = json.dumps(nums)
path.write_text(contents)