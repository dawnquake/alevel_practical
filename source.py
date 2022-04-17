import matplotlib.pyplot as plt
import numpy as np

def accuracy_vs_precision(precision,
                          accuracy,
                          title):
    
    plt.style.use('dark_background')
    
    precision_input = precision
    accuracy_input = accuracy
    
    if (float(precision_input) > 10
          or float(precision_input) < 1
          or float(accuracy_input) > 10
          or float(precision_input) < 1):
        raise ValueError('Input outside suggested range 1 to 10')
    else:
        pass
    
    precision_control = 1/(float(precision_input) + 1e-3)   ## Avoiding zeros
    accuracy_control = 1/(float(accuracy_input) + 1e-3)  ## Avoiding zeros

    x_true = [1, 2, 3, 4, 5]
    y_true = [2 ,4, 6, 8, 10]

    x_measure = np.array([])
    y_measure = np.array([])
    for value in x_true:
        x_measure = np.concatenate((x_measure,
                                    np.random.uniform(-precision_control,
                                                      precision_control,
                                                      100) 
                                                      + value 
                                                      + accuracy_control),
                                    axis=None)

    for value in y_true:
        y_measure = np.concatenate((y_measure,
                                    np.random.uniform(-precision_control,
                                                      precision_control,
                                                      100) 
                                                      + value 
                                                      + accuracy_control),
                                    axis=None)

    # plt.title('Accuracy ' + str(accuracy_control) + ' Precision ' + str(precision_control))
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.title(title)
    plt.scatter(x_measure, y_measure, label = 'Measured', color = 'b', marker = '+')
    plt.scatter(x_true, y_true, label = 'True', color = 'r', marker = 'x')
    plt.legend()
    plt.show()