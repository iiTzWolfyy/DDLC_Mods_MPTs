init -5 python:

    #The ONLY variable you need to change accordingly to the folder path you wanna use.
    #Don't edit the name of the Natsuri_MPT folder!
    #USE EXPOSER PREVIEWER TO MAKE YOUR EXPRESSIONS EASILY!
    path = "mod_assets/MPT/Natsuri_MPT/"
    
    outfits = path + "outfits/"
    expressions = path + "expressions/"

    #outfits paths
    outfit_green_shirt = outfits + "green_shirt/"
    outfit_uniform = outfits + "uniform/"
    outfit_sweater = outfits + "sweater/"
    outfit_white_shirt = outfits + "white_shirt/"

    #expressions paths
    eyebrows = expressions + "eyebrows/"
    eyes = expressions + "eyes/"
    mouths = expressions + "mouths/"
    nose = expressions + "nose/"
    shy_eyebrows = expressions + "shy_eyebrows/"
    shy_eyes = expressions + "shy_eyes/"
    shy_mouths = expressions + "shy_mouths/"
    shy_nose = expressions + "shy_nose/"

#Natsuri's turned blinking image
image blink_turned:
    alpha 0.0
    renpy.random.randint(2, 5)
    choice:
        alpha 1.0
        eyes + "blink_a.png"
        0.015
        eyes + "blink_b.png"
        0.035
        eyes + "blink_a.png"
        0.015
    choice:
        alpha 1.0
        eyes + "blink_a.png"
        0.015
        eyes + "blink_b.png"
        0.065
        eyes + "blink_a.png"
        0.015
    choice:
        alpha 1.0
        eyes + "blink_a.png"
        0.015
        eyes + "blink_b.png"
        0.095
        eyes + "blink_a.png"
        0.015
    choice:
        alpha 1.0
        eyes + "blink_a.png"
        0.015
        eyes + "blink_b.png"
        0.035
        eyes + "blink_a.png"
        0.015
        alpha 0.0
        0.15
        alpha 1.0
        eyes + "blink_a.png"
        0.015
        eyes + "blink_b.png"
        0.035
        eyes + "blink_a.png"
        0.015
    repeat

#Natsuri's shy blinking image
image blink_shy:
    alpha 0.0
    renpy.random.randint(2, 5)
    choice:
        alpha 1.0
        shy_eyes + "blink_a.png"
        0.015
        shy_eyes + "blink_b.png"
        0.035
        shy_eyes + "blink_a.png"
        0.015
    choice:
        alpha 1.0
        shy_eyes + "blink_a.png"
        0.015
        shy_eyes + "blink_b.png"
        0.065
        shy_eyes + "blink_a.png"
        0.015
    choice:
        alpha 1.0
        shy_eyes + "blink_a.png"
        0.015
        shy_eyes + "blink_b.png"
        0.095
        shy_eyes + "blink_a.png"
        0.015
    choice:
        alpha 1.0
        shy_eyes + "blink_a.png"
        0.015
        shy_eyes + "blink_b.png"
        0.035
        shy_eyes + "blink_a.png"
        0.015
        alpha 0.0
        0.15
        alpha 1.0
        shy_eyes + "blink_a.png"
        0.015
        shy_eyes + "blink_b.png"
        0.035
        shy_eyes + "blink_a.png"
        0.015
    repeat

#Normal facing of Natsuri
layeredimage natsuri turned:

    #better rendering and fixes vertical/horizontal lines issues
    at renpy.partial(Flatten, drawable_resolution=False)

    always expressions + "facebase.png"

    #Outfits. In order: uniform, white shirt (casual), green shirt and a light pink sweater
    group outfit:
        attribute uniform default null
        attribute casual null
        attribute green_shirt null
        attribute sweater null

    group mood: 
        attribute neut default null #neutral
        attribute angr null #angry
        attribute anno null #annoyed
        attribute cry null  #crying
        attribute curi null #curious
        attribute dist null #distant
        attribute doub null #doubtful
        attribute flus null #flustered
        attribute happ null #happy
        attribute laug null #laughing
        attribute lsur null #surprised (lightly)
        attribute nerv null #nervous
        attribute pani null #panicked
        attribute sad null  #sad
        attribute shoc null #shocked
        attribute vang null #VERY angry
        attribute vsur null #surprised (very)
        attribute worr null #worried
        attribute yand null #yandere

    group blush: 
        attribute nobl default null #No blush.
        attribute awkw null #awkward.
        attribute blus null #blushing.  
        attribute blaw null #blushing AND awkward. 

    #Left part of the body
    group left:
        #left arm down (2 variants for the sweater, one is ldown, other is lbehind)
        attribute ldown default if_any(["uniform"]):
            outfit_uniform + "1l.png"
        attribute ldown default if_any(["casual"]):
            outfit_white_shirt + "1l.png"
        attribute ldown default if_any(["green_shirt"]):
            outfit_green_shirt + "1l.png"
        attribute ldown default if_any(["sweater"]):
            outfit_sweater + "1la.png"

        attribute lbehind if_any(["sweater"]):
            outfit_sweater + "1lb.png"

        #left arm up
        attribute lup if_any(["uniform"]):
            outfit_uniform + "2l.png"
        attribute lup if_any(["casual"]):
            outfit_white_shirt + "2l.png"
        attribute lup if_any(["green_shirt"]):
            outfit_green_shirt + "2l.png"
        attribute lup if_any(["sweater"]):
            outfit_sweater + "2l.png"


    #Right part of the body
    group right:
        #right arm down
        attribute rdown default if_any(["uniform"]):
            outfit_uniform + "1r.png"
        attribute rdown default if_any(["casual"]):
            outfit_white_shirt + "1r.png"
        attribute rdown default if_any(["green_shirt"]):
            outfit_green_shirt + "1r.png"
        attribute rdown default if_any(["sweater"]):
            outfit_sweater + "1r.png"

        #left arm on hip
        attribute rhip if_any(["uniform"]):
            outfit_uniform + "2r.png"
        attribute rhip if_any(["casual"]):
            outfit_white_shirt + "2r.png"
        attribute rhip if_any(["green_shirt"]):
            outfit_green_shirt + "2r.png"
        attribute rhip if_any(["sweater"]):
            outfit_sweater + "2r.png"

    #Blush group
    group nose:
        attribute nose default if_any(["nobl"]) null #No blush
        attribute nose default if_any(["awkw", "nerv"]):     #Awkward
            nose + "awkw.png"
        attribute nose default if_any(["blus"]):     #Blushing
            nose + "blus.png"
        attribute nose default if_any(["blaw", "flus"]):     #Blushing and awkward
            nose + "blaw.png"

        #Truncated tags for customization
        attribute n1 null
        attribute n2:
            nose + "awkw.png"
        attribute n3:
            nose + "blus.png"
        attribute n4:
            nose + "blaw.png"

    #Eyes
    group eyes:
        #Open eyes
        attribute oe default if_any(["neut", "angr", "anno", "curi", "doub", "happ", #normal
                                    "laug", "lsur", "nerv", "sad", "worr"]):
            eyes + "e1a.png"
        attribute oe default if_any(["pani", "shoc", "vang", "vsur"]):               #wide-eyed
            eyes + "e1b.png"
        attribute oe default if_any(["dist", "flus"]):                               #looking away
            eyes + "e1c.png"
        attribute oe default if_any(["cry"]):                                        #crying
            eyes + "e1d.png"
        attribute oe default if_any(["yand"]):                                       #yandere
            eyes + "yand.png"

        #Closed eyes
        attribute ce if_any(["happ", "laug", "lsur", "nerv", "yand"]):  #happy closed eyes
            eyes + "e2a.png"
        attribute ce if_any(["neut", "angr", "curi", "dist", 
                            "doub", "sad", "vang", "worr"]):            #sad closed eyes
            eyes + "e2b.png"
        attribute ce if_any(["cry"]):                                   #crying closed eyes
            eyes + "e2c.png"
        attribute ce if_any(["anno", "flus", "pani", "shoc", "vsur"]):  # >.< eyes
            eyes + "e2d.png"
        
        #Truncated tags (use for more custom expressions)
        #Open eyes
        attribute e1a:
            eyes + "e1a.png"    #normal
        attribute e1b:
            eyes + "e1b.png"    #wide-eyed
        attribute e1c:
            eyes + "e1c.png"    #looking away
        attribute e1d:
            eyes + "e1d.png"    #crying
        attribute e1e:
            eyes + "yand.png"   #yandere eyes

        #Closed eyes
        attribute e2a:
            eyes + "e2a.png"    #Happy closed
        attribute e2b:
            eyes + "e2b.png"    #Sad closed
        attribute e2c:
            eyes + "e2c.png"    #Crying 
        attribute e2d:
            eyes + "e2d.png"    # >.< eyes

    #Blinking group. Disabled by default, but you can just put the 'default'
    #keyword on the attribute 'blink' to enable it by default. Doesn't work
    #on closed eyes and yandere eyes (you can just remove the 'e1e' below
    #to enable it on yandere eyes).
    group blink:
        attribute no_blink default null
        attribute blink if_not(["ce", "e1e", "e2a", "e2b", "e2c", "e2d"]):
            "blink_turned"

    #Mouths
    group mouth:
        #Closed mouths
        attribute cm default if_any(["flus", "happ", "laug"]):                      #Smiling
            mouths + "m1a.png"
        attribute cm default if_any(["neut", "angr", "cry", "dist", "doub", "lsur", "sad"]):#Not smiling
            mouths + "m1b.png"
        attribute cm default if_any(["vang"]):                              #gritting teeth
            mouths + "m1c.png"
        attribute cm default if_any(["anno", "curi", "worr"]):                      #slightly opened, like :o
            mouths + "m1d.png"
        attribute cm default if_any(["yand"]):                                      #gritting teeth + smile
            mouths + "m1e.png"
        attribute cm default if_any(["shoc", "vsur"]):                              # ~ mouth
            mouths + "m3a.png"
        attribute cm default if_any(["nerv", "pani"]):                              # ~ mouth, more opened than the latter
            mouths + "m3b.png"

        #Opened mouths
        attribute om if_any(["neut", "anno", "lsur", "worr"]): #Neutral
            mouths + "m2a.png"
        attribute om if_any(["flus", "laug"]):                 #Wide smile
            mouths + "m2b.png"
        attribute om if_any(["angr", "doub", "nerv"]):         #Opened as if she was blaming someone
            mouths + "m2c.png"
        attribute om if_any(["cry", "shoc", "vang", "vsur"]):  #Can be used for angry/sad expressions
            mouths + "m2d.png"
        attribute om if_any(["happ"]):                         #Pretty much a light smile
            mouths + "m2e.png"
        attribute om if_any(["curi", "dist", "sad"]):          #Slightly opened
            mouths + "m2f.png"
        attribute om if_any(["yand"]):                         #Yandered smile
            mouths + "m2g.png"
        attribute om if_any(["pani"]):                         # ~ opened mouth
            mouths + "m3a.png"

        #Truncated tags (use for more custom expressions)
        #Closed mouths
        attribute m1a:
            mouths + "m1a.png"
        attribute m1b:
            mouths + "m1b.png"
        attribute m1c:
            mouths + "m1c.png"
        attribute m1d:
            mouths + "m1d.png"
        attribute m1e:
            mouths + "m1e.png"

        #Opened mouths
        attribute m2a:
            mouths + "m2a.png"
        attribute m2b:
            mouths + "m2b.png"
        attribute m2c:
            mouths + "m2c.png"
        attribute m2d:
            mouths + "m2d.png"
        attribute m2e:
            mouths + "m2e.png"
        attribute m2f:
            mouths + "m2f.png"
        attribute m2g:
            mouths + "m2g.png"

        #Could be used for both closed/opened mouths
        attribute m3a:
            mouths + "m3a.png"
        attribute m3b:
            mouths + "m3b.png"

    #Eyebrows
    group eyebrows:
        #The bc and bh eyebrows can only be used on closed eyes
        attribute brow default if_any(["neut", "happ"]):
            eyebrows + "ba.png"
        attribute brow default if_any(["angr", "vang"]) if_not(["ce", "e2a", "e2b", "e2c", "e2d"]):
            eyebrows + "bb.png"
        attribute brow default if_any(["angr", "vang"]) if_not(["e1a", "e1b", "e1c", "e1d", "e1e", "oe"]):
            eyebrows + "bc.png"
        attribute brow default if_any(["curi", "laug", "pani", "shoc", "vsur", "yand", "lsur"]):
            eyebrows + "bd.png"
        attribute brow default if_any(["cry", "flus", "nerv", "sad", "worr"]) if_not(["ce", "e2a", "e2b", "e2c", "e2d"]):
            eyebrows + "be.png"
        attribute brow default if_any(["anno", "vang"]):
            eyebrows + "bf.png"
        attribute brow default if_any(["dist", "doub"]):
            eyebrows + "bg.png"
        attribute brow default if_any(["cry", "flus", "nerv", "sad", "worr"]) if_not(["e1a", "e1b", "e1c", "e1d", "e1e", "oe"]):
            eyebrows + "bh.png"

        #Truncated tags (use for more customization)
        #Some eyebrows you'll use will be replaced by one
        #that looks like the one you wanted, but will be
        #adapted to fit depending if it's opened/closed eyes
        attribute ba:
            eyebrows + "ba.png"
        attribute bb if_not(["ce", "e2a", "e2b", "e2c", "e2d"]):
            eyebrows + "bb.png"
        attribute bb if_any(["ce", "e2a", "e2b", "e2c", "e2d"]):
            eyebrows + "bc.png"
        attribute bc if_not(["e1a", "e1b", "e1c", "e1d", "e1e", "oe"]):
            eyebrows + "bc.png"
        attribute bc if_any(["e1a", "e1b", "e1c", "e1d", "e1e", "oe"]):
            eyebrows + "bb.png"
        attribute bd:
            eyebrows + "bd.png"
        attribute be if_not(["ce", "e2a", "e2b", "e2c", "e2d"]):
            eyebrows + "be.png"
        attribute be if_any(["ce", "e2a", "e2b", "e2c", "e2d"]):
            eyebrows + "bh.png"
        attribute bf:
            eyebrows + "bf.png"
        attribute bg:
            eyebrows + "bg.png"
        attribute bh if_not(["e1a", "e1b", "e1c", "e1d", "e1e", "oe"]):
            eyebrows + "bh.png"
        attribute bh if_any(["e1a", "e1b", "e1c", "e1d", "e1e", "oe"]):
            eyebrows + "be.png"

    #This group exists so that you can add separated tears to the sprite,
    #using the 'tears' attribute (doesn't work on the e2d and yand eyes). Default isn't used.
    #To remove them, use the '-tears' or 'no_tears' attribute.
    group tears:
        attribute no_tears default null
        attribute tears if_not(["e2d", "e1e", "yand"]):
            expressions + "tears.png"

#Layeredimage for her crossed pose, not looking away.
layeredimage natsuri cross:

    at renpy.partial(Flatten, drawable_resolution=False)

    always expressions + "facebase.png"

    #Outfits. In order: uniform, white shirt (casual), green shirt and a light pink sweater
    group outfit:
        attribute uniform default null
        attribute casual null
        attribute green_shirt null
        attribute sweater null

    group mood: 
        attribute neut default null #neutral
        attribute angr null #angry
        attribute anno null #annoyed
        attribute cry null  #crying
        attribute curi null #curious
        attribute dist null #distant
        attribute doub null #doubtful
        attribute flus null #flustered
        attribute happ null #happy
        attribute laug null #laughing
        attribute lsur null #surprised (lightly)
        attribute nerv null #nervous
        attribute pani null #panicked
        attribute sad null  #sad
        attribute shoc null #shocked
        attribute vang null #VERY angry
        attribute vsur null #surprised (very)
        attribute worr null #worried
        attribute yand null #yandere

    group blush: 
        attribute nobl default null #No blush.
        attribute awkw null #awkward.
        attribute blus null #blushing.  
        attribute blaw null #blushing AND awkward. 

    #Body
    group center:
        #Default cross
        attribute cross default if_any(["uniform"]):
            outfit_uniform + "3a.png"
        attribute cross default if_any(["casual"]):
            outfit_white_shirt + "3a.png"
        attribute cross default if_any(["green_shirt"]):
            outfit_green_shirt + "3a.png"
        attribute cross default if_any(["sweater"]):
            outfit_sweater + "3a.png"
        
        #Cross with the hand up
        attribute crossup if_any(["uniform"]):
            outfit_uniform + "3b.png"
        attribute crossup if_any(["casual"]):
            outfit_white_shirt + "3b.png"
        attribute crossup if_any(["green_shirt"]):
            outfit_green_shirt + "3b.png"
        attribute crossup if_any(["sweater"]):
            outfit_sweater + "3b.png"

    #Blush group
    group nose:
        attribute nose default if_any(["nobl"]) null #No blush
        attribute nose default if_any(["awkw", "nerv"]):     #Awkward
            nose + "awkw.png"
        attribute nose default if_any(["blus"]):     #Blushing
            nose + "blus.png"
        attribute nose default if_any(["blaw", "flus"]):     #Blushing and awkward
            nose + "blaw.png"

        #Truncated tags for customization
        attribute n1 null
        attribute n2:
            nose + "awkw.png"
        attribute n3:
            nose + "blus.png"
        attribute n4:
            nose + "blaw.png"

    #Eyes
    group eyes:
        #Open eyes
        attribute oe default if_any(["neut", "angr", "anno", "curi", "doub", "happ", #normal
                                    "laug", "lsur", "nerv", "sad", "worr"]):
            eyes + "e1a.png"
        attribute oe default if_any(["pani", "shoc", "vang", "vsur"]):               #wide-eyed
            eyes + "e1b.png"
        attribute oe default if_any(["dist", "flus"]):                               #looking away
            eyes + "e1c.png"
        attribute oe default if_any(["cry"]):                                        #crying
            eyes + "e1d.png"
        attribute oe default if_any(["yand"]):                                       #yandere
            eyes + "yand.png"

        #Closed eyes
        attribute ce if_any(["happ", "laug", "lsur", "nerv", "yand"]):  #happy closed eyes
            eyes + "e2a.png"
        attribute ce if_any(["neut", "angr", "curi", "dist", 
                            "doub", "sad", "vang", "worr"]):            #sad closed eyes
            eyes + "e2b.png"
        attribute ce if_any(["cry"]):                                   #crying closed eyes
            eyes + "e2c.png"
        attribute ce if_any(["anno", "flus", "pani", "shoc", "vsur"]):  # >.< eyes
            eyes + "e2d.png"
        
        #Truncated tags (use for more custom expressions)
        #Open eyes
        attribute e1a:
            eyes + "e1a.png"    #normal
        attribute e1b:
            eyes + "e1b.png"    #wide-eyed
        attribute e1c:
            eyes + "e1c.png"    #looking away
        attribute e1d:
            eyes + "e1d.png"    #crying
        attribute e1e:
            eyes + "yand.png"   #yandere eyes

        #Closed eyes
        attribute e2a:
            eyes + "e2a.png"    #Happy closed
        attribute e2b:
            eyes + "e2b.png"    #Sad closed
        attribute e2c:
            eyes + "e2c.png"    #Crying 
        attribute e2d:
            eyes + "e2d.png"    # >.< eyes

    #Blinking group. Disabled by default, but you can just put the 'default'
    #keyword on the attribute 'blink' to enable it by default. Doesn't work
    #on closed eyes and yandere eyes (you can just remove the 'e1e' below
    #to enable it on yandere eyes).
    group blink:
        attribute no_blink default null
        attribute blink if_not(["ce", "e1e", "e2a", "e2b", "e2c", "e2d"]):
            "blink_turned"

    #Mouths
    group mouth:
        #Closed mouths
        attribute cm default if_any(["flus", "happ", "laug"]):                      #Smiling
            mouths + "m1a.png"
        attribute cm default if_any(["neut", "angr", "cry", "dist", "doub", "lsur", "sad"]):#Not smiling
            mouths + "m1b.png"
        attribute cm default if_any(["vang"]):                                      #gritting teeth
            mouths + "m1c.png"
        attribute cm default if_any(["anno", "curi", "worr"]):                      #slightly opened, like :o
            mouths + "m1d.png"
        attribute cm default if_any(["yand"]):                                      #gritting teeth + smile
            mouths + "m1e.png"
        attribute cm default if_any(["shoc", "vsur"]):                              # ~ mouth
            mouths + "m3a.png"
        attribute cm default if_any(["nerv", "pani"]):                              # ~ mouth, more opened than the latter
            mouths + "m3b.png"

        #Opened mouths
        attribute om if_any(["neut", "anno", "lsur", "worr"]): #Neutral
            mouths + "m2a.png"
        attribute om if_any(["flus", "laug"]):                 #Wide smile
            mouths + "m2b.png"
        attribute om if_any(["angr", "doub", "nerv"]):         #Opened as if she was blaming someone
            mouths + "m2c.png"
        attribute om if_any(["cry", "shoc", "vang", "vsur"]):  #Can be used for angry/sad expressions
            mouths + "m2d.png"
        attribute om if_any(["happ"]):                         #Pretty much a light smile
            mouths + "m2e.png"
        attribute om if_any(["curi", "dist", "sad"]):          #Slightly opened
            mouths + "m2f.png"
        attribute om if_any(["yand"]):                         #Yandered smile
            mouths + "m2g.png"
        attribute om if_any(["pani"]):                         # ~ opened mouth
            mouths + "m3a.png"

        #Truncated tags (use for more custom expressions)
        #Closed mouths
        attribute m1a:
            mouths + "m1a.png"
        attribute m1b:
            mouths + "m1b.png"
        attribute m1c:
            mouths + "m1c.png"
        attribute m1d:
            mouths + "m1d.png"
        attribute m1e:
            mouths + "m1e.png"

        #Opened mouths
        attribute m2a:
            mouths + "m2a.png"
        attribute m2b:
            mouths + "m2b.png"
        attribute m2c:
            mouths + "m2c.png"
        attribute m2d:
            mouths + "m2d.png"
        attribute m2e:
            mouths + "m2e.png"
        attribute m2f:
            mouths + "m2f.png"
        attribute m2g:
            mouths + "m2g.png"

        #Could be used for both closed/opened mouths
        attribute m3a:
            mouths + "m3a.png"
        attribute m3b:
            mouths + "m3b.png"

    #Eyebrows
    group eyebrows:
        #The bc and bh eyebrows can only be used on closed eyes
        attribute brow default if_any(["neut", "happ"]):
            eyebrows + "ba.png"
        attribute brow default if_any(["angr", "vang"]) if_not(["ce", "e2a", "e2b", "e2c", "e2d"]):
            eyebrows + "bb.png"
        attribute brow default if_any(["angr", "vang"]) if_not(["e1a", "e1b", "e1c", "e1d", "e1e", "oe"]):
            eyebrows + "bc.png"
        attribute brow default if_any(["curi", "laug", "pani", "shoc", "vsur", "yand", "lsur"]):
            eyebrows + "bd.png"
        attribute brow default if_any(["cry", "flus", "nerv", "sad", "worr"]) if_not(["ce", "e2a", "e2b", "e2c", "e2d"]):
            eyebrows + "be.png"
        attribute brow default if_any(["anno", "vang"]):
            eyebrows + "bf.png"
        attribute brow default if_any(["dist", "doub"]):
            eyebrows + "bg.png"
        attribute brow default if_any(["cry", "flus", "nerv", "sad", "worr"]) if_not(["e1a", "e1b", "e1c", "e1d", "e1e", "oe"]):
            eyebrows + "bh.png"

        #Truncated tags (use for more customization)
        #Some eyebrows you'll use will be replaced by one
        #that looks like the one you wanted, but will be
        #adapted to fit depending if it's opened/closed eyes
        attribute ba:
            eyebrows + "ba.png"
        attribute bb if_not(["ce", "e2a", "e2b", "e2c", "e2d"]):
            eyebrows + "bb.png"
        attribute bc if_not(["e1a", "e1b", "e1c", "e1d", "e1e", "oe"]):
            eyebrows + "bc.png"
        attribute bd:
            eyebrows + "bd.png"
        attribute be if_not(["ce", "e2a", "e2b", "e2c", "e2d"]):
            eyebrows + "be.png"
        attribute bf:
            eyebrows + "bf.png"
        attribute bg:
            eyebrows + "bg.png"
        attribute bh if_not(["e1a", "e1b", "e1c", "e1d", "e1e", "oe"]):
            eyebrows + "bh.png"

    #This group exists so that you can add separated tears to the sprite,
    #using the 'tears' attribute (doesn't work on the e2d and yand eyes). Default isn't used.
    #To remove them, use the '-tears' or 'no_tears' attribute.
    group tears:
        attribute no_tears default null
        attribute tears if_not(["e2d", "e1e", "yand"]):
            expressions + "tears.png"


#Layeredimage for her looking away face, with crossed arms.
layeredimage natsuri shy:

    at renpy.partial(Flatten, drawable_resolution=False)

    always expressions + "shy_facebase.png"

    #Outfits. In order: uniform, white shirt (casual), green shirt and a light pink sweater
    group outfit:
        attribute uniform default null
        attribute casual null
        attribute green_shirt null
        attribute sweater null

    group mood:
        attribute neut default null #neutral
        attribute angr null #angry
        attribute happ null #happy
        attribute sad null  #sad

    #Body
    group center:
        #Default cross
        attribute cross default if_any(["uniform"]):
            outfit_uniform + "4a.png"
        attribute cross default if_any(["casual"]):
            outfit_white_shirt + "4a.png"
        attribute cross default if_any(["green_shirt"]):
            outfit_green_shirt + "4a.png"
        attribute cross default if_any(["sweater"]):
            outfit_sweater + "4a.png"
        
        #Cross with the hand up
        attribute crossup if_any(["uniform"]):
            outfit_uniform + "4b.png"
        attribute crossup if_any(["casual"]):
            outfit_white_shirt + "4b.png"
        attribute crossup if_any(["green_shirt"]):
            outfit_green_shirt + "4b.png"
        attribute crossup if_any(["sweater"]):
            outfit_sweater + "4b.png"

    group blush:

        attribute nobl default null #No blush.
        attribute awkw null #awkward.
        attribute bful null #full face blush. 

    #Be aware that the full face blush (bful) will hide the eyes and eyebrows.
    group nose:
        attribute nose default if_any(["nobl"]) null
        attribute nose default if_any(["awkw"]):
            shy_nose + "awkw.png"
        attribute nose default if_any(["bful"]):
            shy_nose + "bful.png"

        #Truncated tags (customization)
        attribute n1 null
        attribute n2:
            shy_nose + "awkw.png"
        attribute n3:
            shy_nose + "bful.png"
    
    #Mouths, still displayed even if bful
    group mouth:
        #Closed mouths
        attribute cm default if_any(["neut"]):
            shy_mouths + "m1a.png"
        attribute cm default if_any(["sad", "angr"]):
            shy_mouths + "m1b.png"
        attribute cm default if_any(["happ"]):
            shy_mouths + "m1c.png"
        
        #Opened mouths (there isn't really one that fits with her happy mood but eh)
        attribute om if_any(["angr", "neut", "happ"]):
            shy_mouths + "m2a.png"
        attribute om if_any(["sad"]):
            shy_mouths + "m2b.png"
        
        #Truncated tags
        #Closed mouths
        attribute m1a:
            shy_mouths + "m1a.png"
        attribute m1b:
            shy_mouths + "m1b.png"
        attribute m1c:
            shy_mouths + "m1c.png"

        #Opened mouths
        attribute m2a:
            shy_mouths + "m2a.png"
        attribute m2b:
            shy_mouths + "m2b.png"

    #Eyes displayed only if the bful isn't used
    group eyes if_not(["bful", "n3"]):
        #Opened eyes
        attribute oe default if_any(["happ"]):
            shy_eyes + "e1a.png"
        attribute oe default if_any(["neut"]):
            shy_eyes + "e1b.png"
        attribute oe default if_any(["angr"]):
            shy_eyes + "e1c.png"
        attribute oe default if_any(["sad"]):
            shy_eyes + "e1d.png"
        
        #Closed eyes
        attribute ce if_any(["angr"]):
            shy_eyes + "e2a.png"
        attribute ce if_any(["sad"]):
            shy_eyes + "e2b.png"
        attribute ce if_any(["happ", "neut"]):
            shy_eyes + "e2c.png"

        #Truncated tags (customization)
        #Opened eyes
        attribute e1a: 
            shy_eyes + "e1a.png"
        attribute e1b: 
            shy_eyes + "e1b.png"
        attribute e1c: 
            shy_eyes + "e1c.png"
        attribute e1d: 
            shy_eyes + "e1d.png"

        #Closed eyes
        attribute e2a: 
            shy_eyes + "e2a.png"
        attribute e2b: 
            shy_eyes + "e2b.png"
        attribute e2c:
            shy_eyes + "e2c.png"
        
    #Blinking group. Disabled if bful or any closed eyes.
    #Also disabled by default (same as above to enable it by default)
    group blink if_not(["bful", "n3"]):
        attribute no_blink default null
        attribute blink if_not(["ce", "e2a", "e2b", "e2c"]):
            "blink_shy"

    
    #Eyebrows, not displayed if bful
    group eyebrows if_not(["bful", "n3"]):
        attribute brow default if_any(["neut", "happ"]):
            shy_eyebrows + "bb.png"
        attribute brow default if_any(["angr"]):
            shy_eyebrows + "ba.png"
        attribute brow default if_any(["sad"]):
            shy_eyebrows + "bc.png"

        #Truncated tags for customization
        attribute ba:
            shy_eyebrows + "ba.png"
        attribute bb:
            shy_eyebrows + "bb.png"
        attribute bc:
            shy_eyebrows + "bc.png"