init -5 python:

    #base path of the folder. Change this variable to your liking!
    path = "mod_assets/MPT/Satsurika_MPT/" 

    casual_path = path + "outfits/casual/"
    uniform_path = path + "outfits/uniform/"
    
    eyes_path = path + "expressions/eyes/"
    eyebrows_path = path + "expressions/eyebrows/"
    mouths_path = path + "expressions/mouths/"
    nose_path = path + "expressions/nose/"

#Blinking image. Disabled by default in the 'group blink'.
image sat_blink:
    alpha 0.0
    renpy.random.randint(20, 100)*0.1
    choice:
        alpha 1.0
        eyes_path + "blink_a.png"
        0.015
        eyes_path + "blink_b.png"
        0.035
        eyes_path + "blink_a.png"
        0.015
    choice:
        alpha 1.0
        eyes_path + "blink_a.png"
        0.015
        eyes_path + "blink_b.png"
        0.065
        eyes_path + "blink_a.png"
        0.015
    choice:
        alpha 1.0
        eyes_path + "blink_a.png"
        0.015
        eyes_path + "blink_b.png"
        0.095
        eyes_path + "blink_a.png"
        0.015
    choice:
        alpha 1.0
        eyes_path + "blink_a.png"
        0.015
        eyes_path + "blink_b.png"
        0.035
        eyes_path + "blink_a.png"
        0.015
        alpha 0.0
        0.15
        alpha 1.0
        eyes_path + "blink_a.png"
        0.015
        eyes_path + "blink_b.png"
        0.035
        eyes_path + "blink_a.png"
        0.015
    repeat


#Layeredimage of Satsurika. No need to use a 'forward' or 'turned' keyword here,
#since there's only one layeredimage defined for her. To show her:
#   show satsurika [outfit] [body] [mood] [expressions] at [position]
layeredimage satsurika:

    #Better rendering and fixes the vertical/horizontal line issue on most sprites
    at renpy.partial(Flatten, drawable_resolution=False)

    #Always the same facebase
    always path + "expressions/facebase.png" 

    #Outfits
    group outfit:
        attribute uniform default null
        attribute casual null

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
        attribute surp null #surprised
        attribute nerv null #nervous
        attribute pani null #panicked
        attribute sad null  #sad
        attribute sedu null #seductive
        attribute worr null #worried

    #Group used to define the 'nose' image used in the group nose
    group blush:
        attribute nobl default null #no blush
        attribute awkw null #awkward
        attribute blus null #blushing
        attribute blaw null #blushing & awkward

    #Left part of the body
    group left:
        #Left arm down
        attribute ldown default if_any(["uniform"]):
            uniform_path + "1l.png"
        attribute ldown default if_any(["casual"]):
            casual_path + "1l.png"

        #Left arm pointing
        attribute lpoint if_any(["uniform"]):
            uniform_path + "2l.png"
        attribute lpoint if_any(["casual"]):
            casual_path + "2l.png"


    #Right part of the body
    group right:
        #Right arm down
        attribute rdown default if_any(["uniform"]):
            uniform_path + "1r.png"
        attribute rdown default if_any(["casual"]):
            casual_path + "1r.png"

        #Right arm on the hip
        attribute rhip if_any(["uniform"]):
            uniform_path + "2r.png"
        attribute rhip if_any(["casual"]):
            casual_path + "2r.png"

    #Nose group (in order: no blush/awkward/blush/blush & awkward)
    #Some moods can show one of those images: those are the nervous,
    #panicked, seductive and flustered moods.
    group nose:
        attribute nose default if_any(["nobl"]) null
        attribute nose default if_any(["awkw", "nerv", "pani"]):
            nose_path + "awkw.png"
        attribute nose default if_any(["blus", "sedu"]):
            nose_path + "blus.png"
        attribute nose default if_any(["blaw", "flus"]):
            nose_path + "blaw.png"

    #Mouths
    group mouth:
        #Closed mouths
        attribute cm default if_any(["happ", "nerv"]): #wide smile
            mouths_path + "m1a.png"
        attribute cm default if_any(["neut", "dist", "doub", "sad", "worr"]): #not smiling
            mouths_path + "m1b.png"
        attribute cm default if_any(["laug", "sedu"]): #normal smile
            mouths_path + "m1c.png"
        attribute cm default if_any(["angr"]): #showing teeth
            mouths_path + "m1d.png"
        attribute cm default if_any(["cry", "flus", "pani"]): # ^~^ type of mouth
            mouths_path + "m1e.png"
        attribute cm default if_any(["curi", "surp"]): #slightly opened mouth, wondering
            mouths_path + "m3a.png"

        #Opened mouths
        attribute om if_any(["happ", "laug", "nerv", "sedu"]): #smile
            mouths_path + "m2a.png"
        attribute om if_any(["cry", "surp", "pani"]): #panicked
            mouths_path + "m2b.png"
        attribute om if_any(["neut", "curi", "dist", "sad"]): #barely opened
            mouths_path + "m2c.png"
        attribute om if_any(["angr", "doub", "worr"]): #more opened
            mouths_path + "m2d.png"
        attribute om if_any(["flus"]): #slightly opened mouth, wondering
            mouths_path + "m3a.png"

        #Truncated tags (use those for more customization)
        attribute m1a:
            mouths_path + "m1a.png"
        attribute m1b:
            mouths_path + "m1b.png"
        attribute m1c:
            mouths_path + "m1c.png"
        attribute m1d:
            mouths_path + "m1d.png"
        attribute m1e:
            mouths_path + "m1e.png"
        attribute m2a:
            mouths_path + "m2a.png"
        attribute m2b:
            mouths_path + "m2b.png"
        attribute m2c:
            mouths_path + "m2c.png"
        attribute m2d:
            mouths_path + "m2d.png"
        attribute m3a:
            mouths_path + "m3a.png"
        

    #Eyes
    group eyes:
        #Opened eyes
        attribute oe default if_any(["neut", "curi", "happ", "laug"]): #normal Monika's eyes
            eyes_path + "green_e1a.png"
        attribute oe default if_any(["nerv"]):  #looking away Monika's eyes
            eyes_path + "green_e1b.png"
        attribute oe default if_any(["angr", "doub", "sedu"]):  #seductive Monika's eyes
            eyes_path + "green_e1c.png"
        attribute oe default if_any(["sad", "worr"]): #normal Sayori's eyes
            eyes_path + "blue_e1a.png"
        attribute oe default if_any(["cry"]):   #crying Sayori's eyes
            eyes_path + "blue_e1b.png"
        attribute oe default if_any(["dist"]):  #looking away Natsuki's eyes
            eyes_path + "pink_e1a.png"
        attribute oe default if_any(["surp", "pani"]):  #surprised Yuri's eyes
            eyes_path + "purple_e1a.png"
        attribute oe default if_any(["flus"]):  #looking away Yuri's eyes
            eyes_path + "purple_e1b.png"
        
        #Closed eyes
        attribute ce if_any(["curi", "flus", "happ", "laug", "surp", "nerv", "sedu"]): # "happy" closed eyes
            eyes_path + "e2a.png"
        attribute ce if_any(["neut", "angr", "cry", "dist", "doub", "pani", "sad", "worr"]): # "sad" closed eyes
            eyes_path + "e2b.png"

        #Truncated tags (use for more customization)
        #Green eyes
        attribute green_eyes1:
            eyes_path + "green_e1a.png"
        attribute green_eyes2:
            eyes_path + "green_e1b.png"
        attribute green_eyes3:
            eyes_path + "green_e1c.png"
        
        #Blue eyes
        attribute blue_eyes1:
            eyes_path + "blue_e1a.png"
        attribute blue_eyes2:
            eyes_path + "blue_e1b.png"

        #Pink eyes
        attribute pink_eyes:
            eyes_path + "pink_e1a.png"
        
        #Purple eyes
        attribute purple_eyes1:
            eyes_path + "purple_e1a.png"
        attribute purple_eyes2:
            eyes_path + "purple_e1b.png"

        attribute e2a: #Happy closed eyes
            eyes_path + "e2a.png"
        attribute e2b: #Sad closed eyes
            eyes_path + "e2b.png"
        
        
    #Group to make Satsurika blink in game. It is
    #disabled by default. To enable it, either remove the 
    # 'default' keyword below to the first attribute and put
    #it on the other one (recommended) so that it looks like this:
    #   attribute blink default if_not(...):
    #or just use the 'blink' attribute when showing her (possible 
    # but depends what you wanna do).
    group blink:
        attribute no_blink default null
        #blink if it's not closed eyes
        attribute blink if_not(["ce", "e2a", "e2b"]):
            "sat_blink"


    #Eyebrows
    group eyebrows:
        attribute brow default if_any(["cry", "curi", "happ", "surp"]):
            eyebrows_path + "ba.png"
        attribute brow default if_any(["nerv", "sad", "worr"]):
            eyebrows_path + "bb.png"
        attribute brow default if_any(["neut", "dist", "flus", "laug", "pani", "sedu"]):
            eyebrows_path + "bc.png"
        attribute brow default if_any(["angr", "doub"]):
            eyebrows_path + "bd.png"
        
        #Truncated tags (use for more customization)
        attribute ba:
            eyebrows_path + "ba.png"
        attribute bb:
            eyebrows_path + "bb.png"
        attribute bc:
            eyebrows_path + "bc.png"
        attribute bd:
            eyebrows_path + "bd.png"
