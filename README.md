# Univerzal configurable discord bot

## Basic Setup
1. Create a file named `SECRET`
2. Paste discord bot token into the SECRET file
3. Run `main.py` and enjoy!

## Adding Modules
1. Create a python file that you can import from the `univerzal/` directory. In that file, subclass `unz_modules.UnzBaseModule` and override the `name` static variable; override methods like `check_data`, `event_on_message`, etc. to implement functionality (check out existing modules for examples).
2. Regsiter your new module in `module_registry.py` by adding `reg.autoregister(<module class>)` lines in `get_default_registry`
3. Enable your new module by adding its name to `LOADED_MODULES` in `settings.py`
