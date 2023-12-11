/*
 176. 第二高的薪水
 Employee 表：
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
在 SQL 中，id 是这个表的主键。
表的每一行包含员工的工资信息。
查询并返回 Employee 表中第二高的薪水 。如果不存在第二高的薪水，查询应该返回 null(Pandas 则返回 None) 。
查询结果如下例所示。
 */
select (select distinct Salary from Employee order by Salary desc limit 1 offset 1) as SecondHighestSalary;


