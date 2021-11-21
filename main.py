import time
for i in range(30):
  if i % 5 == 0:
	  print("dummo")
  time.sleep(1)
	if i == 1:
		continue 
	print(i, " seconds has passed")
