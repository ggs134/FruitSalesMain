#-*- coding: utf-8 -*-

class FruitSeller:
    def __init__(self, money, appleNum, price):
        self.my_money=money
        self.num_of_apple=appleNum
        self.APPLE_PRICE=price
    def saleApple(self, money):
        self.num=money/self.APPLE_PRICE
        self.num_of_apple-=self.num
        self.my_money+=money
        return self.num
    def showSaleResult(self):
        print "남은 사과는 %d입니다."%(self.num_of_apple)
        print "판매 수익 : %d"%(self.my_money)


class FruitBuyer:
    def __init__(self, money):
        self.myMoney=money
        self.numOfApple=0
    def buyApple(self, seller, money):
        self.numOfApple+=seller.saleApple(money)
        self.myMoney-=money
    def showBuyResult(self):
        print "잔액 : %d"%(self.myMoney)
        print "사과 갯수 : %d"%(self.numOfApple)


if __name__=="__main__":
    seller1=FruitSeller(0,30,1500)
    seller2=FruitSeller(0,20,1000)

    buyer=FruitBuyer(10000)
    buyer.buyApple(seller1, 4500)
    buyer.buyApple(seller2, 2000)

    print "status of seller1"
    seller1.showSaleResult()

    print "status of seller2"
    seller2.showSaleResult()

    print "status of buyer"
    buyer.showBuyResult()
