import json
import re
href='src = "security/afafsff/?ip=123.4.56.78&id=45"'
answer=re.findall('\d+\.\d+\.\d+\.\d+',href)
print(answer)
j='{"persons":[{"name":"yu","age":"23"},{"name":"zhang","age":"34"}]}'
j=json.loads(j)
print(j)
print(list(j.values()))
print(list(list(j.items())[0][1][0].values())[0])