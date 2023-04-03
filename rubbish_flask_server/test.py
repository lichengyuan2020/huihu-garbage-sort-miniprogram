import datetime
today=datetime.date.today()
today=today.strftime('%Y/%m/%d')
yesterday=(datetime.date.today()+datetime.timedelta(days=0)).strftime('%Y/%m/%d')
print(yesterday)