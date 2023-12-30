SELECT subjects.id, subjects.name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
WHERE subjects.professor_id = :selected_professor_id AND grades.student_id = :selected_student_id;