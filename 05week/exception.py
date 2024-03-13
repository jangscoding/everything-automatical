# 존재하지 않는 파일을 읽기 모드로 여는 경우 : 
# myFile = open('NotExist.txt','r')

# 잘못된 접근 : IndexError 후 종료 
# myList = [1,2,3]
# print(myList[3])

# 예외처리 : try ~ except
try:
    myFile = open('NotExist.txt', 'r')
except FileNotFoundError as e:
    print('파일이 존재하지 않습니다.')
    print(e)

try:
    myList =[1,2,3]
    print(myList[3])
except IndexError as e:
    print('리스트의 인덱스가 존재하지 않습니다.')
    print(e)

try:
    print('Hello world!')
    raise Exception('My Exception')
except Exception as e:
    print(e)

# 예외처리 : try ~ except ~ finally 
# 여러개의 예외를 한번에 처리하려면 튜플로 묶어서 처리 할 수 있음
# except (FileNotFoundError, IndexError, ZeroDivisionError) as e:
try:
    myFile_1 = open('example.txt','w')
    myFile_1.write('Hello world!')
    myList = [1,2,3]
    result = myList[3] / 0
    print(result)
except FileNotFoundError as e:
    print('파일이 존재하지 않습니다.')
    print(e)
