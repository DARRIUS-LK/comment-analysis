data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0:
			print(len(data))
print('total no. of reviews',len(data))
sum_len = 0
for d in data:
	sum_len += len(d)
print('average length', sum_len / len(data))
