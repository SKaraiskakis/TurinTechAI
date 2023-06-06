import numpy as np

def interleave_time_series(data):
    new_data = []
    for i in range(len(data) - 1):
        current_point = data[i]
        next_point = data[i + 1]
        
        # Append current_point to new_data
        new_data.append(current_point)

        # Calculate and append the average of current_point and next_point to new_data
        average_point = (current_point + next_point) / 2
        new_data.append(average_point)
        
    # Add the last data point to the new_data
    new_data.append(data[-1])
    
    return np.array(new_data)

# An example usage with a sample dataset
data = np.array([10, 20, 30, 40, 50])
interleaved_data = interleave_time_series(data)
print(interleaved_data)



try:
    import rpy2
    print("rpy2 is installed")
except ImportError:
    print("rpy2 is not installed")