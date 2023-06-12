# import numpy as np

# def interpolate_time_series_augmentation(T, RandomIndexing, R):
#     n = len(T)
#     L = n
    
#     X = np.arange(n)
#     X_star = np.linspace(0, n - 1, num=L * R - R + 1)
#     Interpolator = np.interp(X_star, X, T)
#     T_star = Interpolator
#     T_hat = np.zeros(L)
    
#     for i in range(L):
#         if not RandomIndexing:
#             K = np.random.randint(0, R)
#             T_hat[i] = T_star[i * R + K]
#         else:
#             K_star = np.random.randint(0, R)
#             T_hat[i] = T_star[i * R + K_star]

#     return T_hat

# # Example usage
# time_series = np.array([12, 16, 20, 14, 18, 22, 26])
# RandomIndexing = True
# R = 3

# synthetic_time_series = interpolate_time_series_augmentation(time_series, RandomIndexing, R)

# print("Original Time Series:", time_series)
# print("Synthetic Time Series:", synthetic_time_series)
import numpy as np

def interpolate_time_series_augmentation(T, RandomIndexing, R):
    n = len(T)
    L = n // R  # Length of synthetic time series
    T_hat = np.zeros(L)
    
    X = np.arange(1, n + 1)
    X_star = np.linspace(1, n, num=L * R - R + 1)
    Interpolator = np.interp(X_star, X, T)
    T_star = Interpolator
    
    K = np.random.randint(1, R)
    
    for i in range(L):
        if not RandomIndexing:
            T_hat[i] = T_star[i * R + K - 1]
        else:
            K_star = np.random.randint(1, R)
            T_hat[i] = T_star[i * R + K_star - 1]

    return T_hat

# Example usage
time_series = np.array([12, 16, 20, 14, 18, 22, 26])
RandomIndexing = True
R = 3

synthetic_time_series = interpolate_time_series_augmentation(time_series, RandomIndexing, R)

print("Original Time Series:", time_series)
print("Synthetic Time Series:", synthetic_time_series)