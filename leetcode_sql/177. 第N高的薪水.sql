/*
 177. 第N高的薪水
 表: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
在 SQL 中，id 是该表的主键。
该表的每一行都包含有关员工工资的信息。
查询 Employee 表中第 n 高的工资。如果没有第 n 个最高工资，查询结果应该为 null 。
查询结果格式如下所示。
 */


CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    declare m int;
    set m = N - 1;
  RETURN (
      # Write your MySQL query statement below.
        select distinct salary from Employee order by salary desc limit 1 offset M
  );
END
