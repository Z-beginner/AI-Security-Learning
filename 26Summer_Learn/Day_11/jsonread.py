from pathlib import Path
import json

#json.loads()
#将json格式的字符串转化为python对象
path = Path('nums.json')
contents = path.read_text()
print(contents)
print(type(contents))
nums = json.loads(contents)
print(nums)
print(type(nums))