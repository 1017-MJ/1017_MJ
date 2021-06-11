userMessage= input('메세지를 입력하세요. ')
MsgLen = len(userMessage)
if MsgLen <= 50:
    print('SMS 발송')
else:
    print('MMS 발송')
    
print('메세지 길이: ', MsgLen)