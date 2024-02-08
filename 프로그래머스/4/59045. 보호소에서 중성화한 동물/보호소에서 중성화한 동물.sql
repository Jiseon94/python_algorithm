-- 코드를 입력하세요
-- 조건절에서 중성화 조건의 문자열을 포함하는지를 알아내고 싶으면... 어떻게해야하지 => like '문자열%' 로 찾을 수 잇는데
-- 대,소문자 구분을 못하므로 엄격하게 적어줘야한다... 대소문자 무시하고 싶으면 어떻게 하지...
-- 두개의 문자열 패턴을 or 로 해서 확인하는걸 어떻게 하지..
-- => OR 조건을 사용할 때는 각 조건을 명확히 나누어야한다!! 괄호!!!

SELECT I.ANIMAL_ID, I.ANIMAL_TYPE, I.name
from ANIMAL_INS I, ANIMAL_OUTS O
where I.ANIMAL_ID = O.ANIMAL_ID
and SEX_UPON_INTAKE like 'Intact%'
AND (SEX_UPON_OUTCOME LIKE 'Spayed%' OR SEX_UPON_OUTCOME LIKE 'Neutered%')
order by I.ANIMAL_ID asc;