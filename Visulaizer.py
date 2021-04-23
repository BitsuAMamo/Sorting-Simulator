# TODO: A bit of clean up work
# Imports 
import pygame
import random
from typing import List
from pygame.time import Clock, delay
from threading import Thread, Lock

# CONSTANTS
# Colors
WHITE = (255, 255, 255)
PURPLE = (255, 0, 255)
BLACK = (0, 0, 0)
EMPTY = (0, 0, 0, 0)

# Pygame constants
FPS = 144



class Visualizer:
    def __init__(self, win: pygame.Surface, max_height, num_elements, delay, color_array):
        self.array: List = [int(random.random() * max_height)
                            for i in range(num_elements)]
        self.window: pygame.Surface = win
        self.height = self.window.get_height()
        self.width = self.window.get_width()
        self.scale_w = self.width/len(self.array)
        self.scale_h = self.height/max(*self.array)
        self.delay = delay
        self.color_array = color_array
        self.update_lock = Lock()

    def draw_element(self, index, color):
        item_height = self.array[index] * self.scale_h
        item_width = self.scale_w
        item_rect = pygame.Rect(
            index * item_width, self.height - item_height, item_width, item_height)
        pygame.draw.rect(self.window, color, item_rect)

    def draw_array(self, index=-1):
        with self.update_lock:
            self.window.fill(EMPTY)
            self.draw_bg(BLACK)
            for i in range(len(self.array)):
                if index == i:
                    color = PURPLE
                else:
                    color = self.color_array[(i % len(self.color_array)) - 1]
                self.draw_element(i, color)

    # Fuction to draw background
    def draw_bg(self, bg_color):
        self.window.fill(bg_color)

    # TODO: Has a werid bug that the other one doesn't but basically does the same thing
    # The bug is interesting though

    def bubble_sort(self):
        for i in range(len(self.array) - 1):
            for j in range(len(self.array) - 1):
                if self.array[j] > self.array[i]:
                    self.array[j], self.array[i] = self.array[i], self.array[j]
                    self.draw_array(j)
                    delay(self.delay)

    # Function that check the value beween a given index and the one to the left
    # and swaps the values if the check is true

    def visualize(self, func):
        self.run = True
        thread = Thread(target=self.update, daemon=True)
        thread.start()
        self.draw_array()
        func()
        self.run = False
        thread.join()

    def update(self):
        while self.run:
            # self.draw_array()
            with self.update_lock:
                pygame.display.update()
            delay(int(1000/FPS))

    def get_color(self):
        return WHITE
