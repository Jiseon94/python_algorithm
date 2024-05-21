-- 코드를 입력하세요
SELECT ingredient_type, sum(total_order) as total_order
from FIRST_HALF F, ICECREAM_INFO I
WHERE F.flavor = I.flavor
GROUP BY I.ingredient_type
ORDER BY total_order;
