import pygame
import json


class SceneManager:
    """Represents the main game and contains the game loop

    It must be used with Scene objects that inherit from SceneTemplate
    """

    def __init__(self, settingsfile):
        with open(settingsfile) as json_data:
            settings = json.load(json_data)
        resolution = (settings['screen_width'], settings['screen_height'])
        self.screen = pygame.display.set_mode((resolution))
        pygame.display.set_caption(settings['caption'])
        key_repeat = settings['key_repeat']
        if key_repeat:
            pygame.key.set_repeat(key_repeat[0], key_repeat[1])
        self.clock = pygame.time.Clock()
        self.fps = settings['fps']
        self.quit_flag = False

    def loop(self):
        while not self.quit_flag:
            self.clock.tick(self.fps)
            self.scene.on_event(pygame.event)
            self.scene.on_update()
            self.scene.on_render(self.screen)
            pygame.display.flip()

    def change_scene(self, scene):
        self.scene = scene
