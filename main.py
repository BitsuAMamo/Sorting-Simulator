# Imports 
from SortingAlgorithms import SortingAlgorithms
import pygame

# Constants
WIDTH = 1280
HEIGHT = 300


if __name__ == '__main__':
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    # vis = Visualizer(win, 35, 100 , 100)
    # vis.visualize(vis.bubble_sort)
    vis = SortingAlgorithms(win, 35, 100, 0)
    vis.visualize(vis.bubble_sort_visualize)
    pygame.time.delay(2000)
