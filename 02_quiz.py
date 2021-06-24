"""This file's job is to quiz the user on their video game knowledge."""
# Importing all of the needed things
from tkinter import *
from functools import partial

# Global lists for use in stats class
correct_and_incorrect_answers_1 = ["2013", "2014", "2010", "2016"]
correct_and_incorrect_answers_2 = ["Ree Toxic Stans", "Real Tab Stigma",
                                   "Real Time Strategy", "Reggie Tis Sus"]
correct_and_incorrect_answers_3 = ["Bangladeshi", "Bhutanese", "Japanese",
                                   "Indian"]
correct_and_incorrect_answers_4 = ["Belarus", "Russia", "Poland", "Australia"]
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
        # Non global lists for parameters in the later functions
        answers_1 = ["2013", "2014", "2010", "2016"]
        answers_2 = ["Ree Toxic Stans", "Real Tab Stigma",
                     "Real Time Strategy", "Reggie Tis Sus"]
        answers_3 = ["Bangladeshi", "Bhutanese", "Japanese",
                     "Indian"]
        answers_4 = ["Belarus", "Russia", "Poland", "Australia"]
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
                                   text="Statistics", justify=LEFT,
                                   bg="#F0FFFF", width=10,
                                   command=lambda: self.statistics())
        self.stats_button.grid(row=6, column=0)
    # Function for asking the questions and activating the buttons

    def answer_function(self, answer, answers_1, answers_2,
                        answers_3, answers_4, questions):
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
                correct_and_incorrect_answers_1.append("On Question 1: "
                                                       "you got it Correct")
            else:
                print("Sorry that is incorrect it was actually 2013")
                self.question_label.config(text=questions[1])
                self.the_drop_box.destroy()
                correct_and_incorrect_answers_1.append("On Question 1: you "
                                                       "got it Incorrect")
        # Question two is asked here
        elif self.the_drop_box_2.winfo_exists():
            if answer == answers_2[2]:
                print("Well done that is correct moving onto next question")
                self.question_label.config(text=questions[2])
                self.the_drop_box_2.destroy()
                correct_and_incorrect_answers_2.append("On Question 2: "
                                                       "you got it Correct")
            elif answer in answers_1:
                print("Please select a new answer")
            else:
                print("Sorry that is incorrect it was actually "
                      "Real Time Strategy")
                self.question_label.config(text=questions[2])
                self.the_drop_box_2.destroy()
                correct_and_incorrect_answers_2.append("On Question 2: you "
                                                       "got it Incorrect")
        # Question three is asked here
        elif self.the_drop_box_3.winfo_exists():
            if answer == answers_3[3]:
                print("Well done that is correct moving onto next question")
                self.question_label.config(text=questions[3])
                self.the_drop_box_3.destroy()
                correct_and_incorrect_answers_3.append("On Question 3: "
                                                       "you got it Correct")
            elif answer in answers_2:
                print("Please select a new answer")
            else:
                print("Sorry that is incorrect he's actually Indian")
                self.question_label.config(text=questions[3])
                self.the_drop_box_3.destroy()
                correct_and_incorrect_answers_3.append("On Question 3: you "
                                                       "got it Incorrect")
        # Question four is asked here
        elif self.the_drop_box_4.winfo_exists():
            if answer == answers_4[1]:
                print("Well done that is correct moving onto next question")
                self.the_drop_box_4.destroy()
                correct_and_incorrect_answers_4.append("On Question 4: "
                                                       "you got it Correct")
            elif answer in answers_3:
                print("Please select a new answer")
            else:
                print("Sorry that is incorrect it's actually made in Russia")
                self.the_drop_box_4.destroy()
                correct_and_incorrect_answers_4.append("On Question 4: you "
                                                       "got it Incorrect")

    def statistics(self):
        Statistics(self)


class Statistics:
    def __init__(self, partner):
        background_color = "#4682B4"  # Background color for wireframe

        # Answers and questions for the stats function
        answer = StringVar()

        # Disables stats button when the wireframe is up
        partner.stats_button.config(state=DISABLED)

        # Creates box
        self.stats_box = Toplevel()

        # Destroys stats box and re-enables stats button
        self.stats_box.protocol('WM_DELETE_WINDOW',
                                partial(self.close_stats, partner))

        # Frame for the statistics wireframe
        self.stats_frame = Frame(self.stats_box, bg=background_color,
                                 padx=10, pady=10)
        self.stats_frame.grid()
        # Heading for stats wireframe
        self.stats_heading = Label(self.stats_frame, text="Statistics",
                                   font=("times new roman", 17, "bold"),
                                   bg=background_color, fg="white")
        self.stats_heading.grid(row=0, column=0)
        # Text that explains how the wireframe
        self.stats_explanation_label = Label(self.stats_frame,
                                             text="Here is the results of "
                                                  "your questions\n if you "
                                                  "haven't answered any "
                                                  "questions yet\n then "
                                                  "this will be blank\n "
                                                  "or say that you haven't "
                                                  "answered any question yet "
                                                  "\n You can also export "
                                                  "these results to a text "
                                                  "file\n if you click the "
                                                  "export button ",
                                             font=("arial", 12),
                                             justify=CENTER,
                                             bg=background_color, fg="white",
                                             padx=10, pady=10)
        self.stats_explanation_label.grid(row=1, column=0)
        self.stats_label_1 = Label(self.stats_frame, text="",
                                   font=("arial", 14), justify=CENTER,
                                   bg=background_color, fg="white",
                                   padx=10, pady=10)
        self.stats_label_1.grid(row=2, column=0)
        self.stats_label_2 = Label(self.stats_frame, text="",
                                   font=("arial", 14), justify=CENTER,
                                   bg=background_color, fg="white",
                                   padx=10, pady=10)
        self.stats_label_2.grid(row=3, column=0)
        self.stats_label_3 = Label(self.stats_frame, text="",
                                   font=("arial", 14), justify=CENTER,
                                   bg=background_color, fg="white",
                                   padx=10, pady=10)
        self.stats_label_3.grid(row=4, column=0)
        self.stats_label_4 = Label(self.stats_frame, text="",
                                   font=("arial", 14), justify=CENTER,
                                   bg=background_color, fg="white",
                                   padx=10, pady=10)
        self.stats_label_4.grid(row=5, column=0)

        # Question one checked here
        if len(correct_and_incorrect_answers_1) == 5:
            self.stats_label_1.config(text=correct_and_incorrect_answers_1[4])
        else:
            self.stats_label_1.config(text="Question 1: No input entered")
        # Question two answer checked here
        if len(correct_and_incorrect_answers_2) == 5:
            self.stats_label_2.config(text=correct_and_incorrect_answers_2[4])
        else:
            self.stats_label_2.config(text="Question 2: No input Entered")
        # Question three answer checked here
        if len(correct_and_incorrect_answers_3) == 5:
            self.stats_label_3.config(text=correct_and_incorrect_answers_3[4])
        else:
            self.stats_label_3.config(text="Question 3: No input entered")
        # Question four answer checked here
        if len(correct_and_incorrect_answers_4) == 5:
            self.stats_label_4.config(text=correct_and_incorrect_answers_4[4])
        else:
            self.stats_label_4.config(text="Question 4: No input entered")

    def close_stats(self, partner):
        partner.stats_button.config(state=NORMAL)
        self.stats_box.destroy()


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Gaming Quiz")
    something = Questions()
    root.mainloop()
