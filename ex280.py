import random


class Account:
    # class variable
    account_count = 0

    def __init__(self, name, balance):
        self.deposit_count = 0
        self.deposit_log = []      #입금 내역
        self.withdraw_log = []     #출금 내역

        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        # 3-2-6
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  # Account.account_count

    def deposit(self, amount):
        if amount >= 1:
            self.deposit_log.append(amount)  #입금 내역 입력
            self.balance += amount

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:         # 5, 10, 15
                # 이자 지금
                self.balance = (self.balance * 1.01)


    def withdraw(self, amount):
        if self.balance > amount:
            self.withdraw_log.append(amount)   #출금 내역 입력
            self.balance -= amount

    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

    def withdraw_history(self):
        for amount in self.withdraw_log:   #출금한 내역 가져오기
            print(amount)                  #출금

    def deposit_history(self):
        for amount in self.deposit_log:    #입금한 내역 가져오기
            print(amount)                   #입금


k = Account("Kim", 1000)    #kim 계좌에 천원있음
k.deposit(100)              #100원 입금
k.deposit(200)              #200원 입금
k.deposit(300)              #300원 입금
k.deposit_history()         #입금 내역

k.withdraw(100)             #100원 출금
k.withdraw(200)             #200원 출금
k.withdraw_history()        #출금