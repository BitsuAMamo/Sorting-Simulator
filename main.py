# Imports

import pygame
import random
from typing import List
from pygame.time import Clock, delay
from threading import Thread

# CONSTANTS

# Colors
WHITE = (255, 255, 255)
PURPLE = (255, 0, 255)
BLACK = (0, 0, 0)
EMPTY = (0,0,0,0)
COLOR_ARRAY = [(122,145,123), (255,67,89), (234,123,45), (34,67,25), (67,56,78)]

# Pygame constants
FPS = 144
WIDTH = 1280
HEIGHT = 300

class Visualizer:


    def __init__(self, win: pygame.Surface, max_height, num_elements, delay=50, color_array = COLOR_ARRAY):
        self.array:List = [int(random.random() * max_height) for i in range(num_elements)]
        self.window:pygame.Surface = win
        self.height = self.window.get_height()
        self.width = self.window.get_width()
        self.scale_w = self.width/len(self.array)
        self.scale_h = self.height/max(*self.array)
        self.delay = delay
        self.color_array = color_array


    def draw_element(self, index, color):
        item_height = self.array[index] * self.scale_h
        item_width = self.scale_w
        item_rect = pygame.Rect(index * item_width, self.height - item_height, item_width, item_height)
        pygame.draw.rect(self.window, color, item_rect)


    def draw_array(self, index = -1):
        self.window.fill(EMPTY)
        self.draw_bg(BLACK)
        for i in range(len(self.array)):
            if index == i:
                color = PURPLE
            else:
                color = self.color_array[(i % len(self.color_array)) - 1]
            self.draw_element(i, color)


    # Overlaoded array for the quck sort
    # TODO: Find better way to implement it. Kaleab says so!!
    def draw_array(self, low = -1, high = -1):
        self.window.fill(EMPTY)
        self.draw_bg(BLACK)
        for i in range(len(self.array)):
            if i in range(low, high + 1):#low == i or high == i:
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
    def bubble_iterate(self, target_index):
        if target_index == 0:
            return False

        cur = self.array[target_index]
        prev = self.array[target_index -1]

        if  cur < prev:
            self.array[target_index - 1] = cur
            self.array[target_index] = prev
            return True
        return False

    def bubble_sort_visualize(self):
        target_index = 0

        while(target_index != len(self.array)):
            iterate = self.bubble_iterate(target_index)
            # Draw the list first to initialize the screen
            self.draw_array()
            while (iterate):
                # Update the targegt index to check for the other values
                target_index -= 1
                iterate = self.bubble_iterate(target_index)
                # Draw the list again to show progress of current index
                self.draw_array(target_index - 1)
                delay(self.delay)

            target_index +=1


    def partition(self, low, high):
        i = (low-1)         # index of smaller element
        pivot = self.array[high]     # pivot

        for j in range(low, high):

            # If current element is smaller than or
            # equal to pivot
            if self.array[j] <= pivot:

                # increment index of smaller element
                i = i+1
                self.array[i], self.array[j] = self.array[j], self.array[i]

        self.array[i+1], self.array[high] = self.array[high], self.array[i+1]
        return (i+1)



    def quick_sort(self, low = 0, high = 99):

        if len(self.array) == 1:
            return self.array
        if low < high:

            # pi is partitioning index, self.array[p] is now
            # at right place
            pi = self.partition(low,high)

            # Separately sort elements before
            # partition and after partition
            # self.draw_array()
            self.draw_array()
            self.quickSort(low, pi-1)
            self.draw_array(low, high)
            self.quickSort(pi+1, high)
            self.draw_array(low, high)
            delay(self.delay)
        print(self.array)


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
            pygame.display.update()

    def get_color(self):
        return WHITE


if __name__ == '__main__':
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    vis = Visualizer(win, 35, 100, 250)
    vis.visualize(vis.quick_sort)
    delay(5000)
