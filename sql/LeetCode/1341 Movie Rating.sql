# Write your MySQL query statement below
(SELECT U.name as results FROM Users as U
JOIN MovieRating as M ON U.user_id = M.user_id
GROUP BY U.name
ORDER BY COUNT(*) DESC, U.name
LIMIT 1)

UNION ALL

(SELECT M.title as results FROM Movies as M
JOIN MovieRating as MR ON M.movie_id = MR.movie_id
WHERE MR.created_at LIKE '2020-02%'
GROUP BY M.title
ORDER BY AVG(MR.rating) DESC, M.title
LIMIT 1)