# import numpy as np

# def upsample_time_series(series, n, m):
#     assert m < n, "m should be less than n"
    
#     # Select m consecutive points randomly
#     start_index = np.random.randint(0, len(series) - m)
#     selected_points = series[start_index : start_index + m]

#     # Interpolate missing points
#     r = n - m
#     interpolated_points = np.interp(
#         np.linspace(0, m - 1, n), 
#         np.arange(m), 
#         selected_points
#     )

#     return interpolated_points

# # Example usage
# original_series = np.array([12, 16, 20, 14, 18, 22, 26])
# n = 12
# m = 4

# up_sampled_series = upsample_time_series(original_series, n, m)
# print("Original series:", original_series)
# print("Up-sampled series:", up_sampled_series)

import numpy as np

def upsample_time_series_dataset(dataset, n, m):
    assert m < n, "m should be less than n"
    
    upsampled_dataset = []
    
    for series in dataset:
        # Select m consecutive points randomly
        start_index = np.random.randint(0, len(series) - m)
        selected_points = series[start_index : start_index + m]

        # Interpolate missing points
        r = n - m
        interpolated_points = np.interp(
            np.linspace(0, m - 1, n), 
            np.arange(m), 
            selected_points
        )

        upsampled_dataset.append(interpolated_points)

    return np.array(upsampled_dataset)

# Example usage
original_dataset = np.array([[12, 16, 20, 14, 18, 22, 26],
                             [30, 35, 40, 45, 50, 55, 60]])
n = 12
m = 4

up_sampled_dataset = upsample_time_series_dataset(original_dataset, n, m)
print("Original dataset:")
print(original_dataset)
print("Up-sampled dataset:")
print(up_sampled_dataset)