#!/usr/bin/env python
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit


# Body


def infinite_stairway_room(input_name,count=0):
    print input_name, "walks through the door to see a dimly lit hallway."
    print "At the end of the hallway is a", count * 'long ', 'staircase going towards some light'
    next = raw_input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print input_name,"takes the stairs"
        if (count > 0):
            print "but you're not happy about it"
        infinite_stairway_room(input_name,count + 1)
    #option_2 == "?????"
	if next == "?????":
		pass


def gold_room(input_name):
	print "This room is full of gold.  How much does",input_name,"take?"
	next = raw_input("> ")
	try:
		how_much = int(next)
	except:
		dead("Man, learn to type a number.")
	else:
		if how_much < 50:
			print "Nice,",input_name,"is not greedy,",input_name ,",wins!"
			exit(0)
		else:
			dead("You greedy bastard!")


def bear_room(input_name):
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How is",input_name,"going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take" or next == "honey" or next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif ((next == "taunt bear" or next == "taunt") and not bear_moved):
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif ((next == "taunt bear" or next == "taunt") and bear_moved):
            dead("The bear gets pissed off and chews your leg off.")
        elif ((next == "open door" or next == "open" or next == "door") and bear_moved):
            gold_room(input_name)
        else:
            print "I got no idea what that means."


def cthulhu_room(input_name):
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ")

    if "flee" in next:
        main()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room(input_name)

def back_room(input_name):
	print "Hi",input_name,"This is the back room"
	print "It's filled with awkward programmers."
	print "You state your name but nobody listens.You soon start programming python and never leave"
	exit(0)

def dead(why):
    print why, "Good job!"
    exit(0)


##############################################################################
def main():
    # START the TextAdventure game
	input_name = raw_input("Please enter your name: ")
	print input_name
	print input_name,"is in a dark room."
	print "There is a door to your right,left and back."
	print "Which one do you take?"
	next = raw_input("> ")

	if next == "left":
		bear_room(input_name)
	elif next == "right":
		cthulhu_room(input_name)
	elif next == "back":
		back_room(input_name)
	elif next == "none":
		infinite_stairway_room(input_name,count=0)
	else:
		dead("You stumble around the room until you starve.")

if __name__ == '__main__':
    main()
