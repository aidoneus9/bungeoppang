# 붕어빵 가격
price = dict(zip(["팥붕어빵", "슈크림붕어빵", "초코붕어빵"], [800, 700, 900]))

def calculate_sales():
    total_sales = sum(sales[key] * price[key] for key in sales)
    # total_sales = sum(sales[i] * price[i] for i, _ in zip(sales, price))
    print(f"오늘의 총 매출 💰: {total_sales}")

while True:
    print("주문 | 관리자 | 종료")
    mode = input("원하시는 모드를 입력해 주세요: ")
    
    # 유효성 검사 
    if mode not in ["주문", "관리자", "종료"]:
        print("주문, 관리자, 종료 중에서 입력해 주세요.")
        continue
    
    # 종료 조건 
    elif mode == "종료":
        print("서비스 종료 중...")
        break
    
    elif mode == "주문":
        order_bungeoppang()
   
    elif mode == "관리자":
        admin_mode()

calculate_sales()