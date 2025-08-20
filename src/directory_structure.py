import configparser
import os

def load_config():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to the config file relative to the script's directory
    config_file = os.path.join(script_dir, '../config/settings.ini')
    
    # Check if the config file exists
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"The config file {config_file} does not exist.")
    
    # Load the configuration file
    config = configparser.ConfigParser()
    config.read(config_file)
    
    return config

def list_directory_contents(path):
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f'{indent}{os.path.basename(root)}/')
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            print(f'{sub_indent}{f}')

if __name__ == "__main__":
    try:
        # Call the load_config without any arguments
        config = load_config()
        
        # Get the parent directory from the config file
        parent_dir = config['Directories']['parent_dir']
        
        # List directory contents
        list_directory_contents(parent_dir)
        
    except KeyError as e:
        print(f"Configuration error: {e}")
    except FileNotFoundError as e:
        print(e)
