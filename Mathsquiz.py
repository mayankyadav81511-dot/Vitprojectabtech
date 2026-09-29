print("""WELCOME TO MATHS QUIZ, THE AIM OF THE QUIZ IS TO PROVIDE GOOD PRACTICE OF 
ADDITION,SUBTRACTION YOU CAN CHOOSE 
ANYONE TOPIC TO STUDY""")
name=str(input("ENTER YOUR NAME:"))

print("CHOOSE YOUR TOPIC FOR QUIZ:")
print("""1.CHOOSE 1 FOR ADDITION
2.CHOOSE 2 FOR SUBTRACTION
PRESS ENTER TO MAKE CHOICE""")
choice=int(input("ENTER YOUR CHOICE:"))
import random
additions = [
    ["""Q) 1 + 7 =

     a. 21

     b. 8

     c. 52

     d. 6""","b"],
     ["""Q) 7 + 5 =

     a. 14

     b. 12

     c. 6

     d. 7""","b"],
     ["""Q) 4 + 5 =

     a. 6

     b. 7

     c. 9

     d. 10""","c"],
     ["""Q) 7 + 111 =

     a. 118

     b. 117

     c. 118

     d. 119""","a"],
     ["""Q) 3 + 6

     a. 5

     b. 6

     c. 8

     d. 9""","d"],
     ["""Q) 17 + 2 =

     a. 18

     b. 19

     c. 11

     d. 12""","b"],
     ["""Q) 7 + 3 =

     a. 12

     b. 10

     c. 14

     d. 15""","b"],
     ["""Q) 5 + 14 =

     a. 19

     b. 8

     c. 7

     d. 6""","a"],
     ["""Q) 12 + 12 =

     a. 10

     b. 13

     c. 27

     d. 24""","d"],
     ["""Q) 91 + 31 =

     a. 100

     b. 110

     c. 122

     d. 133""","c"],
     ["""Q) 18 + 3 =

     a. 21

     b. 11

     c. 10

     d. 13""","a"],
     ["""Q) 19 + 9 =

     a. 15

     b. 26

     c. 25

     d. 28""","d"],
     ["""Q) 18 + 7 =

     a. 23

     b. 24

     c. 26

     d. 25""","d"],
     ["""Q) 18 + 2 =

     a. 20

     b. 15

     c. 21

     d. 17""","a"],
     ["""Q) 17 + 10 =

     a. 10

     b. 17

     c. 16

     d. 27""","d"],
     ["""Q) 16 + 9 =

     a. 13

     b. 14

     c. 25

     d. 16""","c"],
     ["""Q) 81 + 6 =

     a. 81

     b. 87

     c. 83

     d. 84""","b"],
     ["""Q) 16 + 2 =

     a. 18

     b. 17

     c. 12

     d. 19""","a"],
     ["""Q) 13 + 18 + 13 =

     a. 42

     b. 43

     c. 44

     d. 45""","c"],
     ["""Q) 41 + 42 + 10 + 41 + 58 =

     a. 156

     b. 165

     c. 170

     d. 192""","d"]
     ]
subtraction=[
  ["""Q) 100-5=

  a.95

  b.61

  c.77

  d.89
  ""","a"
  ],
  ["""Q) 160-5=

  a.147

  b.135

  c.125

  d.155""","d"],
  ["""Q) 20-13=

  a.6

  b.7

  c.8

  d.9""","b"],
  ["""Q) 27-7=

  a.10

  b.20

  c.30

  d.40""","b"],
  ["""Q) 17-6=

  a.11

  b.9

  c.10

  d.17""","a"],
  ["""Q) 19-1=

  a.14

  b.15

  c.16

  d.18""","d"],
  ["""Q) 16-7=

  a.11

  b.12

  c.13

  d.9""","d"],
  ["""Q) 14-12=

  a.1

  b.2

  c.3

  d.4""","b"],
  ["""Q) 45-25=

  a.18

  b.19

  c.20

  d.21""","c"],
  ["""Q) 78-6=

  a.71

  b.72

  c.73

  d.74""","b"],
  ["""Q) 100-75=

  a.26

  b.25

  c.28

  d.29""","b"],
  ["""Q) 36-3=

  a.33

  b.32

  c.34

  d.35""","a"],
  ["""Q) 47-2=

  a.44

  b.42

  c.46

  d.45""","d"],
  ["""Q) 54-10=

  a.41

  b.44

  c.43

  d.48""","b"],
  ["""Q) 89-19=

  a.74

  b.64

  c.64

  d.70""","d"],
  ["""Q) 77-44=

  a.45

  b.40

  c.33

  d.44""","c"],
  ["""Q) 120-90=

  a.30

  b.40

  c.20

  d.50""","a"],
  ["""Q) 459-245=

  a.213

  b.212

  c.214

  d.215""","c"],
  ["""Q) 565-543=

  a.22

  b.34

  c.54

  d.64""","a"],
  ["""Q) 890-600=

  a.344

  b.345

  c.290

  d.456""","c"]
]

  


    # Randomize questions


if choice==1:
    

    
     

    # Randomize questions
    random.shuffle(additions)

    correct = 0
    incorrect = 0
    total_questions = 0

    print("QUIZ")
    print("The quiz will end after 3 incorrect answers.\n")

    for   addition in additions:

      # Stop if 3 answers are incorrect
      if incorrect == 3:
        break
   
      print(addition[0])

      answer = input("Your answer: ")

      total_questions += 1

      if answer.lower() == addition[1].lower():
        print("Correct!\n")
        correct += 1
      else:
        print("Incorrect!")
        print("Correct answer:", addition[1])
        print()
        incorrect += 1
elif choice==2:
      random.shuffle(subtraction)
  
      correct = 0
      incorrect = 0
      total_questions = 0
  
      print("QUIZ")
      print("The quiz will end after 3 incorrect answers.\n")
  
      for   subs in subtraction:
  
        # Stop if 3 answers are incorrect
        if incorrect == 3:
          break
     
        print(subs[0])
  
        answer = input("Your answer: ")
  
        total_questions += 1
  
        if answer.lower() == subs[1].lower():
          print("Correct!\n")
          correct += 1
        else:
          print("Incorrect!")
          print("Correct answer:", subs[1])
          print()
          incorrect += 1
elif choice==2:
      random.shuffle(subtraction)
  
      correct = 0
      incorrect = 0
      total_questions = 0
  
      print("QUIZ")
      print("The quiz will end after 3 incorrect answers.\n")
  
      for   subs in subtraction:
  
        # Stop if 3 answers are incorrect
        if incorrect == 3:
          break
     
        print(subs[0])
  
        answer = input("Your answer: ")
  
        total_questions += 1
  
        if answer.lower() == subs[1].lower():
          print("Correct!\n")
          correct += 1
        else:
          print("Incorrect!")
          print("Correct answer:", subs[1])
          print()
          incorrect += 1

          

print("NAME:",name)
print("QUIZ RESULT")
print("Total questions attempted:", total_questions)
print("Correct answers:", correct)
print("Incorrect answers:", incorrect)
