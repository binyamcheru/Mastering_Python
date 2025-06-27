# standard library 
import array
import math
import random
import json
from datetime import datetime,timedelta
import time
import re

arr = array.array('i',[1,2,3,4,5])
print(arr[0])
print(math.sqrt(25))

print(random.randint(1,10))
print(random.choice(['option1','option2','option3','option4']))

# data serialization
data = {"name":"John","age":23}
json_str = json.dumps(data)
print(json_str)
print(type(json_str))

parsed_data = json.loads(json_str)
print(parsed_data)
print(type(parsed_data)) 

## datetime
now = datetime.now()
print(now)

yesterday = now-timedelta(days=1)
print(yesterday)

print(time.time())
time.sleep(2)
print(time.time())

# regular expression
pattern = r'\d+'
text = "There are 123 apples 234"
match = re.search(pattern,text)
print(match.group())