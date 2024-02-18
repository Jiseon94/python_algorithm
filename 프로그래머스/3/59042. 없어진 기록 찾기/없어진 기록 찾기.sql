-- 코드를 입력하세요
-- # SELECT count(O.ANIMAL_ID), count(I.animal_id)
-- # from ANIMAL_INS I, ANIMAL_outs O
-- # where I.animal_id = O.animal_id

-- # SELECT count(I.animal_id)
-- # from ANIMAL_INS I

-- # SELECT count(*) from animal_outs
-- # SELECT count(*) from animal_ins

-- # select O.animal_id, O.name, O.datetime from ANIMAL_INS I, ANIMAL_outs O where I.animal_id = O.animal_id

select animal_id, name from animal_outs
minus
select O.animal_id, O.name from ANIMAL_INS I, ANIMAL_outs O where I.animal_id = O.animal_id