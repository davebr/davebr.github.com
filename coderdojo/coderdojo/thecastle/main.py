from sys import exit
from random import randint

from armory import Armory
from hall import Hall
from kitchen import Kitchen
from bedroom import Bedroom
from throneroom import Throneroom
from scene import Scene

class Death(Scene):
    quips = [
        "You died",
        "A giant block falls from the ceiling",
        "A duck wanders out and eats you",
        "You fall down a hole and can't get out"    
    ]

    def enter(self):
        print Death.quips[randing(0, len(self.quips) - 1)]
        exit(1)

class Map(object):
    scenes = {
        'armory': Armory(),
        'hall': Hall(),
        'kitchen': Kitchen(),
        'throneroom': Throneroom(),
        'bedroom': Bedroom()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n------------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


a_map = Map('hall')
a_game = Engine(a_map)
a_game.play()
