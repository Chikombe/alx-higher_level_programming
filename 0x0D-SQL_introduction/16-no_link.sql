-- Lists all records of the table second_table in my MySQL server.
-- Records should be listed by descending score
SELECT score, name FROM second_table WHERE name != "" ORDER BY score DESC;
