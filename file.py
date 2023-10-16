#You must write a comment for every chunk of code you write from now on along with your author tag***
#4-6
#Create a Python file named lab_4-6.py
#Write a program that asks for user input for an animal and a dish. 
print("please give us a animal and a dish")
animal = input("animal")
dish = input("dish")
#Your program should print true or false to indicate whether the beast is allowed to bring the dish to the feast 
#(the first letter of the animal is the same as the first and last letter of the dish).
#Assume that beast and dish are always lowercase strings, and that each has at least two letters. 
#beast and dish may contain hyphens and spaces, but these will not appear at the beginning or end of the string. They will not contain numbers.
print(True if animal[0] == dish[0] and animal[0] == dish[len(dish)-1] else False)
#_________________________________________________

4-7
#Create a Python file named lab_4-7.py
#Write a program that prompts a uses 5 inputs to prompt a user for a number. 
print("please give me 5 numbers")
one = input ("first number")  
two = input ("next number")
three = input ("next number")
four = input ("next number")
five = input ("next number")
#Store all numbers as a single string with a space in between each numbers
allnum = (f"{one} {two} {three} {four} {five}") 
#(i.e num_string = ‘1 2 3 4 5’). Print this string. Using string methods, 
print (allnum)
#extract the smallest and largest number from the string & print them,
i=0
big = int(allnum[0])
small = int(allnum[0]
while i < len(allnum):
    if big < int(allnum[i]):
        big = i
    i += 2
    
print(big)    
#with a label (i.e smallest num given was 1). 
#Print the product of the two numbers you have extracted, with a label (i.e. the product of the two numbers extracted was 5).


#___________________________________________________

4-8
#Create a Python file named lab_4-8.py
#Write a program that prompts a use to enter a 6 letter sequence of DNA. (a series of a,c,t,g) 
#Print out the complementary DNA sequence (a – t, c – g). 
#You can assume all inputs are valid and lowercase

