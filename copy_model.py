import cv2
import shutil
import os

source = os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_default.xml')
dest_dir = 'monitor/ml_models'
dest = os.path.join(dest_dir, 'haarcascade_frontalface_default.xml')

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

try:
    shutil.copy(source, dest)
    print(f"Successfully copied model to {dest}")
except Exception as e:
    print(f"Error copying model: {e}")
