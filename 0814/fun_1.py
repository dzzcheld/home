#def 함수이름():
#실행 전에는 정의만 되어있다
def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):
    print("임급이 완료되었습니다 잔액은 {0}원 입니다" .format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance>=money:
        print("출금이 완료되었습니다. 잔액은 {0} 원 입니다" .format(balance))
        return balance-money
    else:
        print("출급이 완료되지 않았습니다. 잔액은 {0} 원 입니다.".format(balance))
        return balance

def withdrwa_night(balance, money):
    commission=100
    return commission, balance-money-commission

balance=0
balance = deposit(balance, 1000)
print(balance)

# balance=withdraw(balance,500)
commission, balance=withdrwa_night(balance,500)
print("수수료{0} 원이며, 잔액은 {1} 원입니다" .format(commission, balance))