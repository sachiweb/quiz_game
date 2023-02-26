def new_game():
    question_number=1
    correct_guesses=0
    total_scored=0
    guesses=[]
    for key in question:
        print("------------------------------------------------------------------------")
        print(key)
        for i in options[question_number-1]:
            print(i)
        guess=input("chose a option from(A,B,C or D):").upper()
        guesses.append(guess)
        total_scored+=match_answer(question.get(key),guess)
        question_number+=1
    print("answer:")
    for i in question:
         
         print(question.get(i),end=" ")
    print("guesses:")
    for i in guesses:
         
         print(i,end=" ")
    display_score(total_scored,question,guesses)


def match_answer(answer,guesses):
    if answer==guesses:
        return 1
    else:
        return 0

def display_score(total_scored,question,guesses):
    score=int(total_scored/len(question)*100)
    print(score,"%")
def play_again():
    new_game()

total_scored=0

question={"who is the pm of india:":"A",
"cricket created by which country:":"D",
"what is sum of 3 and 4:":"A",
"statue of liberty situeted in where:":"B"
}
options=[
    ["A=n.d.d.modi","B=s.k.rajib","C=m.s.lochan","D=d.s.raman"],
    ["A=india","B=japan","C=chin","D=england"],
    ["A=7","B=4","C=1","D=9"],
    ["A=afganistan","B=america","C=india","D=maxico"]
    ]

new_game()
print("do you want to play again(yes or no):")
x=input().lower()
if x=="yes":
    new_game()
else:
    print("byeee!")