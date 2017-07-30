import pygame
import json


class SceneManager:
    """
    """

    def __init__(self):
        with open("SceneManagerSettings.json") as json_data:
            settings = json.load(json_data)
        resolution = (settings['screen_width'], settings['screen_height'])
        self.screen = pygame.display.set_mode((resolution))
        pygame.display.set_caption(settings['caption'])
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
