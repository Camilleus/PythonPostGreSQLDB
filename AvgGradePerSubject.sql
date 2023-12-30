SELECT professors.id, professors.name, AVG(grades.grade) AS avg_grade
FROM professors
JOIN subjects ON professors.id = subjects.professor_id
JOIN grades ON subjects.id = grades.subject_id
WHERE subjects.id = :selected_subject_id
GROUP BY professors.id;