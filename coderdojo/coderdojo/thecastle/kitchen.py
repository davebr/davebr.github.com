from scene import Scene

class Kitchen(Scene):

    def enter(self):
        print "you are in the kitchen"
        print "press any key to move back into the hall"

        raw_input("> ")

        return 'hall'

