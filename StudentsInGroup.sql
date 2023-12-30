SELECT students.id, students.name
FROM students
WHERE students.group_id = :selected_group_id;