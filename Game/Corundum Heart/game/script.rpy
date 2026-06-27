## The script of the game goes in this file. Duh.




## Define some shit in this section

## CHARACTERS
define np = Character("Now Playing:")
define e = Character("Eris Daedalus")
define l = Character("LFTR 03-215")
define g = Character("Galatea")
define f = Character("LFTR 1514")

## AUDIO
define audio.demo_sgt = "she's got torque quickloop.mp3"
define audio.demo_cg = "cloud gateway (demo).mp3"
define audio.demo_rt = "rhel's theme.mp3"

## IMAGES
## No need to define an image if you're not doing anything complicated with it. Just call the file name.


## VARIABLES





## Label Start
label start:
    jump sceneselect

label sceneselect:
    scene black
    menu:
        "Scene Select"

        "Sound Test":
            jump soundtest
        "Act 1 Scene 3":
            jump act1_scene3

label soundtest:
    menu:
        "Sound Test"

        "She's Got Torque (Loopable)":
            play music demo_sgt
            np "She's got Torque (Loopable)"
        "Cloud Gateway (demo)":
            play music demo_cg
            np "Cloud Gateway (demo)"
        "Rhel's Theme":
            play music "<loop 11.707 to 40.976>rhel's theme.mp3"
            np "Rhel's Theme"
        "Back to Scene Select menu":
            stop music
            jump sceneselect
    stop music
    jump soundtest


label act1_scene3:
    ## Scene 3: LFTR Repairs ##

    ## 251 and 1514 are on screen at 251's workshop area
    ## 1514 has a worried expression
    scene bg workshop placeholder
    with None
    play music demo_sgt
    show 251 placeholder sprite1 at left
    with moveinright
    show lftr08 placeholder sprite at right
    with moveinright

    "After the shift is over I take 1514 to my makeshift workshop"

    l "Alrighty, let me get a better look at you."

    f "Right, sorry about this."

    l "It's really no worry!"

    "I examine the area around the shoulder joint that had stopped working."

    "The damage on 1514 isn't so bad, she just needed a couple of new screws around the joint areas that had their threading stripped from repeated heavy actions."

    l "Okay I see the issue, some of the screws here have gotten lose and jammed themselves between the joint area, should be an easy fix!"

    ## 1514 has a happy expression

    f "That's a huge relief, I was worried that they might decomission me because of this!"

    ## 251's expression falls

    "I pause for a moment, being reminded of LFTR-06-848."

    "I had been doing repairs on 848 too, but despite all my efforts 848 continued to breakdown and was taken to a reclamation facility."

    ## 251 returns to a neutral expression

    l "No, don't worry, you still have a long time before you need to worry about something like that, some of the screws they used on your model line had a manufacuring issue and just need to be replaced."

    "Grabbing some extra screws and the screwdriver I manage to unjam the screws caught in the joint and carefully start putting in the new ones."

    ## 1514 returns to a neutral expression

    f "I know, it's just... this is the first time something like this happened to me."

    ## 1514 gets a sad expression

    f "I know we were made for this but... we have sentience" 

    f "why can the humans just make us do their work for them" 

    f "and then if we become too much of a hassle they just..." 

    f "use us for parts?"

    "I take a moment to come up with a response, this kind of sentiment wasn't exactly new, but like the news article from before said, things were heating up on Mars."

    l "I like to think of it as they gave us sentience, they gave us the closest thing they could to life, we owe them for that."

    f "Right... no you're right, it just... I wish there was more, you know?"

    "I do know, I wish I could be doing more, spending more time helping the others with repairs"

    "making it so that no one else has to be decomissioned like 848 was."

    ## beat
    ""

    "I finish tightening the last screw"

    l "Well, how does it work?"

    "1514 rotates the arm around a few times"

    ## 1514 gets a happy expression

    f "It's perfect! Feels just like when I came off the factory floor! Thank you so much!"

    ## 251's expression becomes happy

    l "No problem, if anything else like that happens again let me know."

    "I take one more look at 1514 before she leaves, feeling pride that I was able to help someone out."

    ## 1514 leaves

    l "Now to do my own repairs..."



label ending:
    stop audio
    stop sound
    stop voice
    stop music
    scene black
    "GAME END"

    ## return ends the game and shunts you back to the main menu.
    return