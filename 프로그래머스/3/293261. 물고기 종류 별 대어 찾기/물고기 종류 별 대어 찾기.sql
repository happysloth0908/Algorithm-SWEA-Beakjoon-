-- 코드를 작성해주세요
SELECT i.ID, t.FISH_NAME, i.LENGTH
FROM FISH_INFO i JOIN FISH_NAME_INFO t ON i.FISH_TYPE = t.FISH_TYPE
WHERE (t.FISH_TYPE, i.LENGTH) IN (SELECT FISH_TYPE, MAX(LENGTH) AS LENGTH
                              FROM FISH_INFO
                               GROUP BY FISH_TYPE
                               )
                               ORDER BY 1
                               
