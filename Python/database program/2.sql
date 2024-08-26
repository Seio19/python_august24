use kashish_db;
create table employees(id int primary key auto_increment, name varchar(50) not null, designation varchar(40) not null, technology varchar(30) not null, phone_num bigint unique, commission int, salary float default 0, years_of_exp int);

select * from employees;

insert into employees(name, designation, technology, phone_num, commission, salary, years_of_exp)values('kash', 'dubai', 'it', 0124578963, 40, 60000, 8);
insert into employees(name, designation, technology, phone_num, commission, salary, years_of_exp)values('siri', 'hyderabad', 'it', 1598742360, 40, 50000, 2);
insert into employees(name, designation, technology, phone_num, commission, salary, years_of_exp)values('taylor', 'NY city', 'it', 0365214789, 50, 100000, 1);
insert into employees(name, designation, technology, phone_num, commission, salary, years_of_exp)values('swift', 'NY city', 'it', 6765211236, 50, 150000, 4);
insert into employees(name, designation, technology, phone_num, commission, salary, years_of_exp)values('rio', 'NY city', 'it', 566521436, 50, 100000, 5);
insert into employees(name, designation, technology, phone_num, commission, salary, years_of_exp)values('rekha', 'new city', 'it', 1235212549, 50, 100000, 5);
