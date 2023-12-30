SELECT students.id, students.name, grades.grade, grades.date
FROM students
JOIN grades ON students.id = grades.student_id
WHERE students.group_id = :selected_group_id AND grades.subject_id = :selected_subject_id;