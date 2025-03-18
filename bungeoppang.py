# 🛠️ 보완 사항:
# 관리자 모드에서 한 번 종료 시 전체 종료되도록 하기 
# 현재 재고 출력 시 예쁘게 출력되도록 하기 (line 50)
# 재고에 새로운 종료의 붕어빵 출시되었을 때 (코드 완전 수정) 

# 📦 붕어빵 재고와 판매
stock = dict(zip(["팥붕어빵", "슈크림붕어빵", "초코붕어빵"],[10, 8, 5]))
sales = dict(zip(["팥붕어빵", "슈크림붕어빵", "초코붕어빵"],[0, 0, 0]))

# 🙋🏻‍♂️ 주문 
def order_bungeoppang():
    while True:
        print("팥붕어빵 | 슈크림붕어빵 | 초코붕어빵")
        bungeoppang_type = input("🙋🏻‍♂️ 주문하실 붕어빵의 종류를 입력해 주세요 (또는 '뒤로가기'): ")

        if bungeoppang_type not in ["팥붕어빵", "슈크림붕어빵", "초코붕어빵", "뒤로가기"]:
            print("팥, 슈크림, 초코 또는 뒤로가기 중에서 입력해 주세요.")
            continue

        # 뒤로가기 
        if bungeoppang_type == "뒤로가기":
            break # return 
        
        # 🙋🏻‍♂️ 메뉴 주문
        if bungeoppang_type in stock: 
            bungeoppang_count = int(input(f"🙋🏻‍♂️ 주문하실 {bungeoppang_type}의 개수를 입력해 주세요: "))
            if stock[bungeoppang_type] >= bungeoppang_count:
                stock[bungeoppang_type] -= bungeoppang_count
                sales[bungeoppang_type] += bungeoppang_count
                print(f"{bungeoppang_type}을 {bungeoppang_count}개 주문하셨습니다. 고맙습니다 😄")
            else:
                print(f"죄송합니다. {bungeoppang_type}은 재고가 부족합니다 😭 현재 {stock[bungeoppang_type]}개만 주문 가능합니다.")
################################
# 🤖 관리자
def admin_mode():
    while True:
        print("팥붕어빵 | 슈크림붕어빵 | 초코붕어빵")
        bungeoppang_type = input("🙋🏻‍♂️ 추가하실 붕어빵의 종류를 입력해 주세요 (또는 '종료')")
        
        if bungeoppang_type not in ["팥붕어빵", "슈크림붕어빵", "초코붕어빵", "종료"]:
            print("팥, 슈크림, 초코 또는 종료 중에서 입력해 주세요.")
            continue

        # 종료 조건 
        if bungeoppang_type == "종료":
            break

        if bungeoppang_type in stock:
            bungeoppang_count = int(input(f"🙋🏻‍♂️ 추가하실 {bungeoppang_type}의 개수를 입력해 주세요: "))
            stock[bungeoppang_type] += bungeoppang_count
            print(f"{bungeoppang_type}을 {bungeoppang_count}개 추가하셨습니다. 현재 재고: {stock}")
        else: 
            print("올바른 붕어빵의 종류를 입력해 주세요.")           
################################
# 붕어빵 가격
price = dict(zip(["팥붕어빵", "슈크림붕어빵", "초코붕어빵"], [800, 700, 900]))

def calculate_sales():
    total_sales = sum(sales[key] * price[key] for key in sales)
    # total_sales = sum(sales[i] * price[i] for i, _ in zip(sales, price))
    print(f"오늘의 총 매출 💰: {total_sales}")
#################################
# ✔️ 메인 (주문 / 관리자 / 종료 중 선택)
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
        order_bungeoppang() # 
   
    elif mode == "관리자":
        admin_mode()

calculate_sales()