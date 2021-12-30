from datetime import datetime
text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
print(y)