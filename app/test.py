import time

Ymd = '2018-03-04'
t_unix = time.mktime(time.strptime(Ymd, '%Y-%m-%d'))
print int(t_unix)