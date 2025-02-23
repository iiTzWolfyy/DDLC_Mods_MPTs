init python:

    #base folder of the MPT. If you need to change the path for
    #whatever reason, just change the one below!
    base_path  = "mod_assets/MPT/FeMC_MPT/"

    outfits_path = base_path + "outfits/"
    expressions_path = base_path + "expressions/"


#Images for blinking
image femc_blink:
    alpha 0.0
    renpy.random.randint(20, 100)*0.1
    choice:
        alpha 1.0
        expressions_path + "eyes/e2b.png"
        0.015
        expressions_path + "eyes/e2a.png"
        0.035
        expressions_path + "eyes/e2b.png"
        0.015
    choice:
        alpha 1.0
        expressions_path + "eyes/e2b.png"
        0.015
        expressions_path + "eyes/e2a.png"
        0.065
        expressions_path + "eyes/e2b.png"
        0.015
    choice:
        alpha 1.0
        expressions_path + "eyes/e2b.png"
        0.015
        expressions_path + "eyes/e2a.png"
        0.095
        expressions_path + "eyes/e2b.png"
        0.015
    choice:
        alpha 1.0
        expressions_path + "eyes/e2b.png"
        0.015
        expressions_path + "eyes/e2a.png"
        0.035
        expressions_path + "eyes/e2b.png"
        0.015
        alpha 0.0
        0.15
        alpha 1.0
        expressions_path + "eyes/e2b.png"
        0.015
        expressions_path + "eyes/e2a.png"
        0.035
        expressions_path + "eyes/e2b.png"
        0.015
    repeat

layeredimage femc turned: #not crossed pose (use 'femc cross' for her to cross her arms) see line 288

    #better rendering
    at renpy.partial(Flatten, drawable_resolution=False)

    #Facebases.
    #This one is for the uniforms
    always base_path + "facebase.png" if_not(["casual", "summer"])
    #This one is for the summer dress
    always base_path + "facebase_2.png" if_all(["summer"]) if_not(["casual", "uniform_blue", "uniform_red"])
    #This one is for the casual outfit
    always base_path + "facebase_3.png" if_all(["casual"]) if_not(["summer", "uniform_blue", "uniform_red"])

    group outfit:
        #uniform with blue node
        attribute uniform_blue default null
        #uniform with red node
        attribute uniform_red null
        #casual
        attribute casual null
        #summer outfit
        attribute summer null

    #All the default moods
    group mood: 
        attribute neut default null #neutral
        attribute angr null #angry
        attribute cry null  #crying
        attribute curi null #curious
        attribute dist null #distant
        attribute doub null #doubtful
        attribute flus null #flustered
        attribute happ null #happy
        attribute laug null #laughing
        attribute nerv null #nervous
        attribute pout null #pouting
        attribute sad null  #sad
        attribute surp null #surprised
        attribute worr null #worried

    #blushes
    group blush:
        #default blush
        attribute nobl default null
        #awkward blush
        attribute awkw null

    #Left part of the body
    group left:
        #blue uniform
        attribute ldown default if_any(["uniform_blue"]):
            outfits_path + "no_vest_blue/ldown.png"
        attribute lup if_any(["uniform_blue"]):
            outfits_path + "no_vest_blue/lup.png"
        
        #red uniform
        attribute ldown default if_any(["uniform_red"]):
            outfits_path + "no_vest_red/ldown.png"
        attribute lup if_any(["uniform_red"]):
            outfits_path + "no_vest_red/lup.png"

        #casual
        attribute ldown default if_any(["casual"]):
            outfits_path + "casual/ldown.png"
        attribute lup if_any(["casual"]):
            outfits_path + "casual/lup.png"
        
        #summer
        attribute ldown default if_any(["summer"]):
            outfits_path + "summer/ldown.png"
        attribute lup if_any(["summer"]):
            outfits_path + "summer/lup.png"

    #right part of the body
    group right:
        #blue uniform
        attribute rhip default if_any(["uniform_blue"]):
            outfits_path + "no_vest_blue/rhip.png"
        attribute rup if_any(["uniform_blue"]):
            outfits_path + "no_vest_blue/rup.png"
        
        #red uniform
        attribute rhip default if_any(["uniform_red"]):
            outfits_path + "no_vest_red/rhip.png"
        attribute rup if_any(["uniform_red"]):
            outfits_path + "no_vest_red/rup.png"

        #casual
        attribute rhip default if_any(["casual"]):
            outfits_path + "casual/rhip.png"
        
        #summer
        attribute rhip default if_any(["summer"]):
            outfits_path + "summer/rhip.png"
        attribute rup if_any(["summer"]):
            outfits_path + "summer/rup.png"

    #Blush
    group nose:
        attribute nose default if_any(["nobl"]):
            expressions_path + "nose/nobl.png"
        attribute nose default if_any(["awkw"]):
            expressions_path + "nose/awkw.png"
        
        #Truncated tags (for customization)
        attribute n1:
            expressions_path + "nose/nobl.png"
        attribute n2:
            expressions_path + "nose/awkw.png"
    
    #Mouths
    group mouth:
        #Closed mouths default
        attribute cm default if_any(["happ"]):  #smiling
            expressions_path + "mouths/m1a.png"
        attribute cm default if_any(["dist", "doub", "neut", "pout", "sad"]):  #neutral, not smiling
            expressions_path + "mouths/m1b.png"
        attribute cm default if_any(["angr"]):  #gritted teeth
            expressions_path + "mouths/m1c.png"
        attribute cm default if_any(["curi", "surp"]):  #slightly surprised
            expressions_path + "mouths/m1d.png"
        attribute cm default if_any(["laug", "nerv"]):  #Almost laughing
            expressions_path + "mouths/m1e.png"
        attribute cm default if_any(["cry", "flus", "worr"]):  #slightly opened
            expressions_path + "mouths/m3a.png"

        #Opened mouths
        attribute om if_any(["curi", "flus", "happ", "laug"]):  #Wide open, smiling
            expressions_path + "mouths/m2a.png"
        attribute om if_any(["dist", "doub", "neut", "pout", "sad"]):
            expressions_path + "mouths/m2b.png" #Slightly opened, without teeth
        attribute om if_any(["cry", "nerv"]):
            expressions_path + "mouths/m2c.png" #Crying/Flustered mouth
        attribute om if_any(["angr", "surp", "worr"]):
            expressions_path + "mouths/m3a.png" #surprised

        #Truncated tags
        #Closed mouths
        attribute m1a:
            expressions_path + "mouths/m1a.png"
        attribute m1b:
            expressions_path + "mouths/m1b.png"
        attribute m1c:
            expressions_path + "mouths/m1c.png"
        attribute m1d:
            expressions_path + "mouths/m1d.png"
        attribute m1e:
            expressions_path + "mouths/m1e.png"

        #Opened mouths
        attribute m2a:
            expressions_path + "mouths/m2a.png"
        attribute m2b:
            expressions_path + "mouths/m2b.png"
        attribute m2c:
            expressions_path + "mouths/m2c.png"

        #Can be both
        attribute m3a:
            expressions_path + "mouths/m3a.png"
    
    #Eyes
    group eyes:
        #Opened eyes
        attribute oe default if_any(["neut", "angr", "curi", "doub", 
                                    "happ", "laug", "sad", "surp"]):  #Normal eyes
            expressions_path + "eyes/e1a.png"
        attribute oe default if_any(["dist", "flus", "nerv", "pout", "worr"]):  #Looking away
            expressions_path + "eyes/e1b.png"
        attribute oe default if_any(["cry"]):   #Crying
            expressions_path + "eyes/e1c.png"
        
        #Closed eyes
        attribute ce if_any(["neut", "angr", "dist", "doub", "pout", "sad", "worr"]):  #Supposedly sad closed eyes
            expressions_path + "eyes/e2a.png"
        attribute ce if_any(["curi", "flus", "happ", "laug", "nerv", "surp"]):  #Supposedly happy closed eyes
            expressions_path + "eyes/e2b.png"
        attribute ce if_any(["cry"]):   #Crying closed eyes
            expressions_path + "eyes/e2c.png"

        #Truncated tags (for customization)
        #Opened eyes
        attribute e1a:
            expressions_path + "eyes/e1a.png" #normal
        attribute e1b:
            expressions_path + "eyes/e1b.png" #looking away
        attribute e1c:
            expressions_path + "eyes/e1c.png" #cry

        #Closed eyes
        attribute e2a:
            expressions_path + "eyes/e2a.png" #sad
        attribute e2b:
            expressions_path + "eyes/e2b.png" #happy
        attribute e2c:
            expressions_path + "eyes/e2c.png" #Cry
    
    #Blinking group. You can disable the blinking using the 'no_blink' attribute in your 'show' statement.
    group blink:

        anchor (0,0) subpixel (True)

        attribute blink_a default if_not(["ce","e2a","e2b","e2c"]):
            "femc_blink"
        attribute no_blink null
        
    #Eyebrows
    group eyebrows:
        attribute brow default if_any(["curi", "doub"]): #One eyebrow raised
            expressions_path + "eyebrows/ba.png"
        attribute brow default if_any(["angr", "pout"]): #frowned eyebrows
            expressions_path + "eyebrows/bb.png"
        attribute brow default if_any(["cry", "sad", "worr"]): #rather sad eyebrows
            expressions_path + "eyebrows/bc.png"
        attribute brow default if_any(["laug", "flus", "happ", "nerv", "surp"]): #Surprised eyebrows
            expressions_path + "eyebrows/bd.png"
        attribute brow default if_any(["dist", "neut"]): #'normal' eyebrows
            expressions_path + "eyebrows/be.png"

        #Truncated tags (for customization)
        attribute ba:
            expressions_path + "eyebrows/ba.png" #One eyebrow raised
        attribute bb:
            expressions_path + "eyebrows/bb.png" #frowned eyebrows
        attribute bc:
            expressions_path + "eyebrows/bc.png" #rather sad eyebrows
        attribute bd:
            expressions_path + "eyebrows/bd.png" #Surprised eyebrows
        attribute be:
            expressions_path + "eyebrows/be.png" #'normal' eyebrows
        

layeredimage femc cross:

    #better rendering
    at renpy.partial(Flatten, drawable_resolution=False)

    #Facebases. One will be for the 'summer' outfit, the other is for
    #all the other outfits.
    always base_path + "facebase.png" if_not(["casual", "summer"])
    always base_path + "facebase_2.png" if_all(["summer"]) if_not(["casual", "uniform_blue", "uniform_red"])
    always base_path + "facebase_3.png" if_all(["casual"]) if_not(["summer", "uniform_blue", "uniform_red"])

    group outfit:
        #uniform with blue node
        attribute uniform_blue default null
        #uniform with red node
        attribute uniform_red null
        #casual
        attribute casual null
        #summer outfit
        attribute summer null

    #All the default moods
    group mood: 
        attribute neut default null #neutral
        attribute angr null #angry
        attribute cry null  #crying
        attribute curi null #curious
        attribute dist null #distant
        attribute doub null #doubtful
        attribute flus null #flustered
        attribute happ null #happy
        attribute laug null #laughing
        attribute nerv null #nervous
        attribute pout null #pouting
        attribute sad null  #sad
        attribute surp null #surprised
        attribute worr null #worried

    #blushes
    group blush:
        #default blush
        attribute nobl default null
        #awkward blush
        attribute awkw null

    #Crossed body
    group center:
        attribute center default if_any(["uniform_blue"]):
            outfits_path + "no_vest_blue/crossed.png"
        attribute center default if_any(["uniform_red"]):
            outfits_path + "no_vest_red/crossed.png"
        attribute center default if_any(["casual"]):
            outfits_path + "casual/crossed.png"
        attribute center default if_any(["summer"]):
            outfits_path + "summer/crossed.png"
        
    #Blush
    group nose:
        attribute nose default if_any(["nobl"]):
            expressions_path + "nose/nobl.png"
        attribute nose default if_any(["awkw"]):
            expressions_path + "nose/awkw.png"
        
        #Truncated tags (for customization)
        attribute n1:
            expressions_path + "nose/nobl.png"
        attribute n2:
            expressions_path + "nose/awkw.png"
    
    #Mouths
    group mouth:
        #Closed mouths default
        attribute cm default if_any(["happ"]):  #smiling
            expressions_path + "mouths/m1a.png"
        attribute cm default if_any(["dist", "doub", "neut", "pout", "sad"]):  #neutral, not smiling
            expressions_path + "mouths/m1b.png"
        attribute cm default if_any(["angr"]):  #gritted teeth
            expressions_path + "mouths/m1c.png"
        attribute cm default if_any(["curi", "surp"]):  #slightly surprised
            expressions_path + "mouths/m1d.png"
        attribute cm default if_any(["laug", "nerv"]):  #Almost laughing
            expressions_path + "mouths/m1e.png"
        attribute cm default if_any(["cry", "flus", "worr"]):  #slightly opened
            expressions_path + "mouths/m3a.png"

        #Opened mouths
        attribute om if_any(["curi", "flus", "happ", "laug"]):  #Wide open, smiling
            expressions_path + "mouths/m2a.png"
        attribute om if_any(["dist", "doub", "neut", "pout", "sad"]):
            expressions_path + "mouths/m2b.png" #Slightly opened, without teeth
        attribute om if_any(["cry", "nerv"]):
            expressions_path + "mouths/m2c.png" #Crying/Flustered mouth
        attribute om if_any(["angr", "surp", "worr"]):
            expressions_path + "mouths/m3a.png" #surprised

        #Truncated tags
        #Closed mouths
        attribute m1a:
            expressions_path + "mouths/m1a.png"
        attribute m1b:
            expressions_path + "mouths/m1b.png"
        attribute m1c:
            expressions_path + "mouths/m1c.png"
        attribute m1d:
            expressions_path + "mouths/m1d.png"
        attribute m1e:
            expressions_path + "mouths/m1e.png"

        #Opened mouths
        attribute m2a:
            expressions_path + "mouths/m2a.png"
        attribute m2b:
            expressions_path + "mouths/m2b.png"
        attribute m2c:
            expressions_path + "mouths/m2c.png"

        #Can be both
        attribute m3a:
            expressions_path + "mouths/m3a.png"
    
    #Eyes
    group eyes:
        #Opened eyes
        attribute oe default if_any(["neut", "angr", "curi", "doub",
                                    "happ", "laug", "sad", "surp"]):  #Normal eyes
            expressions_path + "eyes/e1a.png"
        attribute oe default if_any(["dist", "flus", "nerv", "pout", "worr"]):  #Looking away
            expressions_path + "eyes/e1b.png"
        attribute oe default if_any(["cry"]):   #Crying
            expressions_path + "eyes/e1c.png"
        
        #Closed eyes
        attribute ce if_any(["neut", "angr", "dist", "doub", "pout", "sad", "worr"]):  #Supposedly sad closed eyes
            expressions_path + "eyes/e2a.png"
        attribute ce if_any(["curi", "flus", "happ", "laug", "nerv", "surp"]):  #Supposedly happy closed eyes
            expressions_path + "eyes/e2b.png"
        attribute ce if_any(["cry"]):   #Crying closed eyes
            expressions_path + "eyes/e2c.png"

        #Truncated tags (for customization)
        #Opened eyes
        attribute e1a:
            expressions_path + "eyes/e1a.png" #normal
        attribute e1b:
            expressions_path + "eyes/e1b.png" #looking away
        attribute e1c:
            expressions_path + "eyes/e1c.png" #cry

        #Closed eyes
        attribute e2a:
            expressions_path + "eyes/e2a.png" #sad
        attribute e2b:
            expressions_path + "eyes/e2b.png" #happy
        attribute e2c:
            expressions_path + "eyes/e2c.png" #Cry
        
    #Eyebrows
    group eyebrows:
        attribute brow default if_any(["curi", "doub"]): #One eyebrow raised
            expressions_path + "eyebrows/ba.png"
        attribute brow default if_any(["angr", "pout"]): #frowned eyebrows
            expressions_path + "eyebrows/bb.png"
        attribute brow default if_any(["cry", "sad", "worr"]): #rather sad eyebrows
            expressions_path + "eyebrows/bc.png"
        attribute brow default if_any(["laug", "flus", "happ", "nerv", "surp"]): #Surprised eyebrows
            expressions_path + "eyebrows/bd.png"
        attribute brow default if_any(["dist", "neut"]): #'normal' eyebrows
            expressions_path + "eyebrows/be.png"

        #Truncated tags (for customization)
        attribute ba:
            expressions_path + "eyebrows/ba.png" #One eyebrow raised
        attribute bb:
            expressions_path + "eyebrows/bb.png" #frowned eyebrows
        attribute bc:
            expressions_path + "eyebrows/bc.png" #rather sad eyebrows
        attribute bd:
            expressions_path + "eyebrows/bd.png" #Surprised eyebrows
        attribute be:
            expressions_path + "eyebrows/be.png" #'normal' eyebrows
    
    #Blinking group. You can disable the blinking using the 'no_blink' attribute in your 'show' statement.
    group blink:

        anchor (0,0) subpixel (True)

        attribute blink_a default if_not(["ce","e2a","e2b","e2c"]):
            "femc_blink"
        attribute no_blink null