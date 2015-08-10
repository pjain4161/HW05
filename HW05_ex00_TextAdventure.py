#!/usr/bin/env python
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
import sys
from sys import exit


# Body


def infinite_stairway_room(count, user):
    print "%s walks through the door to see a dimly lit hallway." %(user)
    print "At the end of the hallway is a", count * 'long ', 'staircase going towards some light'
    next = raw_input("> ")
     
    # infinite stairs option
    if next == "take stairs":
        print '%s takes the stairs' %(user)
        if (count >= 0) and (count < 2):
            print "but you're not happy about it"
            infinite_stairway_room(count + 1, user)
        elif (count >= 2):
            print "congrats! %s won" %(user)
            exit(0)
        
#     option 2 == ?????
    if next == "I am tired":
        dead (("oh %s lost the game in between!") %(user))
        
        
        
def back_room(user):
    print "It is filled with awkward programmers"
    print "%s states %s's name but nobody listens. %s soon starts programming python and never leave" %(user,user,user)
    exit(0)

def gold_room(user):
    print "This room is full of gold.  How much does %s take?" %(user)

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    
    if how_much < 50:
        print "Nice, %s is not greedy, %s win!" %(user, user)
        exit(0)
    elif (how_much < 150):
        print "To take so much money, %s needs to take stairs" %(user)
        infinite_stairway_room(0, user)
    else:
        dead("%s greedy bastard!"  %(user))


def bear_room(user):
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How is %s going to move the bear?" %(user)
    bear_moved = False

    while True:
        next = raw_input("> ")

        if (next == "take") or (next == "honey"):
            dead("The bear looks at %s then slaps %s's face off.") %(user, user)
        elif (next == "taunt") and not bear_moved:
            print "The bear has moved from the door. %s can go through it now." %(user)
            bear_moved = True
        elif (next == "taunt") and bear_moved:
            dead("The bear gets pissed off and chews %s's leg off.") %(user)
        elif (next == "open") or (next == "door") and bear_moved:
            gold_room(user)
        elif(next == "back"):
            back_room(user)
        
            
        else:
            print "I got no idea what that means."


def cthulhu_room(user):
    print "Here %s sees the great evil Cthulhu." %(user)
    print "He, it, whatever stares at %s and %s goes insane." %(user, user)
    print "Do %s flees for your life or eats %s's head?" %(user, user)

    next = raw_input("> ")

    if "flee" in next:
        main()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room(user)


def dead(why):
    print why, "Good job!"
    exit(0)


##############################################################################
def main():
    # START the TextAdventure game
    user = sys.argv[1]
    print "%s is in a dark room." %(user)
    print "There is a door to %s's right and left." %(user)
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "left":
        bear_room(user)
    elif next == "right":
        cthulhu_room(user)
    else:
        dead("%s stumble around the room until you starve." %(user))

if __name__ == '__main__':
    main()
