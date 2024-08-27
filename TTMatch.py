def TTMatch(player1,player2):
	sets=[0,0]
	matchInprogress=1
	while(matchInprogress):
		print(player1+"  "+str(sets[0])+"  -  "+str(sets[1])+"  "+player2)
		print("set "+str(sets[0]+sets[1]+1)+" started")
		gameInprogress=1
		points=[0,0]
		gamewinner=-1
		while(gameInprogress):
			time.sleep(3)
			pointto=random.randint(0,1)
			points[pointto]=points[pointto]+1
			print(player1+"  "+str(points[0])+"  -  "+str(points[1])+"  "+player2)
			if(points[pointto]>10 and (point[0]-point[1]>1 or point[1]-point[0]>1)):
				gameInprogress=0
				gamewinner=pointto
		sets[gamewinner]=sets[gamewinner]+1
		if(sets[gamewinner]==3):
			matchInprogress=0
	print("match completed")

