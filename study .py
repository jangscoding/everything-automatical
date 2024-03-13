treeHit = 0 
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." %treeHit)
    if treeHit == 10:
        print ("나무 넘어갑니다. ")

coffe = 10
money = 500
while money:
    print("돈을 받았으니 커피를 줍니다. ")
    coffe = coffe - 1
    print("남은 커피의 양은 %d개 입니다." %coffe)

    if not coffe:
        print("커피가 다 떨어졌습니다. ")
        break