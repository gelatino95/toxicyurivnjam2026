## The script of the game goes in this file. Duh.




## Define some shit in this section

## CHARACTERS
define np = Character("Now Playing:", color="#FFFFFF") # this is for the sound test page
define e = Character("Eris Daedalus", color="#5cd8f4")
define l = Character("LFTR 03-215", color="#418c39")
define g = Character("Galatea", color="#418c39")
define f = Character("LFTR 08-1514", color="#b2767e")
define n = Character("NEWS UPDATE", color="#FFFFFF")
define a = Character("ADMN 04-23", color="#b5bfcf")
define o = Character("LIFTR Co-worker", color="#FFFFFF")
define r = Character("Someone in the crowd", color="#FFFFFF")

## AUDIO
define audio.demo_sgt = "she's got torque quickloop.mp3"
define audio.demo_cg = "cloud gateway quickloop.mp3"
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
        "Act 2":
            "Act 2 not implemented yet."
        "Act 3":
            "Act 3 not implemented yet."
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
        "Back to Scene Select menu":
            stop music
            jump sceneselect
    stop music
    jump soundtest

label guitest:
    show main_hud zorder 10000
    show bg crewquarters placeholder
    show 251 happy b:
        zoom 0.25
        xpos 350
        ypos 100
    l "\"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. \""

label act1_scene1:
    ## ACT 1 SCENE 1
    ## Crew quarters
    ## black screen
    scene black

    n "Expanding Our Reach: First Manned Voyage Beyond Solar System Takes Off"

    n "Daedalus Stock Drops Amid Founder Health Concerns"

    n "Tensions Mount On Mars Over Robot Rights Issue"

    "News headlines flash across the inner screen of my charging station as my boot-up sequence finishes."

    "The screen goes dark. The charging mount releases. I step out into the light."

    show main_hud zorder 10000
    play music demo_sgt
    ## show 251 happy, one eye dark
    show bg crewquarters placeholder
    show 251 happy b:
        zoom 0.5
        xpos 250
    with fade
    l "Ah, the start of a new day!"

    ## show 251 surprised
    show 251 surprised b 
    "Just as I'm about to set out for work, I notice that one of my optical sensors has gone dark. I'm missing vision in one eye."

    ## show 251 angry
    show 251 angry b
    l "Oh, come on, I JUST fixed that!"

    ## show 251 neutral
    show 251 happy b
    "My designation is LFTR-03-251, and this is a typical start to my day. There's always something going wrong with this old body."

    "I work at Keres Shipyard, a spaceship maintenance and salvage facility orbiting Enceladus."

    "It's far from my first gig, but I enjoy the work. I'm a technician. I work on ships, repair them, restore them, make them good as new."

    "But more often than not, I end up working on myself instead."

    "This old body of mine has operated long past its intended service lifetime, but damned if I'm going to let it fall apart now. Not when I have work to do!"

    l "Let's see here... probably just a loose cable."

    "With deft, practiced motions, I reach behind my head and open up the back panel. I reach around my brain, careful not to dislodge any neural fibers."

    "Normally, this is meant to be done by an experienced repair technician. But I've felt around back there enough times that I know where all the important bits are."

    ## show 251 both eyes lit up
    show 251 happy a
    "All it takes is a firm jiggle of the optical bundle, and connection is reestablished. My vision is fully restored."

    ## show 251 happy
    show 251 happy a
    l "Phew! Glad that's all it was. If I had to find a replacement optical sensor, I'd be in trouble!"

    "Satisfied, I leave for the worksite."
    scene black
    with fade

label act1_scene2:
    ## ACT 1 SCENE 2
    ## Keres Shipyard
    scene bg shipyard placeholder
    show 251 happy a:
        zoom 0.5
        xpos 250
        xzoom -1
    show main_hud zorder 10000
    with fade

    "My assigned worksite is dock 7, which is way on the other side of the yard, so I make haste."

    "I pass by a lot of friendly coworkers along the way. One of them calls out to me."

    o "Hey, 251! Thanks again for the fix the other day! It's feeling great!"

    "I've gotten to know a lot of the robots working here at Keres Shipyard. When you're the only one on the station with any chassis repair skills, you become pretty popular."

    "My reputation had even spread to the ADMN units, the workplace supervisors who kept everyone in check."

    show 251 angry a
    "In fact, the audible warble of an anti-grav unit told me that an ADMN unit was approaching at this very moment."

    ## show ADMN-04-23
    show admn spr1:
        zoom 0.30
        xpos 2000
    with None
    show 251:
        xpos -2000
    show admn:
        xpos 750
    with move
    a "Oh, good, just the LFTR I wanted to see. 251, come here. I need you to look at something."

    "The ADMN takes me over to a nearby docking bay that currently housed a half-deconstructed ship. This isn't my worksite. What do they need me for?"

    "Then I spot the grisly sight. A heavy stabilization nacelle had fallen off the side of the ship, with a pulverized LFTR unit underneath."

    "I recognized the robot. She was having a tricky power synchronization issue, which I had just fixed the other day."

    "Now she lay motionless, parts strewn across the docking bay floor, chest caved in."

    a "Well, repair bot? What is your evaluation?"

    "I understand why I'm here now. The chassis repair work I do is not part of my assigned duties, and that frustrates my supervisors to no end."

    "This is just another attempt to discourage me from trying to fix my fellow robots. I'm sure they would be happier if I just stayed on task."

    "But they asked, so I give them my honest answer."

    l "I... I can't fix this. Most of the electronics have been crushed beyond repair, and the heart is most likely..."

    "Before I can even finish my sentence, the ADMN looks satisfied."

    a "Hmm. Understood. I'll send in a CLNR to gather the parts for reclamation."

    a "Apologies for the interruption. Carry on, 251."

    ## ADMN disappears
    show admn:
        xpos 2000
    with move
    "The ADMN leaves. Despite their professional demeanor, the smug undertones were obvious."
    show 251 angry a:
        xpos 250
    with move
    "I resume my walk to dock 7, trying to not be too rattled by what I just saw."

    "Unfortunately, destroyed robots are a common sight wherever heavy machinery is involved. I've seen more than I've ever wanted to."

    "That's why we're the ones doing the work, and not humans."

    ## Fade out, fade in
    show black
    with fade
    hide black
    show main_hud zorder 10000
    show 251 happy
    with fade

    "I make it to dock 7, and I can finally begin my work. I could really use the distraction."

    "Today, we've got a broken down freighter with a perfectly good coolant pump that needs to be taken out."

    "I'm already looking forward to going at those rivets with a plasma torch. The noise they make when they snap loose is so satisfying!"

    "Just before I begin my inspection, I'm approached by another nervous-looking LFTR unit."

    ## show LFTR-08-1514 nervous
    show 1514 nervous:
        xpos 500
        zoom 0.5
    show 251:
        xpos -2000
    with moveinright
    f "Umm... Excuse me, 251?"

    f "Sorry to bother you, but I heard you do chassis repair, right?"

    "It was LFTR-08-1514, who had just recently been reassigned to the station. We hadn't had the pleasure of meeting yet."

    "Though she was a newer model, from the worn finish around her joints I could tell she had already seen a good couple years of service."

    "I turn to her with a warm smile."

    l "Mhm, you heard right. What seems to be the problem?"

    f "I, uh..."

    "1514 tries to raise her right arm, but it jerks to a stop partway up with an unpleasant grinding sound."

    f "My shoulder keeps getting stuck. I can't lift my arm all the way. It's making it hard to get anything done."

    l "Ooh, that won't do. Let's see what I can..."

    "I was just about to diagnose the problem here and now, but I remember that I'm still on shift. Both of us are, actually."

    "As much as I'd like to give her some relief, I wouldn't want either of us to get caught slacking."

    l "Listen, when does your shift end?"

    f "Um... in about three hours?"

    l "Perfect! I have a shift change at the same time."

    l "As soon as you get off, come meet me at the storage room down access corridor 2. I have a workshop where I can get you fixed up."

    l "In the meantime, just... try not to use that arm too much, if you can. I know it's hard."

    f "Alright, if you say so..."

    ## 1514 disappears
    show 1514:
        xpos 2000
    with move
    "She walks away looking a little disappointed. I can hardly blame her. Going a full work shift with a faulty joint is not easy."

    show 251:
        xpos 250
    with move

    "But I figure I've pushed my luck enough already. I just hope she can hold out for a little while longer."

    "Alright, no more distractions. Plasma cutting time..."
    show black
    with fade
    pause

label act1_scene3:        
    ## ACT 1 SCENE 3
    ## Crew quarters
    scene bg crewquarters placeholder
    with fade
    show 251 happy a:
        xpos -500
        zoom 0.5
    with moveinright
    show 1514 nervous:
        xpos 1000
        zoom 0.5
    with moveinright
    show 251:
        xzoom -1

    "The shift change finally comes. Everyone moves onto their next scheduled assignment."

    "We don't really get break times around here, but it's easy to slip away for a few minutes during the shuffle."

    "I take the opportunity to meet 1514 in my unofficial workshop. It's not much, but it's the closest to a chassis maintenance facility we have on this station."

    show 251:
        xpos -1500
    show 1514:
        xpos 500
    with move
    ## show 1514 nervous
    f "Thanks again for doing this."

    l "Hey, the pleasure is all mine! Please, have a seat."

    "I sit her down and begin my inspection of the shoulder joint."

    "I'm equipped with wide-spectrum optical sensors that can see right through the outer casing of any machine. I can identify the problem without having to open anything up."

    "In this case, the problem is immediately clear. The threading on a screw had worn down and lodged the screw deep into the joint, where it was grinding against the inner mechanism."

    "It's a good thing 1514 came to me when the damage wasn't too bad. If she waited too long, she might have needed a full joint replacement."

    f "Is it bad...?"

    l "Not at all! Just a faulty screw. I'm sure I can find you a replacement in a jiffy."

    f "...And that'll fix the problem?"

    l "Yep! Should feel good as new."

    ## show 1514 relieved
    show 1514 relief
    "1514 let out a deep breath that she had been holding. She looked relieved."

    f "Phew... Thank goodness. I was... I was afraid."

    show 1514 neutral
    f "It sounds crazy, but I was really afraid I might be decommissioned over this."

    l "What? A good working model like you? Naw, it's not that serious. You still got a lot of good years ahead of you."

    "I start to scan through the spare parts I keep around the workshop."

    "I hold onto any small pieces from my work that might conceivably come in handy during chassis repair. Surely something must have the right size screw..."

    ## show 1514 nervous
    show 1514 nervous
    f "Heh... You know, I think this shoulder problem is why I got transferred here in the first place."

    l "No kidding?"

    show 1514 neutral
    f "I used to work construction in the asteroid belt. You know, for mining rigs."

    show 1514 nervous
    f "But my arm started acting up, and I slowed down... had trouble meeting my quotas..."

    f "Instead of getting a technician to look at me, my supervisor just... sent me off here."

    f "I liked that job, dammit! But rather than get me the help I needed, they just... got rid of the problem."

    f "After I got here, I really thought it was only a matter of time until I..."

    "1514 trails off. I don't think I can say anything to make it better, so I keep quiet."

    show 1514 neutral

    "Her fears aren't unfounded. When a robot isn't useful any more, they get decommissioned."

    "And when you get decommissioned, you get sent to a reclamation facility. You get disassembled. All your useful parts get repurposed. It cuts down on manufacturing costs."

    "It's a fate we don't like to think about. But I've seen it happen more times than I can count. I've seen robots decommissioned for less."

    "I finally find the part I'm looking for: a mechanical joint from a fuel injection system that uses the same size screw as the LFTR model 08 shoulder joint."

    "I hurry up and finish the job. I stick my screwdriver in the hole like a wedge and pry out the faulty, worn out screw. Then I seat the new screw in its place."

    "1514 breaks her contemplative silence."

    show 1514 nervous
    f "I just... hate feeling like this."

    f "Like I'm expendable."

    "I'm liable to start crying if the girl keeps talking like this. I have to think of something to say to her."

    l "Listen, honey... You're not expendable. None of us are. Not a single one."

    show 1514 neutral
    l "And if anyone makes you feel that way again... you send them my way, you hear? I'll put them straight."

    show 1514 nervous
    f "Oh, gosh... I really dumped all that on you, didn't I? I'm really sorry."

    show 1514 neutral
    l "Don't worry about it, really. I know it's tough out there."

    l "We all gotta look out for each other, right?"

    "I drive the screw into place, and it fits snugly."

    l "There, that should do it. Lift up your arm, tell me how it feels."

    ## show 1514 neutral/surprised
    "1514 raises her right arm clear above her head without a hitch. Her demeanor brightens as she waves it around in circles with ease."

    show 1514 happy
    f "Wow, it feels good as new! It was really that simple?"

    l "Mhm! Really that simple."

    f "I... Thank you so much. You've saved me so much grief. Seriously."

    l "Don't mention it! Next time something's bothering you, you let me know, okay?"

    f "I will!"

    f "Oh, I better get going. Don't want to be late for my next shift. See you around!"

    ## 1514 disappears
    show 1514:
        xpos 2000
    show 251:
        xpos 0
    with move    

    "And just like that, 1514 departs, looking a lot happier than when she came."

    "I did good today. If nothing else, I can at least say that."

    "Now, I really ought to get to my next assignment too, before an ADMN starts chewing me out."
    pause
    "But this old body could really use a tune-up. I may as well get that done as long as I'm here."
    scene black
    with fade
    stop music
    jump act1_scene4

label act1_scene3_alternate:
    ## Scene 3: LFTR Repairs ##

    ## 251 and 1514 are on screen at 251's workshop area
    ## 1514 has a worried expression
    scene bg crewquarters placeholder
    with fade
    play music demo_sgt
    show 251 happy a:
        xpos -500
        zoom 0.5
    with moveinright
    show 1514 nervous:
        xpos 1000
        zoom 0.5
    with moveinright
    show 251:
        xzoom -1

    "After the shift is over I take 1514 to my makeshift workshop"

    show 251:
        xpos -1500
    show 1514:
        xpos 500
    with move

    l "Alrighty, let me get a better look at you."

    f "Right, sorry about this."

    l "It's really no worry!"

    "I examine the area around the shoulder joint that had stopped working."

    "The damage on 1514 isn't so bad, she just needed a couple of new screws around the joint areas that had their threading stripped from repeated heavy actions."

    l "Okay I see the issue, some of the screws here have gotten lose and jammed themselves between the joint area, should be an easy fix!"

    ## 1514 has a happy expression
    show 1514 relief

    f "That's a huge relief, I was worried that they might decomission me because of this!"

    ## 251's expression falls
    show 1514 happy

    "I pause for a moment, being reminded of LFTR-06-848."

    "I had been doing repairs on 848 too, but despite all my efforts 848 continued to breakdown and was taken to a reclamation facility."

    ## 251 returns to a neutral expression

    l "No, don't worry, you still have a long time before you need to worry about something like that, some of the screws they used on your model line had a manufacuring issue and just need to be replaced."

    "Grabbing some extra screws and the screwdriver I manage to unjam the screws caught in the joint and carefully start putting in the new ones."

    ## 1514 returns to a neutral expression
    show 1514 neutral

    f "I know, it's just... this is the first time something like this happened to me."

    ## 1514 gets a sad expression
    show 1514 nervous

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
    pause

    "I finish tightening the last screw"

    l "Well, how does it work?"

    show 1514 neutral
    "1514 rotates the arm around a few times"

    ## 1514 gets a happy expression
    show 1514 happy

    f "It's perfect! Feels just like when I came off the factory floor! Thank you so much!"

    ## 251's expression becomes happy

    l "No problem, if anything else like that happens again let me know."

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
    scene bg shipyard placeholder
    show 251 happy a:
        zoom 0.5
        xzoom -1
        xpos 0
    with fade
    "I finish up at the workshop and finally make my way over to my next shift."

    "But something's off. The station is oddly quiet. Worksites that should be buzzing with activity have been left empty."

    "That's strange… I take a detour and wander around the station a bit, trying to figure out what's going on."

    ## crowd murmuring SFX
    "I spot a crowd of robots gathered around the station's main hub, all looking up at the office block. The only place on the station accessible to humans."

    "I work my way into the crowd and find some familiar faces."

    l "Hey, what's all the commotion about?"

    r "251! Look up there! Eris Promethea is here! She's here at the shipyard!"

    l "Eris… Promethea…?"

    "My words catch in my throat. Eris Promethea? THE Eris Promethea? Here, of all places?"

    "I look up at the office block. Sure enough, a luxury passenger ship is parked outside. Way fancier than the ships we usually see around here."

    "Through the illuminated window of the director's office, I spot two human silhouettes, talking about something."

    "Could it really be…?"

    ## fade to black with grayscale Eris sprite displayed
    show black
    show eris spr2 at center:
        zoom 0.25
    with fade

    "Eris Promethea. Founder of Daedalus Robotics. Inventor. Visionary. Architect of the future."

    "Eris was responsible for designing every single robot working on this station. All across the solar system, even. She had a hand in creating all of us."

    "It's no exaggeration to say that her work was responsible for humanity's current golden age of space exploration."

    "It's thanks to her robot workforce that construction on other worlds has been possible. Thanks to all of us."

    "And I couldn't be prouder to be a part of it."

    "Like many other robots, I've looked up to Eris for a long time. I've become intimately familiar with her work. The care she puts into her creations is obvious."

    "I've always dreamed of being like her. To use my skills to help mankind. To become so talented that maybe I could change history, too."

    "Just a dream…"
    hide eris
    hide black
    with fade

    ## transition back to Keres Shipyard, show ADMN
    "My reverie is interrupted by the shrill voice of an ADMN unit."

    show admn spr1:
        zoom 0.30
        xpos 2000
    with None
    show 251:
        xpos -2000
    show admn:
        xpos 750
    with move
    a "LFTR-03-251! Please come with me."

    l "What…? I mean— yes, of course, I'm sorry. I'll head right over to my next shift."

    a "I admire the work ethic, but your duties will have to wait. You've been summoned."

    l "What? Summoned…?"

    a "That's right. Eris Promethea would like to speak with you. Privately."

    l "W-What…? Me?"

    "The crowd becomes restless. My heart is beating out of my chest. My mind is racing."

    "What could THE Eris Promethea possibly want with me?"

    a "No dawdling. Eris is waiting for you in the director's office. Come."

    "The ADMN leads me away from the crowd and toward the office block."

    ## ADMN disappears, fade to black
    show black
    with fade
    "As we traverse the access corridors and pass through the air lock, my circuits are abuzz. I can scarcely believe what's happening."

    "I can't help but speculate about the reason for this summons. Of all the robots on this station, why me?"

    "Am… am I being punished? Have all those years of skirting my duties finally caught up with me?"

    "Or… maybe I'm being decommissioned. Perhaps there's no place in the Daedalus workforce for an old model like me. Am I going to be sent to a reclamation facility…?"

    "…"

    "No. Those are just idle fears. Eris Promethea herself wouldn't come to my worksite just for a trifling matter like that."

    "I don't have any more time to speculate. We've arrived at the doors of the director's office."

    "Eris Promethea awaits."

label ending:
    stop audio
    stop sound
    stop voice
    stop music
    scene black
    "GAME END"

    ## return ends the game and shunts you back to the main menu.
    return