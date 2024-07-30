SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS orders, address, user, store, product, review, review_backup, user_address, order_product;

SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE `orders` (
	`idx`	INT	NOT NULL,
	`address`	VARCHAR(100)	NULL,
	`store_idx`	INT	NULL,
	`product_id`	INT	NULL,
	`order_price`	INT	NULL,
	`delivery_price`	INT	NULL,
	`discount_price`	INT	NULL,
	`total_price`	INT	NULL
);

CREATE TABLE `address` (
	`idx`	INT	NOT NULL,
	`address`	VARCHAR(50)	NULL,
	`detail_address`	VARCHAR(50)	NULL,
	`user_idx`	INT	NULL,
	`create_at`	TIMESTAMP	NULL,
	`updated_at`	TIMESTAMP	NULL,
	`status`	VARCHAR(7)	NULL
);

CREATE TABLE `user` (
	`idx`	INT	NOT NULL,
	`email`	VARCHAR(45)	NULL,
	`password`	VARCHAR(255)	NULL,
	`name`	VARCHAR(30)	NULL,
	`phone`	VARCHAR(20)	NULL,
	`address_idx`	INT	NULL,
	`pay_type`	VARCHAR(8)	NULL
);

CREATE TABLE `store` (
	`id`	INT	NOT NULL,
	`name`	VARCHAR(50)	NULL,
	`phone`	VARCHAR(20)	NULL,
	`address`	VARCHAR(80)	NULL,
	`introduction`	VARCHAR(500)	NULL,
	`rocket`	BOOL	NULL,
	`delivery_time`	VARCHAR(20)	NULL
);

CREATE TABLE `product` (
	`id`	INT	NOT NULL,
	`field`	VARCHAR(50)	NULL,
	`price`	INT	NULL,
	`introduction`	VARCHAR(500)	NULL,
	`remain`	INT	NULL,
	`store_id`	INT	NULL
);

CREATE TABLE `review` (
	`id`	INT	NOT NULL,
	`contents`	VARCHAR(500)	NULL,
	`rating`	DOUBLE	NULL,
	`store_id`	INT	NULL,
	`product_id`	INT	NULL,
	`img`	TEXT	NULL,
	`written_date`	DATETIME	NULL,
	`r_status`	BOOL	NULL
);

CREATE TABLE `review_backup` (
	`id`	INT	NOT NULL,
	`contents`	VARCHAR(500)	NULL,
	`rating`	DOUBLE	NULL,
	`store_id`	INT	NULL,
	`product_id`	INT	NULL,
	`img`	TEXT	NULL,
	`written_date`	DATETIME	NULL,
	`r_status`	BOOL	NULL,
    'deleted_date' DATETIME NULL
);

CREATE TABLE `user_address` (
	`user_idx`	INT	NOT NULL,
	`address_idx`	INT	NOT NULL
);

CREATE TABLE `order_product` (
	`order_id`	INT	NOT NULL,
	`product_id`	INT	NOT NULL,
	`quantity`	INT	NOT NULL
);

ALTER TABLE `orders` ADD CONSTRAINT `PK_ORDERS` PRIMARY KEY (
	`idx`
);

ALTER TABLE `address` ADD CONSTRAINT `PK_ADDRESS` PRIMARY KEY (
	`idx`
);

ALTER TABLE `user` ADD CONSTRAINT `PK_USER` PRIMARY KEY (
	`idx`
);

ALTER TABLE `store` ADD CONSTRAINT `PK_STORE` PRIMARY KEY (
	`id`
);

ALTER TABLE `product` ADD CONSTRAINT `PK_PRODUCT` PRIMARY KEY (
	`id`
);

ALTER TABLE `review` ADD CONSTRAINT `PK_REVIEW` PRIMARY KEY (
	`id`
);

ALTER TABLE `review_backup` ADD CONSTRAINT `PK_REVIEW_BACKUP` PRIMARY KEY (
	`id`
);

ALTER TABLE `user_address` ADD CONSTRAINT `PK_USER_ADDRESS` PRIMARY KEY (
	`user_idx`,
	`address_idx`
);

ALTER TABLE `order_product` ADD CONSTRAINT `PK_ORDER_PRODUCT` PRIMARY KEY (
	`order_id`,
	`product_id`
);

ALTER TABLE `user_address` ADD CONSTRAINT `FK_user_TO_user_address_1` FOREIGN KEY (
	`user_idx`
)
REFERENCES `user` (
	`idx`
);

ALTER TABLE `user_address` ADD CONSTRAINT `FK_address_TO_user_address_1` FOREIGN KEY (
	`address_idx`
)
REFERENCES `address` (
	`idx`
);

ALTER TABLE `order_product` ADD CONSTRAINT `FK_orders_TO_order_product_1` FOREIGN KEY (
	`order_id`
)
REFERENCES `orders` (
	`idx`
);

ALTER TABLE `order_product` ADD CONSTRAINT `FK_product_TO_order_product_1` FOREIGN KEY (
	`product_id`
)
REFERENCES `product` (
	`id`
);

---------------------------------------------------------------------------------------------
-- orders 테이블 더미 데이터

INSERT INTO orders (idx, address, store_idx, product_id, order_price, delivery_price, discount_price, total_price) VALUES
(1, '서울특별시 강남구', 1, 1, 10000, 3000, 1000, 12000),
(2, '서울특별시 서초구', 2, 2, 20000, 4000, 2000, 22000),
(3, '서울특별시 송파구', 3, 3, 30000, 5000, 3000, 32000);
-- address 테이블 더미 데이터
INSERT INTO address (idx, address, detail_address, user_idx, create_at, updated_at, r_status) VALUES
(1, '서울특별시 강남구', '삼성동 123-45', 1, '2024-07-01 10:00:00', '2024-07-15 10:00:00', 'active'),
(2, '서울특별시 서초구', '서초동 678-90', 2, '2024-07-02 11:00:00', '2024-07-16 11:00:00', 'active'),
(3, '서울특별시 송파구', '잠실동 111-22', 3, '2024-07-03 12:00:00', '2024-07-17 12:00:00', 'active');
-- user 테이블 더미 데이터
INSERT INTO user (idx, email, password, name, phone, address_idx, pay_type) VALUES
(1, 'user1@example.com', 'password1', '홍길동', '010-1234-5678', 1, 'card'),
(2, 'user2@example.com', 'password2', '이순신', '010-2345-6789', 2, 'cash'),
(3, 'user3@example.com', 'password3', '김유신', '010-3456-7890', 3, 'card');
-- store 테이블 더미 데이터
INSERT INTO store (id, name, phone, address, introduction, rocket, delivery_time) VALUES
(1, '스토어1', '02-123-4567', '서울특별시 강남구 삼성동', '이것은 스토어1 입니다.', TRUE, '30분'),
(2, '스토어2', '02-234-5678', '서울특별시 서초구 서초동', '이것은 스토어2 입니다.', FALSE, '40분'),
(3, '스토어3', '02-345-6789', '서울특별시 송파구 잠실동', '이것은 스토어3 입니다.', TRUE, '50분');
-- product 테이블 더미 데이터
INSERT INTO product (id, field, price, introduction, remain, store_id) VALUES
(1, '전자제품', 100000, '이것은 전자제품입니다.', 10, 1),
(2, '가구', 200000, '이것은 가구입니다.', 20, 2),
(3, '의류', 300000, '이것은 의류입니다.', 30, 3);
-- review 테이블 더미 데이터
INSERT INTO review (id, contents, rating, store_id, product_id, img, written_date, r_status) VALUES
(1, '좋아요!', 5.0, 1, 1, 'image1.jpg', '2024-07-01 10:00:00', TRUE),
(2, '별로에요.', 2.0, 2, 2, 'image2.jpg', '2024-07-02 11:00:00', TRUE),
(3, '그저 그래요.', 3.0, 3, 3, 'image3.jpg', '2024-07-03 12:00:00', TRUE);
-- user_address 테이블 더미 데이터
INSERT INTO user_address (user_idx, address_idx) VALUES
(1, 1),
(2, 2),
(3, 3);
-- order_product 테이블 더미 데이터
INSERT INTO order_product (order_id, product_id, quantity) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3);

------------------------------------------------------------------------------------------------------
-- review backup 프로시저

DELIMITER //
CREATE PROCEDURE delete_review(IN reviewId INT)
BEGIN
    -- 1. 리뷰 상태를 FALSE로 변경 (논리적 삭제)
    UPDATE review
    SET r_status = FALSE
    WHERE id = reviewId;
	
    -- 2. REVIEW2 테이블에 리뷰 복사
    -- review_status가 TRUE에서 FALSE로 변경된 경우에만 복사
    IF (ROW_COUNT() > 0) THEN
        INSERT INTO review_backup (
			id,
            contents,
            rating,
            store_id,
            product_id,
            img,
            written_date,
            r_status,
            delete_date
		)
        SELECT
			id,
			contents,
            rating,
            store_id,
            product_id,
            img,
            written_date,
            r_status,
            now()
        FROM review
        WHERE id = reviewId;
    END IF;
END //
DELIMITER ;
-- 구현 순서
-- 1. reviewID에 넣기
-- 변수 선언 SET @test_reviewID = 123;
SET @test_reviewID = 1;
-- 2. 프로시져 콜하기
-- CALL delete_review(@test_reviewID)
CALL delete_review(@test_reviewID);
-- 3.기존 review table에서 review_status가 FALSE인걸 확인
SELECT ID, r_status FROM review WHERE id = @test_reviewID;
— 3.1)
select * from	review;
-- 4. review 백업 테이블에 복사가 되었는지 확인
SELECT * FROM review_backup;
