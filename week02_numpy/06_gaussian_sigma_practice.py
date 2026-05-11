from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def create_2d_gaussian(size=256, sigma=0.25):
    x = np.linspace(-1, 1, size)
    y = np.linspace(-1, 1, size)

    xx, yy = np.meshgrid(x, y)

    gaussian = np.exp(-(xx ** 2 + yy ** 2) / (2 * sigma ** 2))

    return gaussian


def save_image(image, output_path, title):
    plt.imshow(image, cmap="gray")
    plt.colorbar()
    plt.title(title)
    plt.savefig(output_path, dpi=300)
    plt.close()


def main():
    script_dir = Path(__file__).resolve().parent
    results_dir = script_dir / "results" / "gaussian_sigma"
    results_dir.mkdir(parents=True, exist_ok=True)

    sigmas = [0.15, 0.25, 0.40]

    for sigma in sigmas:
        gaussian = create_2d_gaussian(size=256, sigma=sigma)

        print("\nSigma:")
        print(sigma)

        print("Shape:")
        print(gaussian.shape)

        # TODO: print min, max, mean, std

        print("Min:")
        print(gaussian.min())

        print("Max:")
        print(gaussian.max())

        print("Mean:")
        print(gaussian.mean())

        print("Standard Deviation:")
        print(gaussian.std())

        output_path = results_dir / f"gaussian_sigma_{sigma:.2f}.png"
        title = f"2D Gaussian Beam, sigma={sigma:.2f}"

        save_image(gaussian, output_path, title)

        print("Saved to:")
        print(output_path)


if __name__ == "__main__":
    main()