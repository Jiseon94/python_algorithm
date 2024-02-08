-- 코드를 입력하세요
-- 문자열 검색할때 in 을 써야할지 = 을 써야할지 헷갈리네..
-- 지금은 DESC 를 쓰면 안되지만,, 어떻게 쓰는지 까먹음...
-- date 에서 원하는 포맷으로 출력하는거 어떻게 했더라.......
-- 조인 구문에서 조건 나열 중 테이블 조인을 우선했었는지... 검색조건 우선했는지 기억이 안나네...
-- SELECT book_id, author_name, to_date(published_date, 'yy mm dd')
-- from book B, author A 
-- where B.AUTHOR_ID = A.AUTHOR_ID
-- and category = '경제';

SELECT book_id, author_name, 
    TO_CHAR(published_date, 'YYYY-MM-DD') AS PUBLISHED_DATE
from book B, author A 
where B.AUTHOR_ID = A.AUTHOR_ID
and category = '경제'
order by PUBLISHED_DATE;