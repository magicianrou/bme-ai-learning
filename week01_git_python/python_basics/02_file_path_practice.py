from pathlib import Path

def main():
    project_root = Path.cwd()
    data_dir = project_root / "data"
    results_dir = project_root / "results"

    data_dir.mkdir(exist_ok=True)
    results_dir.mkdir(exist_ok=True)

    print("Current working directory: ", project_root)

    print("data_dir: ", data_dir)

    print("Results directory: ", results_dir)

if __name__ == "__main__":
    main()