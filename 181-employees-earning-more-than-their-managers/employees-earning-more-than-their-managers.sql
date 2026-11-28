# Write your MySQL query statement below
SELECT e.name AS Employee
FROM EMPLOYEE e
JOIN EMPLOYEE m
ON e.managerId = m.id
WHERE e.salary > m.salary;
