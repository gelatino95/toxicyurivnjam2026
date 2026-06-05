# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define eris = Character("Eris")
define liftr = Character("LIFTR 03-215")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg construction1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file with a matching name to the images
    # directory.

    show liftr neutral

    # These display lines of dialogue.

    eris "Say \"placeholder text\" for me, if you please."

    liftr "Placeholder text!"

    # This ends the game.

    "End game."

    return
