## The script of the game goes in this file. Duh.




## Define some shit in this section

## CHARACTERS
define e = Character("Eris")
define l = Character("LIFTR 03-215")
define g = Character("Galatea")

## AUDIO
define audio.demo1 = "she's got torque (demo).mp3"

## IMAGES??? do I need to define these here? Maybe for animations

## VARIABLES





## Label Start
label start:
    scene bg construction1

    show liftr neutral

    e "Say \"placeholder text\" for me, if you please."

    l "Placeholder text!"

    play music demo1

    l "Playing Music track now."
    l "..."
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