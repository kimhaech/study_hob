-- DATE 타입인 date_of_birth에서 포맷을 맞춰야함 -> Y,y/M,m/D,d 대, 소문자별로 표현이 조금씩 다름
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(date_of_birth, "%Y-%m-%d") AS DATE_OF_BIRTH from member_profile
where month(date_of_birth) = '03' and gender = 'W' and tlno is not null 