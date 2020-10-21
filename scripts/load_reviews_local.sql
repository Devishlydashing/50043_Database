use 50043_DB;

/* create a table for storing user data*/
drop table if exists users;
create table users(
    id integer primary key,
    name varchar(100),
    email varchar(100),
    password varchar(100),
    recent_login datetime
);

/* create a table for importing the data into*/
drop table if exists review;
create table review(
id integer not null auto_increment primary key,
asin varchar(100),
helpful varchar(100),
overall integer,
reviewText varchar(255),
reviewTime varchar(255),
reviewerID varchar(100),
reviewerName varchar(100),
summary varchar(255),
unixReviewTime integer
);

load data local infile "kindle_reviews.csv" into table review fields terminated by ',' enclosed by '"' escaped by '"' lines terminated by '\n' ignore 1 rows;