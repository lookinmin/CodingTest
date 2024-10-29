SELECT 
CASE
    WHEN G.Grade <= 7 THEN NULL
    ELSE S.Name
END AS NAME,
G.Grade, S.Marks
FROM Students as S JOIN Grades as G
ON S.Marks BETWEEN G.Min_Mark AND G.Max_Mark
ORDER BY G.Grade DESC,
    CASE
        WHEN G.Grade >= 8 THEN NAME
        ELSE S.Marks
    END ASC;