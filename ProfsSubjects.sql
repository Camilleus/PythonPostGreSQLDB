SELECT subjects.id, subjects.name
FROM subjects
WHERE subjects.professor_id = :selected_professor_id;