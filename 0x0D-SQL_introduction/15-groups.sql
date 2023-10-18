-- Lists the number of records with the same score in the table second_table in my MySQL server.
-- The list should be sorted by the number of records (descending)
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
