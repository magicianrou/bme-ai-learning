from pathlib import Path

def main():
    # input_file = Path("results/test_files/sample_001.txt")
    script_dir = Path(__file__).resolve().parent
    input_file = script_dir / "results" / "test_files" / "sample_001.txt"

    # if not input_file.exists():
    #     print("File does not exist. Please run 03_batch_create_files.py first.")
    #     return

    content = input_file.read_text(encoding="utf-8")

    output_file = Path("results/read_result.txt")
    output_file.write_text(
        "The content of sample001.txt is:\n" + content,
        encoding="utf-8"
    )

    print("Read content:", content)

    print("Saved result to:", output_file)

if __name__ == "__main__":
    main()

