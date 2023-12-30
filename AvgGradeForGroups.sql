SELECT groups.id, groups.name, AVG(grades.grade) AS avg_grade
FROM groups
JOIN students ON groups.id = students.group_id
JOIN grades ON students.id = grades.student_id
WHERE grades.subject_id = :selected_subject_id
GROUP BY groups.id
ORDER BY avg_grade DESC;