import re

url = input()
print(re.match('^[http|https]+://[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+[/+a-zA-Z0-9-_.?=]*', url))