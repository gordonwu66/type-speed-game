import time, threading

def generateWord():

	return 'word'

def summonWords():
	words.append(generateWord())
	print(words)
	while gameState == True:
		time.sleep(2) # num seconds interval between new words appearing
		words.append(generateWord())
		print(words)

def typeAnswers():
	global gameState
	while gameState == True:
		answer = input()

		for i in range(0, 1):
			if answer == words[i]:
				words.remove(answer)
				print(words)
				if(len(words) == 0):
					gameState = False
				break;

# game
def playGame():
	# data
	score = 0
	
	threadWords = threading.Thread(target = summonWords)
	threadAnswers = threading.Thread(target = typeAnswers)
		
	threadWords.start()
	threadAnswers.start()

	threadWords.join()
	threadAnswers.join()

	print('Game Over!')

words = []
gameState = True

playGame()
	




