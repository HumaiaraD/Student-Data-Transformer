def transform_dataset(data):
    qualified_students = {}
    subject_summary = {}
    for student in data:
        grades = student['grades']
        subjects = student['subjects']
        if all(grade > 70 for grade in grades):
            avg_grade = round(sum(grades)/len(grades), 2)
            qualified_students[student['student_id']] = avg_grade

            for subject in subjects:
                subject_summary[subject] = subject_summary.get(subject, 0) + 1

    return {
        'qualified_students': qualified_students,
        'subject_summary': subject_summary}


    
data = [
    {
        "student_id": "S123", 
        "grades": [88, 92, 85], 
        "subjects": ["Math", "Science", "History"]
    },
    {
        "student_id": "S124", 
        "grades": [65, 95, 80], 
        "subjects": ["Math", "Science", "English"]
    },
    {
        "student_id": "S125", 
        "grades": [91, 89, 92], 
        "subjects": ["Math", "Physics", "History"]
    },
    {
        "student_id": "S126",
        "grades": [95, 80, 78],
        "subjects": ["Math", "Art", "History"]
    },
    {
        "student_id": "S127",
        "grades": [100, 99, 98],
        "subjects": ["Math", "Science", "Computer Science"]
    },
    {
        "student_id": "S128",
        "grades": [80, 89],
        "subjects": ["English", "History"]
    },
    {
        "student_id": "S129",
        "grades": [75, 70, 68],
        "subjects": ["Math", "Art", "History"]
    },
    {
        "student_id": "S130",
        "grades": [100, 99, 99],
        "subjects": ["Math", "Chemistry", "Biology"]
    },
    {
        "student_id": "S131",
        "grades": [60, 70],
        "subjects": ["English", "Math"]
    }
]

result = transform_dataset(data)
qualified = result['qualified_students']
summary = result['subject_summary']

print("Qualified Students:\n", qualified)
print("\nSubject Summary:\n", summary)
