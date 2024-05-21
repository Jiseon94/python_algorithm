SELECT car_type, count(car_id) as CARS
from CAR_RENTAL_COMPANY_CAR
where options like '%시트%'
GROUP BY car_type
ORDER BY car_type;