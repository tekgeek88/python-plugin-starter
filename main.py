import importlib
from pathlib import Path
import sys
import toml
# pyinstaller --onefile main.py -n PluginSystem

from utils.plugin_utils import get_plugins

def main(config):
    # Get plugin path and append it to the system path
    plugin_path = Path(config.get('plugin_path'))
    sys.path.append(str(plugin_path))

    print(f"Loading plugins from: {plugin_path}")
    plugins = get_plugins(plugin_path)

    for p in plugins:
        # Import plugin
        print(f"Loading plugin: {p}")
        plugin_module = importlib.import_module(p, ".")
        print(f"Imported module: {plugin_module}")
        plugin = plugin_module.Plugin("Hello", "World", option1=1, option2="Options are good")
        plugin.execute()

    # If main completes without error return program success
    return True

if __name__ == '__main__':
    print('Plugin System starting...')

    # Get app config
    config = toml.load('config.toml')
    try:
        # Run main function
        if main(config):
            print('Finished successfully!')
        else:
            print('Failed to finish successfully!')
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print("Failed to finish successfully due to uncaught exception!")



