#This file can be edited by yourself if necessary, especially to change directories, add new images etc...
#For the Cheat Sheet, please mainly refer to the original Yuri Cheat Sheet MPT. There are only some poses that
#are different from the long-haired Yuri, like her bandaged right arm, with her sleeve up or down, and the scars. 
#For these, please see the 'Yuri Short Hair - MPT Cheat Sheet' file provided in the folder or, if you're accustomed to the way the
#MPT works, the name of the attributes written lines 215-235 for the uniform outfit, and 238-254 for the casual outfit.

#THE MAIN DIFFERENCE IN USING THESE LAYEREDIMAGES IS THAT INSTEAD OF WRITING:
    #show yuri turned casual...
    #show yuri shy...

#You'll have to add 'short hair' right after 'yuri', for example:
    #show yuri short hair turned casual...
    #show yuri short hair shy...

#IMPORTANT: YOU WON'T HAVE TO WRITE 'short hair turned/short hair shy' for each show statement, just the first one is necessary!!

#IMPORTANT NOTE: If you were to use both long-haired Yuri and short-haired Yuri in the same mod,
#you will, as always, have to precise which version you are going to show on the first show statement, like below.
#Please be aware that you can't show both of them at the same time ! (that would be weird anyway...)
    #show yuri turned casual happ at t11 (THIS SHOWS THE REGULAR YURI THANKS TO THE simple 'yuri turned' writing)
    #your code...

    #show yuri short hair turned at t11 (THIS WILL SHOW THE SHORT-HAIRED YURI THANKS TO THE 'yuri short hair turned' statement)

#TO SUM UP, use 'show/hide yuri short hair' after having shown/hidden long-haired Yuri, and use 'show/hide yuri turned'
                                                                                        #after having shown/hidden short-haired Yuri

#Both images defined below are images that will make Yuri blink at random times in the game when
#she has one of the open eyes written lines 472 and 694. To disable the blinking of each layeredimage,
#find the 'group blink' defined in each layeredimage and put it in comments by selecting all the lines
#of the latter and doing CTRL + K + C (or completely remove it, that's your file after all). For example:

    #group blink:

        #anchor (0,0) subpixel (True)

        #attribute blink_a default if_not(["ce","e4a","e4b","e4c","e4d","e4f","e4e","e1e","e1f"]):
            #"_yuri_blink_b"

#In case you wanted to put it back as it was, select all the lines of the group blink and do CTRL + K + U.

#Image of Turned Yuri blinking

image _yuri_blink_b:
    alpha 0.0
    renpy.random.randint(20, 100)*0.1 
    choice:
        alpha 1.0
        "mod_assets/MPT/yuri_short_hair/turned_blink/yuri_turned_eyes_blink1.png"
        0.015
        "mod_assets/MPT/yuri_short_hair/turned_blink/yuri_turned_eyes_blink2.png"
        0.035
        "mod_assets/MPT/yuri_short_hair/turned_blink/yuri_turned_eyes_blink1.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/yuri_short_hair/turned_blink/yuri_turned_eyes_blink1.png"
        0.015
        "mod_assets/MPT/yuri_short_hair/turned_blink/yuri_turned_eyes_blink2.png"
        0.065
        "mod_assets/MPT/yuri_short_hair/turned_blink/yuri_turned_eyes_blink1.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/yuri_short_hair/turned_blink/yuri_turned_eyes_blink1.png"
        0.015
        "mod_assets/MPT/yuri_short_hair/turned_blink/yuri_turned_eyes_blink2.png"
        0.095
        "mod_assets/MPT/yuri_short_hair/turned_blink/yuri_turned_eyes_blink1.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/yuri_short_hair/turned_blink/yuri_turned_eyes_blink1.png"
        0.015
        "mod_assets/MPT/yuri_short_hair/turned_blink/yuri_turned_eyes_blink2.png"
        0.035
        "mod_assets/MPT/yuri_short_hair/turned_blink/yuri_turned_eyes_blink1.png"
        0.015
        alpha 0.0
        0.15
        alpha 1.0
        "mod_assets/MPT/yuri_short_hair/turned_blink/yuri_turned_eyes_blink1.png"
        0.015
        "mod_assets/MPT/yuri_short_hair/turned_blink/yuri_turned_eyes_blink2.png"
        0.035
        "mod_assets/MPT/yuri_short_hair/turned_blink/yuri_turned_eyes_blink1.png"
        0.015
    repeat

#Image of Shy Yuri blinking

image _yuri_blink_s_b:
    alpha 0.0
    renpy.random.randint(30, 60)*0.1  
    choice:
        alpha 1.0
        "mod_assets/MPT/yuri_short_hair/shy_blink/yuri_blink_shy1.png"
        0.015
        "mod_assets/MPT/yuri_short_hair/shy_blink/yuri_blink_shy2.png"
        0.035
        "mod_assets/MPT/yuri_short_hair/shy_blink/yuri_blink_shy1.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/yuri_short_hair/shy_blink/yuri_blink_shy1.png"
        0.015
        "mod_assets/MPT/yuri_short_hair/shy_blink/yuri_blink_shy2.png"
        0.065
        "mod_assets/MPT/yuri_short_hair/shy_blink/yuri_blink_shy1.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/yuri_short_hair/shy_blink/yuri_blink_shy1.png"
        0.015
        "mod_assets/MPT/yuri_short_hair/shy_blink/yuri_blink_shy2.png"
        0.095
        "mod_assets/MPT/yuri_short_hair/shy_blink/yuri_blink_shy1.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/yuri_short_hair/shy_blink/yuri_blink_shy1.png"
        0.015
        "mod_assets/MPT/yuri_short_hair/shy_blink/yuri_blink_shy2.png"
        0.035
        "mod_assets/MPT/yuri_short_hair/shy_blink/yuri_blink_shy1.png"
        0.015
        alpha 0.0
        0.15
        alpha 1.0
        "mod_assets/MPT/yuri_short_hair/shy_blink/yuri_blink_shy1.png"
        0.015
        "mod_assets/MPT/yuri_short_hair/shy_blink/yuri_blink_shy2.png"
        0.035
        "mod_assets/MPT/yuri_short_hair/shy_blink/yuri_blink_shy1.png"
        0.015
    repeat



layeredimage yuri short hair turned:

    #Allows the sprite to have one single texture, when appearing or bliking for example, instead of multiple ones
    #at the same time. It is also useful for the alpha property, which would look very weird otherwise.
    at Flatten

    #Depending on the 'uniform' or 'casual' outfit, you'll have one of these two heads
    always "mod_assets/MPT/yuri_short_hair/turned_base/uniform/yuri_turned_facebase.png" if_not(["casual"])

    always "mod_assets/MPT/yuri_short_hair/turned_base/casual/yuri_turned_facebase.png" if_any(["casual"])

    #Attributes for autofocus logic (just copied from the original MPT).
    group af_logic multiple:
        attribute afm null #This attribute controls whether automatic control of the mouths takes place or not.  Add this tag to a character to enable automatic mouth control, remove it to disable it.
        attribute afz null #This attribute controls whether automatic control of zorder takes place or not.  Add this tag to a character to enable automatic zorder control, remove it to disable it.


    group outfit: #The default outfit will always be the uniform, unless the 'casual' word is used, like here: show yuri short hair turned casual...

        attribute uniform default null
        attribute casual null

    group mood: #Mood determines what the default images are for the following attributes: 
        #"oe", "ce", "om", "cm", "brow".
        #By changing what the "mood" attribute is, you can easily switch between premade sets of expressions that work well together, speeding up your workflow.
        #You can add new ones if you feel the need to !
        #Don't worry, the expressions will be the same as the original Yuri MPT
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
        attribute pout null #pouting
        attribute sad null  #sad
        attribute sedu null #seductive
        attribute shoc null #shocked
        attribute vang null #VERY angry
        attribute vsur null #surprised (very)
        attribute worr null #worried
        attribute yand null #yandere


    group blush: #This is the blush/nose Yuri can have if you use it ! Of course, no one is used originally (nobl)
        attribute nobl default null #No blush.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing AND awkward.  defaults for n

    #Left part of her body ! Another one is defined below in order to make sure the right
    #part of her body stays under the left one when her right arm is down
    group left:
        #anchor (0,0)
        subpixel (True)
        yoffset (-0.5)
        xoffset (0.5)
        #uniform
        attribute ldown default if_any(["uniform"]):
            "mod_assets/MPT/yuri_short_hair/turned_base/uniform/ldown.png"
        attribute lup if_any(["rup","rcut", "rcuts_deep", "rolled_up_cuts", "rbandages", "rolled_up_bandages", "rhealed"]) if_all(["uniform"]):
            "mod_assets/MPT/yuri_short_hair/turned_base/uniform/lup.png"

        #casual
        attribute ldown default if_any(["casual"]):
            "mod_assets/MPT/yuri_short_hair/turned_base/casual/ldown.png"
        attribute lup if_any(["rup","rcut", "rcuts_deep", "rolled_up_cuts", "rbandages", "rolled_up_bandages", "rhealed"]) if_all(["casual"]):
            "mod_assets/MPT/yuri_short_hair/turned_base/casual/lup.png"



    group right:
        #anchor (0,0)
        subpixel (True)
        yoffset (-0.5)
        #UNIFORM
        attribute rdown default if_any(["uniform"]):
            "mod_assets/MPT/yuri_short_hair/turned_base/uniform/rdown.png"
        attribute rup if_any(["uniform"]):
            "mod_assets/MPT/yuri_short_hair/turned_base/uniform/rup.png"
        attribute rcut if_any(["uniform"]):
            "mod_assets/MPT/yuri_short_hair/turned_base/uniform/cuts.png"
        attribute rcuts_deep if_any(["uniform"]): 
            "mod_assets/MPT/yuri_short_hair/turned_base/uniform/deep_cuts.png"
        attribute rolled_up_cuts if_any(["uniform"]):
            "mod_assets/MPT/yuri_short_hair/turned_base/uniform/cuts_rolled_up.png"
        attribute rbandages if_any(["uniform"]):
            "mod_assets/MPT/yuri_short_hair/turned_base/uniform/bandages.png"
        attribute rolled_up_bandages if_any(["uniform"]):
            "mod_assets/MPT/yuri_short_hair/turned_base/uniform/bandages_rolled_up.png"
        attribute rhealed if_any(["uniform"]):
            "mod_assets/MPT/yuri_short_hair/turned_base/uniform/healed.png"
        
        
        #CASUAL
        attribute rdown default if_any(["casual"]):
            "mod_assets/MPT/yuri_short_hair/turned_base/casual/rdown.png"
        attribute rup if_any(["casual"]):
            "mod_assets/MPT/yuri_short_hair/turned_base/casual/rup.png"
        attribute rcut if_any(["casual"]):
            "mod_assets/MPT/yuri_short_hair/turned_base/casual/cuts.png"
        attribute rcuts_deep if_any(["casual"]):
            "mod_assets/MPT/yuri_short_hair/turned_base/casual/deep_cuts.png"
        attribute rolled_up_cuts if_any(["casual"]):
            "mod_assets/MPT/yuri_short_hair/turned_base/casual/cuts_rolled_up.png"
        attribute rbandages if_any(["casual"]):
            "mod_assets/MPT/yuri_short_hair/turned_base/casual/bandages.png"
        attribute rolled_up_bandages if_any(["casual"]):
            "mod_assets/MPT/yuri_short_hair/turned_base/casual/bandages_rolled_up.png"
        attribute rhealed if_any(["casual"]):
            "mod_assets/MPT/yuri_short_hair/turned_base/casual/healed.png"


    group left:#This is here a second time to deal with if the right half of Yuri is shown only down; the left half of her with her arm up has to render over the right half.
        #anchor (0,0)
        subpixel (True)
        yoffset (-0.5)
        xoffset (0.5)
        #uniform
        attribute lup if_not(["rup","rcut", "rcuts_deep", "rolled_up_cuts", "rbandages", "rolled_up_bandages", "rhealed"]) if_all(["uniform"]):
            "mod_assets/MPT/yuri_short_hair/turned_base/uniform/lup.png"

        #casual
        attribute lup if_not(["rup","rcut", "rcuts_deep", "rolled_up_cuts", "rbandages", "rolled_up_bandages", "rhealed"]) if_all(["casual"]):
            "mod_assets/MPT/yuri_short_hair/turned_base/casual/lup.png"

    
    group nose:

        anchor (0,0) subpixel (True)

        #Default nose/blush.
        attribute nose default if_any(["nobl"]):#default nose
            "mod_assets/MPT/yuri_short_hair/turned_nose/yuri_turned_nose_n1.png"
        attribute nose default if_any(["awkw"]):#default nose when "awkward"
            "mod_assets/MPT/yuri_short_hair/turned_nose/yuri_turned_nose_n2.png"
        attribute nose default if_any(["blus"]):#default nose when "blushing"
            "mod_assets/MPT/yuri_short_hair/turned_nose/yuri_turned_nose_n3.png"
        attribute nose default if_any(["blaw"]):#default nose when "blushing" and "awkward"
            "mod_assets/MPT/yuri_short_hair/turned_nose/yuri_turned_nose_n4.png"


        ###All noses - truncated tags:
        attribute n1:
            "mod_assets/MPT/yuri_short_hair/turned_nose/yuri_turned_nose_n1.png"
        attribute n2:
            "mod_assets/MPT/yuri_short_hair/turned_nose/yuri_turned_nose_n2.png"
        attribute n3:
            "mod_assets/MPT/yuri_short_hair/turned_nose/yuri_turned_nose_n3.png"
        attribute n4:
            "mod_assets/MPT/yuri_short_hair/turned_nose/yuri_turned_nose_n4.png"



    group mouth:

        anchor (0,0) subpixel (True)

        #Default Closed Mouths:
        attribute cm default if_any(["happ","laug"]):
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_ma.png"
        attribute cm default if_any(["neut","lsur","worr"]):
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_md.png"#
        attribute cm default if_any(["sedu"]):
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_me.png"
        attribute cm default if_any(["pout","curi"]):
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_mf.png"
        attribute cm default if_any(["shoc"]):
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_mg.png"
        attribute cm default if_any(["dist","anno","vsur","sad","angr","cry","doub"]):
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_mj.png"
        attribute cm default if_any(["nerv","flus"]):
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_mk.png"
        attribute cm default if_any(["vang","pani"]):
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_mm.png"
        attribute cm default if_any(["yand"]):
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_mo.png"

        #Open Mouths:
        attribute om if_any(["happ"]):
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_mb.png"
        attribute om if_any(["laug","nerv","yand"]):
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_mc.png"
        attribute om if_any(["worr","pout"]):
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_me.png"
        attribute om if_any(["sedu"]):
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_mf.png"
        attribute om if_any(["dist","lsur","angr","cry"]):
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_mg.png"
        attribute om if_any(["neut","anno","vsur","curi"]):
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_mh.png"
        attribute om if_any(["flus","doub"]):
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_mi.png"
        attribute om if_any(["sad"]):
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_mk.png"                  
        attribute om if_any(["vang","shoc","pani"]):
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_ml.png"

        #THERE ARE 4 MOUTHS THAT AREN'T DEFINED HERE, WHICH HAVE mla, mlb, mlc and mld AS A SUFFIX.
        #YOU CAN USE THEM YOURSELF IF NEEDED BY DEFINING THEM LIKE BELOW, YOU JUST HAVE TO DO:
            #attribute name_of_the_mouth:
                #"directory of the mouth"
        ###All mouths - truncated tags:
        attribute ma:
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_ma.png"
        attribute mb:
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_mb.png"
        attribute mc:
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_mc.png"
        attribute md:
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_md.png"
        attribute me:
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_me.png"
        attribute mf:
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_mf.png"
        attribute mg:
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_mg.png"
        attribute mh:
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_mh.png"
        attribute mi:
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_mi.png"
        attribute mj:
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_mj.png"
        attribute mk:
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_mk.png"
        attribute ml:
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_ml.png"
        attribute mm:
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_mm.png"
        attribute mn:
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_mn.png"
        attribute mo:
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_mo.png"
        attribute mp:
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_mp.png"
        attribute mq:
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_mq.png"
        attribute mr:
            "mod_assets/MPT/yuri_short_hair/turned_mouth/yuri_turned_mouth_mr.png"



    group eyes:

        anchor (0,0) subpixel (True)

        #Default Opened eyes:
        attribute oe default if_any(["neut","sedu"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e1a.png"
        attribute oe default if_any(["dist","worr"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e1b.png"
        attribute oe default if_any(["happ","angr","pout","curi"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e1d.png"
        attribute oe default if_any(["cry"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e1h.png"
        attribute oe default if_any(["lsur","vang"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e2a.png"
        attribute oe default if_any(["anno","flus","laug","sad"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e2b.png"
        attribute oe default if_any(["nerv","doub"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e2c.png"
        attribute oe default if_any(["shoc","pani","vsur"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e2d.png"
        attribute oe default if_any(["yand"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e3a.png"

        #Default Closed eyes:
        attribute ce if_any(["dist","anno","vang","flus","lsur","shoc","vsur","worr","sad","angr","nerv","curi","doub"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e4a.png"
        attribute ce if_any(["neut","happ","yand","pani","laug","sedu","pout"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e4b.png"
        attribute ce if_any(["cry"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e4e.png"


        ###All eyes - truncated tags:
        attribute e1a:
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e1a.png"
        attribute e1b:
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e1b.png"
        attribute e1c:
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e1c.png"
        attribute e1d:
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e1d.png"
        attribute e1e:
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e1e.png"
        attribute e1f:
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e1f.png"
        attribute e1g:
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e1g.png"
        attribute e1h:
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e1h.png"
        attribute e2a:
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e2a.png"
        attribute e2b:
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e2b.png"
        attribute e2c:
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e2c.png"
        attribute e2d:
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e2d.png"
        attribute e3a:
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e3a.png"
        attribute e3b:
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e3b.png"
        attribute e4a:
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e4a.png"
        attribute e4b:
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e4b.png"
        attribute e4c:
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e4c.png"
        attribute e4d:
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e4d.png"
        attribute e4e:
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e4e.png"
        attribute e0a:
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e0a.png"
        attribute e0b:
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_e0b.png"
        attribute ela:
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_ela.png"
        attribute elb:
            "mod_assets/MPT/yuri_short_hair/turned_eyes/yuri_turned_eyes_elb.png"


    group blink:

        anchor (0,0) subpixel (True)

        attribute blink_b default if_not(["ce","e4a","e4b","e4c","e4d","e4f","e4e","e1e","e1f", "e2d" "e0a", "e0b"]):
            "_yuri_blink_b"

    group eyebrows:

        anchor (0,0) subpixel (True)

        #Default Eyebrows:
        attribute brow default if_any(["neut"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyebrows/yuri_turned_eyebrows_b1a.png"
        attribute brow default if_any(["flus","lsur","laug"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyebrows/yuri_turned_eyebrows_b1b.png"
        attribute brow default if_any(["dist","sedu"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyebrows/yuri_turned_eyebrows_b1c.png"
        attribute brow default if_any(["anno"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyebrows/yuri_turned_eyebrows_b1d.png"
        attribute brow default if_any(["vang","angr"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyebrows/yuri_turned_eyebrows_b1e.png"
        attribute brow default if_any(["curi","doub"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyebrows/yuri_turned_eyebrows_b1f.png"
        attribute brow default if_any(["happ"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyebrows/yuri_turned_eyebrows_b2a.png"
        attribute brow default if_any(["worr","sad","nerv","cry"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyebrows/yuri_turned_eyebrows_b2b.png"
        attribute brow default if_any(["yand","shoc","vsur","pani"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyebrows/yuri_turned_eyebrows_b2c.png"
        attribute brow default if_any(["pout"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyebrows/yuri_turned_eyebrows_b3b.png"


        ###All eyebrows - truncated tags:
        #This first set of definitions has only the logic to exclude certain eyebrows for particular large eye Yuri expressions.
        attribute b1a:
            "mod_assets/MPT/yuri_short_hair/turned_eyebrows/yuri_turned_eyebrows_b1a.png"
        attribute b1b:
            "mod_assets/MPT/yuri_short_hair/turned_eyebrows/yuri_turned_eyebrows_b1b.png"
        attribute b1c if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyebrows/yuri_turned_eyebrows_b1c.png"
        attribute b1d if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyebrows/yuri_turned_eyebrows_b1d.png"
        attribute b1e if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyebrows/yuri_turned_eyebrows_b1e.png"
        attribute b1f:
            "mod_assets/MPT/yuri_short_hair/turned_eyebrows/yuri_turned_eyebrows_b1f.png"
        attribute b2a:
            "mod_assets/MPT/yuri_short_hair/turned_eyebrows/yuri_turned_eyebrows_b2a.png"
        attribute b2b if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyebrows/yuri_turned_eyebrows_b2b.png"
        attribute b2c:
            "mod_assets/MPT/yuri_short_hair/turned_eyebrows/yuri_turned_eyebrows_b2c.png"
        attribute b3a if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyebrows/yuri_turned_eyebrows_b3a.png"
        attribute b3b if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyebrows/yuri_turned_eyebrows_b3b.png"
        attribute b3c:
            "mod_assets/MPT/yuri_short_hair/turned_eyebrows/yuri_turned_eyebrows_b3c.png"


        #This second set allows those above eyebrows to render on problematic moods...so long as their eyes are closed.
        attribute b1c if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyebrows/yuri_turned_eyebrows_b1c.png"
        attribute b1d if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyebrows/yuri_turned_eyebrows_b1d.png"
        attribute b1e if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyebrows/yuri_turned_eyebrows_b1e.png"
        attribute b2b if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyebrows/yuri_turned_eyebrows_b2b.png"
        attribute b3a if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyebrows/yuri_turned_eyebrows_b3a.png"
        attribute b3b if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            "mod_assets/MPT/yuri_short_hair/turned_eyebrows/yuri_turned_eyebrows_b3b.png"



    #This group is intentionally last on this list, so it will render over top of every other thing on the face.
    group special:

        anchor (0,0) subpixel (True)

        attribute scream:
            "mod_assets/MPT/yuri_short_hair/turned_scream/yuri_turned_scream.png"


#Here is the layered image of Shy Yuri !
layeredimage yuri short hair shy:

    at Flatten
    #There will also be 2 bases, both the full body and head (same syntax than for the turned version)
    #Which one is used will be determined by the uniform or casual attribute defined after
    always "mod_assets/MPT/yuri_short_hair/shy_base/yuri_base_shy_uniform.png" if_not(["casual"])

    always "mod_assets/MPT/yuri_short_hair/shy_base/yuri_base_shy_casual.png" if_any(["casual"])

    #Attributes for autofocus logic (just copied from the original MPT).
    group af_logic multiple:
        attribute afm null #This attribute controls whether automatic control of the mouths takes place or not.  Add this tag to a character to enable automatic mouth control, remove it to disable it.
        attribute afz null #This attribute controls whether automatic control of zorder takes place or not.  Add this tag to a character to enable automatic zorder control, remove it to disable it.


    group outfit: #The default outfit will always be the uniform, unless the 'casual' word is used, like here: show yuri short hair shy casual...

        attribute uniform default null
        attribute casual null

    group mood: #Mood determines what the default images are for the following attributes:
        #"oe", "ce", "om", "cm", "brow".
        #By changing what the "mood" attribute is, you can easily switch between premade sets of expressions that work well together, speeding up your workflow.
        #You can add new ones if you feel the need to !
        #Don't worry, the expressions will be the same as the original Yuri MPT
        attribute neut default null #neutral
        attribute angr null #angry
        attribute happ null #happy
        attribute sad null  #sad

    group blush:
        attribute nobl default null #No blush.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing AND awkward.  defaults for n
        attribute bful null #full face blush.  Only works for this pose, not for the turned version


    group nose:

        anchor (0,0) subpixel (True)

        #Default nose/blush.
        attribute nose default if_any(["nobl"]):#default nose
            "mod_assets/MPT/yuri_short_hair/shy_nose/yuri_shy_nose_n1.png"
        attribute nose default if_any(["awkw"]):#default nose when "awkward"
            "mod_assets/MPT/yuri_short_hair/shy_nose/yuri_shy_nose_n2.png"
        attribute nose default if_any(["blus"]):#default nose when "blushing"
            "mod_assets/MPT/yuri_short_hair/shy_nose/yuri_shy_nose_n3.png"
        attribute nose default if_any(["blaw"]):#default nose when "blushing" and "awkward"
            "mod_assets/MPT/yuri_short_hair/shy_nose/yuri_shy_nose_n4.png"
        attribute nose default if_any(["bful"]):#Full face blush
            "mod_assets/MPT/yuri_short_hair/shy_nose/yuri_shy_nose_n5.png"


        ###All noses - truncated tags:
        attribute n1:
            "mod_assets/MPT/yuri_short_hair/shy_nose/yuri_shy_nose_n1.png"
        attribute n2:
            "mod_assets/MPT/yuri_short_hair/shy_nose/yuri_shy_nose_n2.png"
        attribute n3:
            "mod_assets/MPT/yuri_short_hair/shy_nose/yuri_shy_nose_n3.png"
        attribute n4:
            "mod_assets/MPT/yuri_short_hair/shy_nose/yuri_shy_nose_n4.png"
        attribute n5:
            "mod_assets/MPT/yuri_short_hair/shy_nose/yuri_shy_nose_n5.png"



    group mouth:

        anchor (0,0) subpixel (True)

        #default closed mouths
        attribute cm default if_any(["neut"]):
            "mod_assets/MPT/yuri_short_hair/shy_mouth/yuri_shy_mouth_m1.png"
        attribute cm default if_any(["angr","sad"]):
            "mod_assets/MPT/yuri_short_hair/shy_mouth/yuri_shy_mouth_m2.png"
        attribute cm default if_any(["happ"]):
            "mod_assets/MPT/yuri_short_hair/shy_mouth/yuri_shy_mouth_m3.png"

        #default open mouth.  As of this writing...she only has one open mouth.
        attribute om:
            "mod_assets/MPT/yuri_short_hair/shy_mouth/yuri_shy_mouth_m4.png"


        #All mouths - truncated tags:
        attribute m1:
            "mod_assets/MPT/yuri_short_hair/shy_mouth/yuri_shy_mouth_m1.png"
        attribute m2:
            "mod_assets/MPT/yuri_short_hair/shy_mouth/yuri_shy_mouth_m2.png"
        attribute m3:
            "mod_assets/MPT/yuri_short_hair/shy_mouth/yuri_shy_mouth_m3.png"
        attribute m4:
            "mod_assets/MPT/yuri_short_hair/shy_mouth/yuri_shy_mouth_m4.png"



    group eyes if_not(["n5","bful"]): #Cannot show if full-face blush is present.

        anchor (0,0) subpixel (True)

        #Open eyes
        attribute oe default if_any(["happ"]):
            "mod_assets/MPT/yuri_short_hair/shy_eyes/yuri_shy_eyes_e1.png"
        attribute oe default if_any(["neut"]):
            "mod_assets/MPT/yuri_short_hair/shy_eyes/yuri_shy_eyes_e2.png"
        attribute oe default if_any(["angr"]):
            "mod_assets/MPT/yuri_short_hair/shy_eyes/yuri_shy_eyes_e3.png"
        attribute oe default if_any(["sad"]):
            "mod_assets/MPT/yuri_short_hair/shy_eyes/yuri_shy_eyes_e4.png"

        #Closed eyes
        attribute ce if_any(["angr","neut","happ"]):
            "mod_assets/MPT/yuri_short_hair/shy_eyes/yuri_shy_eyes_e5.png"
        attribute ce if_any(["sad"]):
            "mod_assets/MPT/yuri_short_hair/shy_eyes/yuri_shy_eyes_e6.png"


        #All eyes - truncated tags:
        attribute e1:
            "mod_assets/MPT/yuri_short_hair/shy_eyes/yuri_shy_eyes_e1.png"
        attribute e2:
            "mod_assets/MPT/yuri_short_hair/shy_eyes/yuri_shy_eyes_e2.png"
        attribute e3:
            "mod_assets/MPT/yuri_short_hair/shy_eyes/yuri_shy_eyes_e3.png"
        attribute e4:
            "mod_assets/MPT/yuri_short_hair/shy_eyes/yuri_shy_eyes_e4.png"
        attribute e5:
            "mod_assets/MPT/yuri_short_hair/shy_eyes/yuri_shy_eyes_e5.png"
        attribute e6:
            "mod_assets/MPT/yuri_short_hair/shy_eyes/yuri_shy_eyes_e6.png"


    group blink:

        anchor (0,0) subpixel (True)

        attribute blink_a default if_not(["ce","e5","e6","n5", "bful"]):
            "_yuri_blink_s_b"


    group eyebrows if_not(["n5","bful"]): #Cannot show if full-face blush is present.

        anchor (0,0) subpixel (True)

        attribute brow default if_any(["happ"]):
            "mod_assets/MPT/yuri_short_hair/shy_eyebrows/yuri_shy_eyebrows_b1.png"
        attribute brow default if_any(["neut","sad"]):
            "mod_assets/MPT/yuri_short_hair/shy_eyebrows/yuri_shy_eyebrows_b2.png"
        attribute brow default if_any(["angr"]):
            "mod_assets/MPT/yuri_short_hair/shy_eyebrows/yuri_shy_eyebrows_b3.png"


        #all brows - truncated:
        attribute b1:
            "mod_assets/MPT/yuri_short_hair/shy_eyebrows/yuri_shy_eyebrows_b1.png"
        attribute b2:
            "mod_assets/MPT/yuri_short_hair/shy_eyebrows/yuri_shy_eyebrows_b2.png"
        attribute b3:
            "mod_assets/MPT/yuri_short_hair/shy_eyebrows/yuri_shy_eyebrows_b3.png"