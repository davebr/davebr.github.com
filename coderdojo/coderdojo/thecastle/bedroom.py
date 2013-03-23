from scene import Scene

class Bedroom(Scene):

    def enter(self):
        print "you are in the bedroom"
        print "press any key to move back into the hall"

        raw_input("> ")

        return 'hall'


