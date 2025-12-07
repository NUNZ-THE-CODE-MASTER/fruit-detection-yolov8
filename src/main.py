"""Main program"""
import cv2
from src.fruit_detector import FruitDetector
from src.color_detector import ColorSorter
from src.arm_controller import ArmController

class FruitSortingRobot:
    def __init__(self):
        """Start everything"""
        print("="*50)
        print("Starting Fruit Sorting Robot...")
        print("="*50)
        
        self.detector = FruitDetector()
        self.sorter = ColorSorter()
        self.arm = ArmController()
        
        self.camera = cv2.VideoCapture(0)
        print("All systems ready!")
    
    def run(self):
        """Run detection"""
        print("\nPress 'q' to quit, 's' to sort")
        
        while True:
            ret, frame = self.camera.read()
            if not ret:
                break
            
            detections = self.detector.detect(frame)
            annotated = self.detector.draw_detections(frame, detections)
            
            cv2.imshow('Fruit Detection', annotated)
            
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('s') and len(detections) > 0:
                self.sort_fruit(detections[0])
        
        self.camera.release()
        cv2.destroyAllWindows()
    
    def sort_fruit(self, detection):
        """Sort one fruit"""
        fruit_name = detection['class']
        print(f"\nSorting: {fruit_name}")
        
        bin_pos, color = self.sorter.get_sorting_bin(fruit_name)
        pick_pos = self.sorter.get_detection_position()
        
        self.arm.pick_and_place(pick_pos, bin_pos)
        print(f"✓ {fruit_name} sorted!")

def main():
    robot = FruitSortingRobot()
    robot.run()

if __name__ == "__main__":
    main()
