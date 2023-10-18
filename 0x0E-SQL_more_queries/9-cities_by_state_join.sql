-- Lists all cities contained in the database hbtn_0d_usa
-- Results must be sorted in ascending order by cities.id
SELECT a.id AS id, a.name AS name, b.name AS name
FROM cities a 
INNER join states b
ON a.state_id = b.id
ORDER BY a.id ASC;
