## The script of the game goes in this file. Duh.




## Define some shit in this section

## CHARACTERS
define eris = Character("Eris")
define liftr = Character("LIFTR 03-215")

## AUDIO
define audio.demo1 = "she's got torque (demo).mp3"

## IMAGES??? do I need to define these here? Maybe for animations

## VARIABLES





## Label Start
label start:
    scene bg construction1

    show liftr neutral

    eris "Say \"placeholder text\" for me, if you please."

    liftr "Placeholder text!"

    play music demo1

    liftr "Playing Music track now."
    liftr "..."
    jump Ending

## PASTE SCRIPT STUFF IN HERE 
## |
## V



## ^
## |
## PASTE SCRIPT STUFF IN HERE

label Ending:
    "End game."

    ## This ends the game.
    return