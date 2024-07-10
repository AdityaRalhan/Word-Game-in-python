# import time
from PyDictionary import PyDictionary

score = 0

# "il", "er", "an", "nt",
# def timer(seconds = 5):
#     print(f"Timer set for {seconds} seconds.")
#     time.sleep(seconds)
#     print(f"{seconds} seconds are up!")

def dictionary_check(answer):
    dictionary = PyDictionary()
    meaning = dictionary.meaning(answer)
    if meaning is not None:
        return True
    
    else :
        print("Word does not exist")
        return False


def fulfil_condition(answer,question_word):
    parts = question_word[0], question_word[1]

    for i in range(0, len(answer) - 1):
        if answer[i] == parts[0] and answer[i+1] == parts[1]:
            print("Great")
            return True
        
    print("Condition not fulfilled")
    return False

    
question_word_list = ["ee", "ar"]

def display_question():
        global question_word_list
        if question_word_list:
            question_word = question_word_list.pop()
            print(question_word)
            return question_word
        else:
            print("Game over. No more questions left.")
            return None
        

def display_same_question(question_word):
    print(question_word)
    answer = input("ANSWER : ")

    if fulfil_condition(answer, question_word) and dictionary_check(answer):
        note_ans(answer)
        # score += 1
        return True
    
    else :
        display_same_question(question_word)
        


def note_ans(answer):
    with open("answers.txt", "a") as f:
        f.write(answer + '\n')



working = 1
start =  input("Welcome, press s to start the game : ")

if start =="s":
    while start == "s":
        
        while working > 0:
            # while start == "s":
            question_word = display_question()
            

            if question_word:
                answer = input("ANSWER : ")
                if fulfil_condition(answer,question_word) and dictionary_check(answer):
                    print("valid word!")
                    note_ans(answer)
                    # score += 1
                    break

                else:
                    disp_same_q = display_same_question(question_word)

                    if disp_same_q == True:
                        display_question()
                        # score += 1
            
            elif question_word == None:
                start == "end"
                working = 0
                break
                        
                    
else:
    print("Please enter correct character")

   



