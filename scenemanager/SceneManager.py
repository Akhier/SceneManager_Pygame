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
        self.quit_flag = False
