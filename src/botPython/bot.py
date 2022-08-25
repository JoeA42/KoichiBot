# Change this file and add here the code for your bot.
# "Main" python file for bot code

class Bot(bType):
    def __init__(self):
        self.botType = bType


class DesktopBot(Bot):
    pass

    def action(self, execution):
        # using browse from browser module
        self.browse(...)
        # using find from display module
        self.find(...)
        # using mouse_move from mouse module
        self.mouse_move(x=100, y=200)
        # using enter from keyboard module
        self.enter()


class WebBot(Bot):
    pass

    def __init__(self):
        super().__init__()
        self.headless = None

    def action(self, execution):
        # Configure whether to run on headless mode
        self.headless = False

        # using browse from browser module
        self.browse(...)
        # using find from display module
        self.find(...)
        # using mouse_move from mouse module
        self.mouse_move(x=100, y=200)
        # using enter from keyboard module
        self.enter()

        # Stop the browser and clean up
        self.stop_browser()
