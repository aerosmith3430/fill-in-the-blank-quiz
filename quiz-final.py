'''The set_level function prompts the user to select a difficulty level.

Input: The user types in their choice of one of three difficulty level options.

Output: Returns the difficulty level that the user selected.
'''

def set_level():
    print "Please select a game difficulty by typing it in!"
    print "Do you choose easy, medium, or hard?"
    print "DIFFICULTY LEVEL:"
    level = raw_input()
    return level

# A list of blanks that will be in each phrase and the answers for each level. 
blanks  = ["__1__", "__2__", "__3__", "__4__"]
easy_answers = ["compiler", "computer", "interpreter", "ambiguity"]
medium_answers = ["nanosticks", "bugs", "variable", "assignment"]
hard_answers = ["string", "first", "plus", "concatenation"]

# The following are the phrases that the user will be filling in the blanks.
easy_phrase = "A __1__ is a program that produces other programs. \nA __2__ is a machine that can be programmed. \nPython is an example of an __3__, which executes a program using code that is input into it. \nLanguage __4__ refers to differences in interpretation in natural languages."
medium_phrase = "Admiral Grace Hopper was famous for walking around with __1__. \nProgramming mistakes are called __2__. \nA __3__ uses an __4__ statement to store a value and recall it using a name."
hard_phrase = "A __1__ is a sequence of characters surrounded by quotes. \nAugusta Ada King was considered the world's __2__ computer programmer. \nThe act of combining strings with the __3__ operator is called __4__."

'''The print_phrase function takes the level that the user selected and returns
the phrase and answers.

Input: Difficulty level

Output: The fill in the blank phrase and the answers that correlate to the level
that the user chose.
'''
def print_phrase(level):
    if level == "easy":
        return easy_phrase, easy_answers
    elif level == "medium":
        return medium_phrase, medium_answers
    else:
        return hard_phrase, hard_answers

'''
The word_in_phrase function iterates over each word in the phrase and checks to see
if one of the blanks contained in the blanks array is present in the phrase.  If the
blank is present, it returns the blank, otherwise it returns None.

Input: The blanks array

Output: Returns each blank in the blanks array if it is found.  If the word in the
phrase is not a blank, returns None.
'''
def word_in_phrase(word, blanks):
    for blank in blanks:
        if blank in word:
            return blank
    return None

'''
The play_game function takes in the phrase and answers based on the level the user
chose.  It initiates a counter and an empty array.  It takes the phrase that was
passed in and splits it into a list.  It then prints the phrase for the user to see.
The for loop iterates over the phrase that has been passed in and assigns any blanks
to the variable replacement.  When a blank is encountered, the program prompts the
user to enter their answer for that blank.  The while loop checks to see if the user's
answer matches the answer in the answers array that was passed in.  If the user's 
answer does not match, it prompts the user to try again.  If the user's answer does
match, it replaces the blank with the user's answer.  The index counter advances and
the phrase is reprinted with the blank filled in.  If a blank is not encountered, it
takes the word in the phrase and appends it to the replaced array.  Once all of the
blanks have been filled in, the join function is used to turn the list array back
into a string and prints the string along with a congratulatory message.

Input: Phrase and answers based on the level that the user selected.  User input
is collected in the body of the function and replaces the blanks.

Output:  The completed string with blanks filled in.
'''
def play_game(phrase, answers): 
    index = 0
    replaced = []
    words = phrase.split()
    print phrase
    for word in words:
        replacement = word_in_phrase(word, blanks)
        if replacement != None:
            user_input = raw_input("Type in your answer for " + replacement + " :")  
            while user_input != answers[index]:
                user_input = raw_input("I'm sorry, that answer is incorrect. \nType in your answer for " + replacement + " :")
            phrase = phrase.replace(blanks[index], answers[index])
            index += 1
            print
            print phrase
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    print "Congratulations! You have completed the quiz."

'''
The main function organizes all of the function calls and assigns them to variables
that are passed in to the next function.

Input: Return statements from the previously defined functions.

Output: Level, phrase and answers that are used as arguments for the next function.
'''
def main():
    level = set_level()
    phrase, answers = print_phrase(level)
    play_game(phrase, answers)

main()