"""YOLOv8 Detection"""
from ultralytics import YOLO
import cv2

class FruitDetector:
    def __init__(self, model_path='models/best.pt'):
        """Load YOLOv8 model"""
        print("Loading model...")
        self.model = YOLO(model_path)
        print("Model loaded!")
    
    def detect(self, frame):
        """Detect fruits in image"""
        results = self.model(frame, conf=0.5, verbose=False)
        
        detections = []
        for result in results:
            boxes = result.boxes
            for box in boxes:
                cls_id = int(box.cls[0])
                conf = float(box.conf[0])
                bbox = box.xyxy[0].cpu().numpy()
                class_name = result.names[cls_id]
                
                detections.append({
                    'class': class_name,
                    'confidence': conf,
                    'bbox': bbox
                })
        
        return detections
    
    def draw_detections(self, frame, detections):
        """Draw boxes on image"""
        for det in detections:
            x1, y1, x2, y2 = det['bbox'].astype(int)
            label = f"{det['class']} {det['confidence']:.2f}"
            
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        return frame
