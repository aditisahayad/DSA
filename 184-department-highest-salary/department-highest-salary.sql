# Write your MySQL query statement below
SELECT d.name as Department, e.name as Employee, e.salary as Salary 
from Employee e join Department d
on e.departmentId = d.id
where (e.departmentId, e.salary) IN (
    SELECT departmentId, MAX(salary)
    FROM Employee e
    group by e.departmentId
)
