# student_grades.py
# Simple student grade management program for Codacy static analysis testing

students = [
    {"name": "Alice", "marks": [85, 90, 88]},
    {"name": "Bob", "marks": [70, 60, 65]},
    {"name": "Charlie", "marks": [95, 100, 98]}
]

def calculate_average(marks):
  total=0
  for m in marks:
    total += m
  return total / len(marks)

def get_grade(avg):
    if avg >= 90:
      grade = 'A'
    elif avg>=80:
      grade = 'B'
    elif avg>=70:
      grade='C'
    else:
      grade='D'
    return grade

def display_results(students):
    print("Student Results:")
    for s in students:
      avg = calculate_average(s["marks"])
      grade = get_grade(avg)
      print(s["name"], "=> Avg:", avg, "Grade:", grade)

def find_top_student(students):
    top_student = None
    top_avg = 0
    for s in students:
        avg = calculate_average(s["marks"])
        if avg>top_avg:
            top_avg = avg
            top_student=s["name"]
    return top_student

def main():
    display_results(students)
    print("Top student is:", find_top_student(students))

if __name__=="__main__":
    main()
