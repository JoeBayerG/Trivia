import random
import os

file_list = os.listdir("questions")
questions = []
for files in file_list:
    file = open("questions/"+files,"r")
    #hente spørsmål og svar fra tekstdokument
    try:
        for line in file:
            question = line.split("/")
            if question != [""]:
                questions.append(question)
    except:
        pass
score = 0
print("Quiz - Sporsmaal")
name = str(input("Hva er ditt navn: "))
num_questions = int(input("Hvor mange Sporsmasal vil du ha?: "))
print("-----------------------")
#funskjon som skriver ut et spørsmåltemplate.
def questionAsk(spm, ans, cat):
    global score
    print("Sporsmaal nr. " + str(i+1) + " | Kategory: " + cat)
    print(spm)
    user_input = str(input("Svar: "))
    a = 0
    for a in range(len(ans)):
        if user_input.lower() == ans[a].lower():
            score += 1
            print("Riktig!\n")
            return None
    print("Feil, riktig svar er: {}\n".format(ans[0]))
#kaller funskjonen med gitte sted fra arraylisten
for j in range(num_questions):
    i = random.randint(0, len(questions)-2)
    answers = []
    for p in range(2, len(questions[i])-2):
        if questions[i][p] != "" and questions[i][p+1] != questions[i][-1]:
            answers.append(questions[i][p])
    questionAsk(questions[i][-1], answers, questions[i][1])
#printe siste melding
print("{} fikk {}/{} rikitge!".format(name, score, num_questions))
