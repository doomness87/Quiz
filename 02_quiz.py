"""This file's job is to quiz the user on their video game knowledge."""
# Importing all of the needed things
from tkinter import *
from functools import partial
import re

# Global lists for use in stats class
correct_and_incorrect_answers_1 = ["2013", "2014", "2010", "2016"]
correct_and_incorrect_answers_2 = ["Ree Toxic Stans", "Real Tab Stigma",
                                   "Real Time Strategy", "Reggie Tis Sus"]
correct_and_incorrect_answers_3 = ["Bangladeshi", "Bhutanese", "Japanese",
                                   "Indian"]
correct_and_incorrect_answers_4 = ["Belarus", "Russia", "Poland", "Australia"]
statistics_for_export = []
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
                                   font=("time new roman", 17, "bold"),
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
        # Results for question 1
        self.stats_label_1 = Label(self.stats_frame, text="",
                                   font=("arial", 14), justify=CENTER,
                                   bg=background_color, fg="white",
                                   padx=10, pady=10)
        self.stats_label_1.grid(row=2, column=0)
        # Results for question 2
        self.stats_label_2 = Label(self.stats_frame, text="",
                                   font=("arial", 14), justify=CENTER,
                                   bg=background_color, fg="white",
                                   padx=10, pady=10)
        self.stats_label_2.grid(row=3, column=0)
        # Results for question 3
        self.stats_label_3 = Label(self.stats_frame, text="",
                                   font=("arial", 14), justify=CENTER,
                                   bg=background_color, fg="white",
                                   padx=10, pady=10)
        self.stats_label_3.grid(row=4, column=0)
        # Results for question 4
        self.stats_label_4 = Label(self.stats_frame, text="",
                                   font=("arial", 14), justify=CENTER,
                                   bg=background_color, fg="white",
                                   padx=10, pady=10)
        self.stats_label_4.grid(row=5, column=0)
        # Button for the export class calling the functions
        # that calls the class
        self.export_button = Button(self.stats_frame, text="Export to file",
                                    font=("arial", 10, "bold"),
                                    command=lambda: self.export())
        self.export_button.grid(row=6, column=0)
        # Button for destroying stats after not needed
        self.dismiss_button = Button(self.stats_frame, text="Dismiss",
                                     font=("arial", 10, "bold"),
                                     command=partial(self.close_stats, partner))
        self.dismiss_button.grid(row=6, column=1)

        # Question one checked here
        if len(correct_and_incorrect_answers_1) == 5:
            self.stats_label_1.config(text=correct_and_incorrect_answers_1[4])
            statistics_for_export.append(correct_and_incorrect_answers_1[4])
        else:
            self.stats_label_1.config(text="Question 1: No input entered")
        # Question two answer checked here
        if len(correct_and_incorrect_answers_2) == 5:
            self.stats_label_2.config(text=correct_and_incorrect_answers_2[4])
            statistics_for_export.append(correct_and_incorrect_answers_2[4])
        else:
            self.stats_label_2.config(text="Question 2: No input Entered")
        # Question three answer checked here
        if len(correct_and_incorrect_answers_3) == 5:
            self.stats_label_3.config(text=correct_and_incorrect_answers_3[4])
            statistics_for_export.append(correct_and_incorrect_answers_3[4])
        else:
            self.stats_label_3.config(text="Question 3: No input entered")
        # Question four answer checked here
        if len(correct_and_incorrect_answers_4) == 5:
            self.stats_label_4.config(text=correct_and_incorrect_answers_4[4])
            statistics_for_export.append(correct_and_incorrect_answers_4[4])
        else:
            self.stats_label_4.config(text="Question 4: No input entered")

    def close_stats(self, partner):
        partner.stats_button.config(state=NORMAL)
        self.stats_box.destroy()

    def export(self):
        Export(self)


class Export:
    def __init__(self, partner):

        print(statistics_for_export)

        background_color = "#8b0000"  # Color is dark red same as wireframe

        # Disabling button while inside export thing
        partner.export_button.config(state=DISABLED)
        # Export window
        self.export_box = Toplevel()
        # If user closes the box with the x button it will close
        self.export_box.protocol('WM_DELETE_WINDOW',
                                 partial(self.close_export, partner))
        # Frame for all of the export labels and buttons etc
        self.export_frame = Frame(self.export_box, width=200,
                                  bg=background_color)
        self.export_frame.grid()
        # Export heading for top of wireframe
        self.export_heading = Label(self.export_frame, text="Export",
                                    font=("arial", 14, "bold"), fg="white",
                                    bg=background_color)
        self.export_heading.grid(row=0, column=0)
        # Tells user how to export
        self.export_explanation = Label(self.export_frame,
                                        text="Enter the name of the file "
                                             "in the box below and press save"
                                             " button to your statistics "
                                             "to a text file",
                                        justify=CENTER, bg=background_color,
                                        fg="white", font=("arial", 12,
                                                          "italic"),
                                        wrap=225, padx=10, pady=10)
        self.export_explanation.grid(row=1, column=0)
        # Warning export text
        self.export_explanation_waring = Label(self.export_frame,
                                               text="If the filename you "
                                                    "enter already exists "
                                                    "its contents will be "
                                                    "replaced with these "
                                                    "new statistics",
                                               justify=CENTER,
                                               bg=background_color,
                                               fg="white", font=("arial", 10,
                                                                 "italic"),
                                               wrap=225, padx=10, pady=10)
        self.export_explanation_waring.grid(row=2, column=0)
        # Entry for filename
        self.export_entry = Entry(self.export_frame, width=30,
                                  font=("arial", 12), justify=CENTER)
        self.export_entry.grid(row=3, pady=10)
        # Error Message Labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="white",
                                      bg=background_color)
        self.save_error_label.grid(row=4)
        # Frame for the buttons
        self.button_frames = Frame(self.export_frame)
        self.button_frames.grid(row=5, pady=10)
        # Save to file button and close window button
        self.save_to_file_button = Button(self.button_frames,
                                          text="Save to file",
                                          command=partial(lambda: self.save_export(partner)))
        self.save_to_file_button.grid(row=6, column=0)
        self.close_window_button = Button(self.button_frames,
                                          text="Close window",
                                          command=partial(self.close_export, partner))
        self.close_window_button.grid(row=6, column=1)
        if len(statistics_for_export) == 0:
            self.save_to_file_button.config(state=DISABLED)
        else:
            self.save_to_file_button.config(state=NORMAL)

    def save_export(self, partner):
        # checking for valid input
        valid_characters = "[A-Za-z0-9_]"
        has_errors = "no"

        filename = self.export_entry.get()
        print(filename)

        for no_input_entered in filename:
            if re.match(valid_characters, no_input_entered):
                continue
            elif filename == " ":
                problem = "no spaces allowed"

            else:
                problem = ("no {}'s allowed".format(no_input_entered))
            has_errors = "yes"
            break
        if filename == "":
            problem = "can't be blank"
            has_errors = "yes"
        if has_errors == "yes":
            # Display the error message
            self.save_error_label.config(text="Invalid filename - {}".format(problem))
            # Change background color to show the user it is wrong
            self.export_entry.config(bg="#CD5C5C")
            print()

        else:
            # If there are no errors create the file
            # add the suffix of .txt
            filename = filename + ".txt"

            # create file
            file = open(filename, "w+")

            # add new line after every question
            for item in statistics_for_export:
                file.write(item + "\n")

            # close file
            file.close()

            # close box
            self.close_export(partner)

    def close_export(self, partner):
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Gaming Quiz")
    something = Questions()
    root.mainloop()
