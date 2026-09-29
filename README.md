Maths Quiz

Project Overview

Maths Quiz is a Python console-based quiz program for practicing two mathematics topics:

Addition

Subtraction

The program asks the user for their name, allows the user to choose a topic, displays randomized multiple-choice questions, checks the submitted answer, gives immediate feedback, and displays the final quiz result.

This README describes the source code exactly as provided for the project. The source code itself has not been changed.

Features

User name input

Topic selection

Addition question bank

Subtraction question bank

Randomized question order

Multiple-choice questions

Automatic answer checking

Immediate correct/incorrect feedback

Displays the correct answer after a wrong answer

Quiz ends after 3 incorrect answers

Final result display

Counts total attempted, correct, and incorrect answers

Technologies Used

Python 3

Python random module

Python console / terminal

No third-party Python libraries are used by the source code.

How to Run

Save the source code as a Python file, for example maths_quiz.py, and run:

python maths_quiz.py

How the Program Works

The program displays a welcome message.

The user enters their name.

The user chooses Addition or Subtraction.

The selected question list is shuffled using random.shuffle().

Questions are displayed one at a time.

The user enters an option such as a, b, c, or d.

The answer is compared with the stored correct option.

The correct/incorrect count is updated.

The quiz stops when the user reaches 3 incorrect answers or finishes the question list.

The final quiz result is printed.

Project Scope

The current source code is a small console application. It does not contain a graphical interface, database, user accounts, online features, score history, or persistent storage.

Testing

The program should be manually tested using choice 1, choice 2, correct answers, incorrect answers, three incorrect answers, and completion of the question list.

Source Code Note

The source code represented by this documentation is the code supplied for the project. This documentation does not change the source code or claim features that are not present in it.
