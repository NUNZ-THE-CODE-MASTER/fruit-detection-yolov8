"""Helper functions"""
import yaml

def load_config(config_file):
    """Load YAML configuration"""
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)

def get_fruit_color(fruit_name, config):
    """Get color for a fruit"""
    return config['fruit_colors'].get(fruit_name, 'red')

def get_bin_position(color, config):
    """Get bin coordinates"""
    bin_number = config['color_bins'].get(color, 0)
    return config['bin_positions'][bin_number]

def load_classes(classes_file='models/classes.txt'):
    """Load class names"""
    with open(classes_file, 'r') as f:
        return [line.strip() for line in f.readlines()]
