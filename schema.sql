/* creating the table "drop table"  table: userinfo */

DROP TABLE IF EXISTS userinfo;
/*  Should I store passwords in my database to? 
    When I type in password I get in blue text so like is it a type of input as well?  
    If i can use it then how do i do it?*/
CREATE TABLE userinfo (
    id SERIAL PRIMARY KEY,
    username TEXT,
    user_password password,
    home_airport TEXT,
);