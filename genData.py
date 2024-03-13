import random 
#점수를 계산해서 평균에 따른 학점을 반환
#편의상 A,B,C로 구분함. 
def calcGrade(kor,math):
    mean = int((kor+ math)/2)
    grade = "C"
    if 70 <= mean:
        grade = "A"
    elif 40<= mean:
        geade = "B"
    return mean,grade
# 100개 데이터를 만들어 CSV에 기록한다. 
fp = open("data.csv","w", encoding = "utf-8")
for i in range (1000):
    kor = random.randint(10,100)
    math = random.randint(10,100)
    mean,grade = calcGrade (kor,math)
    fp.write("{0},{1},{2},{3},{4}/r/n".format(i,kor,math,mean,grade))
fp.close()
print("Done")


