def average(lst):
    lst2 = []
    for marks in lst:  # Iterate through each student's marks
        sum_marks = 0
        for mark in marks:  # Sum the marks of the student
            sum_marks += int(mark)
        avg = sum_marks / len(marks)  # Calculate the average
        lst2.append(avg)  # Append the average to the result list
    return lst2


def process_students():
    names = input("Enter all names separated by a comma: ")
    name1 = names.split(",")
    name1 = [name.strip() for name in name1]  # Strip extra spaces

    marks = []
    for i in range(len(name1)):
        mark = input(f"Enter marks for {name1[i]} separated by a comma: ")
        marks.append(mark.split(","))  # Convert marks input to a list of strings

    avg = average(marks)  # Calculate average marks for each student

    results = []  # To store the final results

    for i in range(len(avg)):
        if avg[i] >= 85:
            performance = "Excellent"
        elif 70 <= avg[i] < 85:
            performance = "Good"
        else:
            performance = "Needs Improvement"
        
        results.append(f"{name1[i]}: {performance}")  # Add result for each student

    print(results)  # Print all results

process_students()
