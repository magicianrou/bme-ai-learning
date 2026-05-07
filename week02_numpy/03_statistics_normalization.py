import numpy as np


def min_max_normalize(data):
    data_min = np.min(data)
    data_max = np.max(data)

    normalized_data = (data - data_min) / (data_max - data_min)

    return normalized_data


def z_score_normalize(data):
    data_mean = np.mean(data)
    data_std = np.std(data)

    normalized_data = (data - data_mean) / data_std

    return normalized_data


def main():
    data = np.array([10, 12, 15, 20, 30, 100], dtype=np.float32)

    print("Original data:")
    print(data)

    print("\nMean:")
    print(np.mean(data))

    print("\nStandard deviation:")
    print(np.std(data))

    print("\nMinimum:")
    print(np.min(data))

    print("\nMaximum:")
    print(np.max(data))

    min_max_data = min_max_normalize(data)
    z_score_data = z_score_normalize(data)

    print("\nMin-max normalized data:")
    print(min_max_data)

    print("\nZ-score normalized data:")
    print(z_score_data)

    print("\nMean of z-score normalized data:")
    print(np.mean(z_score_data))

    print("\nStandard deviation of z-score normalized data:")
    print(np.std(z_score_data))


if __name__ == "__main__":
    main()