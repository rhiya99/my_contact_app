 
# creating table for table 
CREATE TABLE user_table (
    name text,
    emailid text,
    number text,
    password text,
    secretcode text
);

DROP TABLE user_table;

SELECT name, emailid FROM user_table;

SELECT * FROM user_table;

INSERT INTO user_table
VALUES ("test user 1", "test user email", "345678","abcd","qwerty");
INSERT INTO user_table
VALUES ("test user 2", "test user email 2", "34567800000","abcdef","qy");

SELECT * FROM user_table WHERE  emailid='test user email';

UPDATE user_table
SET name = 'Alfred Schmidt', number= '2222222'
WHERE emailid = "test user email";




sudo pip3 install flask
