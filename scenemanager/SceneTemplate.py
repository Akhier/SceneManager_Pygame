class SceneTemplate:
    """Template for what a scene needs to be

    All scenes must inherit this classes attributes to be
    used with the SceneManager
    """

    def __init__(self, scenemanager):
        self.scenemanager = scenemanager

    def on_update(self):
        raise NotImplementedError("on_update abstract method must be defined")

    def on_event(self, event):
        raise NotImplementedError("on_even abstract method must be defined")

    def on_render(self, screen):
        raise NotImplementedError("on_render abstract method must be defined")
