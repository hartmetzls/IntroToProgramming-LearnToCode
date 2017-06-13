#I broke my code up into 4 procedures to meet this criteria: "No functions are longer than 18 lines of code"


def quiz(): #Contains the starting paragraphs, calls a function to set the answer list and paragraph, lets user set the
    #number of guesses they get, calls a function to check the answers and outputs those results.
    easy_paragraph = "A ___1___ is created with the def keyword. You specify the inputs a " \
                     "___1___ takes by adding ___2___ separated by commas between the parentheses. " \
                     "___1___s by default return ___3___ if you don't specify the value to return. " \
                     "___2___ can be standard data types such as string, number, dictionary, tuple, " \
                     "and ___4___ or can be more complicated such as objects and lambda functions."
    medium_paragraph = "___1___ is the amount of information that can be transmitted per unit time. " \
                       "___1___ is usually measured in bits per second. On the internet, we usually " \
                       "speak in terms of Mbps, where the M stands for ___2___, which is one ___3___" \
                       "bits per second. A bit can have only one of ___4___ values."
    hard_paragraph = "The word computer in Mandarin Chinese is ___1___. The word for internet in " \
                     "Mandarin is ___2___. Python is a ___3___ (programming language). The Mandarin word for " \
                     "software developer is ___4___."
    answer_list, paragraph = set_paragraph_and_answers(easy_paragraph, medium_paragraph, hard_paragraph)
    num_guesses = raw_input("How many guesses should I give you? ")
    print "The current paragraph reads as such:"
    print paragraph
    return check_answers_win_lose(answer_list, paragraph, num_guesses)


def set_paragraph_and_answers(easy_paragraph, medium_paragraph, hard_paragraph): #taking the inputs of the paragraphs,
    #lets the user set the difficulty, outputs the answer list and the correct paragraph.
    difficulty = raw_input("Select a game difficulty by typing it in! \n "
                           "Possible choices include easy, medium, and hard. ")
    if difficulty == "easy":
        print "You newb! Jk, it's cool, you're learning."
        paragraph = easy_paragraph
        answer_list = ["function", "arguments", "None", "list"]
    if difficulty == "medium":
        print "You have chosen medium."
        paragraph = medium_paragraph
        answer_list = ["Bandwidth", "mega", "million", "two"]
    if difficulty == "hard":
        print "All the blanks you fill in will be Chinese Mandarin pinyin. Don't worry about filling in the tones, " \
              "just type in the pinyin without them."
        paragraph = hard_paragraph
        answer_list = ["diannao", "yintewang", "diannaoyuyan", "diannaoyezhe"]
    return answer_list, paragraph


def check_answers_win_lose(answer_list, paragraph, num_guesses): #inputs are the answers, paragraph, and number of
    #guesses; this procedure iterates through each answer and calls a function to check the user's answers and will
    #output text indicating whether or not the user answered everything correctly
    for i in range(1, len(answer_list) + 1): #Iterates starting from 1, so i can be used as the integer in the middle
        # of each blank in the fill_blanks function.
        num_guesses_remaining = int(num_guesses)
        while num_guesses_remaining:
            num_guesses_remaining, paragraph = fill_blanks(answer_list, i, num_guesses_remaining, paragraph)
    if "___" in paragraph:
        return "Study more, then try again!"
    else:
        return "You win! You know all the things."


def fill_blanks(answer_list, i, num_guesses_remaining, paragraph): #inputs are the answers, i, remaining guesses, and
    #the paragraph; checks whether or not the user's answer is correct; outputs remaining guesses and the paragraph
    answer = raw_input("What should be substituted for ___" + str(i) + "___? ")
    if answer == answer_list[i - 1]:
        paragraph = paragraph.replace("___" + str(i) + "___", answer)
        print "Correct!"
        print paragraph
        num_guesses_remaining = 0 #Resets so we can go on to the next question.
    else:
        num_guesses_remaining = num_guesses_remaining - 1
        if num_guesses_remaining != 0:
            print "Try again :)"
        else:
            print "That was your last guess."
            #Rather than end the game at this point, I decided to let the user
            #go on to the next question.
    return num_guesses_remaining, paragraph


print quiz()


# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!



# The answer for ____1____ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/
