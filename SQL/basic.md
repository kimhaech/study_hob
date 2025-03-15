# SQL 기본 문법 정리

## 데이터베이스 및 테이블 관리
### 데이터베이스 생성, 삭제
``` sql
CREATE DATABASE DB명; -- 생성
DROP DATABASE DB명; -- 삭제
USE DB명; -- 특정 DB 사용
```

### 테이블 생성, 삭제
``` sql
CREATE TABLE 테이블명 ( -- 생성
    컬럼명 데이터타입 [제약조건],
    컬럼명 데이터타입 [제약조건],
    ,,,
);
DROP TABLE 테이블명; -- 테이블 자체 삭제
TRUNCATE TABLE 테이블명; -- 테이블의 모든 데이터 삭제(구조 유지)
```
-> 예제
``` sql
CREATE TABLE motorcycles (
    veh_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    brand VARCHAR(50) NOT NULL,
    displacement INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 데이터 조작 (DML :  Data Manipulation Language)
### 데이터 삽입 (INSERT)
``` sql
INSERT INTO 테이블명 (컬럼1, 컬럼2, ...) VALUES (값1, 값2, ...);
```
-> 예제
``` sql
INSERT INTO motorcycles (name, brand, displacement) VALUES ('iron 883', 'Harley Davidson', 883);
```

### 데이터 조회 (SELECT)
``` sql
SELECT 컬럼명 FROM 테이블명 WHERE 조건;
SELECT * FROM 테이블명; -- * 는 전체를 의미 -> 모든 컬럼 조회
```
-> 예제
``` sql
SELECT name, brand, displacement 
FROM motorcycles 
WHERE displacement >= 800;
```
조건 연산자
| 연산자 | 설명 |
|--------|--------|
| = | 같음 |
| != or <> | 다름 |
| >, < | 초과, 미만 |
| >=, <= | 이상, 이하|
| BETWEEN A AND B | A 이상 B 이하 |
| IN (값1, 값2, ...) | 값 목록 중 하나와 일치 |
| LIKE '패턴' | 특정 패턴과 일치 (% : 여러글자, _ : 한 글자) |
| IS NULL | NULL 값 찾기(앞에 NOT을 붙이면 반대로 사용 가능) |
-> 예제
``` sql
SELECT * FROM motorcycles WHERE name LIKE '%CVO'; -- 이름에 CVO가 들어감
SELECT * FROM motorcycles WHERE displacement BETWEEN 800 AND 1300; -- 배기량 800~1300 사이
```
### 정렬 (ORDER BY)
``` sql
SELECT * FROM motorcycles ORDER BY displacement ASC; -- 배기량 오름차순 정렬
SELECT * FROM motorcycles ORDER BY name DESC; -- 이름 내림차순 정렬
```
### 중복제거 (DISTINCT)
``` sql
SELECT DISTINCT 컬럼명 FROM 테이블명;
```
### 그룹화 (GROUP BY, HAVING)
``` sql
SELECT 컬럼명, COUNT(*) FROM 테이블명 GROUP BY 컬럼명;
SELECT 컬럼명, COUNT(*) FROM 테이블명 GROUP BY 컬럼명 HAVING COUNT(*) > 1;
```
-> 예제
``` sql 
SELECT brand, COUNT(*) FROM motorcycles GROUP BY brand; -- 브랜드로 숫자 집계(count가 세는 역할)
SELECT brand, COUNT(*) FROM motorcycles GROUP BY brand HAVING COUNT(*) > 2; -- 브랜드별 집계된 바이크 수가 2개 초과인 브랜드만 조회
```
### 데이터 수정 (UPDATE)
``` sql
UPDATE 테이블명 SET 컬럼명 = 값 WHERE 조건;
```
-> 예제
``` sql
UPDATE motorcycles SET name = 'Sportster iron 883' WHERE name = 'iron 883'; -- 이름이 iron 883 인 바이크를 SET 문장과 같이 수정
```
### 데이터 삭제 (DELETE)
``` sql
DELETE FROM 테이블명 WHERE 조건;
```
-> 예제
``` sql 
DELETE FROM motorcycls WHERE brand = 'honda';
```
