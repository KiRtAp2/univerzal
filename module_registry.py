import unz_modules


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
    return reg
