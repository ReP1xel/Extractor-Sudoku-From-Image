import cv2
import sys
from time import time
import matplotlib.pyplot as plt
from SudokuExtractor import extract_sudoku

def show_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image)
    plt.show()

def main(image_path):
    image = extract_sudoku(image_path)
    show_image(image)
        

if __name__ == '__main__':
    image_path = 'sudoku.jpg'
    main(image_path)