# prob link : http://www.spoj.com/problems/AGGRCOW/
def check(target, ls, c):
	length = len(ls)
	cnt = 1
	lst = 0
	for i in range(len(ls)):
		if ls[i]-ls[lst] >= target:
			lst = i
			cnt += 1
	return cnt >= c

t = int(raw_input())
while t:
	t -= 1
	n,c = map(int, raw_input().split())
	ls = []
	for i in range(n):
		pos = int(raw_input())
		ls.append(pos)
	ls.sort()
	lo = 0
	hi = 1000000000
	res = 0
	while lo <= hi:
		mid = (lo + hi)/2
		#print "mid ",mid
		if check(mid, ls, c):
			#print "yes"
			res = mid;
			lo = mid+1
		else:
			#print "no"
			hi = mid-1
	print res


		