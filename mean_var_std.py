import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')

    arr = np.array(list)
    arr.shape = (3,3)
    mast_dict = {}

    mean_axis0 = np.mean(arr, axis=0)
    mean_axis1 = np.mean(arr, axis=1)
    mean_axis = np.mean(arr)
    mean_values = {'mean': [mean_axis0.tolist(), mean_axis1.tolist(), mean_axis]}
    mast_dict.update(mean_values)

    var_axis0 = np.var(arr, axis=0)
    var_axis1 = np.var(arr, axis=1)
    var_axis = np.var(arr)
    var_values = {'variance': [var_axis0.tolist(), var_axis1.tolist(), var_axis]}
    mast_dict.update(var_values)

    std_axis0 = np.std(arr, axis=0)
    std_axis1 = np.std(arr, axis=1)
    std_axis = np.std(arr)
    std_values = {'standard deviation': [std_axis0.tolist(), std_axis1.tolist(), std_axis]}
    mast_dict.update(std_values)

    amax_axis0 = np.amax(arr, axis=0)
    amax_axis1 = np.amax(arr, axis=1)
    amax_axis = np.amax(arr)
    amax_values = {'max': [amax_axis0.tolist(), amax_axis1.tolist(), amax_axis]}
    mast_dict.update(amax_values)

    amin_axis0 = np.amin(arr, axis=0)
    amin_axis1 = np.amin(arr, axis=1)
    amin_axis = np.amin(arr)
    amin_values = {'min': [amin_axis0.tolist(), amin_axis1.tolist(), amin_axis]}
    mast_dict.update(amin_values)

    sum_axis0 = np.sum(arr, axis=0)
    sum_axis1 = np.sum(arr, axis=1)
    sum_axis = np.sum(arr)
    sum_values = {'sum': [sum_axis0.tolist(), sum_axis1.tolist(), sum_axis]}
    mast_dict.update(sum_values)

    calculations = mast_dict
    return calculations