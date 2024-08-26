
use kashish_db;
create table IF NOT EXISTS persons(id int primary key auto_increment, name varchar(50) not null,gender varchar(2), location varchar(50), age int check(age>0));

select * from persons;
insert into persons(name,gender, location, age)values('nithin', 'm', 'mysuru', 40);
insert into persons(name,gender, location, age)values('kashish', 'f', 'bgm', 20);
insert into persons(name,gender, location, age)values('seio','f', 'bgm', 19);
insert into persons(name,gender, location, age)values('sindhu','f','bgm',18);
insert into persons(name,gender, location, age)values('shy' , 'm ','NYcity', 21);
insert into persons(name,gender, location, age)values('siri' , 'f ','new mexico', 21);
insert into persons(name,gender, location, age)values('alexa' , 'f ','NYcity', 22);
insert into persons(name,gender, location, age)values('naina' , 'f ','delhi', 21);
insert into persons(name,gender, location, age)values('riya' , 'f ','blore', 24);
insert into persons(name,gender, location, age)values('soumya' , 'f ','blore', 24);
insert into persons(name,gender, location, age)values('sindhu' , 'f ','blore', 22);
insert into persons(name,gender, location, age)values('manoj' , 'm ','pune', 24);
insert into persons(name,gender, location, age)values('Prashant' , 'm','blore', 24);
insert into persons(name,gender, location, age)values('sahil' , 'm','blore', 24);
insert into persons(name,gender, location, age)values('tirupati' , 'm','blore', 30);
insert into persons(name,gender, location, age)values('prapti' , 'f','blore', 23);
insert into persons(name,gender, location, age)values('shreyas' , 'm','blore', 24);


