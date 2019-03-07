import itchat
import time
import pandas as pd

df = pd.read_json('output.json')
line_list = df[df.line != '']

itchat.auto_login()


friends = itchat.get_friends()
for f in friends:
    if f.PYQuanPin == 'mixue':
        user = f.UserName

for i in range(10):
    itchat.send(line_list.loc[i].item(), toUserName=user)
    time.sleep(3600)
