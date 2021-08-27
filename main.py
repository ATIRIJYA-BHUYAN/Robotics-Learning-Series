class Game:#add a class
    # game="choose a number"
    def number(self):
        print(self.num)
    def game1(self):
        if (self.num1==self.Num1):
            print(f"{self.Num1} is in right position")
    def game2(self):
        if (self.num2==self.Num2):
            print(f"{self.Num2} is in the right position")
    def game3(self):
        if (self.num3==self.Num3):
            print(f"{self.Num3} is in the right position")
    def game4(self):
        if (self.num4==self.Num4):
            print(f"{self.Num4} is in the  right position")
    def game5(self):
        if(self.Num1==self.num2 or self.Num1==self.num3 or self.Num1==self.num4):
            print(f"{self.Num1} is in the wrong position")
    def game6(self):
        if(self.Num2==self.num1 or self.Num2==self.num3 or self.Num2==self.num4):
            print(f"{self.Num2} is in the wrong position")
    def game7(self):
        if(self.Num3==self.num2 or self.Num3==self.num1 or self.Num3==self.num4):
            print(f"{self.Num3} is in the wrong position")
    def game8(self):
        if(self.Num4==self.num2 or self.Num4==self.num3 or self.Num4==self.num1):
            print(f"{self.Num4} is in the wrong position")
    def score(self):
        print(f"{self.point}  Your final score")

limit=1
import random#import random module
game=Game()
game.num = random.randint(1000,9999)#auto-choose 4digit number
game.number()
game.point=20
game.your_turn=int(input("Guess a number: "))#Enter your number
while limit<=10:
    if game.num==game.your_turn:
        game.point+=5
        game.num = random.randint(1000,9999)
        game.number()

    else:
        game.Num1=int(game.your_turn)%10
        game.Num2=(int(game.your_turn)//10)%10
        game.Num3=(int(game.your_turn)//100)%10
        game.Num4=(int(game.your_turn)//1000)%10

        game.num1=int(game.num)%10
        game.num2=(int(game.num)//10)%10
        game.num3=(int(game.num)//100)%10
        game.num4=(int(game.num)//1000)%10

        game.game1()
        game.game2()
        game.game3()
        game.game4()
        game.game5()
        game.game6()
        game.game7()
        game.game8()
        game.point-=2
        game.your_turn=int(input("Guess a number: "))
    limit+=1
game.score()

