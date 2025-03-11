/* Write your PL/SQL query statement below */
SELECT sample_id, dna_sequence, species,
CASE
    WHEN dna_sequence LIKE 'ATG%' THEN 1
    ELSE 0
END AS has_start,
CASE
    WHEN REGEXP_LIKE(dna_sequence, '(TAA|TAG|TGA)$') THEN 1
    ELSE 0
END AS has_stop,
CASE
    WHEN dna_sequence LIKE '%ATAT%' THEN 1
    ELSE 0
END AS has_atat,
DECODE(REGEXP_SUBSTR(dna_sequence, 'G{3,}'), NULL, 0, 1) AS has_ggg
FROM Samples
ORDER BY sample_id;