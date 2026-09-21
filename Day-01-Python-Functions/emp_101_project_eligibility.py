def check_project_eligibility(experience, training_completed):
    if experience >= 2 and training_completed:
        return "Eligible for Project"
    else:
        return "Not Eligible"


eligibility = check_project_eligibility(3, True)

print(eligibility)