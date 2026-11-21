# web app
import webview

# other
from pathlib import Path

# custom
import logger
import database_handler as dh

SRC = Path(__file__).resolve().parents[3]

# Ends the program and leaves a log. Anything else in the future should be written here.
def end_program():
    logger.log("Ending program. Thank you for playing!")

if __name__ == "__main__":
    window = webview.create_window("Fox Adventures","./../front_end/main_menu.html")
    # to connect events to webview, type : window.events.event += on_event <- this is a function
    webview.start(debug=True) #TODO : remove debug or set to false if not debugging
    logger.log("Game booted...")
    # wait for front-end
    logger.log("Have fun!")