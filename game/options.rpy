## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Getting Familiar")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False


## The version of the game.

define config.version = "1.1"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
Created by Jeanie Choi, M Ebel, and Eliza Velasquez.

Source code (Python and Ren'Py files) are licensed under the {a=https://www.gnu.org/licenses/gpl-3.0.en.html}GPL v3.0{/a}. Original art assets are copyright Jeanie Choi, M Ebel, and Eliza Velasquez. All rights reserved.

Click {q}Credits{/q} or view CREDITS.txt for a detailed list of third-party attribution and licensing information.
""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "getting-familiar"


## Sounds and music ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = False


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = "music/Moonlight Hall.mp3"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = Dissolve(0.2)
define config.exit_transition = Dissolve(0.2)


## Between screens of the game menu.

define config.intra_transition = None


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = dissolve


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = MoveTransition(0.5, enter=Transform(yalign=0.0, ypos=1.0), leave=Transform(yalign=1.0, ypos=0.0), enter_time_warp=_warper.ease)
define config.window_hide_transition = MoveTransition(0.5, enter=Transform(yalign=1.0, ypos=0.0), leave=Transform(yalign=0.0, ypos=1.0), leave_time_warp=_warper.ease)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

init python:
    preferences.text_cps = 240


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "catjam-1708301369"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.webp"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**/*.rpy', None)
    build.classify('game/debug.rpyc', None)
    build.classify('**/*.md', None)
    build.classify('tools/**', None)
    build.classify('**/*.xcf', None)
    build.classify('Makefile', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to perform in-app purchases. It can be
## found in the Google Play developer console, under "Monetize" > "Monetization
## Setup" > "Licensing".

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"

## Other Stuff #################################################################
init python:
    def replace_text(s):
        s = s.replace("'", '’')
        s = s.replace('--', '\u2014') # em dash
        s = s.replace('...', '\u2026') # ellipsis
        return s
    config.replace_text = replace_text

    def custom_text_tag_enclose(start, end):
        return lambda tag, _, contents: (
            [(renpy.TEXT_TEXT, start)]
            + contents
            + [(renpy.TEXT_TEXT, end)]
        )
    config.custom_text_tags = {
        "q": custom_text_tag_enclose("“", "”"),
        "sq": custom_text_tag_enclose("‘", "’"),
    }

    config.window_auto_hide.extend(["scene", "pause"])
    config.window_auto_hide.remove("menu")

    renpy.music.register_channel("bg", "sfx", loop=True)

    _dismiss_pause = False

    config.skip_delay = 100
