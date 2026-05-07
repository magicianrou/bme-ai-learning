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
    spectrum = np.array([120, 135, 160, 210, 400, 380, 250, 180, 150], dtype=np.float32)
    print("Original spectrum: ", spectrum)
    print("Shape:" , spectrum.shape)
    print("Dtype:", spectrum.dtype)
    print("Mean:", spectrum.mean())
    print("Std:", spectrum.std())
    print("Min:", spectrum.min())
    print("Max:", spectrum.max())
    print("Min and Max after Min-Max normalized:", min_max_normalize(spectrum).min(),min_max_normalize(spectrum).max())
    print("Mean and Std after Z-Score normalized:", z_score_normalize(spectrum).mean(), z_score_normalize(spectrum).std())

if __name__ == "__main__":
    main()

