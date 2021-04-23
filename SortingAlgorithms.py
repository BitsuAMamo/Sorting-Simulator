#TODO: this is for all the different algorithms. If possible I have to create a new draw array 
# For most. Also Some clean up work is required.
# Imports 
from Visulaizer import Visualizer
from pygame.time import Clock, delay
import pygame

# Constants
COLOR_ARRAY = [(122, 145, 123), (255, 67, 89),
               (234, 123, 45), (34, 67, 25), (67, 56, 78)]


class SortingAlgorithms(Visualizer):
    def __init__(self, win: pygame.Surface, max_height, num_elements, delay=50, color_array=COLOR_ARRAY):
        super(SortingAlgorithms, self).__init__(
            win, max_height, num_elements, delay, color_array)

    def bubble_iterate(self, target_index):
        if target_index == 0:
            return False

        cur = self.array[target_index]
        prev = self.array[target_index - 1]

        if cur < prev:
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

            target_index += 1

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

    def quick_sort(self, low=0, high=99):

        if len(self.array) == 1:
            return self.array
        if low < high:

            # pi is partitioning index, self.array[p] is now
            # at right place
            pi = self.partition(low, high)

            # Separately sort elements before
            # partition and after partition
            # self.draw_array()
            self.quick_sort(low, pi-1)
            self.quick_sort(pi+1, high)
            self.draw_array()
            delay(self.delay)
        print(self.array)
