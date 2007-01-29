﻿## This file contains some of the options that can be changed to customize
## your Ren'Py game. It only contains the most common options... there
## is quite a bit more customization you can do.
##
## Lines beginning with two '#' marks are comments, and you shouldn't
## uncomment them. Lines beginning with a single '#' mark are
## commented-out code, and you may want to uncomment them when
## appropriate.

init -1:
    python hide:

        ## Should we enable the use of developer tools? This should be
        ## set to False before the game is released, so the user can't
        ## cheat using developer tools.

        config.developer = True
        
        ## These control the width and height of the screen.

        config.screen_width = 800
        config.screen_height = 600

        ## This controls the title of the window, when Ren'Py is
        ## running in a window.

        config.window_title = u"The Ren'Py Demo Game"

        ## We then want to call a theme function. themes.roundrect is
        ## a theme that features the use of rounded rectangles. It's
        ## the only theme we currently support.
        ##
        ## The theme function takes a number of parameters that can
        ## customize the color scheme.
        theme.roundrect(

            ## The color of an idle widget face.
            widget = "#003c78",

            ## The color of a focused widget face.
            widget_hover = "#0050a0",

            ## The color of the text in a widget.
            widget_text = "#c8ffff",

            ## The color of the text in a selected widget. (For
            ## example, the current value of a preference.)
            widget_selected = "#ffffc8",

            ## The color of a disabled widget face. 
            disabled = "#404040",

            ## The color of disabled widget text.
            disabled_text = "#c8c8c8",

            ## The color of informational labels.
            label = "#ffffff",

            ## The color of a frame containing widgets.
            frame = "#6496c8",

            ## If this is True, in-game menus are placed in the center
            ## the screen. If False, they are placed inside a window
            ## at the bottom of the screen.
            button_menu = True,

            ## If this is True, the in-game window is rounded. If False,
            ## the in-game window is square.
            rounded_window = False,
            
            ## The background of the main menu. This can be a color
            ## beginning with '#', or an image filename. The latter
            ## should take up the full height and width of the screen.
            mm_root = "mainmenu.jpg",

            ## The background of the game menu. This can be a color
            ## beginning with '#', or an image filename. The latter
            ## should take up the full height and width of the screen.
            gm_root = "#dcebff",

            ## And we're done with the theme. The theme will customize
            ## various styles, so if we want to change them, we should
            ## do so below.            
            )

        # Move the main menu to near the top of the screen.
        style.mm_menu_window.yanchor = 0
        style.mm_menu_window.ypos = 0.05
  

        #########################################
        ## These settings let you customize the window containing the
        ## dialogue and narration, by replacing it with an image.

        ## The background of the window. In a Frame, the two numbers
        ## are the size of the left/right and top/bottom borders,
        ## respectively.

        # style.window.background = Frame("frame.png", 12, 12)
        
        ## Margin is space surrounding the window, where the background
        ## is not drawn.

        # style.window.left_margin = 6
        # style.window.right_margin = 6
        # style.window.top_margin = 6
        # style.window.bottom_margin = 6
        
        ## Padding is space inside the window, where the background is
        ## drawn.

        # style.window.left_padding = 6
        # style.window.right_padding = 6
        # style.window.top_padding = 6
        # style.window.bottom_padding = 6

        ## This is the minimum height of the window, including the margins
        ## and padding.

        # style.window.yminimum = 250


        #########################################
        ## This lets you change the placement of the main menu.
        
        ## The way placement works is that we find an anchor point
        ## inside a displayable, and a position (pos) point on the
        ## screen. We then place the displayable so the two points are
        ## at the same place.

        ## An anchor/pos can be given as an integer or a floating point
        ## number. If an integer, the number is interpreted as a number
        ## of pixels from the upper-left corner. If a floating point,
        ## the number is interpreted as a fraction of the size of the
        ## displayable or screen.

        # style.mm_menu_frame.xpos = 0.5
        # style.mm_menu_frame.xanchor = 0.5
        # style.mm_menu_frame.ypos = 0.75
        # style.mm_menu_frame.yanchor = 0.5


        #########################################
        ## These let you customize the default font used for text in Ren'Py.

        ## The file containing the default font.

        # style.default.font = "DejaVuSans.ttf"

        ## The default size of text.

        # style.default.size = 22

        ## Note that these only change the size of some of the text. Other
        ## buttons have their own styles.


        #########################################
        ## These settings let you change some of the sounds that are used by
        ## Ren'Py.

        ## Set this to False if the game does not have any sound effects.

        config.has_sound = True

        ## Set this to False if the game does not have any music.

        config.has_music = True
        
        ## Set this to False if the game does not have voicing.

        config.has_voice = True
        
        ## Sounds that are used when button and imagemaps are clicked.

        style.button.activate_sound = "click.wav"
        style.imagemap.activate_sound = "click.wav"

        ## Sounds that are used when entering and exiting the game menu.

        config.enter_sound = "click.wav"
        config.exit_sound = "click.wav"

        ## A sample sound that can be played to check the sound volume.

        config.sample_sound = "click.wav"

        ## Music that is played while the user is at the main menu.

        # config.main_menu_music = "main_menu_theme.ogg"

        
        #########################################
        ## Miscellaneous customizations

        ## These let you change the transitions that are used when entering
        ## and exiting the game menu.

        config.enter_transition = dissolve
        config.exit_transition = dissolve
        
