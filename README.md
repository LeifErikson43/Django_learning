**CS50 Web Capstone Project**

This project is a learning platform for ministry called Learn Now. After serving as a pastor in the United Methodist Church for 20, I wanted to try to provide a way to share practical ministry learning with others in multiple courses.

#Technologies Used:

- Django
- Html
- CSS
- Javascript
- Python
- Bootstrap
- Sqlite3

# How to run the application:

## Open the application

When the you first open the website you will see a list each Unit or Category of courses along with all the courses offered. Some classes are currently offered and some are future classes. Each course will have a simple description. 

## Signing up for a class

You will not be able to sign up for a course until you register and/or log into the sight. After logging in, you will be directed to the dashboard to see the classes that you are currently taking. You may navigate to the “home” page to again see all the courses offered. There will now be button reading “join.” Use this button to sign up for a class any class. Once you sign up for a class the button changes to read, “Start” in order to start the class. 

## Starting viewing Lectures

When you click “start” you will then see all the components for the class. There is an introductory video for the class from me. As you scroll down you will see each of the lecture videos followed by a quiz. You are to watch the video then take the quiz. 

## Take each quiz

At the bottom of the each quiz there is a “submit” button. When you submit the quiz, you will then see a box making sure that you want to submit the quiz. If you do not answer each question on the quiz you will be given an error message asking you to please fill out all answers. 

## See your quiz score

Once you submit you will be redirected back to the course showing each lecture. However, the “quiz” button for the quiz you have taken will now say your grade on the quiz. 

## Finish the class

When you submit the final quiz for a class, your overall grad will be calculated and stored. Once you have completed a class, the home page and the dashboard will no longer allow you to resume the course. The home page will simply tell the you that you have completed the course and you need to go to the dashboard to see your grade. The dashboard will show you your grade for all your completed courses. 

## Resume and Drop Courses

On the dashboard page you will be able to resume any course you have started but not completed.  You will also have a button that allows you drop any course that you have started, if you have not completed the course. Once you complete a course you cannot drop the course. If you choose to drop a course a you will see a “confirm” box that ask you if you are sure you want to drop the course. Once you drop a course all needed content is deleted from the database and the button for the course on the “home” page reads “join” instead of “resume.”

# Distinctiveness:

In this course we have not created a learning platform. Likewise, we did not embed video or create and grade quizzes. Therefore, this Learn Now app is distinctive form any previous project in the course.

# Complexity:

This web app utilizes more “Models” than any project we have done. In addition I have designed this app so that new courses could be added through the superuser “admin” and no additional coding. The “save_quiz” view saves multiple information to multiple different tables in the database. I tried to utilize components from each part of the course.

# Specifications

## Django

Django is the development platform used to create the website.

## HTML

The web application consists of nine html pages.

## CSS 

Thirteen different components are styled using the css stylesheet **style1.css**.

## Python

The server side programming is all written in the Python programing language. **Url.py** contains the twelve different url patterns needed for the web application. The **views.py** file contains the python code for the twelve views needed for the application. The most extensive if the **save_quiz** view. This view contains the logic to save and grade a quiz. This view also determine if the quiz is the last one for the course and if so calculates the users final grade. This view then stores the course as completed and save the grade.

## Javascript 

Two different javascript functions were created in the document **script.js**. Javascript is used to join any class from the home page. The homepage html “Join” button will be change to a “Start” button in order to begin the class. In addition, Javascript is used to drop any course that has been started.

## Bootstrap 

Bootstrap is utilized for the look of the navigation bar as well as buttons and forms throughout the web app

## Models 

The server for this web app utilizes nine Models or sqlite3 tables to store data in the database. These models are in the **models.py** file.

## Mobil responsive

I have designed this app to work and multiple different sizes of mobile devises.

## Possible Improvements

I have designs this web app with future expansion in mind. There are multiple components that can be expanded.

- Additional units and courses can be added.
- I would like to generate a certificate of completion for the student when course is completed.
- I designed the application to have an additional app added to manage the professors. Users with - professor credential could then use a different user interface to add courses and quizzes to the web application. Right now additional courses and quizzes are added throughout the Django admin superuser.
- Add the ability for professors to add different types of quizzes. Currently the questions are 	True/False.