"""This file's job is to quiz the user on their video game knowledge."""
# Importing all of the needed things
from tkinter import *
from functools import partial


# First Class this one is the main wireframe that asks all the questions


class Questions:
    """This class' job is to have the questions and their other.

    things like the answers.
    """

    def __init__(self):

        # Color That will show up in the background
        # of the wireframe chosen
        background_color = "gold"
        button_color = "#FFFFFF"
        answer = StringVar()
        answers_1 = ["2013", "2014", "2010", "2016"]
        answers_2 = ["Ree Toxic Stans", "Real Tab Stigma",
                     "Real Time Strategy", "Reggie Tis Sus"]
        answers_3 = ["Bangladeshi", "Bhutanese", "Japanese",
                     "Indian"]
        answers_4 = ["Belarus", "Russia ", "Poland ", "Australia"]
        questions = ["When did The Last of us 1 come out",
                     "What does RTS stand for",
                     "What Nationality is Dhalism from Street Fighter",
                     "What country was Tetris made in"]
        # Frame for main questions
        self.questions_frame = Frame(bg=background_color, padx=10,
                                     pady=10)
        self.questions_frame.grid()
        # Heading for the quiz
        self.quiz_heading_label = Label(self.questions_frame,
                                        font="11", text="Gaming quiz",
                                        bg=background_color, padx=10,
                                        pady=10)
        self.quiz_heading_label.grid(row=0, column=0)
        # Question label for asking
        # question that is selected in drop down menu
        self.question_label = Label(self.questions_frame,
                                    text=questions[0], wrap=290,
                                    justify=CENTER,
                                    bg=background_color, padx=10,
                                    pady=10)
        self.question_label.grid(row=1, column=0)
        # Question four's drop down menu
        self.the_drop_box_4 = OptionMenu(self.questions_frame,
                                         answer, *answers_4)
        self.the_drop_box_4.grid(row=2, column=0)
        self.the_drop_box_4.config(width=30)
        # Question three's drop down menu
        self.the_drop_box_3 = OptionMenu(self.questions_frame,
                                         answer, *answers_3)
        self.the_drop_box_3.grid(row=2, column=0)
        self.the_drop_box_3.config(width=30)
        # Question two's drop down menu
        self.the_drop_box_2 = OptionMenu(self.questions_frame,
                                         answer, *answers_2)
        self.the_drop_box_2.grid(row=2, column=0)
        self.the_drop_box_2.config(width=30)
        # Question one's drop down menu
        self.the_drop_box = OptionMenu(self.questions_frame,
                                       answer, *answers_1)
        self.the_drop_box.grid(row=2, column=0)
        self.the_drop_box.config(width=30)
        # Button to lock in the final answer
        self.submit_button = Button(self.questions_frame, text="Submit",
                                    font=("arial", 18, "bold"),
                                    bg=button_color, padx=10, pady=10,
                                    command=partial(self.answer_function,
                                                    answer, answers_1,
                                                    answers_2, answers_3,
                                                    answers_4, questions))
        self.submit_button.grid(row=3, column=0)
        self.stats_button = Button(self.questions_frame,
                                   font=("arial", 12, "bold"),
                                   text="Statistics",
                                   bg="#F0FFFF", width=25,
                                   command=lambda: self.statistics())
        self.stats_button.grid(row=6, column=0)
    # Function for asking the questions and activating the buttons

    def answer_function(self, answer, answers_1, answers_2,
                        answers_3, answer_4, questions):
        answer = answer.get()
        # If input is blank complain
        if answer == "":
            print("Please enter an answer")
        # Question one is asked here
        elif self.the_drop_box.winfo_exists():
            if answer == answers_1[0]:
                print("Well done that is correct moving onto next question")
                self.question_label.config(text=questions[1])
                self.the_drop_box.destroy()
            else:
                print("Sorry that is incorrect it was actually 2013")
                self.question_label.config(text=questions[1])
                self.the_drop_box.destroy()
        # Question two is asked here
        elif self.the_drop_box_2.winfo_exists():
            if answer == answers_2[2]:
                print("Well done that is correct moving onto next question")
                self.question_label.config(text=questions[2])
                self.the_drop_box_2.destroy()
            elif answer in answers_1:
                print("Please select a new answer")
            else:
                print("Sorry that is incorrect it was actually "
                      "Real Time Strategy")
                self.question_label.config(text=questions[2])
                self.the_drop_box_2.destroy()
        # Question three is asked here
        elif self.the_drop_box_3.winfo_exists():
            if answer == answers_3[3]:
                print("Well done that is correct moving onto next question")
                self.question_label.config(text=questions[3])
                self.the_drop_box_3.destroy()
            elif answer in answers_2:
                print("Please select a new answer")
            else:
                print("Sorry that is incorrect he's actually Indian")
                self.question_label.config(text=questions[3])
                self.the_drop_box_3.destroy()
        # Question four is asked here
        elif self.the_drop_box_4.winfo_exists():
            if answer == answer_4[1]:
                print("Well done that is correct moving onto next question")
                self.the_drop_box_4.destroy()
            elif answer in answers_3:
                print("Please select a new answer")
            else:
                print("Sorry that is incorrect it's actually made in Russia")
                self.the_drop_box_4.destroy()
