import time, threading, random

def generateWord():

	rand = random.Random()
	num = rand.randint(1, 4)
	
	if num == 1: 
		return 'word'
	elif num == 2:
		return 'hello'
	elif num == 3:
		return 'hi'
	elif num == 4:
		return 'python'

def summonWords():

	words.append(generateWord())
	times.append(5)
	print(words)
	print(times)
	while gameState == True:

		# passage of time and events that occur per second
		time.sleep(1)
		countTime()
		time.sleep(1) # num seconds interval between new words appearing
		countTime()

		words.append(generateWord())
		times.append(5)
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
			


# game
def playGame():
	# data
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

playGame()
	




