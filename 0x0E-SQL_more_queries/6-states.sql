-- Creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on my MySQL server.
-- states description: id INT unique, auto generated, can’t be null and is a primary key, name VARCHAR(256) can’t be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE,name VARCHAR(256))