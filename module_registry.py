import unz_modules
import games


class UnzModuleRegistry:
    def __init__(self):
        self.registered = {}

    def register(self, name, module_class):
        if name in self.registered:
            raise ValueError(f"Name already registered: {name}")
        self.registered[name] = module_class

    def autoregister(self, module_class):
        # register with module_class' `name` attribute
        self.register(module_class.name, module_class)

    def get_module(self, name):
        if name not in self.registered:
            raise ValueError(f"No module with name {name} registered")
        return self.registered[name]


def get_default_registry():
    reg = UnzModuleRegistry()
    reg.autoregister(unz_modules.UnzDebugModule)
    reg.autoregister(unz_modules.UnzControlModule)
    reg.autoregister(unz_modules.UnzQuitModule)
    reg.autoregister(unz_modules.UnzMessageModule)
    reg.autoregister(unz_modules.UnzWordsModule)
    reg.autoregister(unz_modules.UnzAutoreplyModule)
    reg.autoregister(unz_modules.UnzAutomessageModule)
    reg.autoregister(games.RPSModule)
    reg.autoregister(unz_modules.audio.UnzAudioModule)
    return reg
