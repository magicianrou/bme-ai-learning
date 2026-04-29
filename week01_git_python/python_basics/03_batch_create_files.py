from pathlib import Path


def main():
    script_dir = Path(__file__).resolve().parent
    # output_dir = Path("results/test_files")
    output_dir = script_dir / "results" / "test_files"
    output_dir.mkdir(parents=True, exist_ok=True)

    for i in range(1, 6):
        file_path = output_dir / f"sample_{i:03d}.txt"
        file_path.write_text(f"This is sample file {i}\n", encoding="utf-8")

    print("Created 5 sample files in:")
    print(output_dir)


if __name__ == "__main__":
    main()