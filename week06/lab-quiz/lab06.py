clubs = ("software", "design", "marketing")
all_students = []
student1 = ["Kadir Demir".strip(), [clubs[0], clubs[1]]]
student2 = ["Mehmethan Erduran".strip(), [clubs[1], clubs[2]]]
student3 = ["Ibrahim Demir".strip(), [clubs[0], clubs[2]]]
all_students = [student1, student2, student3]
president = ["Ayse Yilmaz".strip(), [clubs[0], clubs[1], clubs[2]]]
all_students.insert(0, president)
print(f"Total Registered Students: {len(all_students)}")
all_students.remove(student2)
latest_removed = all_students.pop()
print(f"Latest student removed from the system: {latest_removed[0]}")
new_student = ["Burak Tan".strip(), [clubs[1]]]
all_students.append(new_student)
temp_sorted_students = sorted(all_students)
print("Temporarily Sorted List (sorted()):")
print(temp_sorted_students)
print("Original List (Order Intact):")
print(all_students)
all_students.sort()
print("Permanently Sorted List (sort()):")
print(all_students)