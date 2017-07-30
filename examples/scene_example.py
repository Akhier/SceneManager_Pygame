import sys
sys.path.append("..")
import scenemanager
import pygame


class ExampleSceneA(scenemanager.SceneTemplate):
    def __init__(self, scenemanager):
        super().__init__(scenemanager)

    def on_update(self):
        pass

    def on_event(self, events):
        for event in events.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.scenemanager.quit_flag = True
                else:
                    self.scenemanager.change_scene(
                        ExampleSceneB(self.scenemanager))

    def on_render(self, screen):
        screen.fill((0, 0, 0))


class ExampleSceneB(scenemanager.SceneTemplate):
    def __init__(self, scenemanager):
        super().__init__(scenemanager)

    def on_update(self):
        pass

    def on_event(self, events):
        for event in events.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.scenemanager.quit_flag = True
                else:
                    self.scenemanager.change_scene(
                        ExampleSceneA(self.scenemanager))

    def on_render(self, screen):
        screen.fill((255, 0, 255))


if __name__ == '__main__':
    manager = scenemanager.SceneManager('SceneManagerSettings.json')
    manager.change_scene(ExampleSceneA(manager))
    manager.loop()
