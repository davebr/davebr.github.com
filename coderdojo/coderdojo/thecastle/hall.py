from scene import Scene

class Hall(Scene):

    def enter(self):
        print "You enter the Hall There are 4 doors around you, pick an number between 1 and 4 to explore the room"
        action = raw_input("> ")

        if action == "1":
            return 'kitchen'

        elif action == "2":
            return 'armory'

        elif action == "3":
            return 'throneroom'

        elif action == "4":
            return 'bedroom'

        else:
            print "DOES NOT COMPUTE!"
            return 'hall'

