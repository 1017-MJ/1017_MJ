moringTemp = int(input('아침 최저 기온 : '))
afternoonTemp = int(input('오후 최고 기온 : '))
gapTemp = afternoonTemp - afternoonTemp

if gapTemp >= 10 : print('감기 조심하세요.')
elif afternoonTemp >= 28: print('초여름 날씨입니다.')