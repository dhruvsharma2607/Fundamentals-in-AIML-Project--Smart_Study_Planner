def calculate_priority(difficulty, days_left):
    # assign weight based on difficulty
    if difficulty.lower() == "high":
        diff_score = 3
    elif difficulty.lower() == "medium":
        diff_score = 2
    else:
        diff_score = 1

    # assign weight based on deadline
    if days_left <= 2:
        time_score = 3
    elif days_left <= 5:
        time_score = 2
    else:
        time_score = 1

    # total priority
    return diff_score + time_score


def create_plan(subjects, hours):
    total_priority = 0

    # calculate priority for each subject
    for sub in subjects:
        sub["priority"] = calculate_priority(sub["difficulty"], sub["days_left"])
        total_priority += sub["priority"]

    # allocate time based on priority
    for sub in subjects:
        sub["allocated_hours"] = round((sub["priority"] / total_priority) * hours, 2)

    return subjects


def show_plan(plan):
    print("\nYour Study Plan:\n")
    for sub in plan:
        print(sub["name"], "->", sub["allocated_hours"], "hours")


# simple test run
if __name__ == "__main__":
    subjects = []

    n = int(input("Enter number of subjects: "))

    for i in range(n):
        print("\nSubject", i + 1)
        name = input("Enter subject name: ")
        difficulty = input("Enter difficulty (High/Medium/Low): ")
        days_left = int(input("Days left for exam: "))

        subjects.append({
            "name": name,
            "difficulty": difficulty,
            "days_left": days_left
        })

    total_hours = float(input("\nEnter total study hours available: "))

    plan = create_plan(subjects, total_hours)
    show_plan(plan)
