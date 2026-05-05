from pathlib import Path

def main():
    script_dir = Path(__file__).resolve().parent
    output_dir = script_dir / "results" / "experiment_log"
    output_dir.mkdir(parents=True, exist_ok=True)

    experiment = {
        "experiment_name": "Raman Denoising Test",
        "method": "low-rank constraint",
        "snr_values": [12.5, 15.2, 18.7, 20.1],
        "accuracy_values": [0.72, 0.78, 0.83, 0.86]
    }

    mean_snr = mmax(experiment["snr_values"])
    max_snr = mmax(experiment["snr_values"])
    mean_accuracy = mmax(experiment["accuracy_values"])
    max_accuracy = mmax(experiment["accuracy_values"])

    with open(output_dir / "latest_report.txt", "w") as f:
        f.write("mean_snr is : " + str(mean_snr) + "\n")
        f.write("max_snr is : " + str(max_snr) + "\n")
        f.write("mean_accuracy is : " + str(mean_accuracy) + "\n")
        f.write("max_accuracy is : " + str(max_accuracy) + "\n")

    with open(output_dir / "history_log.txt", "a") as f:
        f.write(str(experiment))


def mmean(numbers):
    return sum(numbers) / len(numbers)

def mmax(numbers):
    return max(numbers)

if __name__ == "__main__":
    main()