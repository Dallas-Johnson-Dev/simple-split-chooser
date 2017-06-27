from random import random
fic_list = []

#Recursively split the array until there is only one element left.
#When a split happens a side is randomly chosen to be used. All other elements are discarded.
#Keep doing this until one is left.
def split_list(anArray):
	#uncomment to see every recursion of the function print to the screen.
	#print(anArray)
	randomIndex = 0
	side = 0 #if side is 0, go left. If side is 1, go right.
	if len(anArray) == 1:
		return anArray[0]
	randomIndex = int(random() * (len(anArray)-1))
	#If our random index is 0: Choose a boolean value of either 0 or 1
	#If we go left just return the value
	#if we go right re-run the array without the first element.
	#do the same but in reverse for the last element.
	side = int((random() * 100)) % 2
	if randomIndex == 0 and side == 0:
		return anArray[0]
	elif randomIndex == len(anArray)-1 and side == 1:
		return anArray[len(anArray)-1]
	else:
		#determine where to split the array and re-run it with the new array
		new_array = []
		if side == 0:
			new_array = anArray[0:randomIndex]
		else:
			new_array = anArray[randomIndex:len(anArray)-1]
		return split_list(new_array)

#Make a list.txt file in the same directory as this script.
#Put each item you want to choose from on its own line.
def read_list_file():
	with open("list.txt","r") as f:
		content = f.readlines()
	return content

if __name__ == "__main__":
	print(split_list(read_list_file()))
