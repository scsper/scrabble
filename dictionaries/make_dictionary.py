twl_file = open('twl.txt', 'r')
unix_file = open('unix.txt', 'r')
common_file = open('common.txt', 'w')

twl = set()
unix = set()


for word in twl_file:
	twl.add(word)

for word in unix_file:
	unix.add(word)


common_set = twl & unix
common = []

for word in common_set:
	common.append(word)

common.sort()

for word in common:
	common_file.write(word)
