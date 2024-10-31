SELECT H.hacker_id, H.name
FROM Submissions AS S
JOIN Hackers as H USING(hacker_id)
JOIN Challenges as C USING(challenge_id)
JOIN Difficulty as D USING(difficulty_level)
WHERE S.score = D.score
GROUP BY H.Hacker_id, H.name
HAVING COUNT(H.name) > 1
ORDER BY COUNT(H.name) DESC, H.Hacker_id;