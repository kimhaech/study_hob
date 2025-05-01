# 📘 SQL 함수 요약 정리 (Cheat Sheet)

## 📊 1. 집계 함수 (Aggregate Functions)
| 함수       | 설명               | 예시 |
|------------|--------------------|------|
| COUNT()    | 행 개수 계산       | `SELECT COUNT(*) FROM users;` |
| SUM()      | 합계 계산          | `SELECT SUM(price) FROM sales;` |
| AVG()      | 평균값 계산        | `SELECT AVG(score) FROM exams;` |
| MIN()      | 최솟값 반환        | `SELECT MIN(age) FROM people;` |
| MAX()      | 최댓값 반환        | `SELECT MAX(salary) FROM jobs;` |

---

## 🔤 2. 문자열 함수 (String Functions)
| 함수                      | 설명              | 예시 |
|---------------------------|-------------------|------|
| CONCAT(a, b)              | 문자열 연결       | `SELECT CONCAT(first_name, ' ', last_name);` |
| SUBSTRING(str, start, len)| 부분 문자열 추출 | `SELECT SUBSTRING('SQL Tutorial', 5, 3);` |
| LENGTH()                  | 문자열 길이       | `SELECT LENGTH('hello');` |
| UPPER()                   | 대문자로 변환     | `SELECT UPPER(name);` |
| LOWER()                   | 소문자로 변환     | `SELECT LOWER(name);` |
| TRIM()                    | 공백 제거         | `SELECT TRIM(' hello ');` |
| REPLACE()                 | 문자열 치환       | `SELECT REPLACE('abcabc', 'a', 'x');` |

---

## 📆 3. 날짜/시간 함수 (Date & Time Functions)
| 함수                  | 설명                      | 예시 |
|-----------------------|---------------------------|------|
| NOW()                 | 현재 날짜와 시간 반환     | `SELECT NOW();` |
| CURDATE()             | 오늘 날짜 반환            | `SELECT CURDATE();` |
| DATE()                | 날짜만 추출              | `SELECT DATE(NOW());` |
| YEAR(), MONTH(), DAY()| 연, 월, 일 추출          | `SELECT YEAR(order_date);` |
| DATEDIFF(a, b)        | 두 날짜 차이 (일수)       | `SELECT DATEDIFF(NOW(), '2024-01-01');` |

---

## 🔢 4. 수학 함수 (Math Functions)
| 함수           | 설명             | 예시 |
|----------------|------------------|------|
| ABS()          | 절댓값            | `SELECT ABS(-5);` |
| ROUND(x, n)    | 반올림            | `SELECT ROUND(3.1415, 2);` |
| FLOOR()        | 내림              | `SELECT FLOOR(3.7);` |
| CEIL()         | 올림              | `SELECT CEIL(3.1);` |
| RAND()         | 0~1 사이의 난수   | `SELECT RAND();` |

---

## ✅ 5. 조건 함수
### IF
```sql
SELECT IF(score >= 60, 'PASS', 'FAIL') FROM exams;
```

### CASE WHEN
```sql
SELECT
  CASE
    WHEN age >= 20 THEN 'adult'
    ELSE 'minor'
  END AS age_group
FROM users;
```

---

> 💡 각 함수는 사용하는 DBMS(MySQL, PostgreSQL, Oracle 등)에 따라 약간의 문법 차이가 있을 수 있습니다.

