from collections import Counter
import matplotlib.pylab as plt
def sum_counters(counters):
    """Sums a list of counters."""
    return sum(counters, Counter())

def text_counters(text):
    """Counts the number of words in a text."""
    return Counter(text.split())

def plot_counter(counter):
    """Plots a counter."""
    plt.bar(counter.keys(), counter.values()) # define the x axis and y axis
    plt.xticks(rotation=90)
    plt.show()