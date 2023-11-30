import random

name ="Asd"
question = "Am I going to live forever?"
answer = ""
random_number = random.randint(1, 12)
#print(random_number)

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "This bitch bumb af"
elif random_number == 11:
  answer = "Yes, honey"
elif random_number == 12:
  answer = "Of course my horse"
else:
  answer = "Error"

if len(name) == 0:
  print("Question: " + question)
  print("Magic-8-Ball's answer:", answer) 
elif len(question) == 0:
    print("The fabric of reality is at risk!")
else:
  print(name, "asks:", question)
  print("Magic 8-Ball's answer:", answer)  

 