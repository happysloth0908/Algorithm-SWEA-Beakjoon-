# -- 코드를 작성해주세요
# SELECT d.ID, d.EMAIL, d.FIRST_NAME, d.LAST_NAME
# FROM DEVELOPERS d JOIN 
# (SELECT *
# FROM SKILLCODES
# WHERE CATEGORY = 'Front End') AS s
#  ON d.SKILL_CODE & s.CODE <> 0
# ORDER BY 1

# 오답 이유
# 위처럼 하면 프론트엔드 기술 여러 개 가진 사람이 중복되어 나옴
# 그래서 하나라도 있으면 한 번 나오게끔하려면 exist 를 써야 함. 
SELECT d.ID, d.EMAIL, d.FIRST_NAME, d.LAST_NAME
FROM DEVELOPERS d
WHERE EXISTS (
    SELECT 1
    FROM SKILLCODES s
    WHERE CATEGORY = 'Front End'
    AND d.SKILL_CODE & s.CODE <> 0
)
ORDER BY 1