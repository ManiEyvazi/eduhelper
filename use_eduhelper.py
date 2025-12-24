import eduhelper

# Grades
scores = [4, 3.5, 5]
print("Average score:", eduhelper.average_score(scores))
print("GPA:", eduhelper.calculate_gpa(scores))
print("Weighted GPA:", eduhelper.weighted_gpa(scores, [3, 2, 4]))
print("Pass/Fail:", eduhelper.pass_or_fail(3.2))
print("Letter grade:", eduhelper.letter_grade(4.1))
print("Grade summary:", eduhelper.grade_summary(scores))

# Time utilities
print("\nDays left:", eduhelper.days_left("2025-01-20"))
print("Is urgent:", eduhelper.is_urgent("2025-01-05"))
print("Deadline status:", eduhelper.deadline_status("2025-01-05"))
print("Days between:", eduhelper.days_between("2025-01-01", "2025-01-15"))

# Study planning
print("\nDaily study plan:", eduhelper.daily_study_plan(4))
print("Pomodoro sessions:", eduhelper.pomodoro_sessions(3))
print("Study intensity:", eduhelper.study_intensity(5))
print("Study recommendation:", eduhelper.study_recommendation(5))
print("Weekly plan:", eduhelper.weekly_plan(3, 6))