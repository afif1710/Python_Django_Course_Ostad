-- 1) students table
CREATE TABLE students(
	student_id INT PRIMARY KEY,
  	name VARCHAR(100) NOT NULL,
  	department VARCHAR(50) NOT NULL
);

-- 2) attendance table
CREATE TABLE attendance (
	id INT AUTO_INCREMENT PRIMARY KEY,
  	student_id INT NOT NULL,
  	total_classes INT,
  	attended_classes INT, 	
  	FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- 3) Performance table
CREATE TABLE performance (
	id INT AUTO_INCREMENT PRIMARY KEY,
  	student_id INT NOT NULL,
  	course VARCHAR(100) NOT NULL,
  	score DECIMAL(5, 2) NOT NULL,
  	FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- Insert sample students
INSERT INTO students (student_id, name, department)
VALUES 
(1, 'Nafis Fuad', 'CSE'),
(2, 'Rafi Hossain', 'EEE'),
(3, 'Nabila Noor', 'BBA'),
(4, 'Sara Rahman', 'CSE'),
(5, 'Abir Ahmed', 'CE');

-- Insert sample attendance
INSERT INTO attendance (student_id, total_classes, attended_classes)
VALUES 
(1, 30, 28),
(2, 30, 18),
(3, 35, 20),
(4, 30, 30),
(5, 28, 28);

-- Insert sample performance
INSERT INTO performance (student_id, course, score)
VALUES 
(1, 'Database Systems', 85.5),
(1, 'Algorithms', 90.0),
(2, 'Circuits', 45.0),
(3, 'Accounting', 93.0),
(3, 'Economics', 90.0),
(4, 'Web Development', 95.0),
(4, 'AI Fundamentals', 88.0),
(5, 'Fluid Mechanics', 82.0);

-- Q1. Show all students
SELECT * FROM students;

-- Q2. Show all students with their attendance percentage
SELECT s.name, a.student_id, (attended_classes / total_classes * 100) AS attendance_percentage
FROM students s
JOIN attendance a ON s.student_id = a.student_id;

-- Q3. Show students whose attendance percentage is below 75%
SELECT s.name, a.student_id, (attended_classes / total_classes * 100) AS attendance_percentage
FROM students s
JOIN attendance a ON s.student_id = a.student_id
WHERE a.total_classes > 0	-- Makes sure we don’t get Division by Zero error
  AND (a.attended_classes / a.total_classes * 100) < 75
ORDER BY attendance_percentage;

-- Q4. Show each student’s average score
SELECT s.student_id, s.name, AVG(p.score) AS average_score 
FROM students s
JOIN performance p ON s.student_id = p.student_id
GROUP BY s.student_id, s.name
ORDER BY average_score DESC;		-- Show in descending order of average_score

-- Q5. Show courses where student scored below 50
SELECT s.student_id, s.name, p.course, p.score
FROM students s
JOIN performance p ON s.student_id = p.student_id
WHERE p.score < 50;

-- Q6. Show students with perfect attendance
SELECT s.student_id, s.name, a.total_classes, a.attended_classes
FROM students s
JOIN attendance a ON s.student_id = a.student_id
WHERE a.total_classes > 0 AND a.total_classes = a.attended_classes;

-- Q7. Show top 3 students with highest average scores
SELECT s.student_id, s.name, AVG(p.score) AS average_score 
FROM students s
JOIN performance p ON s.student_id = p.student_id
GROUP BY s.student_id, s.name
ORDER BY average_score DESC
LIMIT 3;

-- Q8. Show CSE students with average score above 80
SELECT s.student_id, s.name, s.department, AVG(p.score) AS average_score 
FROM students s
JOIN performance p ON s.student_id = p.student_id
WHERE s.department LIKE 'CSE'
GROUP BY s.student_id, s.name
HAVING AVG(p.score) > 80
ORDER BY average_score DESC;

-- Q9. Show courses where max score is 90 or less
SELECT course
FROM performance
GROUP BY course
HAVING MAX(score) <= 90;

-- Q10. Show students with attendance below 75% and avg score below 50
SELECT s.name, a.student_id,
       (attended_classes / total_classes * 100) AS attendance_percentage,
       AVG(p.score) AS avg_score
FROM students s
JOIN attendance a ON s.student_id = a.student_id
JOIN performance p ON s.student_id = p.student_id
WHERE a.total_classes > 0
  AND (a.attended_classes / a.total_classes * 100) < 75
GROUP BY s.student_id, s.name, a.attended_classes, a.total_classes
HAVING AVG(p.score) < 50;
