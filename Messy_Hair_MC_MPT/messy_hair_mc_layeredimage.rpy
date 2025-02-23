#There aren't any moods for this layeredimage, so you'll need to 
#write the attributes manually. As always, I'd recommend using Exposer Previewer!

init python:
    #Change this path to match your own folders!
    path = "mod_assets/MPT/Messy_Hair_MC_MPT/"


layeredimage messy mc turned:

    at renpy.partial(Flatten, drawable_resolution=False)

    group outfit:
        attribute uniform default null
        attribute casual null
    
    group left if_any(["uniform"]) if_not(["crossed"]): # had to make two different groups for the left part
        attribute ldown default:
            path + "outfits/uniform_ldown.png" #left arm down (default)
        
        attribute lup:
            path + "outfits/uniform_lup.png" #left arm up
        
        attribute lscratch:
            path + "outfits/uniform_lscratch.png" #scratching his head
        
    group left if_any(["casual"]) if_not(["crossed"]): # since this one is a bit off centered
        subpixel True
        anchor (0.0, 0.0)
        xoffset 0.3

        attribute ldown default:
            path + "outfits/casual_ldown.png" #left arm down (default)

        attribute lup:
            path + "outfits/casual_lup.png" #left arm up

        attribute lscratch:
            path + "outfits/casual_lscratch.png" #scratching his head

    group right:
        attribute rdown default if_any(["uniform"]) if_not(["crossed"]):
            path + "outfits/uniform_rdown.png"
        attribute rdown default if_any(["casual"]) if_not(["crossed"]):
            path + "outfits/casual_rdown.png"
        
        attribute rpocket if_any(["uniform"]) if_not(["crossed"]):
            path + "outfits/uniform_rpocket.png"
        attribute rpocket if_any(["casual"]) if_not(["crossed"]):
            path + "outfits/casual_rpocket.png"

    group center:
        attribute not_crossed default null
        attribute crossed if_any(["uniform"]):
            path + "outfits/uniform_crossed.png"
        attribute crossed if_any(["casual"]):
            path + "outfits/casual_crossed.png"
    
    always: # render the head above the body, otherwise the back of the sweater overlaps
        subpixel True
        anchor (0.0, 0.0)
        yoffset -0.1
        
        path + "facebase.png"

    group nose:
        attribute na default null                         # nothing
        attribute nb:
            path + "nose_b.png"     # sweat drop
        attribute nc:
            path + "nose_c.png"     # blush

    group mouth:
        attribute ma default:
            path + "mouth_a.png"    # smiling
        attribute mb:
            path + "mouth_b.png"    # smiling + talking
        attribute mc:
            path + "mouth_c.png"    # big ass smile
        attribute md:
            path + "mouth_d.png"    # closed mouth
        attribute me:
            path + "mouth_e.png"    # closed mouth but it's a bit open
        attribute mf:
            path + "mouth_f.png"    # talking
        attribute mg:
            path + "mouth_g.png"    # closed mouth, "yeah no shit!" style
        attribute mh:
            path + "mouth_h.png"    # surprised
        attribute mi:
            path + "mouth_i.png"    # awkward laugh
        attribute mj:
            path + "mouth_j.png"    # anger

    group eyes:
        attribute ea default:
            path + "eyes_a.png"     # neutral
        attribute eb:
            path + "eyes_b.png"     # serious
        attribute ec:
            path + "eyes_c.png"     # surprised
        attribute ed:
            path + "eyes_d.png"     # closed
        attribute ee:
            path + "eyes_e.png"     # closed + happy
        
    group eyebrows:
        attribute ba default:
            path + "eyebrows_a.png" # neutral
        attribute bb:
            path + "eyebrows_b.png" # serious
        attribute bc:
            path + "eyebrows_c.png" # surprised
        attribute bd:
            path + "eyebrows_d.png" # anger
        attribute be:
            path + "eyebrows_e.png" # worried
