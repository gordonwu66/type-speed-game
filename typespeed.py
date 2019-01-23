import time, threading, random, csv

def generateWord():
	filename = 'words/' +difficulty +'.csv'
	file = open(filename)
	reader = csv.reader(file)
	wordsList = list(reader)
	size = len(wordsList[0])

	rand = random.Random()
	num = rand.randint(0, size - 1)

	return wordsList[0][num]

def summonWords():

	global timeInterval
	words.append(generateWord())
	times.append(timeInterval * 2)
	print(words)
	print(times)
	while gameState == True:

		#passage of time
		for i in range(0, timeInterval):
			time.sleep(1)
			countTime()

		words.append(generateWord())
		times.append(timeInterval * 2) # num seconds duration for each word
		print(words)
		print(times)

def typeAnswers(wordPoints):
	score = 0

	while gameState == True:
		answer = input()

		if len(words) > 0:
			if answer == words[0]:
				words.remove(words[0])
				times.remove(times[0])
				print(words)
				print(times)
				score += wordPoints

	print('Score: ' +str(score))

def countTime(): # Another thread?

	global gameState
	for i in range(0, len(times)):
		times[i] -= 1
		if times[i] == 0:
			gameState = False
			print('Game Over! Enter anything to end and see score: ')
			

def main():
	#setup
	global difficulty
	global speed
	global timeInterval
	print('Choose word difficulty (Easy, Medium, Hard): ')
	difficulty = input()
	if not (difficulty == 'Easy' or difficulty == 'Medium' or difficulty == 'Hard'):
		print('Input not recognized, difficulty has been set to Easy by default.')
		difficulty = 'Easy'

	print('Choose speed (Slow, Normal, Fast, Lightning): ')
	speed = input()
	if not (speed == 'Slow' or speed == 'Normal' or speed == 'Fast' or speed == 'Lightning'):
		print('Input not recognized, speed has been set to Slow by default.')
		speed = 'Slow'

	if speed == 'Slow':
		timeInterval = 6
	elif speed == 'Normal':
		timeInterval = 4
	elif speed == 'Fast':
		timeInterval = 2
	elif speed == 'Lightning':
		speed == 1

	wordPoints = 100
	
	threadWords = threading.Thread(target = summonWords)
	threadAnswers = threading.Thread(target = typeAnswers, args = [wordPoints])
		
	threadWords.start()
	threadAnswers.start()

	threadWords.join()
	threadAnswers.join()

words = []
times = []
gameState = True
difficulty = 'Easy'
speed = 'Slow'
timeInterval = 6

main()