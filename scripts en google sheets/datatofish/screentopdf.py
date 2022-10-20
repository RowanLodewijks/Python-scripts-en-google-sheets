import pyautogui
from PIL import Image
import os

my_screenshot = pyautogui.screenshot()
screenshot_path = r'C:\Users\lodew\OneDrive\Pictures\test\screenshot_1.png'
my_screenshot.save(screenshot_path)

image_1 = Image.open(screenshot_path)
im_1 = image_1.convert('RGB')
pdf_path = r'C:\Users\lodew\OneDrive\Pictures\test\pdf_1.pdf'
im_1.save(pdf_path)

os.remove(screenshot_path)