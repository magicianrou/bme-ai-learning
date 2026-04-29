def calculate_mean(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

def main():
    scores = [91, 92, 93, 94, 95]

    student = {
        "name" : "Lou Xinhang",
        "major" : "biomedical engineering",
        "school" : "Southeast University"
    }

    mean_score = calculate_mean(scores)

    print("student information:", student)

    print("Scores:", scores)

    print("meanscore:", mean_score)

if __name__ == "__main__":
    main()