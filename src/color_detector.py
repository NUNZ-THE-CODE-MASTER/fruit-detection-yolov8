"""Color sorting logic"""
from src.utils import load_config, get_fruit_color, get_bin_position

class ColorSorter:
    def __init__(self, config_path='config/color_mapping.yaml'):
        """Load color configuration"""
        self.config = load_config(config_path)
        print("Color sorter ready!")
    
    def get_sorting_bin(self, fruit_name):
        """Find which bin for this fruit"""
        color = get_fruit_color(fruit_name, self.config)
        bin_position = get_bin_position(color, self.config)
        
        print(f"{fruit_name} -> {color} bin at {bin_position}")
        return bin_position, color
    
    def get_detection_position(self):
        """Get starting position"""
        return self.config['detection_position']
