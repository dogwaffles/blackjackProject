# MAY 31:
> -Developed a class for card, with a function to display string data indicating suit (ascii graphic) and card face. It's unfinished, but debugged and cleaned up. I still havve to add a dictionary-type object with the card names and values, as well as a way to produce a full deck as an array.\
> -I also installed VS Code and got git pushes working from console.\
> -Implemented a big fix in the card printer (faulty logic in comparison operators). Cleaned up comments. Reorganized README.
 
 # June 1:
 > -Today, I aim to create a deck builder and deal function (morning) and then create dealer and player action (evening).\
  If I have extra time, I will split up the classCard functions into single-purpose functions, for practice.\
> -I did make a deck generate function; generates all card values, faces, and suits. I settled on nested for loops iterating over lists.\
Later I will stick to a deal function and continue planning.\
> -(Evening) classes are being a bit trickier than expected, but I'm making progress...\
> -2 hours, I've got classes for Stack and Deal, both working. Stack can create multiple\
decks in a stack, with class card in a single list. Deal randomizes the stack (this could\
be made into a new class, I may do that to warm up tomorrow) Deals 2 cards from top of stack\
to both player and dealer. I'm satisfied for tonight's progress.  
> -quick update I am going with Pandas instead of Tensorflow as I don't think I have a reasonable\
chance of getting any results out of TF in the time frame.

# June 2:
> -I got some work done in the early AM - started on main.py to get basic functionality up and running.\
> -Prof told me to ease up - just get the requirements done - I am pushing myself because the brain is a muscle,
and this is the place to push myself, not the workplace.\
> -I am planning to do cleanup, commenting, and refactoring today: I've realized that transforming  
class Card in main.py is unneccessary, it can & should be done in class Card.\
> -"No functions in main" -Okay\
> -Looking good. I reorganized down to 3 class files. main is free of functions, yet functional. Junk code is removed.  
Comments are up-to-date. Final push shouldn't be too much of a hassle (jinx)...

# June 3:
> -Was up overnight. I've gotten a lot done. I think I'll sit around and work on ideas for moving forward, today.  
    #FIXME DEAPOSTROPHIZER
    #removes apostrophes from output of string in array->PRINTCARD
    #may require relocating. [thanks, drunk me!]
    #maybe output as !array


# Project Overview:

    Project Title: Louis Reilly's Blackjack Trainer
    Objective: Its basic functionality is to realistically simulate 
    games of blackjack, using random.seed(x) and random.random() for deal behavior.
        -It will feature full casino rules, including dealer behavior 
        (which is programmatic), and player (H)it (S)tand (D)ouble and (S)plit.
        -It will have several difficulty parameters including 
        (number of decks) and (% of cards removed from dealer stack)
        -It will also keep track of player statistics,
         creating a user file based on name entered by user input
        -This will be useful for blackjack practice - 
        keeping track of win/loss statistics is helpful in improving one's game.
    Key Features: Outline how you plan to use:
        -Variables Class variables will be imported, including user_name, 
        user_hand, dealer_hand, win/loss(current_session), win/loss(all_time), etc.
        -Functions shuffling, dealing, player actions, exporting to user data file
        -If/Else statements dealer behavior (hit/stand) is programmatic. 
        There is also dynamic actions based on user's current hand. 
        (Split, 5-card, Ace value,...)
        -Loops Shuffling, dealing, player action, updating output data
    “One New Thing”: initially I will import class definitions to keep things clean, 
    and use Pandas to create data tables
        -As "extras" - programmatic player behavior (user defined bot behavior), 
        dynamic player behavior ("AI" bot behavior), a GUI, just graphics, multi-player, etc.
    Plan: Daily programming session, one hour first thing in the morning, 
    one in the afternoon after a short nap. 
        -One week for basic program functionality (including classes and Pandas data tables)
        -One week for 'extras' (bot plays, graphics, etc.)
    Team or Individual: Individual

    *Please note that while blackjack is not the most moral of pursuits, 
    it can be an enjoyable diversion that is winnable with skill and presence. 
    I understand that any gambling game can be problematic, so
    if you feel that you have a problem - please reach out. there is help out there.