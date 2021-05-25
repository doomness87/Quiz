def questions(question_1, question_2, question_3, question_4, question_5):
    question_1 = input("When did the last of us 1 come out\n"
                       "a: 2013 "
                       "b: 2014 "
                       "c: 2010 "
                       "d: 2016")
    if question_1 != "2013" and "a":
        print("Sorry that is incorrect it was actually 2013")
    else:
        print("Well done that is correct moving onto next question")


print(questions("", "", "", "", ""))
