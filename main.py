import time
for i in range(30):
  if i % 5 == 0:
	  print("Andrew")
  time.sleep(1)
	if i == 1:
		print("1 second has passed")
		continue 
	print(i, " seconds has passed")
