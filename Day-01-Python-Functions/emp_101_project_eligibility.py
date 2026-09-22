
# Day 1 — Company Ticket 🎫

# இப்ப நான் Team Leadனு நினைச்சுக்கோ. உனக்கு Jira ticket வந்திருக்கு.

# Ticket ID: EMP-101
# Title: Employee Project Eligibility

# Requirement:
# Create a function named check_project_eligibility.

# The function must accept:

# experience
# training_completed

# Business Rules:

# Experience must be 2 years or more
# Training must be completed (True)
# If both conditions are satisfied → return "Eligible for Project"
# Otherwise → return "Not Eligible"

# Test with:

# experience = 3
# training_completed = True

# Expected:

# Eligible for Project



def check_project_eligibility(experience, training_completed):
    if experience >= 2 and training_completed:
        return "Eligible for Project"
    else:
        return "Not Eligible"


eligibility = check_project_eligibility(3, True)

print(eligibility)