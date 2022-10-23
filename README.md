# Plugin System
Plugin System is a simple program used to show how to dynamically add modules to your Python project.

# Installation
Simply clone the repo and run the following command to install the requirements
```bash
pip install -r requirements.txt
```

Open `config.toml` to set the plugin path

Execute with the following command
```
python3 main.py
```

### Example Output

```
Plugin System starting...
Loading plugins from: plugins
Loading plugin: one
Imported module: <module 'one' from '/Users/cargabright/Dev/python/python-plugin-starter/plugins/one.py'>
Plugin one initialised
Plugin one args:  ('Hello', 'World') {'option1': 1, 'option2': 'Options are good'}
Executing plugin one
Loading plugin: two
Imported module: <module 'two' from '/Users/cargabright/Dev/python/python-plugin-starter/plugins/two.py'>
Plugin two initialised
Plugin two args:  ('Hello', 'World') {'option1': 1, 'option2': 'Options are good'}
Executing plugin two
Finished successfully!
```

## License
[MIT](https://choosealicense.com/licenses/mit/)