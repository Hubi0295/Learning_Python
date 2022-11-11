"""
from Chef import Chef
from MasterChef import MasterChef
myChef = Chef()
myChef.make_special()

myMaster = MasterChef()
myMaster.make_master()
myMaster.make_chicken()
"""

"""
from Student import  Student

student1 = Student("Oscar", "Accounting", 3.1)
student2 = Student("Jack", "IT", 4.0)
print(student2.on_honor_roll())
"""

"""
from Question import Question
question_prompts = [
    "pytanie",
    "pytanie2",
    "pytanie3"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score+=1
    print("You got"+ str(score)+ "/" + str(len(questions)) + "Correct")
run_test(questions)
"""
"""
from Student import Student

student1 = Student("Jim", "Bussiness", 3.1, False)
student2 = Student("Tom", "IT", 4.1, True)
print(student2.name)
"""

"""
import usefull_tools
print(usefull_tools.roll_dice(10))
"""

"""
employees_file = open("employees.txt", "r")
for x in employees_file.readlines():
    print(x)
employees_file.close()

employees_append = open("employees.txt", "a")
employees_append.write("\nToby - HR")
employees_append.close()

employees_write = open("employees1.txt", "w")
employees_write.write("Kelly - Service")
employees_write.close()
for x in range(0,3):
    name = "index"+str(x)+".html"
    employees_write = open(name, "w")
    employees_write.write("<html><head></head><body><p>HELLLLO BACK AGAIN MY SHIT FRIEND</p></body></html>")
    employees_write.close()
"""

"""
def podaj():
    try:
        value = 10/0
        number = int(input("Podaj: "))
        print(number)
    except ZeroDivisionError as err:
        print(err)
    except ValueError:
        print("Wrong type")
podaj()
"""

"""
def trans(word):
    translation = ""
    for letter in word:
        if letter in "AEIOUaeiou":
            if letter.islower():
                translation = translation+"g"
            else:
                translation = translation + "G"
        else:
            translation = translation+letter
    return translation
print(trans(input("input word: ")))
"""

"""
word = input("Input word: ")
i = 0
wordd = []
while i<len(word):
    if word[i]=='a' or  word[i]=='e' or word[i]=='o' or word[i]=='l' or word[i]=='u':
        wordd.append("g")
        i+=1
    else:
        wordd.append(word[i])
        i += 1
print(word)
wynik=""
i = 0
while i<len(wordd):
    wynik+=wordd[i]
    i+=1
print(wordd)
print(wynik)
"""

"""
numbers=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
a=0
b=0
x=0
y=0
z=0
while a<len(numbers):
    b=0
    while b<len(numbers[a]):
        print(numbers[a][b])
        b=b+1
    a=a+1
for row in numbers:
    for col in row:
        print(col)
"""

"""
numbers = [0, 1, 2, 3, 4, 5, 5, 135, 3, 5, 32, 523, 4, 23, 4223, 423, 4234, 32, 4, 234, 23, 4, 2343, 24234, 230]
names = ["ted", "bed", "med", "def", "fed", "asf", "gas", "awe", "aas", "afgaf", "asdfa", "gas", "gas",]
print(names)
names.append("teddy")
print(names)
names.insert(0,"teddy")
print(names)
print(names.count("gas"))
names.sort()
numbers.sort()
print(names)
print(numbers)
numbers2=numbers.copy()
numbers2.append(12313)
print(numbers2)
"""
#coordinates = [(4,5, "and"),(2,4,"or")]
#print(coordinates[0])

"""
def calculaotr(a,b,c):
    if c=="+":
        return a+b
    elif c=="-":
        return a-b
    elif c=="*":
        return a*b
    elif c=="/":
        return a/b
    else:
        pass
a = int(input("Input first number: "))
b = int(input("Input secound number: "))
c = input("What do you want to make with those numbers?: ")
print(calculaotr(a,b,c))
"""

"""
monthConvertion = {
    0:"January",
    1:"February",
    2:"March",
    3:"January",
    4:"May",
    5:"June",
    6:"July",
    7:"August",
    8:"Deptember",
    9:"October",
    10:"November",
    11:"December",
}
print(monthConvertion.get(1, "Not a valid key"))
"""

"""
secret_word = "Giraffe"
word = ""
flaga = 0
x=0
def gra(word, guess):
    for x in range(0,3):
        word = input("Guess the word: ")
        if word==secret_word:
            print("Yess this was " + word)
            break
        else:
            if x==2:
                print("you loser! ")
                break
            else:
                print("Nope, try again")
gra(secret_word,word)
"""