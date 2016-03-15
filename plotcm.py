#print(__doc__)

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

def plot_confusion_matrix(cm,channels, title='Confusion matrix', cmap=plt.cm.Blues,filename="confusion_matrix.png"):
    #plt.figure()
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(channels))
    plt.xticks(tick_marks, channels, rotation=45,ha='right')
    plt.yticks(tick_marks, channels)
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.savefig(filename)
    plt.show()