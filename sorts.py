import matplotlib.pyplot as plt
import numpy as np

def bubble_sort(title):
    data = np.random.rand(50)
    _, ax = plt.subplots()
    ax.set_title(title)
    bars = ax.bar(range(len(data)), data)

    for i in range(len(data)):
        for j in range(len(data) - i - 1):

            bars[j].set_color('r')
            bars[j + 1].set_color('r')
            if data[j] > data[j + 1]:

                data[j], data[j + 1] = data[j + 1], data[j]

                bars[j].set_height(data[j])
                bars[j + 1].set_height(data[j + 1])

            plt.pause(0.001)

            bars[j].set_color('tab:blue')
            bars[j + 1].set_color('tab:blue')

    plt.show()


def quick_sort(title):
    data = np.random.rand(50)
    _, ax = plt.subplots()
    ax.set_title(title)

    def s(data, low, high):
        if low < high:
            pivot_index = partition(data, low, high)
            s(data, low, pivot_index - 1)
            s(data, pivot_index + 1, high)

        ax.clear()
        ax.bar(range(len(data)), data)

        for i in range(low, high + 1):
            ax.bar(i, data[i], color = 'r')

        plt.show(block = False)
        plt.pause(0.001)

    def partition(data, low, high):
        pivot = data[high]
        i = low
        for j in range(low, high):
            if data[j] < pivot:
                data[i], data[j] = data[j], data[i]
                i += 1
        data[i], data[high] = data[high], data[i]
        return i

    s(data, 0, len(data) - 1)

    ax.clear()
    ax.bar(range(len(data)), data)

    plt.show()

def selection_sort(title):
    data = np.random.rand(50)
    _, ax = plt.subplots()  
    ax.set_title(title)

    for i in range(len(data)):
        min_index = i

        for j in range(i+1, len(data)):
            if data[j] < data[min_index]:
                min_index = j

        data[i], data[min_index] = data[min_index], data[i]

        plt.bar(range(len(data)), data)

        plt.bar(i, data[i], color = 'r')

        plt.show(block = False)
        plt.pause(0.001)
        plt.clf()

    plt.bar(range(len(data)), data)
    plt.show()

def heap_sort(title):
    data = np.random.rand(50)
    _, ax = plt.subplots()  
    ax.set_title(title)

    def visualize(arr, i, j, color):
        plt.clf()
        plt.bar(range(len(arr)), arr, color = color)
        plt.bar(i, arr[i], color='r')
        plt.bar(j, arr[j], color='g')
        plt.draw()
        plt.pause(0.001)

    def heapify(arr, n, i):
        largest = i 
        l = 2 * i + 1 
        r = 2 * i + 2 

        if l < n and arr[l] > arr[largest]:
            largest = l

        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i] 
            visualize(arr, i, largest, 'b') 
            heapify(arr, n, largest) 

    n = len(data)

    for i in range(n, -1, -1):
        heapify(data, n, i)

    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        visualize(data, 0, i, 'b')
        heapify(data, i, 0)

    visualize(data, 0, 0, 'b')