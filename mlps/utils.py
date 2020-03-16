import pickle as pkl

def load_validation_set():
    fileObject = open('test_spectra.pkl', 'rb')
    Xtest = pkl.load(fileObject)
    fileObject.close()
    fileObject = open('test_labels.pkl', 'rb')
    ytest = pkl.load(fileObject)
    fileObject.close()
    return Xtest, ytest

def check_hit_rate(y_pred, y_true):
    '''
    Checks how the model has preformed comparing the predicted values against true labels
    Args:
        y_pred: An array of outputs one value per prediction - each value a float in range 0-1
        y_true: The true labels one per instance - binary 1 or 0
    Returns:
        Fraction of correct answers

    '''

    correct = 0
    for i, y in enumerate(y_pred):
        if round(y[0]) == y_true[i]:
            correct += 1
    return correct/len(y_pred)
