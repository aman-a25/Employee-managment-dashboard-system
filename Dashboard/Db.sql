CREATE DATABASE project1; 
USE project1;

-- Create the emp table
CREATE TABLE emp (
    e_id INT PRIMARY KEY,
    e_name VARCHAR(255),
    post VARCHAR(255),
    salary INT
);

-- Create the emp_log table
CREATE TABLE emp_log (
    logID INT AUTO_INCREMENT PRIMARY KEY,
    e_id INT,
    status TEXT,
    data_and_time DATETIME,
    FOREIGN KEY (e_id) REFERENCES emp(e_id)
);

-- Creating triggers to automate the insertion of data into emp_log table

create trigger t1 after insert on emp for each row
insert into emp_log(e_id,status,date_and_time)
value(new.e_id,'insert',now());

create trigger t2 after update on emp for each row
insert into emp_log(e_id,status,date_and_time)
value(new.e_id,'update',now());

create trigger t3 after delete on emp for each row
insert into emp_log(e_id,status,date_and_time)
value(old.e_id,'delete',now());
