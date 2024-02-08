-- 코드를 입력하세요
-- 날짜 비교를 어떻게 하지?
SELECT I.ANIMAL_ID, I.name
from ANIMAL_INS I, ANIMAL_OUTS O
where I.ANIMAL_ID = O.ANIMAL_ID
and I.DATETIME > O.DATETIME
order by I.DATETIME ASC;