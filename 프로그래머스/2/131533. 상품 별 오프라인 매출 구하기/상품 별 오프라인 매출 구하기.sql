-- 코드를 입력하세요
-- 그냥 = 으로 join 구문을 간단하게 쓰는게 왜 여기서는 안되는걸까..? ==> where 절 잘못 썼음..^^;
-- 매출액이 같다면 상품코드를 기준으로 오름차순 정렬 ==> order by 2개 정렬!!!!
-- group by 어떻게 쓰지.. 왜 안되지...=> 하나의 기준으로 통합되는 과정에서 제각각의 price 중 어떤걸 선택해야할지 몰라서 에러를 내뱉는거다. group by 를 해줬으면 그에 합당한 통합정보를 요청해야한다.

-- SELECT PRODUCT_CODE, SUM(SALES_AMOUNT*PRICE) SALES
-- from product P, OFFLINE_SALE O
-- where P.PRODUCT_ID = O.PRODUCT_ID
-- GROUP BY PRODUCT_CODE
-- ORDER BY SALES DESC, PRODUCT_CODE ASC;

select PRODUCT_CODE, sum(SALES_AMOUNT*PRICE) SALES
from product P, OFFLINE_SALE O
where P.PRODUCT_ID = O.PRODUCT_ID
group by product_code
order by SALES desc, PRODUCT_CODE asc;

