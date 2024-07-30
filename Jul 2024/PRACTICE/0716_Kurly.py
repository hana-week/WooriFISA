class Product:
    
    def __init__(self, name, price):
        # 제품의 이름과 가격을 초기화
        self.name = name
        self.price = price


class Plain:
    
    def __init__(self, points_rate=0.005):
        # 기본 포인트 적립 비율을 설정 (0.5%)
        self.points_rate = points_rate
        # 사용 가능한 쿠폰 수 초기화
        self.coupons = 0
        # 쿠폰 할인 금액 설정
        self.coupon_discount = 5000
        
    def buy(self, product, quantity):
        # 제품이 Product 클래스의 인스턴스인지 확인
        if not isinstance(product, Product):
            return "바코드를 읽을 수 없습니다."
        # 총 가격 계산
        total_price = product.price * quantity
        # 쿠폰 할인 적용
        total_price = self.apply_coupon_discount(total_price)
        # 적립금 계산
        points = total_price * self.points_rate
        # 결과 문자열 생성
        result = f"{quantity}개의 {product.name}(을)를 구매하셨습니다.\
        총 금액: {total_price:.2f}원, 적립금: {points:.2f}원"
        # 추가 혜택 적용
        result = self.apply_additional_benefits(product, quantity, total_price, points, result)
        return result
        
    def apply_additional_benefits(self, product, quantity, total_price, points, result):
        # 기본 클래스에서는 추가 혜택이 없음
        return result
        
    def use_coupon(self):
        # 쿠폰 사용 가능 여부 확인 및 사용
        if self.coupons > 0:
            self.coupons -= 1
            return True
        else:
            return False
            
    def apply_coupon_discount(self, total_price):
        # 쿠폰을 사용하여 총 가격에서 할인 적용
        if self.use_coupon():
            total_price -= self.coupon_discount
            # 가격이 음수가 되지 않도록 조정
            if total_price < 0:
                total_price = 0
        return total_price


class Friends(Plain):
    
    def __init__(self, points_rate=0.01, coupon_threshold=6000):
        # 기본 클래스 초기화 및 포인트 적립 비율, 쿠폰 기준 금액 설정
        super().__init__(points_rate)
        self.coupon_threshold = coupon_threshold
        
    def apply_additional_benefits(self, product, quantity, total_price, points, result):
        # 총 가격이 쿠폰 기준 금액 이상이면 쿠폰 발급
        if total_price >= self.coupon_threshold:
            self.coupons += 1
            result += " 할인쿠폰이 발급되었습니다."
        return result


class Purple(Friends):
    
    def __init__(self, points_rate=0.07, coupon_threshold=10000, review_bonus=2.0):
        # 기본 클래스 초기화 및 포인트 적립 비율, 쿠폰 기준 금액, 후기 보너스 설정
        super().__init__(points_rate, coupon_threshold)
        self.review_bonus = review_bonus
        
    def apply_additional_benefits(self, product, quantity, total_price, points, result):
        # 부모 클래스의 추가 혜택 적용
        result = super().apply_additional_benefits(product, quantity, total_price, points, result)
        # 후기 적립금 추가
        result += f" 더블 후기 적립금: {points * self.review_bonus:.2f}원"
        return result
