SUBJECT_COUNT = 5
MAX_MARK = 100


def grade_for(percentage):
	if percentage >= 90:
		return "A"
	if percentage >= 80:
		return "B"
	if percentage >= 70:
		return "C"
	if percentage >= 60:
		return "D"
	return "F"


def main():
	marks = []

	for subject_number in range(1, SUBJECT_COUNT + 1):
		while True:
			try:
				mark = float(input(f"Enter marks for subject {subject_number} (0-100): "))
				if 0 <= mark <= MAX_MARK:
					marks.append(mark)
					break
				print("Marks must be between 0 and 100.")
			except ValueError:
				print("Please enter a valid number.")

	total = sum(marks)
	average = total / SUBJECT_COUNT
	percentage = total / (SUBJECT_COUNT * MAX_MARK) * 100
	grade = grade_for(percentage)

	print("\n--- Results ---")
	print(f"Total marks: {total:g} / {SUBJECT_COUNT * MAX_MARK}")
	print(f"Average: {average:.2f}")
	print(f"Percentage: {percentage:.2f}%")
	print(f"Grade: {grade}")


if __name__ == "__main__": 
    main()

