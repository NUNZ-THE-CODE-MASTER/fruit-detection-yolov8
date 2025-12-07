"""Robot arm control - TEMPLATE"""
import time

class ArmController:
    def __init__(self):
        """Setup robot arm"""
        print("Connecting to robot arm...")
        # TODO: Add your robot initialization here
        print("Robot arm ready!")
    
    def move_to(self, position):
        """Move arm to position [x, y, z]"""
        print(f"Moving to: {position}")
        # TODO: Add real movement code here
        time.sleep(1)
    
    def open_gripper(self):
        """Open claw"""
        print("Opening gripper...")
        # TODO: Add gripper code here
        time.sleep(0.5)
    
    def close_gripper(self):
        """Close claw"""
        print("Closing gripper...")
        # TODO: Add gripper code here
        time.sleep(0.5)
    
    def pick_and_place(self, pick_pos, place_pos):
        """Pick from pick_pos, place at place_pos"""
        print(f"Picking from {pick_pos}")
        self.move_to(pick_pos)
        self.close_gripper()
        
        print(f"Placing at {place_pos}")
        self.move_to(place_pos)
        self.open_gripper()
        
        print("Done!")
