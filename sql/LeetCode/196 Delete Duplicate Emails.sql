DELETE P1 FROM Person as P1, Person as P2
WHERE P1.email = P2.email AND P1.id > P2.id