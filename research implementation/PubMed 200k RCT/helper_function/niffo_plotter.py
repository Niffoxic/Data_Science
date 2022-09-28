import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import itertools
import numpy as np
import warnings
warnings.filterwarnings("ignore")


def plot_histogram(data, bins=5, xlabel="", ylabel="", title="", figsize=(12, 6)):

    sns.set_style("darkgrid")
    matplotlib.rcParams["font.size"] = 14
    matplotlib.rcParams["figure.figsize"] = figsize

    plt.figure(facecolor="#F6F6F6")
    plt.axes().set_facecolor("#EEEEEE")

    plt.hist(data, bins=bins, color="#DD4A48")
    plt.xlabel(xlabel=xlabel)
    plt.ylabel(ylabel=ylabel)
    plt.title(title, weight="bold", fontname="monospace", fontsize=20)
    plt.show()


def plot_model_history_loss(history, figsize=(10, 6), model_name="Model"):
    """
    :param history:         model_history
    :param figsize:         size of the graph
    :param model_name:      model name to be added with the title
    :return:                Plots the loss of the model history
    """
    sns.set_style("darkgrid")
    matplotlib.rcParams["font.size"] = 14
    matplotlib.rcParams["figure.figsize"] = figsize

    plt.figure(facecolor="#F6F6F6")
    plt.axes().set_facecolor("#EEEEEE")

    loss = history.history["loss"]
    val_loss = history.history["val_loss"]

    length = len(history.history["loss"]) + 1
    epochs = range(1, length)

    plt.plot(epochs, loss, label="training_loss", color="#344CB7")
    plt.plot(epochs, val_loss, label="valid_loss", color="#DD4A48")
    title = model_name + " Loss Function Graph"
    plt.title(label=title, weight="bold", fontname="monospace", fontsize=20)
    plt.xlabel("Epochs")
    plt.ylabel("Loss")

    plt.xlim([1, length - 1])
    plt.xticks([i for i in range(1, length)])

    plt.legend(facecolor="#FAFAFA")
    plt.show()


def plot_model_history_accuracy(history, figsize=(10, 6), model_name="Model"):
    """
    :param history:         model_history
    :param figsize:         size of the graph
    :param model_name:      model name to be added with the title
    :return:                Plots the Accuracy of the model history
    """
    sns.set_style("darkgrid")
    matplotlib.rcParams["font.size"] = 14
    matplotlib.rcParams["figure.figsize"] = figsize

    plt.figure(facecolor="#F6F6F6")
    plt.axes().set_facecolor("#EEEEEE")

    acc = history.history["accuracy"]
    val_acc = history.history["val_accuracy"]

    length = len(history.history["accuracy"]) + 1
    epochs = range(1, length)

    plt.plot(epochs, acc, label="training_accuracy", color="#344CB7")
    plt.plot(epochs, val_acc, label="valid_accuracy", color="#DD4A48")
    title = model_name + " Accuracy Graph"
    plt.title(label=title, weight="bold", fontname="monospace", fontsize=20)
    plt.xlabel("Epochs")
    plt.ylabel("Loss")

    plt.xlim([1, length - 1])
    plt.xticks([i for i in range(1, length)])

    plt.legend(facecolor="#FAFAFA")
    plt.show()


def plot_confusion_matrix(y_true, y_predict, classes=None, figsize=(10, 10), text_size=15, norm=False,
                          fontsize=20):

    # Create the confusion matrix
    sns.set_style("whitegrid", {'axes.grid': False})
    cm = confusion_matrix(y_true, y_predict)
    cm_norm = cm.astype("float") / cm.sum(axis=1)[:, np.newaxis]
    n_classes = cm.shape[0]
    fig, ax = plt.subplots(figsize=figsize)
    cax = ax.matshow(cm, cmap="Reds")
    fig.colorbar(cax)

    if classes:
        labels = classes
    else:
        labels = np.arange(cm.shape[0])

    ax.set(title="Confusion Matrix",
           ylabel="True label",
           xlabel="Predicted label",
           xticks=np.arange(n_classes),
           yticks=np.arange(n_classes),
           xticklabels=labels,
           yticklabels=labels)

    ax.xaxis.set_label_position("bottom")
    ax.xaxis.tick_bottom()
    threshold = (cm.max() + cm.min()) / 2.

    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        if norm:
            plt.text(j, i, f"{cm[i, j]} ({cm_norm[i, j]*100:.1f}%)",
                     horizontalalignment="center",
                     color="white" if cm[i, j] > threshold else "black",
                     size=text_size)
        else:
            plt.text(j, i, f"{cm[i, j]}",
                     horizontalalignment="center",
                     color="white" if cm[i, j] > threshold else "black",
                     size=text_size)
