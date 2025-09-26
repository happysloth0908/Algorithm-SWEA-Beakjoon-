-- 코드를 작성해주세요
SELECT 
    CASE 
    WHEN EXISTS (
        SELECT 1
        FROM SKILLCODES s
        WHERE s.CATEGORY = 'Front End' AND (s.CODE & d.SKILL_CODE) <> 0 
    ) 
 
    AND EXISTS (
        SELECT 1
        FROM SKILLCODES ss
        WHERE ss.NAME = 'Python' AND (d.SKILL_CODE & ss.CODE) <> 0 
        ) THEN 'A'
 
 
 WHEN EXISTS 
        (SELECT 1
        FROM SKILLCODES sss
        WHERE sss.NAME = 'C#' AND (d.SKILL_CODE & sss.CODE) <> 0 
        ) THEN 'B'
    WHEN EXISTS ( -- 그 외 Front End
           SELECT 1
           FROM SKILLCODES sfe2
           WHERE sfe2.CATEGORY = 'Front End'
             AND (d.SKILL_CODE & sfe2.CODE) <> 0 )
      THEN 'C'
 END AS GRADE 
, ID, EMAIL 
FROM DEVELOPERS d
HAVING GRADE is not null
ORDER BY GRADE, d.ID