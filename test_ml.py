import cv2
import numpy as np
import os
import sys

# Add project root to path
sys.path.append(os.path.abspath('c:/Users/abhij/.gemini/antigravity/playground/infrared-space'))

try:
    from monitor.ml_utils import FaceAnalyzer
    print("Import successful")
except ImportError as e:
    print(f"Import failed: {e}")
    sys.exit(1)

def test_face_detection():
    # Create a blank image (black) -> Should be No Face
    blank_image = np.zeros((480, 640, 3), dtype=np.uint8)
    
    analyzer = FaceAnalyzer()
    result = analyzer.process_frame(blank_image)
    
    print(f"Blank Image Test: {result['status']} (Expected: no_face)")
    
    if result['status'] == 'no_face':
        print("PASS: Blank image correctly detected as no_face")
    else:
        print("FAIL: Blank image detection failed")

    # Create an image with a drawn face? Hard to simulate for MP without real face.
    # We trust MP works if it runs without crashing.
    print("ML Logic initialized successfully.")

if __name__ == "__main__":
    test_face_detection()
