#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *

# Ask a simple question without multicolumns
# Show multichoice window and return selected item
class AskForChoice(Frame):

    # question is a simple string
    # answers - is a dictionary object like
    #           { 'a' => 'Choice 1', 'b' => 'Choice 2', 'c' => 'Choice 3'}
    def __init__(self, question="", answers={}, master=None):
        Frame.__init__(self, master)
        self.grid()
        
        # default choice
        self.choice=StringVar()
        
        # Show prompt
        self.draw(question, answers)
        
    # Show the question and possible answers
    def draw(self, question, answers):
        
        # Show the question itself
        row=0        
        questionLabel=Label(self, text=question)
        questionLabel.grid(row=row, column=0, columnspan=2)
        
        # Show possible answers in 2 columns (one for A, B, .. ) other for text
        row+=1
        for k in sorted(answers.keys()):
            w=Radiobutton(self, text=k+".", value=k, variable=self.choice, command=self.selected, justify=RIGHT)
            w.grid(row=row, column=0)
            l=Label(self, text=answers[k], justify=LEFT)
            l.grid(row=row, column=1)
            row+=1
        
        # Show :Quit: button
        quitButton = Button(self, text="Quit", command=self.quitPressed) 
        quitButton.grid(row=row, column=0)

        # Show :Next: button
        self.nextButton = Button(self, text="Next", command=self.next, state=DISABLED) 
        self.nextButton.grid(row=row, column=1)
        row+=1

    # User selected any choice - enable Next button        
    def selected(self):
        self.nextButton.configure(state=NORMAL)
        
    # User has pressed Next - destroy this window and exit mainloop
    def next(self):
        self.destroy()
        self.quit()
    
    # User pressed "QUIT" button - just exit
    # and set the choice value to the "QUIT" string
    def quitPressed(self):
        self.choice.set("QUIT")
        self.destroy()
        self.quit()
    
    # Return choice (as a string or whatever the key is)
    # Returns a "QUIT" string if user have pressed "Quit" button
    def ask(self):
            self.mainloop()
            return self.choice.get();

# Ask a question for a 2 columns match
# Similar to AskForChoice but accepts different arguments
class AskForChoiceColumns(Frame):

    # question is a simple string
    # choices is an ARRAY of 2 dictionaries 
    #     choices[0] = { 'A' => 'Choice 1', 'B' => 'Choice 2', 'B' => 'Choice 3'}
    #     choices[2] = { 1 => 'Match 1', 2 => 'Match 2'}
    # answers is a dictionary object: key is an answer, value is a LIST
    #     answers = { 'a' => [A1, B2, C3], 'b' => [A2, B1, C3]}
    
    def __init__(self,  choices, answers, master=None, question="Match the following columns:"):
        Frame.__init__(self, master)
        self.grid()
        
        # default choice
        self.choice=StringVar()
        
        # Show prompt
        self.draw(question, choices, answers)
        
    # Show the question and possible answers
    def draw(self, question, choices, answers):
        
        # Show the question itself
        row=0
        questionLabel=Label(self, text=question)
        questionLabel.grid(row=row, column=0, columnspan=3)
        
        
        # Show possible choices in 2 columns
        row+=1
        save_row=row
        
        # Draw 1st column header
        l1=Label(self, text="Column 1", justify=CENTER)
        l1.grid(row=row, column=0)
        # Draw 2nd column header
        l2=Label(self, text="Column 2", justify=CENTER)
        l2.grid(row=row, column=2)

        # Show choices
        # Column 1
        row+=1
        saved_row=row                
        for k in choices[0].keys():
            l=Label(self, text=str(k)+". " + str(choices[0][k]), justify=LEFT)
            l.grid(row=row, column=0)
            row+=1
        # Column 2
        row=saved_row
        for k in choices[1].keys():
            l=Label(self, text=str(k)+". " + str(choices[1][k]), justify=LEFT)
            l.grid(row=row, column=2)
            row+=1
            
        # Show possible answers in 2 columns (one is for A, B, .. ),
        # the other is for text
        for k in answers.keys():
            # Answer key area
            w=Radiobutton(self, text=k+".", value=k, variable=self.choice, command=self.selected, justify=RIGHT)
            w.grid(row=row, column=1)
            # Text area
            l=Label(self, text=' '.join(answers[k]), justify=LEFT)
            l.grid(row=row, column=2)
            row+=1
        
        # Show :Quit: button
        quitButton = Button(self, text="Quit", command=self.quitPressed) 
        quitButton.grid(row=row, column=0)

        # Show :Next: button
        self.nextButton = Button(self, text="Next", command=self.next, state=DISABLED) 
        self.nextButton.grid(row=row, column=1)
        row+=1

    # User selected any choice - enable Next button        
    def selected(self):
        self.nextButton.configure(state=NORMAL)
        
    # User pressed Next - destroy this window and exit mainloop
    def next(self):
        self.destroy()
        self.quit()

    # User pressed "QUIT" button - just exit
    # and set the choice value to the "QUIT" string
    def quitPressed(self):
        self.choice.set("QUIT")
        self.destroy()
        self.quit()

    # Returns choice (as a string or whatever the key is)
    # Returns a "QUIT" string if user have pressed "Quit" button
    def ask(self):
            self.mainloop()
            return self.choice.get();


# Class for Asking user a level
class AskLevel(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master.title("Difficulty Selection")
        self.level=IntVar()

    # Ask player for the difficulty level
    # and return a value (1..3)
    def askLevel(self):
        
        # by default - easy level
        self.level.set(3)
        
        prompt=Label(self, text="Select your level:")
        prompt.grid(row=0, column=0, columnspan=2)

        # Initialize widgets        
        c1=Radiobutton(self, variable=self.level, value=3, justify=RIGHT, width=1)
        l1=Label(self, text="Beginner", justify=LEFT)

        c2=Radiobutton(self, variable=self.level, value=2, justify=RIGHT,width=1)
        l2=Label(self, text="Medium", justify=LEFT)

        c3=Radiobutton(self, variable=self.level, value=1, justify=RIGHT,width=1)
        l3=Label(self, text="Hard", justify=LEFT)

        # Show multi-choice
        c1.grid()
        l1.grid(row=1,column=1)
        c2.grid()
        l2.grid(row=2,column=1)
        c3.grid()
        l3.grid(row=3,column=1)

        # Show "GO" button        
        b=Button(self, text="Start Quiz", command=self.levelSelected)
        b.grid(columnspan=2)

        # Wait for selection
        self.mainloop()
        
        # Return Selected value
        return self.level.get()

    def levelSelected(self):
        self.destroy()
        # exit mainloop()
        self.quit()
        

# Show Main Menu
class PlayDialog(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master.title("Science Trivia")
        self.answer="QUIT"

    # return "QUIT" if quit was pressed
    def show(self):
        
        prompt=Label(self, text="Science Trivia\nPress 'Play' to start")
        prompt.grid(columnspan=2)

        # Show "Quit" button        
        b=Button(self, text="Quit", command=self.quitPressed)
        b.grid(column=0, row=1)

        # Show "Start" button        
        b=Button(self, text="Play", command=self.playPressed)
        b.grid(column=1, row=1)

        # Wait for selection
        self.mainloop()
        
        # Return Selected value
        return self.answer

    def playPressed(self):
        self.destroy()
        self.answer="PLAY"
        self.quit()

    def quitPressed(self):
        self.destroy()
        self.answer="QUIT"
        self.quit()

# Notification general purpose dialog
class SimpleDialog(Frame):
    def __init__(self, text="Press OK to continue", button="OK", title="Alert", master=None):
        Frame.__init__(self, master)
        self.grid()
        self.txt=text
        self.but=button
        self.master.title(title)

    def show(self):
        
        prompt=Label(self, text=self.txt)
        prompt.grid()

        # Show "OK" button        
        b=Button(self, text=self.but, command=self.buttonPressed)
        b.grid()

        # Wait for selection
        self.mainloop()
        
    def buttonPressed(self):
        self.destroy()
        self.quit()

# Main Trivia Class
# all application logic is here
class TriviaScience:
    def __init__(self):

        # Player level
        # 3 - Beginner 
        # 2 - Medium
        # 1 - Hard
        self.level=3
        
        # questions (will be a list of 45 elements)
        self.quiz=[]

        # Initialize array of questions and correct answers
        self.initializeQuiz()

        # Initialize values before each game try
        self.initializeValues()
        
    # Initialize questions somehow (complex list)
    def initializeQuiz(self):

        # Question is a complex list
        # [0] is a question type possible values are:
        #     "SIMPLE" - one line question
        #     "COMPLEX"  - 2 column question
        #
        # [1] is a list of 2 elements
        #     for type "SIMPLE":
        #        [0] is a question STRING
        #        [1] is a DICTIONARY of possible answers, 
        #            like {"a":"Choice 1", "b":"Choice 2"}
        #
        #     for type "COMPLEX":
        #        [0] is a LIST of choices
        #            like [{'A':'Col1 Choice1', 'B':'Col1 ChoiceB'}, \
        #                  {1:'Col2 Choice 1', 2:'Col2 Choice2'}]
        #        [1] is a DICTIONARY of possible answers like in a SIMPLE
        #
        # [2] is a correct answer (string)
        
        self.quiz=[]

        # Lets go
        self.quiz.append(['SIMPLE', ['Which instrument is used to measure pressure?',{'a':'Saccharimeter','b':'Ammeter','c':'Manometer','d':'Lactometer'}], 'c'])
        self.quiz.append(['SIMPLE', ['What does Angstrom measure?',{'a':'Quantity of liquid','b':'Length of light waves','c':'Length of cables','d':'Speed of ships'}], 'd'])
        self.quiz.append(['SIMPLE', ['Light year is related to',{'a':'Energy','b':'Speed','c':'Distance','d':'Intensity'}], 'c'])
        self.quiz.append(['SIMPLE', ['Which of the following instruments is used to measure pressure of gases?',{'a':'Barometer','b':'Manometer','c':'Ammeter','d':'None of these'}], 'b'])
        self.quiz.append(['SIMPLE', ['Joule is the unit of',{'a':'Temperature pressure','b':'Energy','c':'Heat'}], 'c'])
        self.quiz.append(['SIMPLE', ['How many Dynes are there in one gram weight?',{'a':'900','b':'375','c':'981','d':'250'}], 'c'])
        self.quiz.append(['SIMPLE', ['How many Ergs are these in 1 Joule?',{'a':'102','b':'104','c':'106','d':'107'}], 'd'])
        self.quiz.append(['SIMPLE', ['The unit of current is',{'a':'Ohm','b':'Watt','c':'Ampere','d':'None of these'}], 'c'])
        self.quiz.append(['SIMPLE', ['The unit of energy in MKS system is',{'a':'Volt','b':'Erg','c':'Ohm','d':'Joule'}], 'd'])
        self.quiz.append(['SIMPLE', ['The intensity of an earthquake is measured with a',{'a':'Barometer','b':'Hydrometer','c':'Polygraph','d':'Seismograph'}], 'd'])
        self.quiz.append(['SIMPLE', ['Centigrade & Fahrenheit scales give same reading at',{'a':'- 40°','b':'- 32°','c':'- 273°','d':'- 100°'}], 'a'])
        self.quiz.append(['SIMPLE', ['Who among the following described protoplasm as the physical basis of life?',{'a':'T. H. Huxley','b':'Leeuwenhoek','c':'Rudolf Virchow','d':'J. C. Bose'}], 'a'])
        self.quiz.append(['SIMPLE', ['The scientist who first discovered that the earth revolves round the sun was',{'a':'Newton','b':'Dalton','c':'Copernicus','d':'Einstein'}], 'c'])
        self.quiz.append(['SIMPLE', ['Alexander Fleming discovered',{'a':'Penicillin','b':'X-ray','c':'Streptomycin','d':'Telephone'}], 'a'])
        self.quiz.append(['SIMPLE', ['Who among following invented the steam engine?',{'a':'Marconi','b':'James Watt','c':'Thomas Savery','d':'Wright Brothers'}], 'b'])
        self.quiz.append(['SIMPLE', ['Who invented typewriter?',{'a':'Shockley','b':'Pascal','c':'Sholes','d':'Waterman'}], 'c'])
        self.quiz.append(['SIMPLE', ['Who discovered circulation of blood in human body?',{'a':'Edward Jenner','b':'Joseph Lister','c':'William Harvey','d':'Jonon Esals'}], 'c'])
        self.quiz.append(['SIMPLE', ['The first attempt in printing was made in England by',{'a':'James Arkwright','b':'James Watt','c':'William Caxton','d':'Isaac Newton'}], 'c'])
        self.quiz.append(['SIMPLE', ['Who was the surgeon who pioneered antiseptic surgery in 1865?',{'a':'Edward Jenner','b':'Joseph Lister','c':'Henry William','d':'John Sleeman'}], 'b'])
        self.quiz.append(['SIMPLE', ['The credit of inventing the television goes to',{'a':'Faraday','b':'Baird','c':'Edison','d':'Marconi'}], 'b'])
        self.quiz.append(['SIMPLE', ['The credit of developing the polio vaccine goes to',{'a':'Jonas Salk','b':'Alb E. Sabin','c':'Selman Waksman','d':'None of these'}], 'a'])
        self.quiz.append(['SIMPLE', ['Mark the wrong combination',{'a':'James Watt: Steam Engine','b':'A.G. Bell: Telephone','c':'J. L. Baird: Television','d':'J. Perkins: Penicillin'}], 'd'])
        self.quiz.append(['SIMPLE', ['Choose the correct combination',{'a':'Typewriter: Remington','b':'Dynamite: Dunlop','c':'Evolution: Darwin','d':'Aeroplane: Harway'}], 'c'])
        self.quiz.append(['SIMPLE', ['Who invented the ball point pen?',{'a':'Waterman','b':'Oscar','c':'Wilson','d':'Lazlo Biro'}], 'd'])
        self.quiz.append(['SIMPLE', ['Blaze Pascal is associated with',{'a':'Calculating machine','b':'Computer','c':'Cinema','d':'None of these'}], 'a'])
        self.quiz.append(['SIMPLE', ['Wright Brothers are regarded inventors of the',{'a':'Balloon','b':'Bicycle','c':'Aeroplane','d':'None of these'}], 'c'])
        self.quiz.append(['SIMPLE', ['Which of the following pairs is incorrect?',{'a':'Roentgen: X-ray','b':'Newton: Law of gravitation','c':'Faraday: Diffusion of gases','d':'Pasteur: Bacteriology'}], 'c'])
        self.quiz.append(['SIMPLE', ['Philology is the',{'a':'Study of bones','b':'Study of muscles','c':'Study of architecture','d':'Study of languages'}], 'd'])
        self.quiz.append(['SIMPLE', ['Anatomy is the branch of science which deals with',{'a':'Structure of animals and plants','b':'Functioning of body organs','c':'Animal behavior','d':'Cells and tissues'}], 'a'])
        self.quiz.append(['SIMPLE', ['Study of earthquakes is known as',{'a':'Ecology','b':'Seismology','c':'Numismatics','d':'None of these'}], 'b'])
        self.quiz.append(['SIMPLE', ['Ecology deals with',{'a':'Birds','b':'Cell formation','c':'Relation between Organisms and','d':'Tissues'}], 'c'])
        self.quiz.append(['SIMPLE', ['Meteorology is the science of',{'a':'Weather','b':'Meteors','c':'Metals','d':'Earthquakes'}], 'a'])
        self.quiz.append(['SIMPLE', ['Oncology is the study of',{'a':'Birds','b':'Cancer','c':'Mammals','d':'Soil'}], 'b'])
        self.quiz.append(['SIMPLE', ['Study of life in outer space is known as',{'a':'Endobiology','b':'Exobiology','c':'Enterobiology','d':'Neobiology'}], 'b'])
        self.quiz.append(['SIMPLE', ['Numismatics is the study of',{'a':'Coins','b':'Numbers','c':'Stamps','d':'Space'}], 'a'])
        self.quiz.append(['SIMPLE', ['Eugenics is the study of',{'a':'Altering humans beings by changing','b':'People of European origin','c':'Different races of mankind','d':'Genetics of plants'}], 'a'])
        self.quiz.append(['SIMPLE', ['Ornithology is the',{'a':'Study of bones','b':'Study of birds','c':'Study of smells','d':'None of these'}], 'b'])
        self.quiz.append(['SIMPLE', ["Who invented the Doctor's thermometer?",{'a':'Fahrenheit','b':'Edison','c':'Galileo','d':'None of these'}], 'a'])
        self.quiz.append(['SIMPLE', ['The velocity of light was first measured by',{'a':'Einstein','b':'Newton','c':'Romer','d':'Galileo'}], 'c'])
        self.quiz.append(['SIMPLE', ['Who proposed the chemical evolution of life?',{'a':'Darwin','b':'Lammarck','c':'Oparin','d':'Haechel'}], 'c'])
        self.quiz.append(['SIMPLE', ['The telephone was invented by',{'a':'John Logie Baird','b':'Alexander Graham Bell','c':'Thomas Elva Edison','d':'James Watt'}], 'b'])
        self.quiz.append(['SIMPLE', ['Who among the following evolved the concept of relationship between mass and energy?',{'a':'Einstein','b':'Planck','c':'Dalton','d':'Rutherford'}], 'a'])
        self.quiz.append(['SIMPLE', ['Robert Koch worked on',{'a':'Tuberculosis','b':'Cholera','c':'Malaria','d':'Diabetes'}], 'a'])
        self.quiz.append(['SIMPLE', ['Who discovered Uranus?',{'a':'Herschel','b':'Ganleo','c':'Copernicus','d':'None of these'}], 'a'])
        self.quiz.append(['SIMPLE', ['Who among the following is associated with the invention of computers?',{'a':'Edison','b':'Babbage','c':'Mac Millen','d':'Rangabhashyam'}], 'b'])


        
    def initializeValues(self):
        # Difficulty
        # 3 - Beginner 
        # 2 - Medium
        # 1 - Hard    
        self.level=3

        # Current round number (from 0 to 2)
        self.round=0

        # Number of failures prior to this time since the quiz was started
        self.strikes=self.level
    
    # Start the application
    def start(self):
        # Initialize questions
        # Initialize correct answers
        # Main loop - show Welcome message, select level, start Quiz
        choice=""
        while choice!="QUIT":
           self.initializeValues()

           # Show main menu
           d=PlayDialog()
           
           # choice will be either PLAY or QUIT
           choice=d.show()

           if choice=="QUIT": return
                      
           # Create a new Dialog to ask a Difficulty Level
           q=AskLevel()
           self.level=q.askLevel()
           
           # Set number of strikes according to the level
           self.strikes=self.level
           
           # Start Round
           for currentRound in range(3):

               # Show Round started dialog
               s=SimpleDialog(text="Round: "+str(currentRound)+"\nPress START to start", title="Round "+str(currentRound), button="START")
               s.show()

               # get questions sublist
               quizzie=self.quiz[currentRound*15:currentRound*15+15]

               # Ask 15 questions and return list of results
               results=self.askQuestions(currentRound, quizzie)

               # Check if "QUIT" was selected
               if results[-1] == "QUIT":
                   choice="QUIT"
                   break

               # Now check the results
               matched=self.checkResults(results, quizzie)
               self.strikes=self.strikes-(len(quizzie)-matched)

               # too many failures show "Please try again"
               # and exit the round loop
               if self.strikes<0:
                   s=SimpleDialog(text="Please try again", title="Fail", button="Try Again")
                   s.show()
                   break
           
           # Winner is here!
           if choice!="QUIT" and self.strikes>=0:
               s=SimpleDialog(text="You Win", title="Winner", button="OK")
               s.show()

    # Return number of matched answers
    def checkResults(self, list, quiz):
        matched=0
        for (l, q) in map(None, list, quiz):
            # compare ignore case, q[2] is the correct answer letter
            if l.lower() == q[2].lower():
                matched+=1  

        return matched
   
    # One round - ask 15 questions and return a list or results
    def askQuestions(self, round, quizzie):
        result=[]

        # quizzie is a list of questions
        # Question is a complex list
        # [0] is a question type possible values are:
        #     "SIMPLE" - one line question
        #     "COMPLEX"  - 2 column question
        #
        # [1] is a list of 2 elements
        #     for type "SIMPLE":
        #        [0] is a question STRING
        #        [1] is a DICTIONARY of possible answers, 
        #            like {"a":"Choice 1", "b":"Choice 2"}
        #
        #     for type "COMPLEX":
        #        [0] is a LIST of choices
        #            like [{'A':'Col1 Choice1', 'B':'Col1 ChoiceB'}, \
        #                  {1:'Col2 Choice 1', 2:'Col2 Choice2'}]
        #        [1] is a DICTIONARY of possible answers like in a SIMPLE
        #


        # For all questions - ask and accumulate results
        count=0
        for q in quizzie:
            count+=1
            if q[0] == "SIMPLE":
                dialog=AskForChoice(question=q[1][0], answers=q[1][1])
                dialog.master.title("Round: "+str(round)+"/Question: "+str(count))
                choice=dialog.ask()
            elif q[0] == "COMPLEX":
                dialog=AskForChoiceColumns(choices=q[1][0], answers=q[1][1])
                dialog.master.title("Round: "+str(round)+"/Question: "+str(count))
                choice=dialog.ask()
            # Add result to the list
            result.append(choice)

            # Immediate exit on 'QUIT'
            if choice == "QUIT": break
            
        return result       
        

# this is for 2-column questions, commented
#question=None
#choices=[{'A':'Col1 Choice1', 'B':'Col1 ChoiceB'}, \
#{1:'Col2 Choice 1', 2:'Col2 Choice2', 3:'Col2 Choice3'}]
#answers={'a':['A1', 'B2'], 'b':['A3', 'B1']}
#menu2=AskForChoiceColumns(choices=choices, answers=answers)
#choice=menu2.ask()
#print choice


game=TriviaScience()
game.start()
