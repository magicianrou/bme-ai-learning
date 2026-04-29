from pathlib import Path

def main():

    script_dir = Path(__file__).resolve().parent
    student_score_report = script_dir / "results"
    student_score_report.mkdir(parents=True, exist_ok=True)

    student = {
        "name" : "Lou Xinhang",
        "major" : "Biomedical Engineering",
        "scores" : [91, 92, 93, 94, 95]
    }

    meanscore = mean_score(student["scores"])
    maxscore = max_score(student["scores"])
    minscore = min_score(student["scores"])

    output_file = script_dir / "results" / "student_score_report.txt"
    output_file.write_text("")

    with output_file.open("a", encoding="utf-8") as f:

        f.write("The student's name is "+student["name"]+".\n")
        f.write("The student's major is "+student["major"]+".\n")

        for index, score in enumerate(student["scores"]):
            f.write("The student's score "+str(index+1)+" is "+str(score)+".\n")

        f.write("\n")
        f.write(f"The mean score is: {meanscore}\nThe max score is: {maxscore}\nThe min score is: {minscore}\n")


    print("The student score report is saved in ",output_file)


def mean_score(student_scores):
    total = sum(student_scores)
    count = len(student_scores)
    return total / count

def max_score(student_scores):
    return max(student_scores)

def min_score(student_scores):
    return min(student_scores)

if __name__ == "__main__":
    main()


