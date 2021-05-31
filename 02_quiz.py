# Importing all of the needed things
from tkinter import *
from functools import partial


# First Class this one is the main wireframe that asks all the questions


class Questions:
    def __init__(self):

        # Color That will show up in the background of the wireframe chosen
        background_color = "gold"

        # Frame for main questions
        self.questions_frame = Frame(bg=background_color, padx=10, pady=10)
        self.questions_frame.grid()
        # Heading for quiz
        self.quiz_heading_label = Label(self.questions_frame,
                                        font="11",
                                        bg=background_color, padx=10,
                                        pady=10)
        self.quiz_heading_label.grid(row=0, column=0)
        # Frame from buttons
        self.answers_button_frame = Frame(self.questions_frame)
        self.answers_button_frame.grid(row=2, column=0)
        # Buttons for answers
        self.a_button = Button(self.answers_button_frame,
                               text="A", font=("arial", 18, "bold"),
                               bg="orange", padx=10, pady=10)
        self.a_button.grid(row=3, column=0)
        self.b_button = Button(self.answers_button_frame,
                               text="B", font=("arial", 18, "bold"),
                               bg="light blue", padx=10, pady=10)
        self.b_button.grid(row=3, column=1)
        self.c_button = Button(self.answers_button_frame,
                               text="C", font=("arial", 18, "bold"),
                               bg="green", padx=10, pady=10)
        self.c_button.grid(row=4, column=0)
        self.d_button = Button(self.answers_button_frame,
                               text="D", font=("arial", 18, "bold"),
                               bg="pink", padx=10, pady=10)
        self.d_button.grid(row=4, column=1)
        # First question accepts a and 2013 until a is a button
        self.question_1_label = Label(self.questions_frame, text="When did the last of us 1 come out\n"
                                      "a: 2013 "
                                      "b: 2014 "
                                      "c: 2010 "
                                      "d: 2016", wrap=290, justify=CENTER, bg=background_color,
                                      padx=10, pady=10)
        self.question_1_label.grid(row=1, column=0)
        if self.question_1_label == self.a_button:
            print("Well done that is correct moving onto next question")
            """self.question_2_label.config(state=NORMAL)"""
            self.question_1_label.config(state=DISABLED)
        else:
            print("Sorry that is incorrect it was actually 2013")
            """self.question_2_label.config(state=NORMAL)"""
            self.question_1_label.config(state=DISABLED)
        # Second question accepts c and Real Time Strategy until c is a button
        self.question_2_label = Label(self.questions_frame, text="What does RTS stand for\n"
                                      "a: Ree Toxic Stans "
                                      "b: Real Tab Stigma "
                                      "c: Real Time Strategy "
                                      "d: Reggie Tis Sus", wrap=290, justify=CENTER, bg=background_color,
                                      padx=10, pady=10)
        self.question_2_label.grid(row=1, column=0)
        if self.question_2_label == self.c_button:
            print("Well done that is correct moving onto next question")
            self.question_2_label.config(state=DISABLED)
            """self.question_3_label.config(state=NORMAL)"""
        else:
            print("Sorry that is incorrect it was actually Real Time Strategy")
            self.question_2_label.config(state=DISABLED)
            """self.question_3_label.config(state=NORMAL)"""
        # Third question accepts d and Indian until d is a button
        self.question_3_label = Label(self.questions_frame,
                                      text="What nationality is Dhalism from Street Fighter\n"
                                           "a: Bangladeshi "
                                           "b: Bhutanese "
                                           "c: Japanese "
                                           "d: Indian", wrap=290, justify=CENTER,
                                      bg=background_color, padx=10, pady=10)
        self.question_3_label.grid(row=1, column=0)
        if self.question_3_label == self.d_button:
            print("Well done that is correct moving onto next question")
            self.question_3_label.config(state=DISABLED)
            """self.question_4_label.config(state=NORMAL)"""
        else:
            print("Sorry that is incorrect he's actually Indian")
            self.question_3_label.config(state=DISABLED)
            """self.question_4_label.config(state=NORMAL)"""
        # Fourth question accepts a and Russia until a is a button
        self.question_4_label = Label(self.questions_frame,
                                      text="Where was Tetris made"
                                           "a: Russia "
                                           "b: Belarus "
                                           "c: Poland "
                                           "d: Australia", wrap=290, justify=CENTER,
                                      bg=background_color, padx=10, pady=10)
        self.question_4_label.grid(row=1, column=0)
        if self.question_4_label == self.a_button:
            print("Well done that is correct moving onto next question")
            self.question_4_label.config(state=DISABLED)
            """self.question_5_label.config(state=NORMAL)"""
        else:
            print("Sorry that is incorrect it's actually made in Russia")
            self.question_4_label.config(state=DISABLED)
            """self.question_5_label.config(state=NORMAL)"""
        # Final question accepts b and 100 until b is a button
        self.question_5_label = Label(self.questions_frame, text=
                                      "To the closest 10 what is the score on metacritic for Batman Arkham City PS3"
                                      "a: 90 "
                                      "b: 100 "
                                      "c: 40 "
                                      "d: 70", wrap=290, justify=CENTER,
                                      bg=background_color, padx=10, pady=10)
        self.question_5_label.grid(row=1, column=0)
        if self.question_5_label == self.b_button:
            print("Well done that is correct moving onto next question")
        else:
            print("Sorry that is incorrect it's actually 100 did you get the wrong console?\n"
                  "Thanks for doing my quiz")
        self.answer_checker_label = Label(self.questions_frame, font=("Arial", 12, "bold"),
                                          fg="black", bg=background_color, padx=10, pady=10)
        self.answer_checker_label.grid(row=5, column=0)


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Gaming Quiz")
    something = Questions()
    root.mainloop()
