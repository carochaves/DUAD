ALTER TABLE lyfter_duad.users
ADD COLUMN department_id integer;

SET search_path TO lyfter_duad;

SET search_path TO lyfter_duad;
CREATE TABLE IF NOT EXISTS departments (
    id SERIAL PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
);

SET search_path TO lyfter_duad;
INSERT INTO departments (department_name) VALUES
('Human Resources'),
('Sales'),
('Engineering');

SET search_path TO lyfter_duad;

UPDATE users
SET department_id = FLOOR(RANDOM() * 3 + 1)::INTEGER
WHERE age >= 18 AND age <= 60;

SET search_path TO lyfter_duad;

SELECT users.username, departments.department_name
FROM users
INNER JOIN departments ON users.department_id = departments.id;

SET search_path TO lyfter_duad;

SELECT username FROM users
WHERE department_id = (SELECT id FROM departments WHERE department_name = 'Sales');

SET search_path TO lyfter_duad;

SELECT department_id, COUNT(*) AS total_users
FROM users
GROUP BY department_id;

SELECT * FROM users WHERE age > 30;

SET search_path TO lyfter_duad;

SELECT * FROM users ORDER BY username ASC;

SET search_path TO lyfter_duad;

SELECT * FROM users LIMIT 10;
