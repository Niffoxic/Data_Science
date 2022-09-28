from sklearn.metrics import accuracy_score, precision_recall_fscore_support


def calculate_result(y_true, y_predict):
    """

    :param y_true: True labels in the form of 1-D array
    :param y_predict: Predicted labels in the form of 1-D array
    :return: Dictionary of accuracy, precision, recall, f1-score
    """
    mp, mr, f1, _ = precision_recall_fscore_support(y_true, y_predict, average="weighted")
    return {"accuracy": accuracy_score(y_true, y_predict) * 100,
            "precision": mp,
            "recall": mr,
            "f1-score": f1}
