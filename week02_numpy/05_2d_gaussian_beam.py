from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def create_2d_gaussian(size=256, sigma=0.25):
    x = np.linspace(-1, 1, size)
    y = np.linspace(-1, 1, size)

    xx, yy = np.meshgrid(x, y)

    gaussian = np.exp(-(xx ** 2 + yy ** 2) / (2 * sigma ** 2))

    return gaussian


def main():
    script_dir = Path(__file__).resolve().parent
    results_dir = script_dir / "results"
    results_dir.mkdir(parents=True, exist_ok=True)

    gaussian = create_2d_gaussian(size=256, sigma=0.25)

    print("Gaussian shape:")
    print(gaussian.shape)

    print("\nGaussian dtype:")
    print(gaussian.dtype)

    print("\nGaussian min:")
    print(np.min(gaussian))

    print("\nGaussian max:")
    print(np.max(gaussian))

    print("\nGaussian mean:")
    print(np.mean(gaussian))

    plt.imshow(gaussian, cmap="gray")
    plt.colorbar()
    plt.show()
    plt.title("2D Gaussian Beam")
    plt.savefig(results_dir / "gaussian_beam.png", dpi=300)
    plt.close()

    print("\nSaved image to:")
    print(results_dir / "gaussian_beam.png")


if __name__ == "__main__":
    main()