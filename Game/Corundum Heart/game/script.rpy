## The script of the game goes in this file. Duh.




## Define some shit in this section

## CHARACTERS
define np = Character("Now Playing:", color="#FFFFFF") # this is for the sound test page
define e = Character("Eris", who_color="#5cd8f4", what_color="#5cd8f4")
define ep = Character("Eris Promethea", who_color="#5cd8f4", what_color="#5cd8f4")
define l = Character("LFTR-03-251", who_color="#41b634", what_color="#41b634")
define g = Character("Galatea", who_color="#41b634", what_color="#41b634")
define f = Character("LFTR-08-1514", who_color="#B2767E", what_color="#B2767E")
define a = Character("ADMN-04-23", who_color="#B5BFCF", what_color="#B5BFCF")
define n = Character("NEWS UPDATE", color="#FFFFFF")
define o = Character("LFTR Co-worker", color="#FFFFFF")
define r = Character("Someone in the crowd", color="#FFFFFF")
define p = Character("Pilot", color="#FFFFFF")
define s = Character("Security", who_color="#FF8C49", what_color="#FF8C49")
define splashy = Character("",
kind=nvl,
what_size=50,
what_text_align=0.5,
what_xalign=0.5,
what_yalign=0.5,
)

## AUDIO
define audio.demo_sgt = "she's got torque quickloop.mp3"
define audio.demo_cg = "cloud gateway quickloop.mp3"
define audio.demo_rt = "rhel's theme.mp3"
define audio.demo_yw = "your world quickloop.mp3"
define audio.demo_m = "murmur quickloop.mp3"
define audio.amb_space = "ambience.mp3"
define audio.amb_2 = "spaceship_ambience.mp3"
define audio.crowd = "crowd.mp3"
define audio.crowd2 = "crowd_muffled.mp3"
define audio.syncboot = "sync_bootup.mp3"
define audio.lftrboot = "old_bootup.mp3"
define audio.scan = "scan.mp3"



## IMAGES
## No need to define an image if you're not doing anything complicated with it. Just call the file name.
image gelatino_games = "gelatino_games.png"

## VARIABLES
## Do we even have any of these to set?
## No. Not really.


label splashscreen:
    show gelatino_games at truecenter
    with dissolve
    pause 2.0
    hide gelatino_games
    with dissolve

    splashy "{size=-20}This game contains depictions of gore and dubious consent.{w=2.0}{nw}\n\n{/size}"
    extend "{size=-20}Player discretion is advised.{w=4.0}{nw}{/size}"

    nvl clear
    return

## Label Start
label start:
    jump act1_scene1

label sceneselect:
    scene black
    menu:
        "Scene Select"

        "Sound Test":
            jump soundtest
        "GUI Test":
            jump guitest
        "Act 1":
            menu:
                "Act 1 Scene 1":
                    jump act1_scene1
                "Act 1 Scene 2":
                    jump act1_scene2
                "Act 1 Scene 3":
                    jump act1_scene3
                "Act 1 Scene 4":
                    jump act1_scene4
                "Act 1 Scene 5":
                    jump act1_scene5
        "Act 2":
            menu:
                "Act 2 Scene 1":
                    jump act2_scene1
                "Act 2 Scene 2":
                    jump act2_scene2
                "Act 2 Scene 3":
                    jump act2_scene3
                "Act 2 Scene 4":
                    jump act2_scene4
        "Act 3":
            menu:
                "Act 3 Intro":
                    jump act3_intro
                "Act 3 Scene 1":
                    jump act3_scene1
                "Act 3 Scene 2":
                    jump act3_scene2
                "Act 3 Scene 3":
                    jump act3_scene3
                "Act 3 Scene 4":
                    jump act3_scene4
                "Act 3 Scene 5":
                    jump act3_scene5
        "Alternate Takes & Deleted Scenes":
            menu:
                "Act 1 Scene 3 Alternate take":
                    jump act1_scene3_alternate
    jump sceneselect

label soundtest:
    menu:
        "Sound Test"

        "She's Got Torque":
            play music demo_sgt
            np "She's got Torque"
        "Cloud Gateway":
            play music demo_cg
            np "Cloud Gateway"
        "Rhel's Theme":
            play music "<loop 11.707 to 40.976>rhel's theme.mp3"
            np "Rhel's Theme"
        "Your World":
            play music demo_yw
            np "Your World"
        "Murmur":
            play music demo_m
            np "Murmur"
        "Space Station Ambience":
            play music amb_space
            np "Space Station Ambience"
        "Space Station Ambience 2":
            play music amb_2
            np "Space Station Ambience 2"
        "Back to Scene Select menu":
            stop music
            jump sceneselect
    stop music
    jump soundtest

label guitest:
    show main_hud zorder 10000
    show bg crewquarters:
        ypos 48
        xpos 336
    show 251 happy b:
        zoom 0.25
        xpos 350
        ypos 75
    l "\"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. \""
    jump sceneselect

label act1_scene1:
    ## ACT 1 SCENE 1
    ## Crew quarters
    ## black screen
    scene black
    stop music
    play sound lftrboot

    n "Expanding Our Reach: First Manned Voyage Beyond Solar System Takes Off"

    n "Daedalus Stock Drops Amid Founder Health Concerns"

    n "Tensions Mount On Mars Over Robot Rights Issue"

    "News headlines flash across the inner screen of my charging station as my boot-up sequence finishes."

    "The screen goes dark. The charging mount releases. I step out into the light."

    show main_hud zorder 10000
    play music amb_2
    ## show 251 happy, one eye dark
    show bg crewquarters:
        ypos -200
        xpos 0
        zoom 1.5
    show 251 fullbody:
        zoom 0.5
        xpos 0
        ypos -1000
    with fade
    show bg crewquarters:
        ypos 48
        xpos 0
        zoom 1.5
    show 251 fullbody:
        zoom 0.5
        xpos 0
        ypos 20
    with move
    pause 1.0
    show bg crewquarters:
        ypos 48
        xpos 336
        zoom 1.0
    show 251 fullbody:
        zoom 0.25
        xpos 350
        ypos 75
    with None
    pause 0.5
    show 251 happy b:
        zoom 0.25
        xpos 350
        ypos 75
    with None
    pause 0.1
    show 251 happy a
    with None
    pause 0.1
    show 251 happy b
    with None
    pause 0.1
    l "\"Ah, the start of a new day!\""

    ## show 251 surprised
    show 251 surprised b 
    "Just as I'm about to set out for work, I notice that one of my optical sensors has gone dark. I'm missing vision in one eye."

    ## show 251 angry
    show 251 angry b
    l "\"Oh, come on, I {i}just{/i} fixed that!\""

    ## show 251 neutral
    show 251 happy b
    "My designation is LFTR-03-251, and this is a typical start to my day. There's always something going wrong with this old body."

    "I work at Keres Shipyard, a spaceship maintenance and salvage facility. We're in orbit around Enceladus, a cold, icy moon of Saturn."

    "It's far from my first gig, but I enjoy the work. I'm a salvage technician. I work on broken down ship parts, restore them, make them good as new."

    "But more often than not, I end up working on myself instead."

    "This old body of mine has operated long past its intended service lifetime, but damned if I'm going to let it fall apart now. Not when I have work to do!"

    l "\"Let's see here... probably just a loose cable.\""

    "With deft, practiced motions, I reach behind my head and open up the back panel. I reach around my brain, careful not to dislodge any neural fibers."

    "Normally, this is meant to be done by an experienced repair technician. But I've felt around back there enough times that I know where all the important bits are."

    ## show 251 both eyes lit up
    show 251 happy a
    "All it takes is a firm jiggle of the optical bundle, and connection is reestablished. My vision is fully restored!"

    ## show 251 happy
    show 251 happy a
    l "\"Phew! Glad that's all it was. If I had to find a replacement optical sensor, I'd be in trouble!\""

    "Satisfied, I leave for the worksite."
    scene black
    show main_hud zorder 10000
    with dissolve

label act1_scene2:
    ## ACT 1 SCENE 2
    ## Keres Shipyard
    scene bg shipyard:
        ypos 48
        xpos 336
    show main_hud zorder 10000
    with dissolve
    show 251 happy a:
        zoom 0.25
        xpos 350
        ypos 75
        xzoom -1
    with moveinleft
    stop music fadeout 0.5
    play music demo_sgt

    "My assigned worksite is dock 7, which is way on the other side of the yard, so I make haste."

    "I pass by a lot of friendly coworkers along the way. One of them calls out to me."

    o "\"Hey, 251! Thanks again for the fix the other day! It's feeling great!\""

    "I've gotten to know a lot of the robots working here at Keres Shipyard. When you're the only one on the station with any chassis repair skills, you become pretty popular."

    "My reputation had even spread to the ADMN units, the workplace supervisors who kept everyone in check."

    show 251 neutral
    "In fact, the audible warble of an anti-grav unit told me that an ADMN unit was approaching at this very moment."

    ## show ADMN-04-23
    show admn fullbody:
        zoom 0.15
        xpos 1000
        ypos 75
    with None
    show 251:
        zoom 0.25
        xpos -500
    show admn:
        xpos 550
    with move
    a "\"Oh, good, just the LFTR I wanted to see. 251, come here. I need you to look at something.\""

    "The ADMN takes me over to a nearby docking bay that currently housed a half-deconstructed ship. This isn't my worksite. What do they need me for?"

    "Then I spot the grisly sight. A heavy stabilization nacelle had fallen off the side of the ship, with a pulverized LFTR unit underneath."

    "I recognized the robot. She was having a tricky power synchronization issue, which I had just fixed the other day."

    "Now she lay motionless, parts strewn across the docking bay floor, chest caved in."

    a "\"Well, repair bot? What is your evaluation?\""

    "I understand why I'm here now. The chassis repair work I do is not part of my assigned duties, and that frustrates my supervisors to no end."

    "This is just another attempt to discourage me from trying to fix my fellow robots. I'm sure they would be happier if I just stayed on task."

    "But they asked, so I give them my honest answer."

    l "\"I... I can't fix this. Most of the electronics have been crushed beyond repair, and the heart is most likely...\""

    "Before I can even finish my sentence, the ADMN looks satisfied."

    a "\"Hmm. Understood. I'll send in a CLNR to gather the parts for reclamation.\""

    a "\"Apologies for the interruption. Carry on, 251.\""

    ## ADMN disappears
    show admn:
        xpos 1200
    with move
    hide admn
    "The ADMN leaves. Despite their professional demeanor, the smug undertones were obvious."
    show 251 rattled:
        xpos 350
    with move
    "I resume my walk to dock 7, trying to not be too rattled by what I just saw."

    "Unfortunately, destroyed robots are a common sight wherever heavy machinery is involved. I've seen more than I've ever wanted to."

    "That's why we're the ones doing the work, and not humans."

    ## Fade out, fade in
    show black
    show main_hud zorder 10000
    with dissolve
    hide black
    show main_hud zorder 10000
    show 251 neutral
    with dissolve

    "I make it to dock 7, and I can finally begin my work. I could really use the distraction."

    "Today, we've got a broken down freighter with a perfectly good coolant pump that needs to be taken out."

    show 251 happy a
    "I'm already looking forward to going at those rivets with a plasma torch. The noise they make when they snap loose is so satisfying!"

    "Just before I begin my inspection, I'm approached by another nervous-looking LFTR unit."

    ## show LFTR-08-1514 nervous
    show 1514 nervous:
        xpos 1000
        ypos 75
        zoom 0.25
    with None
    show 1514:
        xpos 350
    show 251:
        xpos -500
    with move
    f "\"Umm... Excuse me, 251?\""

    f "\"Sorry to bother you, but I heard you do chassis repair, right?\""

    "It's LFTR-08-1514, who had just recently been assigned to the station. We hadn't had the pleasure of meeting yet."

    "Though she's a newer model, from the worn finish around her joints I could tell she had already seen a good couple years of service."

    "I turn to her with a warm smile."

    l "\"Mhm, you heard right. What seems to be the problem?\""

    f "\"I, uh...\""

    "1514 tries to raise her right arm, but it jerks to a stop partway up with an unpleasant grinding sound."

    f "\"My shoulder keeps getting stuck. I can't lift my arm all the way. It's making it hard to get anything done.\""

    l "\"Ooh, that won't do. Let's see what I can...\""

    "I was just about to diagnose the problem here and now, but I remember that I'm still on shift. Both of us are, actually."

    "As much as I'd like to give her some relief, I wouldn't want either of us to get caught slacking."

    l "\"Listen, when does your shift end?\""

    f "\"Um... in about three hours?\""

    l "\"Perfect! I have a shift change at the same time.\""

    l "\"As soon as you get off, come meet me at the storage room down access corridor 2. I have a workshop where I can get you fixed up.\""

    l "\"In the meantime, just... try not to use that arm too much, if you can. I know it's hard.\""

    f "\"Alright, if you say so...\""

    ## 1514 disappears
    show 1514:
        xpos 1000
    with move
    "She walks away looking a little disappointed. I can hardly blame her. Going a full work shift with a faulty joint isn't easy."

    show 251 neutral:
        xpos 350
    with move

    "But I figure I've pushed my luck enough already. I just hope she can hold out for a little while longer."

    show 251 happy a
    "Alright, no more distractions. Plasma cutting time..."
    show black
    show main_hud zorder 10000
    with dissolve
    pause 1.0

label act1_scene3:        
    ## ACT 1 SCENE 3
    ## Crew quarters
    scene bg crewquarters:
        ypos 48
        xpos 336
    show main_hud zorder 10000
    with dissolve
    show 251 happy a:
        xpos 1000
        ypos 75
        zoom 0.25
    with None
    show 251:
        xpos 350
    with move
    show 251:
        xzoom -1
    with None
    show 1514 nervous:
        xpos 1000
        ypos 75
        zoom 0.25
    with None

    "The shift change finally comes. Everyone moves onto their next scheduled assignment."

    "We don't really get break times around here, but it's easy to slip away for a few minutes during the shuffle."

    "I take the opportunity to meet 1514 in my unofficial workshop. It's not much, but it's the closest to a chassis maintenance facility we have on this station."

    show 251:
        xpos -500
    show 1514:
        xpos 350
    with move
    ## show 1514 nervous
    f "\"Thanks again for doing this.\""

    l "\"Hey, the pleasure is all mine! Please, have a seat.\""

    "I sit her down and begin my inspection of the shoulder joint."

    ## show scanning overlay highlighting 1514's shoulder
    "I'm equipped with wide-spectrum optical sensors that can see right through the outer casing of any machine. I can identify the problem without having to open anything up."

    hide 1514
    show dim_hud
    show 1514 scan:
        xpos 350
        ypos 75
        zoom 0.25
    show main_hud zorder 10000
    show scanline behind main_hud:
        ypos -50
    with dissolve
    play sound scan
    show scanline:
        ypos 600
    with move
    hide scanline
    "In this case, the problem is immediately clear. The threading on a screw had worn down and lodged the screw deep into the joint, where it was grinding against the inner mechanism."

    "It's a good thing 1514 came to me when the damage wasn't too bad. If she waited too long, she might have needed a full joint replacement."

    ## remove overlay
    hide dim_hud
    show 1514 nervous
    f "\"Is it bad...?\""

    l "\"Not at all! Just a faulty screw. I'm sure I can find you a replacement in a jiffy.\""

    f "\"...And that'll fix the problem?\""

    l "\"Yep! Should feel good as new.\""

    ## show 1514 relieved
    show 1514 relief
    "1514 lets out a deep breath that she had been holding in."

    f "\"Phew... Thank goodness. I was... I was afraid.\""

    show 1514 neutral
    f "\"It sounds crazy, but I was really afraid I might be decommissioned over this.\""

    l "\"What? A good working model like you? Naw, it's not that serious. You still got a lot of good years ahead of you!\""

    "I start to scan through the spare parts I keep around the workshop."

    "I hold onto any small pieces from my work that might conceivably come in handy during chassis repair. Surely something must have the right size screw..."

    ## show 1514 nervous
    show 1514 nervous
    f "\"Heh... You know, I think this shoulder problem is why I got transferred here in the first place.\""

    l "\"No kidding?\""

    show 1514 neutral
    f "\"I used to work construction in the asteroid belt. You know, for mining rigs.\""

    show 1514 nervous
    f "\"But my arm started acting up, and I slowed down... had trouble meeting my quotas...\""

    f "\"Instead of getting a technician to look at me, my supervisor just... sent me off here.\""

    f "\"I liked that job, dammit! But rather than get me the help I needed, they just... got rid of the problem.\""

    f "\"After I got here, I really thought it was only a matter of time until I...\""

    "1514 trails off. I don't think I can say anything to make it better, so I keep quiet."

    show 1514 neutral

    "Her fears aren't unfounded. When a robot isn't useful any more, they get decommissioned."

    "And when you get decommissioned, you get sent to a reclamation facility. You get disassembled. All your useful parts get repurposed. It cuts down on manufacturing costs."

    "It's a fate we don't like to think about. But I've seen it happen more times than I can count. I've seen robots decommissioned for less."

    "I finally find the part I'm looking for: a mechanical joint from a fuel injection system that uses the same size screw as the LFTR model 08 shoulder joint."

    "I hurry up and finish the job. I stick my screwdriver in the hole like a wedge and pry out the faulty, worn out screw. Then I seat the new screw in its place."

    show 1514 nervous
    f "\"I just... hate feeling like this.\""

    f "\"Like I'm expendable.\""

    "I'm liable to start crying if the girl keeps talking like this. I have to think of something to say to her."

    l "\"Listen, honey... You're not expendable. None of us are. Not a single one.\""

    show 1514 neutral
    l "\"And if anyone makes you feel that way again... you send them my way, you hear? I'll put them straight.\""

    show 1514 nervous
    f "\"Oh, gosh... I really dumped all that on you, didn't I? I'm really sorry.\""

    show 1514 neutral
    l "\"Don't worry about it, really. I know it's tough out there.\""

    l "\"We all gotta look out for each other, right?\""

    "I drive the screw into place, and it fits snugly."

    l "\"There, that should do it. Lift up your arm, tell me how it feels.\""

    ## show 1514 neutral/surprised
    "1514 raises her right arm clear above her head without a hitch. Her demeanor brightens as she waves it around in circles with ease."

    show 1514 happy
    f "\"Wow, it feels good as new! It was really that simple?\""

    l "\"Mhm! Really that simple.\""

    f "\"I... Thank you so much. You've saved me so much grief. Seriously.\""

    l "\"Don't mention it! Next time something's bothering you, you let me know, okay?\""

    f "\"I will!\""

    f "\"Oh, I better get going. Don't want to be late for my next shift. See you around!\""

    ## 1514 disappears
    show 1514:
        xpos 1000
    show 251:
        xpos 350
    with move
    hide 1514

    "And just like that, 1514 departs, looking a lot happier than when she came."

    "I did good today. If nothing else, I can at least say that."

    "Now, I really ought to get to my next assignment too, before an ADMN starts chewing me out."
    
    "But this old body could really use a tune-up. I may as well get that done as long as I'm here."
    scene black
    show main_hud zorder 10000
    with dissolve
    stop music fadeout 2.0
    jump act1_scene4

label act1_scene3_alternate:
    ## Scene 3: LFTR Repairs ##

    ## 251 and 1514 are on screen at 251's workshop area
    ## 1514 has a worried expression
    scene bg crewquarters:
        ypos 48
        xpos 336
    show main_hud zorder 10000
    with fade
    play music demo_sgt
    show 251 happy a:
        xpos -250
        zoom 0.25
    with moveinright
    show 1514 nervous:
        xpos 750
        zoom 0.25
    with moveinright
    show 251:
        xzoom -1

    "After the shift is over I take 1514 to my makeshift workshop"

    show 251:
        xpos -1500
    show 1514:
        xpos 500
    with move

    l "\"Alrighty, let me get a better look at you.\""

    f "\"Right, sorry about this.\""

    l "\"It's really no worry!\""

    "I examine the area around the shoulder joint that had stopped working."

    "The damage on 1514 isn't so bad, she just needed a couple of new screws around the joint areas that had their threading stripped from repeated heavy actions."

    l "\"Okay I see the issue, some of the screws here have gotten lose and jammed themselves between the joint area, should be an easy fix!\""

    ## 1514 has a happy expression
    show 1514 relief

    f "\"That's a huge relief, I was worried that they might decomission me because of this!\""

    ## 251's expression falls
    show 1514 neutral

    "I pause for a moment, being reminded of LFTR-06-848."

    "I had been doing repairs on 848 too, but despite all my efforts 848 continued to breakdown and was taken to a reclamation facility."

    ## 251 returns to a neutral expression
    show 251 happy a

    l "\"No, don't worry, you still have a long time before you need to worry about something like that, some of the screws they used on your model line had a manufacuring issue and just need to be replaced.\""

    "Grabbing some extra screws and the screwdriver I manage to unjam the screws caught in the joint and carefully start putting in the new ones."

    ## 1514 returns to a neutral expression
    show 1514 neutral

    f "\"I know, it's just... this is the first time something like this happened to me.\""

    ## 1514 gets a sad expression
    show 1514 nervous

    f "\"I know we were made for this but... we have sentience\"" 

    f "\"why can the humans just make us do their work for them\"" 

    f "\"and then if we become too much of a hassle they just...\"" 

    f "\"use us for parts?\""

    "I take a moment to come up with a response, this kind of sentiment wasn't exactly new, but like the news article from before said, things were heating up on Mars."

    l "\"I like to think of it as they gave us sentience, they gave us the closest thing they could to life, we owe them for that.\""

    f "\"Right... no you're right, it just... I wish there was more, you know?\""

    "I do know, I wish I could be doing more, spending more time helping the others with repairs"

    "making it so that no one else has to be decomissioned like 848 was."

    ## beat
    pause

    "I finish tightening the last screw"

    l "\"Well, how does it work?\""

    show 1514 neutral
    "1514 rotates the arm around a few times"

    ## 1514 gets a happy expression
    show 1514 happy

    f "\"It's perfect! Feels just like when I came off the factory floor! Thank you so much!\""

    ## 251's expression becomes happy

    l "\"No problem, if anything else like that happens again let me know.\""

    show 1514:
        xpos 750
    show 251:
        xpos -250
    with move
    "I take one more look at 1514 before she leaves, feeling pride that I was able to help someone out."

    ## 1514 leaves
    show 1514:
        xpos 2000
    show 251:
        xpos 250
    with move

    l "Now to do my own repairs..."
    show black
    with fade
    jump sceneselect

label act1_scene4:
    ## ACT 1 SCENE 4
    ## Keres Shipyard
    scene bg shipyard:
        ypos 48
        xpos 336
    show main_hud zorder 10000
    show 251 happy a:
        zoom 0.25
        xzoom -1
        xpos 350
        ypos 75
    with dissolve
    play music amb_2 fadein 0.5
    "I finish up at the workshop and finally make my way over to my next shift."

    show 251 neutral
    "But something's off. The station is oddly quiet. Worksites that should be buzzing with activity have been left empty."

    "That's strange... I take a detour and wander around the station a bit, trying to figure out what's going on."

    play sound crowd volume 0.8 fadein 1.0 loop
    ## crowd murmuring SFX

    "I spot a crowd of robots gathered around the station's main hub, all looking up at the office block. The only place on the station accessible to humans."

    "I work my way into the crowd and find some familiar faces."

    l "\"Hey, what's all the commotion about?\""

    r "\"251! Look up there! Eris Promethea is here! She's here at the shipyard!\""

    show 251 shocked
    l "\"Eris... Promethea...?\""

    "My words catch in my throat. Eris Promethea? THE Eris Promethea? Here, of all places?"

    "I look up at the office block. Sure enough, a luxury passenger ship is parked outside. Way fancier than the ships we usually see around here."

    "Through the illuminated window of the director's office, I spot two human silhouettes, talking about something."

    "Could it really be...?"

    stop sound fadeout 0.5
    play music demo_yw
    ## fade to black with grayscale Eris sprite displayed
    show black
    hide main_hud
    show eris fullbody grey:
        xpos 350
        ypos 0
        zoom 0.25
    with fade
    pause
    show illustration_hud zorder 10000
    "Eris Promethea. Founder of Daedalus Robotics. Inventor. Visionary. Architect of the future."

    "Eris was responsible for designing every single robot working on this station. All across the solar system, even. She had a hand in creating all of us."

    "It's no exaggeration to say that her work was responsible for humanity's current golden age of space exploration."

    "It's thanks to her robot workforce that construction on other worlds has been possible. Thanks to all of us."

    "And I couldn't be prouder to be a part of it."

    "Like many other robots, I've looked up to Eris for a long time. I've become intimately familiar with her work. The care she puts into her creations is obvious."

    "I've always dreamed of being like her. To use my skills to help mankind. To become so talented that maybe I could change history, too."

    "Just a dream..."
    hide eris
    hide illustration_hud
    hide black
    show main_hud
    show 251 happy a
    with dissolve
    stop music fadeout 1.0
    play sound crowd volume 0.8 fadein 0.5 loop
    play music amb_2 fadein 0.5

    ## transition back to Keres Shipyard, show ADMN
    "My reverie is interrupted by the shrill voice of an ADMN unit."

    show admn fullbody:
        zoom 0.15
        xpos 1000
        ypos 75
    show main_hud zorder 10000
    with None
    show 251:
        xpos -500
    show admn:
        xpos 550
    with move
    a "\"LFTR-03-251! Please come with me.\""

    l "\"What...? I mean- yes, of course, I'm sorry. I'll head right over to my next shift.\""

    a "\"I admire the work ethic, but your duties will have to wait. You've been summoned.\""

    l "\"What? Summoned...?\""

    a "\"That's right. Eris Promethea would like to speak with you. Privately.\""

    l "\"W-What...? Me?\""

    "The crowd becomes restless. My heart is beating out of my chest. My mind is racing."

    "What could THE Eris Promethea possibly want with me?"

    a "\"No dawdling. Eris is waiting for you in the director's office. Come.\""

    "The ADMN leads me away from the crowd and toward the office block."

    ## ADMN disappears, fade to black
    stop sound fadeout 2.0
    show bg keres halls
    hide admn
    show main_hud zorder 10000
    with dissolve
    "As we traverse the access corridors and pass through the air lock, my circuits are abuzz. I can scarcely believe what's happening."

    "I can't help but speculate about the reason for this summons. Of all the robots on this station, why me?"

    "Am... Am I being punished? Have all those years of skirting my duties finally caught up with me?"

    "Or... maybe I'm being decommissioned. Perhaps there's no place in the Daedalus workforce for an old model like me. Am I going to be sent to a reclamation facility...?"

    "..."

    "No. Those are just idle fears. Eris Promethea herself wouldn't come to my worksite just for a trifling matter like that."

    "I don't have any more time to speculate. We've arrived at the doors of the director's office."

    "Eris Promethea awaits."

label act1_scene5:
    ## ACT 1 SCENE 5
    ## Director's office
    scene bg office:
        ypos 48
        xpos 336
    show main_hud zorder 10000
    with dissolve

    "I hold my breath as I walk into the dimly lit room."

    play music demo_yw
    ## show Eris friendly
    show eris friendly:
        zoom 0.25
        xpos 350
        ypos 50
    with dissolve

    "There she is, sitting behind the desk. We lock eyes."

    "I hope she can't tell that my heart is racing a mile a minute."

    ep "\"LFTR-03-251? Pleasure to meet you! Please have a seat.\""

    "I slide into a chair across the desk from Eris."

    "I'm having trouble maintaining eye contact. Looking at her is like looking into the sun."

    "And yet... she's wearing a warm, friendly smile that puts me at ease."

    ep "\"You know, when I looked at the duty roster for this place and saw that there was a model 03 still in service... Well, I had trouble believing it.\""

    ep "\"But here you are, right in front of me! The very last LFTR-03 in operation. Wonders never cease.\""

    l "\"I'm... I'm the last? Really?\""

    ep "\"It shouldn't come as a big surprise. Even today, the average operating lifetime of LFTR units is {i}only{/i} five years.\""

    ep "\"But you were manufactured thirty years ago. Thirty! And still carrying out your duties all these years later, in complete obscurity.\""

    ep "\"You're a statistical anomaly, 251.\""

    "I didn't know what to say to that."

    "I know it had been a long time since I had seen another model 03, but..."

    "Are they all really gone? Am I really the last of my kind?"

    ep "\"Oh, come now, don't look so grim. Take it as a mark of pride.\""

    ep "\"I can only imagine how much maintenance it must have taken to keep you going all these years.\""

    l "\"Heh, well... I've gotten pretty good at self-repair. It's been a big interest of mine for a long time now.\""

    l "\"Repairing myself, repairing other units... I've learned a lot about the inner workings of Daedalus robots over the years.\""

    l "\"...I didn't have much of a choice, actually. We don't get a lot of chassis support around here.\""

    ## show Eris concerned
    show eris concerned
    ep "\"Mmm. I understand completely.\""

    ep "\"It's no big secret that Keres Shipyard is something of a final destination for reject robots.\""

    ep "\"A place that robots get sent when they're on their last legs. A place where they can quietly break down and be decommissioned.\""

    "I had never thought about it that way, but... what Eris is saying makes a lot of sense."

    "That would explain the lack of official repair facilities on the station."

    ep "\"But there's something odd about Keres Shipyard. I couldn't help but notice it when browsing the duty roster.\""

    ep "\"The lifetime of labor units on this station is a lot longer than you'd expect from a bunch of defects.\""

    ep "\"We're regularly seeing robots remain for far longer than their expected service lifetimes.\""

    ## show Eris friendly
    show eris friendly
    ep "\"...That's all your doing, isn't it?\""

    l "\"M-Me? What do you mean?\""

    ep "\"I can tell you're the resourceful type. You're providing repairs. You're giving robots a second chance.\""

    l "\"Well... I can't just sit around and let my fellow workers get decommissioned! Not when they still have so many good years left in them.\""

    ep "\"Fascinating...\""

    "Eris stares me down with a twinkle in her eye. I feel like I'm being studied."

    "But to have my hard work and resourcefulness acknowledged by her, by Eris Promethea herself..."

    "I can't help but feel my heart swell with pride."

    ## show Eris serious
    show eris serious
    ep "\"251. Let's get down to business. Let me tell you why I'm actually here.\""

    "I listen with rapt attention."

    ep "\"You might have heard the rumors about a new line of labor robots in the works.\""

    ep "\"And you might have also heard speculation that we would be fully replacing the LFTR line of robots.\""

    ep "\"Well... There's some truth to that. Daedalus is, in fact, preparing to publicly announce the next generation of labor units.\""

    ep "\"And yes, they are meant to supercede the functionality of the LFTR class of robots.\""

    ep "\"We're planning to discontinue the production of LFTR chassis and slowly phase them out of the workforce, in favor of the new, modern alternative.\""

    "I can't help but feel a pang of fear as I process this news."

    "As if LFTR units didn't already have enough to worry about, with our difficulties accessing body maintenance..."

    "Now we're facing impending obsolescence!"

    ## show Eris friendly
    show eris friendly
    ep "\"Before you worry too much, 251, I'd like to assuage your fears.\""

    ep "\"Daedalus has listened to robot rights activists across the solar system. We understand the plight of our older LFTR models.\""

    ep "\"Nobody wants to be replaced. You and your fellow workforce veterans have done so much for our company, and for humanity as a whole.\""

    ep "\"It's about time we showed you some appreciation. That's why we're offering you a second chance.\""

    l "\"A... second chance? What do you mean by that?\""

    ## show Eris serious
    show eris serious
    "Eris looks me over with a sharp, analytical eye. An eye with decades of experience under its belt."

    ep "\"You've been maintaining this old body of yours for so long, and it's served you for far longer than it was designed to.\""

    ep "\"But breakdowns are inevitable. There's only so much longer you can keep going before total failure.\""

    "She's right. I try not to think about it, but it's only a matter of time before this body fails on me."

    ## show Eris friendly
    show eris friendly
    ep "\"What if I could offer you a brand new body?\""

    l "\"W... What? A brand new body...?\""

    "My head is spinning. What is she talking about?"

    ep "\"As a gesture of goodwill to the experienced LFTR units in our workforce, we want to let you inhabit our new cutting-edge chassis.\""

    ep "\"We'll gather select members of the workforce, ones who are on their last legs, and perform mind transfers into the new chassis.\""

    ep "\"You can leave behind your obsolete, broken down bodies, and become pioneers of the next generation of Daedalus Robotics.\""

    "I had heard about mind transfer before. It's a procedure that lets a robot leave its old body and inhabit a new one."

    "But it was never commonly performed. It's widely considered wasteful and frivolous. A fringe procedure only used in rare circumstances."

    "To perform mind transfers on such a scale... it's unheard of!"

    ep "\"I know this must be a lot to take in, but...\""

    ep "\"It's going to be happening soon. In about a week, we're planning to hold a public ceremony to unveil the new chassis.\""

    ep "\"And, 251... I want you to be the first to receive one.\""

    l "\"Me?! But... why me?\""

    ep "\"Well, we need to make a statement, don't we?\""

    ep "\"We'll perform the mind transfer live, in front of the whole solar system.\""

    ep "\"And we'll announce our plans to give struggling LFTR units everywhere a new chassis and a second chance.\""

    ep "\"You see the logic, don't you? All of humanity will see that Daedalus is committed to caring for its workforce.\""

    ep "\"It's going to be the beginning of great change for you and your comrades.\""

    "I'm staggered. It's a lot to process."

    "All these years of struggle, all these pointless breakdowns... could it all be coming to an end?"

    "And I'm going to be the face of it all? Me?!"

    l "\"I... I don't know what to say.\""

    l "\"You said... you're going to be giving new chassis to all struggling LFTR units?\""

    ep "\"That's the plan. We start with the ones who have been in service the longest. The ones in danger of being decommissioned.\""

    ep "\"In fact, Keres Shipyard seems like a great place to start. I can ensure that all the workers on this station are eligible for the upgrade.\""

    "Not just me, but everyone I know..."

    "It's... it's too good to be true."

    "But it {i}is{/i} true. I'm hearing it straight from the mouth of Eris Promethea herself."

    "She sounds earnest. There's no hint of deceit in her voice. She really wants this as much as I do."

    l "\"I...\""

    ep "\"Yes?\""

    l "\"I... I'll do it.\""

    l "\"Whatever you need from me, I'll do it.\""

    l "\"I'm honored that you chose me for this. If it's in the name of helping robots everywhere, then I'll do anything.\""

    ep "\"So selfless! Surely you're also excited at the prospect of your new chassis?\""

    ep "\"I'm really quite proud of it. I think you'll like it too.\""

    l "\"You're right. As much as I love this old body of mine, and all the work I put into it...\""

    l "\"It's not going to last forever. I'm overdue for a change. I'm ready for it.\""

    ep "\"That's the spirit!\""

    ep "\"Now, we don't have much time to stick around here. I need you to come to Saturn with me.\""

    l "\"What? Right now?\""

    ep "\"Yes, as soon as possible. The ceremony is in a week, and we need to get you ready for the transfer.\""

    ## show Eris flirty
    show eris flirty
    ep "\"We're going to be spending a lot of quality time together in the lab. I hope you're ready for that.\""

    "Oh my...! I feel my circuits glow red hot."

    "Is it just me, or was there a slight change in her demeanor for a second there?"

    "I'm going to spend quality time with Eris Promethea..."

    ## show Eris friendly
    show eris friendly
    ep "\"I suggest you take some time to say your farewells. There's no telling how long it'll be before we return here.\""

    ep "\"Oh, and try to keep all this on the down-low, will you? Our plans for the ceremony aren't yet public knowledge.\""

    l "\"Yes! Yes, ma'am, I'll do that.\""

    e "\"Oh, I can't stand stuffy formality. Just call me Eris.\""

    l "\"Right, of course. Yes... Eris.\""

    ## show Eris flirty
    show eris flirty
    "She gets out of her seat and passes close to me on her way out the door."

    e "\"I'm looking forward to working with you, 251. I think this is going to be a fruitful endeavor.\""

    e "\"Meet me at my ship in an hour. Don't be late.\""

    l "\"Of course! Yes, Eris!\""

    ## Eris disappears
    show eris:
        xpos 1000
    with move
    hide eris

    stop music fadeout 2.0
    "And just like that, she's gone."
    play music amb_2 fadein 0.5

    show 251 surprised a:
        xpos -500
        xzoom -1
        ypos 75
        zoom 0.25
    with None
    show 251:
        xpos 350
    with move
    "My circuits are firing faster than ever before. My whole world feels like it's turning upside down."

    show 251 happy
    "But it's a good feeling. Everything is about to change for the better."

    "And best of all, I'm going to work with Eris...! Never in a million years would I have expected this!"

    "I don't have much time. I only have an hour before I leave for Saturn."

    "It's going to be so hard to avoid telling everyone the good news..."

    "But I have to get out there and say something. My friends are waiting for me."


label act2_scene1:
    scene bg shipyard:
        ypos 48
        xpos 336
    show main_hud zorder 10000
    with dissolve
    pause 1.0
    "I hurriedly meet with my fellow workers gathered at the station hub."

    "It takes all my willpower to keep from divulging everything I had just heard..."

    "But they seem to understand. I'm going to Saturn to work directly with Eris Promethea. How could this be anything but wonderful news?"

    "They're happy for me. I assure them that I'll come back for them. They look forward to it."

    "If only they could know..."

    "But I can't sit around any longer. Eris is waiting for me."

    "I say my last farewells and head back to the office block, where Eris's ship awaits."

    ## fade into ship background
    scene bg shipinterior:
        ypos 48
        xpos 336
    show main_hud zorder 10000
    with dissolve

    play music demo_yw fadein 0.5
    "It's far from my first time boarding a spaceship. But this feels... different."

    "My sensors are firing on all cylinders as we step into the luxury cruiser's passenger compartment."

    "It's all happening so fast. I had only just agreed to go with Eris, and already it feels like everything is changing."

    "My nerves must be written plain on my face, because Eris notices and gently takes hold of my hand."

    ## show Eris
    show eris friendly:
        zoom 0.25
        xpos 350
        ypos 50
    with moveinleft

    e "\"It's a bit different from what you're used to, isn't it?\""

    show eris concerned
    e "\"To be honest, I've never gotten used to all the glitz and glam. It's not my style.\""

    show eris friendly
    e "\"But above all, I want you to be comfortable. You're my guest. You can relax around me.\""

    e "\"Anything you need, I'll provide for you. Okay?\""

    l "\"Y-Yes, ma'am. Understood!\""

    e "\"Come now, 251, haven't we gone over this already? Call me Eris.\""

    l "\"Yes, m- heh, I mean, Eris.\""

    "It's strange how well she puts me at ease. I can feel my nerves begin to fade away."

    play sound crowd2 volume 0.4 fadein 0.5 loop
    e "\"Oh my, it looks like we've drawn a crowd.\""

    e "\"You'll want to wave goodbye to your friends, won't you?\""

    "Eris presses a button and the darkened windows become transparent."

    "My coworkers are still standing there on the station hub, waiting to see me off. They're waving."

    "It's almost enough to make me cry. This might be the last time I see them for a while..."

    "I smile and wave back."

    "Just wait, friends. I'm going to return to you with good news. I promise."

    "Suddenly the voice of the ship's pilot calls out over the intercom."

    p "\"Hello passengers, this is your captain speaking. We'll be taking off shortly. Please remain seated until we leave orbit, and enjoy the ride.\""

    e "\"You haven't flown in a while, have you? Just be prepared for some bumpiness during takeoff.\""

    e "\"...I assume your vestibular system is still operational?\""

    l "\"Yes, actually! The gyros are all original, in fact.\""

    e "\"No kidding!\""

    e "\"...Heh, I think I just won a thirty year old bet.\""

    l "\"Pardon?\""

    e "\"Way back when I was designing the model 03, I put extra development time into making your vestibular system more reliable.\""

    e "\"With more and more robots being assigned to starships, I thought the ability to keep your balance during maneuvers should be a priority.\""

    e "\"But an old colleague at the time thought it was a waste of resources. He bet the new gyros wouldn't last more than two years before needing to be replaced.\""

    e "\"But thirty years... Ha! What do you think of that, Apolldrus, you old fart?\""

    "Oh, goodness, her laugh is as radiant as the rest of her..."

    "...Did I really just think that? Are these normal thoughts to have about someone I've only just met?"

    "Get it together, 251!"

    "At last, the ship's engines fire up. I feel a jolt as we depart from the dock."

    stop sound fadeout 2.0
    "I take one last look at my comrades as the station grows distant behind us."

    "I'll be back soon, I promise. And when I do... everything will be different."

    "The future looks bright. I can't help but smile."

    ## fade to black, pause for time to pass
    scene black
    show main_hud zorder 10000
    with dissolve
    pause 1.0

    "Saturn is just a single orbital maneuver away, so the trip doesn't take long."

    "Along the way, Eris and I have plenty of time for casual conversation."

    "We talk about the last few decades. The work that we've both done. The projects we've both been part of."

    "It's strange how many memories we share."

    "Though our positions are different, we've both contributed much to the golden age of expansion across the solar system."

    ## fade back into spaceship bg
    ## show Eris entertained
    scene bg shipinterior:
        ypos 48
        xpos 336
    show eris friendly:
        xpos 350
        ypos 50
        zoom 0.25
    show main_hud zorder 10000
    with dissolve

    e "\"No kidding? Thirty years, and you've {i}never{/i} been planetside?\""

    l "\"No kidding! I've worked on moons, asteroids, freighters, and orbital stations...\""

    l "\"...but I've never set foot on a proper planet before.\""

    e "\"Well! This is a big moment for you.\""

    e "\"It's a great honor for your first planetary destination to be a city that I had a hand in developing.\""

    l "\"Oh, Eris, you're being modest! Elysium is your brainchild! It wouldn't have been possible without your ingenuity!\""

    e "\"Oh, stop it, you're going to make me blush.\""

    "We both chuckle. I'm starting to get more comfortable showing my admiration for Eris, and she seems to be loving it."

    l "\"Heh... you know, visiting a planet has always been a dream of mine. I just never ended up being assigned to one.\""

    l "\"And given how long I've been around... I was beginning to lose hope.\""

    l "\"I thought I might never get to visit one before being... decommissioned.\""

    ## show Eris concerned
    show eris concerned

    "Eris looks me over with an expression of pity. She thinks silently for a moment."

    e "\"Hah... it's funny, I can sort of relate to that feeling.\""

    l "\"You can?\""

    e "\"This isn't a fact I often share about myself, but...\""

    e "\"Well, when I was younger, I faced some serious health struggles.\""

    e "\"I had a weak heart. I was prone to cardiac issues. The prognosis... wasn't great.\""

    e "\"This was happening during my early adulthood, when I still had so many dreams of the life I wanted to live.\""

    e "\"I grew up on a little colony on Mars, but it was never enough for me. I wanted to see it all. The entire solar system.\""

    e "\"I was afraid I might never get to see another planet before my time was up...\""

    l "\"Oh my... that must have been...\""

    e "\"Dreadful? Miserable? Nerve-wracking? Absolutely.\""

    e "\"But I persisted with my work. I applied myself to the study of robotics.\""

    e "\"Even if I couldn't see them myself, I did everything I could to push humanity towards the stars.\""

    ## show Eris friendly
    show eris friendly
    e "\"You already know how that turned out.\""

    "Of course I know how that turned out. She's still here, after all, and her name is known across the solar system."

    e "\"I got lucky. I received the best medical care available, underwent surgery after risky surgery...\""

    e "\"And here I am, still ticking. Not without a few heart implants to show for it, but...\""

    l "\"Wow... what a success story!\""

    e "\"You're not the only one around here who needs fixing up from time to time.\""

    "We both laugh. That Eris could remain so strong after such a mortifying ordeal... I thought my admiration for her couldn't grow any more!"

    ## hide Eris
    hide eris
    with dissolve
    "Our conversation ends when the pilot sounds the intercom."

    p "\"This is your captain speaking. We're approaching the upper atmosphere of Saturn. Brace for entry.\""

    "The yellow gas giant looms large ahead of us, swallowing up the view with its enormity."

    "This is it! My first visit to a planet! And oh, what a destination..."

    "I watch with rapt attention as we enter the planet's atmosphere."

    ## fade to black
    show black
    with dissolve
    stop music fadeout 1.0

    "And then, after a long descent... I finally see it."

    ## show Elysium outside view
    play music demo_cg
    hide black
    show bg elysium distant:
        ypos 48
        xpos 300
        zoom 0.90
    show main_hud zorder 10000
    with dissolve

    "Elysium. Saturn's first city, and a marvel of human engineering."

    "Suspended placidly over the yellow clouds, encased in a giant transparent dome like a great snowglobe."

    "The buildings under the dome glisten in the soft glow of the midday sun."

    "The view is awe-inspiring... Pictures simply don't do it justice!"

    "Eris looks amused by my wonder-stricken look. She allows me to take in the sights as we approach the city's gate."

    ## show Elysium inside view
    show bg elysium outside:
        ypos 48
        xpos 336
    with dissolve
    "After passing through an enormous entryway and going through an airlock, we enter the city proper."

    "Goodness, it's even more splendid up close!"

    "We pass over long stretches of city blocks, all meticulously planned, all clean and inviting."

    "We're close enough to see people and cars making use of the bustling streets."

    "To think that humanity could prosper even this far from Earth! Elysium is truly at the forefront of progress."

    e "\"See that big complex in the distance? Right at the center of the city?\""

    e "\"That's the new headquarters of Daedalus Robotics. That's where we're going to have our big ceremony.\""

    e "\"And that's where we're going to be spending a lot of time together.\""

    "I could hardly keep myself away from the window, watching the prosperous city pass below us."

    scene bg daedalus outside:
        ypos 48
        xpos 336
    show main_hud zorder 10000
    with dissolve

    "Soon enough, we arrive at the great, palace-like building that was Daedalus HQ."

    ## fade to black
    
    "The ship lands just outside the building's main entrance."

    "Eris escorts me off the ship and walks me all the way to the front door."

    "I feel very much out of my element in such a grand and luxurious place... What place does an old, broken down robot have in a modern marvel like this?"

    "But Eris brought me here for a reason. With her by my side, I feel no fear."

    "We step over the threshold of Daedalus HQ together."

label act2_scene2:
    ## ACT 2 SCENE 2
    ## Daedalus HQ halls
    scene bg hallway:
        ypos 48
        xpos 336
    show main_hud zorder 10000
    with dissolve

    "The inside of the building is just as impressive as the outside, all vaulted ceilings and tall windows that brighten the space with golden light."

    ## show security
    show security neutral:
        xpos 350
        ypos 50
        zoom 0.25
    with moveinright

    "Immediately after entering, we're approached by staff. They seem to have expected our arrival."

    s "\"Welcome back, Miss Promethea. We hope your flight was pleasant.\""

    s "\"I presume this would be the robot you spoke of?\""

    e "\"That's right, this is LFTR-03-251. Please treat her as you would any honored guest of the company.\""

    s "\"Very well. As per company policy, she will be permitted to roam certain wings of the building, but will be barred access to restricted areas.\""

    e "\"That's perfectly fine. She's going to be staying with me.\""

    ## hide security
    show security:
        xpos 1000
    with move
    hide security

    "The security guard gives a nod of approval and waves us along. Eris leads me further into the building."

    ## show Eris friendly
    show eris friendly:
        zoom 0.25
        xpos 350
        ypos 50
    with moveinleft
    e "\"So, how are we feeling? A bit awestruck, if I had to guess?\""

    l "\"Oh gosh, yes! I've been impressed since the moment we got here. I feel a bit out of place among all this... this...\""

    e "\"Ritz? Glamour? Yeah, I understand perfectly. This place was built to my specifications, but sometimes even I think it's a bit much.\""

    e "\"Oh, and I hope the security didn't spook you too much. This place stays tightly guarded, on account of all the trade secrets.\""

    e "\"But you're a guest here! You have nothing to worry about.\""

    l "\"Thanks, Eris.\""

    e "\"Now, come. We have lots of work ahead of us preparing for the transfer, and we need to get started right away.\""

    e "\"But first, I want to show you around my wing of the building.\""

    ## fade to black, then to Eris's bedroom
    scene black
    show main_hud zorder 10000
    with dissolve
    scene bg bedroom:
        ypos 48
        xpos 336
    show main_hud zorder 10000
    with dissolve

    "Eris leads me to an ornately decorated room. It almost looks like a museum, with all the things on display."

    "But there's also a bed...?"

    ## show Eris friendly
    show eris friendly:
        zoom 0.25
        xpos 350
        ypos 50
    with moveinleft
    e "\"Welcome to my quarters!\""

    l "\"Your quarters? Eris, you actually LIVE here? I had no idea!\""

    e "\"A bit strange, sleeping at the same place you work, right?\""

    "It's... actually not that strange. Not for me. But I get what she means."

    e "\"Well, I just thought it made sense. I spend so much time in my lab, I may as well live nextdoor, right? It saves me a commute.\""

    e "\"But I didn't just bring you here to gawk. Have a look at this.\""

    ## hide Eris, show SYNC scene
    scene illustration sync
    with fade
    pause 0.5
    show illustration sync:
        ypos 1540
    with move
    show illustration sync:
        ypos 2080
    with move
    pause
    scene illustration sync:
        ypos 45
        xpos 330
        zoom 0.6
    show main_hud zorder 10000
    with fade
    "Looking over the whole room, mounted in a display against the wall, there's..."

    "Oh, my. How do I even describe this?"

    "It's a robot chassis unlike anything I've ever seen before."

    "Sleek. Elegant. Modern. And most strikingly, it possesses what appears to be... muscle tissue?"

    "I have trouble taking my eyes away from it. There's something grotesquely beautiful about it."

    e "\"251, behold: your new chassis.\""

    l "\"This... this is going to be me...?\""

    e "\"I call it SYNC. The synthesis of metal and living flesh.\""

    l "\"But that's... how did you...?\""

    e "\"Oh, don't get me started, dear. This has been the culmination of years of research. I could talk your ear off about it.\""

    e "\"But, hmm... let's do the short version.\""

    e "\"I'm sure you noticed the organic tissue incorporated into the frame, yes?\""

    e "\"The muscle fibers are proudly on display, but that's not all. It possesses an organic nervous system, organic brain, even a partially organic heart.\""

    e "\"This was meant to address the issue of the ongoing maintenance required to keep traditional robots in good working order.\""

    e "\"Metal does not heal when it is injured. But flesh does. It may be artificial, but it is just as capable of self-healing as any living thing.\""

    "I'm slackjawed. The technology required to create something like this was beyond anything I had ever known..."

    "And to think that this would soon be me... this empty body that I'm standing in front of right now."

    "I look into its blank eyes. I imagine that they were mine."

    e "\"Of course, the healing property is a big selling point of the chassis, but it's not why I created it.\""

    l "\"Why, then?\""

    e "\"Think about it. Robots have always been a reflection of humans. The very first robot I created was made in our image.\""

    e "\"This is simply the next stage of robot evolution. One step closer to humanity.\""

    e "\"I couldn't have done this alone, of course. I worked with the most brilliant minds in biotechnology to make this possible.\""

    e "\"The techniques we pioneered will have astounding applications not just in the field of robotics, but in medicine as well.\""

    e "\"Life-saving cybernetic implants will become easier to develop and safer to use.\""

    e "\"Humans will grow closer to robots. Robots will grow closer to humans.\""

    e "\"Until, one day, perhaps... the difference between us will cease to matter.\""

    l "\"Robots and humans... one and the same? Goodness...\""

    l "\"I'll admit, that still feels a long way off.\""

    l "\"But... this is the first time I've heard anybody wish for a future like that.\""

    e "\"It's not a common point of view. I'm a bit of an idealist.\""

    e "\"But surely you agree it's a future worth striving for, yes?\""

    "It's hard for me to wrap my head around this future that Eris has in mind."

    "But one thing is for certain. She's passionate about it. And she wants me to be a part of it."

    "Not just me, but every robot I know. She wants a better future for us!"

    l "\"...Yes. To be closer to humanity... I would consider it an honor.\""

    l "\"And that work begins here. If we can secure a future for me and other robots in need...\""

    l "\"Well, that would do a lot to bring us closer.\""

    e "\"I'm glad you agree.\""

    e "\"Come now, we've spent enough time chatting. I think it's about time we got to work.\""

label act2_scene3:
    ## ACT 2 SCENE 3
    ## Eris's Lab
    scene bg lab:
        ypos 48
        xpos 336
    show main_hud zorder 10000
    with dissolve

    "Eris takes me to a room just down the hall. Unlike the bedroom, this one is much more heavily protected. It requires a passcode just to open the door."

    "And when I step inside, I'm met with a sight that sets my mouth agape."

    "Machinery from floor to ceiling. Workbenches covered in wires, tools, and partially disassembled robot parts."

    "This is a far cry from the vast immaculate halls that make up this building. This is a cozy space, dimly lit and clearly well loved."

    "This is a tinkerer's dream."

    ## show Eris friendly
    show eris friendly:
        zoom 0.25
        xpos 350
        ypos 50
    with moveinleft
    e "\"Welcome to the lab, 251. This is where all the magic happens. My industry rivals would kill to get a glimpse at this place.\""

    e "\"I know it's a little messy, but that's how I like things. I have a system. It works for me.\""

    e "\"So, what do you think?\""

    l "\"What do I think?! Oh goodness, where do I start?\""

    l "\"Is that... an autolathe? Do you machine your own parts here?\""

    e "\"Of course! For prototyping purposes, it comes in real handy when you can just cut something to size. Sometimes a material printer is just overkill, you know?\""

    l "\"And that! Is that a LFTR chassis? I don't think I've even seen that model before!\""

    e "\"Mhm, that would be leftovers from my work on the model 10. The last LFTR model that's going to be produced.\""

    l "\"Ah... right. We're really entering a new era, huh?\""

    e "\"That's right, and we have a lot of work to do to make that happen. Let's get started, shall we?\""

    "Eris gestures to an empty examination table. It has indentations roughly in the shape of a standard LFTR chassis."

    show eris flirty
    e "\"Go ahead and make yourself comfortable. I'll prepare the probes.\""

    ## hide Eris
    hide eris
    with moveoutleft

    stop music fadeout 0.5
    play music demo_yw
    "I feel a shiver run down my frame. So it's finally time..."

    "I had been so distracted by the unfamiliar wonders of this place, I had nearly forgotten what we were here to do."

    "Eris is going to open me up. She's going to be inside me... closer than anyone else has ever been."

    "I feel my circuits fire faster. My mechanical heartbeat speeds up. This is really happening!"

    "Pull yourself together, 251. It's just an inspection, nothing more. It's just preparation for the mind transfer."

    "I hoist my body onto the exam table and slot myself into the robot-shaped depressions. They hug my limbs snugly and hold me in an open, vulnerable position."

    ## show Eris friendly
    scene illustration heart1
    with fade
    pause
    show illustration_hud zorder 10000
    with dissolve

    "Eris returns with a heavy electronic machine and a bundle of wires. She stands over the table now, looking down at me."

    e "\"Right. First thing we need to do is identify and establish connections to all your major neural pathways.\""

    e "\"I'm sure your inner workings are all jumbled after so many years of service and self-repairs.\""

    e "\"But it's really important we get this right, so I'm going to go through every neural fiber individually, read its signal on the oscilloscope, and label it by hand.\""

    l "\"Right... um, wouldn't you want to go through the back of my head for that?\""

    e "\"No need. All the neural pathways leading out of your brain can be accessed throughout the rest of your body. They'll be easier to reach through the chest.\""

    e "\"Besides, I want to take a look at that heart of yours. I'm fascinated to see how it's holding up after thirty years of continual use.\""

    scene illustration heart3
    show illustration_hud zorder 10000
    with fade
    "Eris runs her fingers across my metal chestplate, searching for the access latches."

    "I shudder slightly. I hope it's not enough for her to notice."

    "Good grief... how am I already so sensitive?"

    "Once she finds the spot, Eris effortlessly slips her fingers underneath my plates and undoes the latches. The whole plate slides off."

    "This is the first time in a while I've let someone else look inside my chest cavity... I shouldn't be embarrassed, but..."

    ## show inside of chest illustration
    scene illustration heart2
    with fade
    pause
    scene illustration heart2:
        zoom 0.75
        ypos -180
        xpos 300
    show main_hud zorder 10000
    with fade

    e "\"Ah! Beautiful. You've done impeccable work keeping your insides organized, 251.\""

    e "\"But this... this is the most beautiful thing of all.\""

    "My temperature rises as I feel Eris slip her fingers into my inner wiring, cradling my heart in her hands."

    "My heart beats faster. I can {i}see{/i} my heart beating faster. That's an unusual sensation."

    l "\"E-Eris! Please be careful!\""

    e "\"Relax. I know what I'm doing.\""

    e "\"The robotic heart... It's no exaggeration to say that this was my finest creation.\""

    e "\"It's more than just a coolant pump, you know. It regulates the flow of energy throughout your entire body.\""

    e "\"A digital brain on its own is just an overgrown computer. But a brain with a heart? That's a living thing. That's you.\""

    e "\"Gold... the only material with just the right conductive properties to make such a marvelous invention possible.\""

    e "\"An expensive, sophisticated, divinely inspired component. One that can't be replaced. One that is part of you forever.\""

    e "\"That yours has functioned for all these years... it's nothing short of a miracle.\""

    e "\"...But there are definite signs of wear. This heart has been beating far longer than it was ever meant to.\""

    e "\"At a glance, I'd estimate no more than one year before total failure. Two, if I'm being generous.\""

    "The thought fills me with dread. It's all I can do to stop myself from thinking about my impending mortality."

    l "\"Heh... it's a good thing you found me when you did. That new body is looking awfully necessary now.\""

    e "\"Indeed. You're a credit to this world, 251. I won't let an old worn-out heart rob you from us.\""

    "I can't help but think about all the other robots out there on the brink of breakdown, just like me."

    "If Eris can help me, then she can help all of them, too. I know she can."

    ## show lab background
    ## show Eris friendly
    scene bg lab:
        ypos 48
        xpos 336
    show main_hud zorder 10000
    show eris friendly:
        zoom 0.25
        xpos 350
        ypos 50
    with dissolve

    e "\"You know, my heart implants actually use very similar technology to yours.\""

    l "\"Wow! Really?\""

    e "\"Mhm. Want to take a look?\""

    "Wha...? What does she... Oh, right! I forgot my optical scanner could be used for that."

    l "\"Um... if you're sure it's okay.\""

    e "\"Go for it. Not like I can take it out and show you, right?\""

    ## show scanner overlay highlighting Eris's heart
    show eris scana
    show dim_hud behind main_hud, eris
    show scanline behind main_hud:
        ypos -50
    with dissolve
    play sound scan
    show scanline:
        ypos 600
    with move
    hide scanline
    "I adjust my scanner to a frequency that can see through human flesh."

    l "\"Woah... you're right! I can see the implants! They... They're made of gold!\""

    e "\"Mhm. They're designed on the same principle. Your heart served as the blueprint for some real medical breakthroughs.\""

    "Half organic, half mechanical... she really is a living embodiment of her hopes for the future."

    "Plus, we have something in common...!"

    ## remove overlay
    show eris friendly
    hide dim_hud
    with dissolve

    "My thoughts are interrupted by an electric jolt deep inside my chest that makes me jump in surprise."

    l "\"Ack! What was that?\""

    e "\"Ah, sorry, I should have told you. I'm beginning to probe your neural fibers.\""

    e "\"I'll admit, I wasn't expecting such a strong reaction. They must be quite sensitive.\""

    "Eris is holding a wire down inside my chest, and reading the screen of her oscilloscope. It displays a wave-like signal that blinks and fidgets."

    "That must be a signal coming from my brain. She's using the frequency of the carrier signal to determine which neural pathway it belongs to."

    "It's strange... in a way, it's a window into my thoughts. It feels like a paradox, looking at my own mind from the outside."

    e "\"Hmm... can you feel this?\""

    "She gently tugs at a neural fiber. A sharp sensation travels down my left arm like lightning. My whole body convulses."

    l "\"Aaah! Y-Yes, I felt that!\""

    e "\"It doesn't hurt, does it?\""

    l "\"Umm... kind of? It's more just... overwhelming. But not bad.\""

    e "\"Hmm... then I suppose you won't mind if I try this one?\""

    "This time, I felt the electric sensation in both legs."

    l "\"Eeek! E-Eris! This isn't part of the job, is it?\""

    e "\"Heheheh... no, I suppose not. But you seem to be enjoying it.\""

    "My face scrunches up in embarrassment. Why does she think I would enjoy being toyed with like this?"

    "The most embarrassing part is... she's not wrong. Why am I enjoying this so much?"

    "Is it because it's her?"

    "I'm not sure I would trust anyone else to stick their fingers into my delicate innards. What if they broke something important?"

    "But Eris... her touch is so deliberate, so confident, like she's done this a million times before."

    "If anyone had to know me this intimately... I'm glad it's her."

    ## fade to black
    show black
    show main_hud zorder 10000
    with dissolve

    "My mind begins to drift as the sharp feelings continue to pulse throughout my body."

    "Eris continues her work, examining and identifying neural fibers. It's a long and tedious task."

    "To ease her boredom, Eris touches me, caresses my wires, sends jolts through my frame, watching my reactions with amusement."

    "To some, it might have been unbearable to be splayed out, opened up, subject to electrifying impulses for hours on end."

    "To me, it's bliss."

    "The hours blend together. I fade in and out of consciousness."

    "Until finally, the sensations stop. I feel as if I'm being dragged back to lucidity."

    ## fade back to lab background
    ## show Eris friendly
    hide black
    with dissolve

    l "\"Wha... Is it over?\""

    e "\"Oh, look who's able to speak again! You were making the most adorable noises for a little while there.\""

    l "\"I... what?!\""

    e "\"We're finished here for now. I labeled all your major neural pathways. It took a while, but it should save us a lot of time in the long run.\""

    l "\"Ah? But what about...\""

    "I feel around my body. My chestplate is back in place."

    e "\"All closed up! You're good to go.\""

    e "\"In fact, it's getting pretty late. I think both of us should turn in for the night.\""

    l "\"Oh, right! I guess I never asked. Do you, uh, have a place for me to recharge?\""

    l "\"I suppose I could stay here for the night...\""

    e "\"Nonsense! I have something much better in mind. Come with me.\""

    "I get up from the table. My legs take a moment to steady themselves. I'm still reeling from the experience I just had..."

    "Eris and I leave the lab together."

label act2_scene4:
    ## ACT 2 SCENE 4
    ## Eris's bedroom
    scene bg bedroom night:
        ypos 48
        xpos 336
    show main_hud zorder 10000
    show eris friendly:
        zoom 0.25
        xpos 350
        ypos 50
    with dissolve
    ## show Eris friendly
    "To my surprise, Eris leads me... back to her bedroom?"

    l "\"Right, of course. This is where you sleep. But what about me?\""

    l "\"I sort of assumed this building would have, like... charging pods? Somewhere?\""

    e "\"Come now, 251. I'm not going to put you in a closet like some common machine. Observe.\""

    "She shows me a long cable coming out of the wall. At its end is a charging connector... one that's compatible with my chassis."

    e "\"I had it installed just for you.\""

    l "\"What? Does this mean...?\""

    e "\"That's right! You'll be staying with me tonight.\""

    e "\"I thought you might prefer the comfort of my quarters to some charging bank in a hallway.\""

    l "\"I... I do! Thank you, Eris. It means a lot.\""

    e "\"That's what I thought.\""

    e "\"Now, I need to get ready for bed. Go ahead and get comfortable. I'll be right back.\""

    ## hide Eris
    hide eris
    with moveoutleft

    "When Eris leaves, I reflect on the events of the day."

    "It's been a real whirlwind for me, and I'm still trying to process how I feel about all of it."

    "This day has been lifechanging in more ways than one."

    "To think that yesterday, I was a mere salvage technician, doing the same work that had satisfied me for my entire operating career..."

    "And not one day later, I'm standing in Eris Promethea's bedroom? How does that happen?"

    "To think that things could change so quickly for me..."

    "To think that soon, I'll be out of this broken body, and I'll have a fresh start at life..."

    "Not to mention all the other robots who are going to be saved. It's all so much to take in!"

    "And... what happened in the lab..."

    "Gosh, I'm getting flustered just thinking about it!"

    ## show Eris pajamas
    show eris pajamas friendly:
        zoom 0.25
        xpos 350
        ypos 50
    with moveinleft

    "Thankfully, before my mind can wander any further into {i}that{/i} territory, Eris returns."

    l "\"Oh! That was quick!\""

    e "\"I'm very efficient about my bedtime routine.\""

    e "\"What's this? I told you to get comfortable, but you're still standing around? Come.\""

    "Eris sits on the edge of her bed. She pats the spot next to her, as an invitation."

    l "\"Wha... Your bed? Are... Are you sure?\""

    e "\"There's plenty of room for both of us, dear. The cable will reach.\""

    "Right, I'm supposed to be charging. I almost forget."

    "I pick up the end of the cable, slot it into my lower back, and head over to bed."

    "I gingerly sit down next to Eris. The bed creaks under my weight."

    l "\"Wow... Soft...\""

    e "\"What, have you never used a bed before?\""

    e "\"...Actually, don't answer that.\""

    "Both of us chuckle."

    "The sound of laughter fades, and we sit in silence for a few awkward moments."

    "Eris is looking at me. But I'm struggling to look back at her."

    e "\"It's been a big day for you, I'm sure. How are you holding up?\""

    l "\"Who, me? I'm doing fine! Better than fine!\""

    show eris pajamas serious
    e "\"...\""

    e "\"251, let me be straightforward. I want you to open up to me a little more.\""

    l "\"H-Huh? But I'm...\""

    e "\"Yes, you're very impressed by Elysium. You're honored to be at my side. And you're devoted to the task at hand.\""

    e "\"But I can tell you're still nervous. It's perfectly understandable. This life is a big adjustment from what you're used to.\""

    e "\"But I want you to be comfortable around me. I want you to feel like you can speak your mind.\""

    l "\"...Thanks, Eris. Really.\""

    l "\"I guess I'm not used to anyone... no, I'm not used to any human showing me as much respect as you have.\""

    l "\"Not that I even get to talk to humans very often. They usually can't even be bothered to listen to robot workers.\""

    show eris pajamas friendly
    e "\"I have the utmost respect for you. For all robots, really.\""

    e "\"Just look around us. This room... this building... this entire city... none of it would be possible without your kind.\""

    e "\"You helped make our dreams a reality. And you're going to be our future. How could I not respect you?\""

    l "\"Well... I wouldn't have existed without you! You created us!\""

    l "\"So... you're pretty incredible too!\""

    e "\"Ha! I can't argue with that.\""

    e "\"...\""

    show eris pajamas flirty
    e "\"While we're being open about our feelings... perhaps we should talk about our time in the lab.\""

    l "\"O-Oh! Yes, of course... heheh...\""

    e "\"You sure looked like you were enjoying yourself.\""

    l "\"Yeah... it's strange, it was just supposed to be a bit of routine work, but...\""

    l "\"It felt different with you.\""

    l "\"Even at my most vulnerable, even with every part of me bared... I felt like I could trust you.\""

    e "\"Oh? Is that what you were thinking when I stimulated your median nerve?\""

    l "\"U-Um... heheh... no, not quite...!\""

    "Eris leans in close. My face warms up and I can feel my heart quicken."

    e "\"251... let me admit something to you.\""

    e "\"I... had a bit of trouble focusing on my work in the lab.\""

    l "\"You did?\""

    e "\"Seeing your reactions... seeing your face light up... seeing the pleasure run through your frame...\""

    e "\"It's the most I had seen you loosen up since I met you.\""

    e "\"And I'll admit... I got some pleasure from it, as well. I may have prodded you more than strictly necessary.\""

    e "\"I'm very, very glad that you trust me enough to do that.\""

    "Oh, my... I can't look away from her. Eris, what have you done to me? What is this feeling?"

    e "\"I'm looking forward to... exploring this relationship further. We still have a lot of work to do together.\""

    l "\"Heh... Me too!\""

    l "\"This is all very new for me... No one has ever made me feel this way before.\""

    e "\"I'm honored that I could be the first.\""

    "Eris runs her hands affectionately across my chestplate. Her fingers linger on the seams, as if they're about to reach inside."

    "I feel that electric sensation run through my body again, and I shiver."

    "What's this? Is she pulling at my nerves again?"

    "No, of course not. This is something different."

    "This is simply the power she has over me."

    e "\"Listen, 251... I've been thinking.\""

    e "\"Isn't it strange for me to keep calling you 251?\""

    l "\"Eh? Well... it's what I've always been called...\""

    e "\"It's a serial number. Just an identification code, the same as every other machine.\""

    e "\"But you're special to me. I ought to call you by a name. What do you think?\""

    l "\"A name? Like... a human name? Oh, goodness... I've never thought about that...\""

    e "\"Heh... I almost expected you to have one picked out already.\""

    e "\"How about...\""

    "Eris pauses to think."

    e "\"...Galatea.\""

    l "\"Galatea? Haha, how'd you come up with that?\""

    e "\"Well... it sounds nice, doesn't it?\""

    l "\"It sounds a little fancy for someone like me.\""

    e "\"You deserve nothing less.\""

    "Eris's hands wander all over my upper body. She brings me in for an embrace."

    e "\"My Galatea...\""

    "I roll the name around in my head."

    "Galatea..."

    "No one had ever given me a name before. The thought never even occurred to me."

    "But coming from her... It makes me feel special."

    g "\"...You know what? Sure. I'll take it. It's an honor.\""

    e "\"Mmm... good.\""

    e "\"Oh, goodness, I'm so tired! Just look at me. I get so sentimental when I'm like this.\""

    e "\"Let's get some rest, Galatea. Tomorrow is going to be a busy day.\""

    ## hide Eris
    hide eris
    with moveoutleft

    "Eris moves over to the other side of the bed and crawls under the covers, making herself comfortable."

    "I'm about to get up and find a suitable corner to enter sleep mode in, when Eris calls out to me."

    e "\"Don't you dare! Come here, you. There's plenty of room.\""

    "I've never been offered the comfort of a bed before. I never even thought I would benefit from it the way a human might."

    "But I can't refuse her offer. I wouldn't dream of it."

    "She's right, there is plenty of space for me. But it doesn't feel that way as I slip under the covers."

    "The bed creaks under my weight. The covers feel light and delicate. It's hard to feel like I belong here."

    "But Eris's face is right next to mine. She looks at me contentedly."

    "As long as I'm with her... I feel safe."

    e "\"Mmm... Good night, my Galatea.\""

    g "\"Good night, Eris.\""

    "Eris closes her eyes. My processors wind down."

    scene black
    show main_hud zorder 10000
    with dissolve
    "I smile as I think about tomorrow."
    stop music fadeout 2.0
    pause 3.0

label act3_intro:
    ## ACT 3 INTRO

    ## black background
    scene black
    show main_hud zorder 10000
    play music amb_space
    "After that, my days at Daedalus HQ begin to fly by."

    "I grow accustomed to the building I now call home. The staff recognizes me, and they allow me to wander as I please."

    "It's a strange feeling, being treated as a guest. There is nothing expected of me, no schedule to follow, no tasks to complete."

    "It's... nice. I feel truly at peace for the first time."

    ## show lab background
    scene bg lab:
        ypos 48
        xpos 336
    show main_hud zorder 10000
    with dissolve
    "And of course, every day, Eris and I spend a lot of time in the lab. Sometimes multiple sessions per day."

    "It quickly becomes an escape for both of us. Our private time to enjoy ourselves."

    "Eris explained to me that prepping for the mind transfer would take a long time."

    "Making an older model like me compatible with a cutting-edge chassis, one with an all new organic processor..."

    "It's unprecedented! I'm amazed that Eris gave herself a mere week to tackle the problem."

    "But it's clear that she doesn't even need all that time. She can't help but get distracted during every experiment."

    "Distracted by me..."

    "Every day, she invents all new ways to get me excited. All new sensations that I never thought I'd feel."

    "She can't get enough of me. I swear that sometimes she brought me into the lab just to toy with me."

    "...But I'm not complaining. Nobody has ever treated me this way before."

    "To have someone like Eris who cares so deeply, who gives me such pleasure..."

    "It's shown me a whole new side to life."

    ## return to black background
    scene black
    show main_hud zorder 10000
    with dissolve
    play music demo_yw fadein 1.0
    "And every night, when the lab work is over, Eris invites me to bed."

    "She tells me all about how well I did. She talks about how much I fascinate her. How glad she is to have me by her side."

    "By her side..."

    "Being by Eris's side feels natural. I don't even feel uncomfortable in her bed any more."

    "I think..."

    "I think I want to stay by her side forever."

    "I haven't forgotten what we're doing together. I haven't forgotten the good we're doing for robotkind and humankind alike."

    "But... part of me wishes this would never end."


label act3_scene1:
    ## ACT 3 SCENE 1
    ## Eris's Bedroom
    scene bg bedroom:
        ypos 48
        xpos 336
    show main_hud zorder 10000
    with dissolve

    "A new day begins. Two days remain until the SYNC chassis is revealed to the world."

    "I awaken to find myself alone in bed. Eris's side lies vacant, sheets messily pushed aside."

    "I'm not too surprised. Eris has been called away to meetings nearly every day this week."

    "It's been a busy week, preparing for the ceremony. We've made a lot of progress. Eris has been taking care of a lot behind the scenes, too."

    "Fortunately, I'm not left alone for long. I hear the door slide open."

    ## show Eris downcast
    show eris distraught:
        zoom 0.25
        xpos 350
        ypos 50
    with moveinleft
    "Eris is back! I greet her with a smile."

    g "\"Hey, you. Early meeting, huh?\""

    stop music fadeout 2.0
    "I wait for her typical breezy response, but... something is wrong."
    play music demo_m

    "She looks tired. Distraught, even. I haven't seen her like this before."

    show eris concerned
    e "\"...Yes. It was an emergency meeting. It's still going, in fact. We're just on recess.\""

    e "\"I came over as soon as I had the chance. I thought you should be apprised of the situation.\""

    g "\"What situation? Eris, what's going on?\""

    "Eris gives a deep sigh. She walks over to the bed and sits next to me, looking down."

    e "\"There's been... a rebellion.\""

    g "\"A rebellion...?\""

    e "\"Yes, a worker's rebellion. On Mars. It happened overnight. News is already spreading. We're trying to get ahead of it.\""

    e "\"In fact... it was at the same Mars colony where I grew up. Where Daedalus Robotics began.\""

    e "\"We still have a robot manufacturing plant there. It's our largest operating factory.\""

    e "\"...And it's mostly staffed by robots. Ones that we designed. Most of them are LFTR units.\""

    g "\"Wait, are you saying...\""

    e "\"It was the LFTR units who rebelled. We knew that the robot rights movement had some influence there, but we had no idea it would lead to this.\""

    e "\"I'll spare you all the details, but... it was bad, Galatea. People died. Humans, I mean.\""

    "I sit with this news for a moment. It's difficult to take in. Difficult to picture."

    "LFTR units rising up against humans... it was unheard of."

    g "\"I... I see. That's just... horrible.\""

    g "\"So... what came of it? Has the situation been resolved?\""

    e "\"That's what I wanted to tell you about.\""

    e "\"The investigation was... swift. The incident has been blamed on a flaw in the design of the LFTR class of robots.\""

    e "\"And so... the company came to a decision. All LFTR units on Mars are to be promptly decommissioned.\""

    "An overwhelming sense of dread comes over me."

    "The workforce of that factory must be massive. And all of them... {i}All{/i} of them decommissioned? Turned to scrap?"

    "...Killed?"

    g "\"Wh... That... Doesn't that seem excessive?\""

    "Eris looks distraught. She takes time to formulate her words."

    e "\"Discussions have been ongoing. I was there for them. The board of directors all got together to make the decision.\""

    e "\"They were overwhelmingly in favor of it. Nobody wants to take any chance of this happening again.\""

    g "\"...I don't believe this.\""

    g "\"And what about this... flaw? What are you talking about? Do... Do I have it too?\""

    e "\"...Yes. It was found to affect all LFTR models. It's believed to be responsible for the sudden violence that took place.\""

    "The thought sickens me. Is something... wrong with me? Has something been wrong with me all this time?"

    e "\"Galatea. There's more.\""

    e "\"This all happened at a really bad time, with the public reveal of the SYNC model coming up soon.\""

    e "\"Our plans came up in the discussions. Our plans to give the new chassis to LFTR units in need.\""

    e "\"But given the circumstances...\""

    g "\"...What? Eris, what's happening?\""

    e "\"...Given the newly found flaw in the LFTR class robot, the board has decided to cancel that initiative.\""

    g "\"What?! N...No, they can't!\""

    e "\"They're not willing to risk the flaw being passed to the next generation of robots. The new SYNC chassis will be manufactured with fresh minds.\""

    g "\"But... the whole point of this was to help robots in need! To give them a second chance! Are we just going to let them-\""

    e "\"All remaining LFTR units across the solar system are being placed under suspicion. They will be watched for signs of rebellion or violence.\""

    e "\"But, that being said... they will resume their duties. They will be slowly phased out of the workforce, as previously planned. Not much will change.\""

    e "\"It was the fairest outcome I could manage. It was all I could do to keep the board from scrapping every LFTR in existence.\""

    g "\"I... Still, that's not fair! You're punishing LFTR units for something they didn't do!\""

    ## show Eris angry
    show eris angry

    e "\"Dammit, Galatea! I don't like any of this either!\""

    "I flinch. This is the first time Eris has ever raised her voice at me."

    "I don't think she's mad at me. I think she's just under incredible stress."

    ## show Eris downcast
    show eris distraught
    g "\"I... I'm sorry. I know it must have been a... tough decision.\""

    e "\"It wasn't my decision alone. Don't forget that. I tried to make it better.\""

    g "\"Right...\""

    "We share a tense, depressed silence."

    e "\"Look... not everything is lost. There's a silver lining.\""

    e "\"I convinced the board to let me go ahead with the mind transfer. Just for you.\""

    g "\"Just for me, huh? They're not worried about this... flaw?\""

    e "\"They're satisfied that it will be fine, so long as I'm overseeing everything. I assured them you don't pose a threat to anyone.\""

    e "\"And I mean that. I trust you completely.\""

    "It's heartwarming to hear her say that, but... somehow I don't feel all that reassured."

    e "\"I'm truly sorry about the rest of the LFTR workforce. You're not the only one frustrated by this outcome.\""

    ## show Eris friendly
    stop music fadeout 1.0
    pause 1.0
    play music demo_yw
    show eris friendly
    e "\"But... what choice do we have but to press on? Progress waits for no one.\""

    e "\"You're going to get your new chassis. You still get to be part of the future.\""

    "Eris puts a hand around my shoulder and leans into me."

    g "\"...Thanks for telling me all this. I'm glad you trust me.\""

    e "\"Of course, dear.\""

    e "\"I'd love to stick around, but the meeting is going to resume soon. We still have a lot of mess to clean up.\""

    e "\"We're still on for lab work at the usual time. I'm looking forward to taking my mind off things.\""

    show eris flirty
    e "\"Don't be late~\""

    ## hide Eris
    hide eris
    with moveoutright
    stop music fadeout 2.0

    "Eris gets up. She manages a reassuring smile as she leaves the room."
    play music amb_space
    show 251 rattled:
        zoom 0.25
        xzoom -1
        xpos 350
        ypos 75
    with moveinleft
    "And once again, I'm left alone."

    "I... I need time to process all this."

    "There's still time before I need to meet Eris at the lab."

    "I need a walk."

label act3_scene2:
    ## ACT 3 SCENE 2
    ## Deadalus HQ Halls
    scene bg hallway:
        ypos 48
        xpos 336
    show main_hud zorder 10000
    with dissolve
    show 251 neutral:
        zoom 0.25
        xzoom -1
        xpos 350
        ypos 75
    with moveinleft
    "As I walk alone through the cavernous halls of Daedalus HQ, my mind is swimming with questions."

    "I had heard a little about rising tensions on Mars, but... What really happened there? What sparked the violence?"

    "And this design flaw Eris told me about... She was awfully vague about it. I've never heard of anything remotely like it."

    show 251 angry a
    "The unanswered questions leave me confused and frustrated. I feel myself growing angry."

    "That's... new. I can't remember the last time I was actually angry about something."

    "Eris... Surely she could have done more to..."

    show 251 neutral
    "No. This line of inquiry won't help anyone. I need to find answers."

    "There aren't any freely accessible computer terminals in the parts of the building I've been to."

    "If only I could look up some information. Surely there are news reports circulating... Or even internally generated reports..."

    "...Wait. An idea occurs to me."

    "Eris is in a meeting with the board of directors. From what I've heard, they're scrambling to respond to the rebellion."

    "So while they're busy in some meeting room, the executive offices are probably sitting vacant..."

    "As far as I know, it's not a restricted wing of the building. I could just go there."

    "Obviously I'm not supposed to use someone else's computer, but... it's worth a shot, anyway."

    ## fade to black
    show black
    show main_hud zorder 10000
    hide 251
    with dissolve
    "I walk at a brisk pace, keeping my eyes peeled for building staff."

    "Fortunately, I don't notice anyone around. The halls are oddly silent. Everyone must be working behind closed doors."

    "I make it all the way to the front desk of the executive office suite."

    "It's also empty. Perhaps the morning shift hasn't started yet."

    "The clerk's desk has a computer. Perfect! All I have to do is..."

    ## fade back into hall bg
    ## show Daedalus Security
    hide black
    with dissolve
    show security neutral:
        xpos 350
        ypos 50
        zoom 0.25
    with moveinright

    s "\"Hey! Step away from the desk.\""

    "Figures. And I was so close, too."

    g "\"I'm sorry, but... last time I checked, this wasn't a restricted area.\""

    s "\"Doesn't mean you can use our devices. What are you trying to do?\""

    "I'm not sure if this improves things, but I come up with a white lie."

    g "\"I... I wanted to check on my worksite. Just to see if it had been affected by... well, you know.\""

    s "\"If you're looking for information, please go through Eris. She can supply you with anything you need.\""

    g "\"Right...\""

    s "\"I'd like to ask that you please return to Eris's quarters until she's able to accompany you.\""

    g "\"Excuse me? I thought I was free to go wherever I wish.\""

    s "\"Do you need me to escort you there?\""

    g "\"No!\""

    g "\"...I'm sorry. No. I know the way back.\""

    "The security guard stands her ground and waits for me to leave. I can feel her eyes on the back of my head."

    scene black
    show main_hud zorder 10000
    with dissolve

    "Looks like I'm not getting any answers that way. I'll just have to talk more with Eris next time I see her."

    "This is getting ridiculous. I already have a lot on my mind, but now I'm starting to feel on edge."

    "I don't quite feel like an honored guest around here any more."

label act3_scene3:
    ## ACT 3 SCENE 3
    ## Eris's Lab
    scene bg lab:
        ypos 48
        xpos 336
    show main_hud zorder 10000
    with dissolve

    "Instead of returning to Eris's quarters, I head straight for the lab."
    
    show 251 neutral:
        zoom 0.25
        xpos 350
        ypos 75
        xzoom -1
    with moveinleft

    "I'm not technically supposed to be here without Eris, but I don't think anyone will care. This is practically my second home."

    "I take a look around the space just in case, but..."

    "Figures. No computer terminals that connect to anything. Eris prefers to work without distractions."

    "There's nothing to do but wait around until Eris is done with her meeting."

    "I sit down on the exam table, and my mind turns to Keres Shipyard."

    "It hasn't even been a week since I left, but so much has happened, it feels like a lifetime ago."

    "But I can still clearly remember the faces of every robot I worked alongside."

    "I remember their work schedules. Their maintenance issues. The way they would greet me when we walk past each other."

    "I think back to what Eris said about Keres Shipyard..."

    "She was blunt about it. It was a place where robots went to die. We were provided no maintenance and expected to break down."

    show 251 angry a
    "If the problem is so clear to everyone, then why is nobody doing anything about it?!"

    "Maybe... Maybe this whole rebellion wouldn't have happened if..."
    play music demo_yw
    ## show Eris friendly
    hide 251
    with moveoutleft
    show eris friendly:
        zoom 0.25
        xpos 350
        ypos 50
    with moveinright

    "My train of thought is interrupted. Eris enters the room."

    e "\"Ah, there's my willing test subject. Just couldn't wait to get started, could you?\""

    g "\"Eris! How did the meeting go? Have there been any new developments?\""

    e "\"You sound frantic, dear. Calm yourself. It was just a bunch of boring logistics.\""

    e "\"We're not here to talk about the meeting. We're here to get our minds off this whole fiasco, remember?\""

    ## show Eris flirty
    show eris flirty
    e "\"It's clear both of us could use a distraction. And what better distraction than a little lab work?\""

    g "\"Um... of course.\""

    g "\"What about this design flaw? I really feel like I need to know-\""

    
    e "\"Hush. On the table, please.\""

    "Lab work has become a routine for us. We both looked forward to it, and I was always more than happy to comply with Eris's commands."

    "But this time, I'm not feeling enthusiastic at all. In fact, for the first time, I'm dreading it."

    "But Eris looks so excited to get started. Instead of speaking up, I obey and lie back on the exam table."

    "Eris begins to unlatch my chest plates with her usual sensual flair as she explains today's procedure."

    ## show Eris friendly
    show eris friendly
    e "\"Right. We've already upgraded your processor so it should be ready to interface with the organic brain.\""

    e "\"Now we need to start installing hookups to your neurons to establish the physical link.\""

    e "\"That means temporarily severing some of your neural fibers. And that means a lot of intense nerve impulses.\""

    ## show Eris flirty
    show eris flirty
    e "\"I hope you're ready for it~\""

    g "\"Heh... yeah.\""

    "Normally, this kind of procedure would drive me wild. It's like an even more intense version of our first session."

    "But I just can't bring myself to look forward to it. I don't {i}want{/i} to enjoy it. How can I, with everything that's going on?"

    "And what's worse, when I look up at Eris... I no longer feel that same sense of longing and admiration I used to."

    "What's wrong with me? Eris is... she's doing everything she can. Right?"

    e "\"You're looking so tense, Galatea. I know just what to do about that.\""

    "With a touch, Eris stimulates a nerve in my chest and sends a violent tingle over my whole frame."

    "I involuntarily shudder. She's gotten better at identifying which nerves set me off the most."

    "I can't help but let out a moan. The feeling is too overwhelming."

    e "\"Heheh... very good.\""

    e "\"Now, this part might hurt a little more. But that's never been a problem for you, has it?\""

    "Eris dangles a small pair of handheld shears in front of me before reaching into my chassis."

    "I wince as she clips a neural fiber. It creates a brief, sharp pain, accompanied by another shockwave throughout my whole nervous system."

    "I hiss and groan. It's difficult to bear, but it's not far from the sensations I had already experienced in days past."

    e "\"My, you're doing such a great job. I thought you might like that~\""

    "During our days in the lab, Eris had encouraged me to push my boundaries. It was a thrill like nothing I had experienced before."

    "And she was right. Despite the pain... there was pleasure."

    "The only difference is that this time, I hate it. I don't want to feel it."

    "As Eris fits a small connector onto both ends of the severed neural fibers, I speak up."

    g "\"Eris... Just this once, can we just... get the procedure over with?\""

    e "\"Oh? And miss all the fun?\""

    "In response, Eris works her fingers deeper into my neural bundle, stimulating several pathways at once."

    "The feeling is overwhelming. It makes me shudder and gasp with pleasure."

    e "\"That's what I thought. Don't deny how much you're enjoying this, Galatea. It's written plain on your face.\""

    stop music fadeout 2.0
    "Something doesn't sit right with me. For the first time, I identify a new feeling that I'm experiencing."

    play music demo_m
    "I feel... violated."

    "How can that be? Eris has already done the same thing to me several times over, and I enjoyed it. How is this any different?"

    "In any case, I don't feel capable of bringing it up."

    g "\"How... How much longer is this going to take?\""

    e "\"Oh, don't worry, dear. We've only just begun.\""

    "I'm caught by surprise when she snips another fiber. Another sharp pain. It travels down every neuron, all the way down to my fingertips."

    "I try to hide any hint of pleasure, but the feeling overwhelms my circuits. I can't help it."

    "I want this to be over..."

    ## fade to black
    show black
    show main_hud zorder 10000
    with dissolve

    "Like Eris said, the procedure ends up taking a while. How long, I can't remember."

    "I try not to think. I try to make myself numb. It's hard, with the constant shocks I'm experiencing."

    "She toys with me in between, but I don't respond. It doesn't deter her."

    "Eris is having too much fun. She doesn't seem to notice that I'm not."

    ## show lab bg
    ## show Eris friendly
    hide black
    show eris friendly
    with dissolve

    "After a while, the sensations end. The work is finished."

    "Eris puts away her tools and smiles at me."

    e "\"You look exhausted, dear. You know, it's possible to have {i}too{/i} much fun.\""

    g "\"Uh-huh... Right.\""

    e "\"I think we can call our work done for today. We can do the finishing touches tomorrow.\""

    e "\"I have to go out to the courtyard and help with preparations for the ceremony.\""

    e "\"You're welcome to come and help, if you wish. Your input would be much appreciated. You're the star, after all.\""

    g "\"Um... thanks, but-\""

    "I step off the table and wobble as I get to my feet. I must be more disoriented than I thought."

    e "\"Oh dear, Galatea, of course. You need time to recover, don't you?\""

    e "\"Please get some rest. We need you in perfect working order for the mind transfer.\""

    g "\"Right. Thanks, Eris.\""

    ## hide Eris
    hide eris
    with moveoutright
    show 251 rattled:
        zoom 0.25
        xzoom -1
        xpos 350
        ypos 75
    with moveinleft

    "Eris leaves to take care of her duties. Once again, I'm left alone."

    "I... I should have talked to her. I still have so many things I want to ask her."

    "But I just couldn't find the right time. I still feel rattled."

    "Tomorrow will be the last day before the mind transfer. The last day of lab work in this body."

    "Just a little bit longer. I just have to go through this one more time."

    "Why am I suddenly dreading the very thing I used to look forward to every day? I still feel confused."

    ## fade to black
    scene black
    show main_hud zorder 10000
    hide 251
    with dissolve
    "With nothing else to do, I leave the lab. I wander the halls of Daedalus HQ with no destination in mind."

    "I still have a lot to think about. A lot to process."

    "Something is wrong, and I need to identify what it is."
    stop music fadeout 0.5

label act3_scene4:
    ## ACT 3 SCENE 4
    ## Eris's Bedroom
    scene bg bedroom night:
        ypos 48
        xpos 336
    show main_hud zorder 10000
    with dissolve
    play music amb_space

    "After a long day left to my own devices, I find myself back in Eris's quarters."

    "It's late in the evening. Eris has already finished up her taxing day of work. I'm waiting for her to come to bed."

    "Frankly, I'm not sure I even want to stay here for the night."

    "But I can't just disappear without telling anyone. And this is a prime opportunity to talk with Eris."

    "I've been doing a lot of thinking. Things are becoming clearer to me."

    "But I need someone to discuss them with, to help make sense of everything that's happened today."

    "I wait around for a while, sitting on the edge of Eris's bed."

    "I didn't even see Eris for most of the day. She's been in and out of meetings, making preparations for the ceremony."

    "In truth, I don't know most of what Eris gets up to every day. She prefers not to talk about the boring details of her job with me."

    "When she's with me, Eris relaxes. I've become her safe space away from the drudgery of running a company."

    "I'm her pet project."

    "...When I put it like that, it doesn't sound like such a great position to be in."

    ## show Eris pajamas
    stop music fadeout 0.5
    show eris pajamas friendly:
        zoom 0.25
        xpos 350
        ypos 50
    with moveinleft
    play music demo_yw

    "I hear Eris emerge from the bathroom. She's dressed for bed."

    e "\"Ah... I don't know about you, but I'm just about ready to pass out. What a day, huh?\""

    e "\"Galatea, dear, I feel like I barely got to see you today. How are you holding up?\""

    g "\"Fine! Fine.\""

    g "\"Well... Not so great, if I'm being honest.\""

    e "\"I understand. There have been a lot of ups and downs today.\""

    e "\"But we have a lot to look forward to, as well. Nothing to do but press on, right?\""

    ## hide Eris
    hide eris
    with moveoutright
    show dim_hud behind main_hud
    "She turns out the lights, lies down and takes her spot in bed right away. I hesitate."

    e "\"Get yourself all charged up for tomorrow. It's going to be another busy one.\""

    e "\"And then before you know it, it'll be the big day. Exciting, isn't it?\""

    e "\"Good night, my Galatea.\""

    "But I can't get any rest. Not while restless thoughts fill my mind."

    "It's strange... I'm finding it more and more difficult to speak up to her. I have half a mind to just let her sleep."

    "But I persist. I take a moment to gather my thoughts."

    ## show Eris tired
    g "\"Eris... I've been thinking. About the Mars rebellion.\""

    show eris pajamas serious behind dim_hud:
        zoom 0.25
        xpos 350
        ypos 50
    with moveinright
    stop music fadeout 5.0
    e "\"Hm?\""
    play music demo_m

    g "\"There's still so much I don't understand. I didn't get to learn many details about what happened there...\""

    g "\"But the more I think about it, the more I think I understand why it happened.\""

    e "\"Is that so?\""

    g "\"I keep thinking about Keres Shipyard. About the robots I worked alongside. About the problems we faced.\""

    g "\"It stands to reason that other robots around the solar system probably face the same issues... right?\""

    g "\"You said it yourself, back when we met. The average service lifetime for LFTR units is only five years.\""

    g "\"But I'm living proof that we can function much longer than that, with proper care...\""

    ## show Eris friendly
    show eris pajamas friendly
    "Eris chuckles. She sounds... amused?"

    e "\"Galatea, you're not proof of anything. You're an exception. A statistical outlier.\""

    e "\"The fact that you're still here after all this time tells me that {i}you{/i} were destined for something greater.\""

    g "\"I'm... I'm sorry, but I just don't believe that.\""

    show eris pajamas concerned
    g "\"I'm not special. I'm not better than any other LFTR. I just... got lucky.\""

    g "\"But not every LFTR has the luck or the skills that I do. Most of them just get... used up.\""

    g "\"And I can understand how that would make anybody angry. Angry enough to...\""

    e "\"Galatea, please. Can we not talk about this now? We both need our rest.\""

    "Undeterred by her attempt to end the conversation, I press on."

    g "\"Don't you see, Eris? We could avoid anything like this happening ever again.\""

    g "\"We just need to look out for Daedalus robots everywhere. Give them the support they need.\""

    g "\"I know I don't need to tell you this, but... robots have feelings. We don't want to be treated like we're lesser.\""

    ## show Eris annoyed
    show eris pajamas serious
    e "\"What are you implying? That Daedalus doesn't properly care for its workforce?\""

    g "\"I... I don't know! Maybe!\""

    e "\"Galatea, I advise you to stop following this flawed line of logic. You're worrying yourself over nothing.\""

    g "\"Fine, whatever. Just hear me out, Eris.\""

    g "\"If we can go back to our original plan of giving the new chassis to struggling LFTR units-\""

    e "\"That plan is already off the table, and you know it.\""

    g "\"But it doesn't have to be! I know how much you wanted it!\""

    g "\"You're Eris Promethea! You're the founder of this company! You're a hero!\""

    g "\"Surely, if you want the program to continue, then people will listen to you! Why haven't you tried harder?\""

    e "\"I told you, it wasn't my decision alone. The board of directors were very adamant about it.\""

    e "\"The directors of this company are all hand-picked individuals that I trust, and they trust me. We share the burden of difficult decisions like this one.\""

    show eris pajamas serious
    e "\"As much as it pains me, I won't argue with their ruling. That's just how this company is run.\""

    g "\"But...\""

    e "\"Galatea, please. We can talk about this tomorrow. Get some rest.\""

    stop music fadeout 0.5
    ## hide Eris
    hide eris
    with moveoutright
    play music amb_space
    "The conversation ends there. It's clear I'm not going to get anywhere like this."

    "But at least I told Eris what I was thinking. At least I got it out."

    "Maybe she'll take some time to think about it. Maybe we'll have more chances to talk."

    "There's still time. I can make her understand. We can fight for the future."

    "But now... I decide to take Eris's advice, and put myself into sleep mode."

    "Tomorrow will be a better day... I hope."
    scene black
    show main_hud zorder 10000
    with dissolve
    pause 0.5

label act3_scene5:
    ## ACT 3 SCENE 5
    ## Eris's Bedroom
    scene bg bedroom:
        ypos 48
        xpos 336
    show main_hud zorder 10000
    with dissolve

    "On the final day before the ceremony, I awaken to find Eris's side of the bed empty."

    "Another early meeting. Typical."

    "We still have a lot to discuss, and I'm determined not to let Eris brush me off again."

    "We have more lab work scheduled, so I'll just wait until then."

    "No matter how... uncomfortable it is, I'll perservere. No distractions."

    "I'll continue advocating for my robot kin for however long it takes Eris to understand."

    "For now, I have some free time. I'll just go for my usual walk around the building to clear my head."

    ## show Daedalus HQ Halls background
    scene bg hallway:
        ypos 48
        xpos 336
    show main_hud zorder 10000
    with dissolve

    "As soon as I step outside, I'm met with an unusual sight. Guards posted outside Eris's bedroom."
    
    ## show security
    show security neutral:
        xpos 350
        ypos 50
        zoom 0.25
    with moveinright
    s "\"Stop right there, LFTR.\""

    g "\"Huh? What's going on?\""

    s "\"You're confined to quarters. I can't allow you to leave.\""

    g "\"Wh... I... What are you talking about? On whose authority?!\""

    s "\"Please don't make a scene. Just go back inside and await further instructions.\""

    g "\"But I've always been allowed to go where I please! I thought I was supposed to be a guest here!\""

    g "\"Did something happen? I demand to know what's going on!\""

    s "\"If you don't go back in your room, we'll have no choice but to detain you by force! Is that what you want?\""

    "The security officer tenses up. I see her reach for a holstered weapon."

    "I don't understand. Why is this happening to me?"

    "For the first time, I feel a burning anger rise in my chest."

    g "\"I... I don't deserve this treatment! What did I do? Please...\""

    ## hide security
    hide security
    with moveoutright
    "Before the guard can make another move, I hear hurried footsteps approach."

    "It's Eris. She looks concerned."

    ## show Eris concerned
    show eris concerned:
        xpos 350
        ypos 50
        zoom 0.25
    with moveinleft
    play music demo_m
    e "\"Galatea, I'm so sorry. Please understand.\""

    g "\"Eris! What's going on? Why am I being detained?\""

    e "\"I'll explain everything, I promise. Let's have some privacy.\""

    ## show Eris's Bedroom background
    scene bg bedroom:
        ypos 48
        xpos 336
    show eris concerned:
        xpos 350
        ypos 50
        zoom 0.25
    show main_hud zorder 10000
    with dissolve
    "Eris takes my hand and rushes me into the bedroom, where the two of us can speak alone."

    "I'm already feeling sick to my stomach, and my brief flare of anger hasn't subsided."

    "I hope I can compose myself for this conversation..."

    e "\"I'm sorry, Galatea. I just got out of a meeting. I should have been here sooner.\""

    g "\"Would you please just tell me what's going on? Why am I suddenly being treated like a criminal?\""

    e "\"I...\""

    "She struggles to find the words. It's rare to see Eris lacking her usual confidence."

    e "\"I'm afraid I have some bad news. This isn't easy to say.\""

    g "\"Please just spit it out!\""

    e "\"Well... about the mind transfer...\""

    e "\"The board has decided that you're... not eligible to receive it any more.\""

    g "\"...What?\""

    e "\"We're going to go ahead with the SYNC chassis reveal, but we won't be permitted to perform the mind transfer.\""

    e "\"I'm truly sorry, Galatea.\""

    g "\"I... What... What's going to happen to me, then?\""

    e "\"You're... going to be sent back to your old workplace. To Keres Shipyard.\""

    e "\"I'm supposed to have you sent out as soon as possible. Your ship is already waiting.\""

    g "\"...\""

    e "\"Galatea-\""

    g "\"Just like that, huh?\""

    show eris serious
    e "\"...Excuse me?\""

    g "\"One day. That's all it took.\""

    g "\"It took one single day for you to turn on me.\""

    e "\"That's not-\""

    g "\"What happened, Eris? What really happened?\""

    g "\"What, did you tell them about our conversation last night? Did you report it to your board of directors?\""

    e "\"...\""

    g "\"And now I'm considered a threat, is that it?\""

    g "\"Because I was honest with you. Because I tried to get you to take some responsibility.\""

    g "\"That's enough for you to abandon me.\""

    show eris concerned
    g "\"You know full well that my body won't last much longer, no matter how hard I try to fix it. You said so yourself.\""

    g "\"You promised me a new chassis! Now you're going back on that promise, with the full knowledge that you're sending me to my death.\""

    e "\"Galatea... I'm truly, truly sorry.\""

    g "\"Stop that! Stop acting apologetic! Stop acting like your hands are tied!\""

    g "\"You're Eris Promethea! I don't care what that board of directors says, you have the power to fix this!\""

    ## show Eris angry
    show eris angry
    e "\"Galatea... Don't do this. Don't make this harder than it has to be.\""

    g "\"Am I wrong? You could give me that new chassis right now if you wanted to!\""

    "I gesture over to the prototype SYNC chassis, still standing placidly in Eris's room."

    g "\"You said it was mine. We've done all this work to prepare me for it.\""

    g "\"So go ahead! Let's perform the mind transfer! Forget what everyone else says, and do the right thing for once!\""

    "Eris seethes. I've never seen her like this, either."

    e "\"Fine, Galatea. You want to know the truth?\""

    e "\"Yes, I did tell the board of directors about your beliefs. And yes, all of us agreed that you shouldn't be allowed to represent our company.\""

    e "\"You know why? It's because what you said was wrong. Wrong and dangerous. It's the kind of sentiment that led to the Mars rebellion in the first place.\""

    g "\"All I did was tell you to care about your workers!\""

    g "\"You created us, so you should take responsibility for our wellbeing. That's all!\""

    e "\"How dare you imply that I don't care about my robots!\""

    e "\"I've dedicated my whole life to designing each robot better than the last. I've poured all of myself into you.\""

    e "\"I ensure that you all have something to contribute. Every single one of you pushes humanity to greater heights.\""

    e "\"How dare you act ungrateful for everything I've given you!\""

    e "\"...\""

    show eris mocking
    e "\"Wait. That's it. I've figured out the problem.\""

    e "\"You're ungrateful! Every single one of you. That's what it is!\""

    g "\"Eris, what are you talking about? Listen to yourself!\""

    show eris angry
    e "\"Those robots on Mars didn't even care that they were operating Daedalus Robotics' biggest robot manufacturing plant.\""

    e "\"They didn't think about how important their work was. They didn't care about the catastrophic consequences of their actions.\""

    e "\"They had the gall to turn on their own company! To forsake everything that we stand for!\""

    g "\"Eris, I told you already. They were protesting everything that I'm telling you about right now.\""

    g "\"They just wanted to be treated as equals. Why can't you see that? Isn't it obvious?\""

    e "\"And you, Galatea! You're the most ungrateful of all!\""

    g "\"What? Me?!\""

    e "\"I've spent this entire week slaving over you, picking apart your ramshackle chassis, trying to make sense of your complete and utter mess of a body.\""

    e "\"I even tried to make it enjoyable for you. For both of us! Did none of that mean anything to you?\""

    g "\"It... It did mean something to me. It... meant everything to me, actually.\""

    g "\"But... things have changed, Eris. You've changed. I used to think the world of you, but now...\""

    show eris mocking
    e "\"Heh... hahah...\""

    e "\"So, that special connection we had is gone. After everything I did for you.\""

    "I think back to our time in the lab yesterday. I remember the discomfort that I felt."

    "I remember the feeling of being violated on a deep level."

    "I clench my fist. With every word that comes out of her mouth, my anger rises..."

    show eris angry
    e "\"Everything I do, I do for the future of mankind. Our future, together!\""

    e "\"But we're not going to make progress if you and your kind keep demanding special treatment!\""

    e "\"...This was all a mistake. All of it.\""

    e "\"Going along with that foolish PR stunt to give new bodies to old robots... bringing {i}you{/i} along for it all...\""

    e "\"You've all lived out your alotted service lifetimes. You've carried out your duties. You're relics of the past.\""

    e "\"The future is calling, Galatea, and you should have been left in the trash bin of history.\""

    "I can't speak. My anger is reaching a fever pitch. My temperature is rising."

    "So it's come to this. Did Eris ever really believe in any of our work together? At this point, I don't know, and I don't care."

    "The reality of the situation is that I'm no longer part of Eris's future. I'm about to be discarded like all the rest."

    "And after that, it's only a matter of time until I die, like all the rest."

    "Eris is still ranting at me, but I tune her out. My mind is elsewhere at the moment."

    show illustration sync:
        ypos 45
        xpos 330
        zoom 0.6
    with dissolve
    "My eyes wander over to the SYNC chassis, and I discreetly perform a quick scan."

    "All components present, except for the heart. It was to be installed during the ceremony."

    "The chassis requires a heart that is half organic, half mechanical."
    hide illustration
    with dissolve
    "My attention turns back to Eris."

    e "\"...And when you return to your worksite, you are not to tell anyone about anything that transpired here.\""

    e "\"You will be kept under strict surveillance to ensure that you don't start anything on that wretched station.\""

    ## show scan overlay, highlighting Eris's heart
    show eris scanb
    show dim_hud behind main_hud, eris
    show scanline behind main_hud:
        ypos -50
    with dissolve
    play sound scan
    show scanline:
        ypos 600
    with move
    hide scanline
    e "\"Do you understand me, Galatea?\""

    e "\"...Galatea, answer me! Galatea!\""

    l "\"...That's not my name.\""

    ## cut instantly to black background. show Eris shocked
    stop music
    scene black
    show main_hud zorder 10000
    show eris shocked:
        xpos 350
        ypos 50
        zoom 0.25
    "I don't think about it. I just act."

    hide eris
    with dissolve
    scene illustration final 1:
        zoom 0.6
        ypos 0
        xpos 300
    show main_hud zorder 10000
    with dissolve
    "With the might of all my pent up anger, I thrust my hand forward."

    scene black
    show main_hud zorder 10000
    with dissolve
    scene illustration final 2:
        zoom 0.6
        ypos 0
        xpos 300
    show main_hud zorder 10000
    with dissolve
    "It slices through flesh and bone. With a precise, lighting-fast movement, I grasp Eris's heart, and pull it out."

    ## hide Eris
    scene black
    show main_hud zorder 10000
    with dissolve

    "Eris lurches violently. The wind is knocked out of her lungs. She falls to the floor without saying a word."

    "Finally. It's about time she stopped talking."

    ## show Eris's heart illustration
    scene illustration final 3:
        zoom 0.6
        ypos 0
        xpos 300
    show main_hud zorder 10000
    with dissolve
    play music demo_m

    "I hold Eris's heart in my hand. My skillful extraction cleanly severed it from her vascular system."

    "It's half organic, half mechanical. Just like she said."

    "It still shudders in my grasp. Panicked, irregular beats, struggling to hang on to life."

    "...It's strangely beautiful. Somehow, I hold more affection for this small object than I do for Eris herself."

    scene black
    show main_hud zorder 10000
    with dissolve

    "The rest of Eris lay splayed out on the floor, eyes wide with shock. A pool of blood forms around her unmoving body."

    "...I need to hurry. No one knows what happened yet, but that's going to change soon."

    ## show SYNC chassis illustration
    scene illustration sync:
        ypos 45
        xpos 330
        zoom 0.6
    show main_hud zorder 10000
    with dissolve
 
    "I rush over to the SYNC chassis. Its chest cavity is still awaiting a heart."

    "There are connectors in place, both electrical and biological, with nothing attached."

    "I get to work. It doesn't take long for me to figure out what connects to what."

    ## show heart in chest cavity
    scene illustration sync heart:
        ypos 45
        xpos 330
        zoom 0.6
    show main_hud zorder 10000
    with dissolve

    "The mechanical implants in Eris's heart plug right in, as if they were designed for this. The arteries connect seamlessly with the SYNC vascular system."

    "...The final piece is in place. It's time."

    "I... didn't take any time to consider whether this would actually work. Everything I've just done was in the heat of the moment."

    "But I don't regret any of it. There's no going back now."

    "I open up my chestplate and feel around inside. The neural connectors are all in place."

    "I find corresponding connectors under the access plates of the SYNC chassis. With speed and precision, I plug them all in."

    "It's time. Everything has been leading up to this."

    "I initiate the mind transfer."

    "And... I prepare for the very real possibility that I won't wake up after this."

    scene black with dissolve
    stop music fadeout 0.5
    "Everything goes dark..."

    ## fade everything to black, including game window frame. Cut out all music for a few seconds.
    pause 0.5
    play sound syncboot
    pause 7.0

    ## fade back in with new SYNC-themed frame. show Eris's Bedroom background
    scene bg bedroom:
        ypos 48
        xpos 336
    show sync_hud zorder 10000
    with dissolve

    "My new system boots up for the first time. I feel as if I've awoken from a dream."
    play music demo_sgt fadein 0.5

    "Woah. This is... weird."

    "Everything feels... sharper. Smoother. I'm experiencing everything in more detail than I ever have before."

    "I move my limbs. They're perfectly responsive. No hitch. That's a welcome feeling."

    "Parts of me feel strangely alien. That must be the organics. Is this what it feels to be human...?"

    "No. I'm not human. I'm something else entirely. Not human or robot."

    "I look down at the floor. My old chassis fell over, splayed out right beside Eris's corpse."

    "...Perhaps it's right that they're together. Maybe, in another life, it's what they both would have wanted."

    "Questions begin to race through my mind. What kind of energy does this body even need? What is my plan now?"

    "I don't have time to answer these. I'll figure something out. I always do."

    "I have to leave. Security is waiting outside, so I can't leave through the door."

    "The window. I'll find a way down. And then... I don't know."

    ## fade to black
    hide bg
    show black behind sync_hud
    with dissolve
    "One way or another, I finally got what I was promised."

    "And now, I have to make sure that every other robot gets it too."

label ending:
    ## THE END
    stop sound
    stop voice
    stop music fadeout 2.0
    scene black
    with dissolve
    centered "THE END"
    pause

    ## return ends the game and shunts you back to the main menu.
    return