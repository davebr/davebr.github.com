from scene import Scene

class Armory(Scene):

    def enter(self):
        print "you are in the armory"
        print "press any key to move back into the hall"

        raw_input("> ")

        return 'hall'

       
    
