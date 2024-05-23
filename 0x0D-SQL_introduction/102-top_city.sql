-- displays the top 3 of cities temperature during July and August ordered by temperature
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city order by avg_temp DESC LIMIT 3;