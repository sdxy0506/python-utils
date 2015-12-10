
import re,os

fo=file(r"/Users/xuyan/Desktop/qqq111.srt","r")
aContent=fo.readlines()
fo.close()

p=r'(\d\d:\d\d:\d\d)(,\d{3} --> )(\d\d:\d\d:\d\d)(,\d{3})'

aContentTgt=[]

def dbStr(_i):
	if _i<10:
		return '0'+str(_i)
	else:
		return str(_i)

def subTime(_t):
	_h,_m,_s=_t.split(":")
	_sTgt=''
	_time=8
	# if int(_s)-_time<0:
	# 	if int(_m)>0:
	# 		_sTgt+=_h+":"+dbStr(int(_m)-1)+":"+dbStr(int(_s)-_time+60)
	# 	else:
	# 		_sTgt+=dbStr(int(_h)-1)+":"+dbStr(int(_m)-1+60)+":"+dbStr(int(_s)-_time+60)
	# else:
	# 	_sTgt+=_h+":"+_m+":"+dbStr(int(_s)-_time)

	if int(_s)+_time>=60:
		if int(_m)<59:
			_sTgt+=_h+":"+dbStr(int(_m)+1)+":"+dbStr(int(_s)+_time-60)
		else:
			_sTgt+=dbStr(int(_h)+1)+":"+dbStr(int(_m)+1-60)+":"+dbStr(int(_s)+_time-60)
	else:
		_sTgt+=_h+":"+_m+":"+dbStr(int(_s)+_time)

	return _sTgt
    
for ln in aContent:
	m=re.search(p,ln)
	if m:
		t1,v1,t2,v2=m.group(1,2,3,4)
		aContentTgt.extend(subTime(t1)+v1+subTime(t2)+v2+"\n")
	else:
		aContentTgt.extend(ln)

ft=file(r"/Users/xuyan/Desktop/qwe222.srt",'w')
ft.writelines(aContentTgt)
ft.close()