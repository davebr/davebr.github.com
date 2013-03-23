from scene import Scene

class Throneroom(Scene):

    def enter(self):
        print "you are in the throne room"
        print "press any key to move back into the hall"

        raw_input("> ")

        return 'hall'
        


