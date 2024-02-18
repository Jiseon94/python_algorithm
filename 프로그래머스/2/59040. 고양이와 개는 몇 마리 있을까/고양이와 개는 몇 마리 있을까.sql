-- 코드를 입력하세요
-- SELECT count(*)
-- from ANIMAL_INS
-- where ANIMAL_TYPE = 'Dog'

-- SELECT count(*)
-- from ANIMAL_INS
-- where ANIMAL_TYPE = 'Cat'

SELECT ANIMAL_TYPE, count(*)
from ANIMAL_INS
group by ANIMAL_TYPE
order by ANIMAL_TYPE ASC
