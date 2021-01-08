import random

def random_text(data):
    number = random.randint(0, len(data)-1)
    return data[number]

data = ["와냐!", "와냐...", "와냐?", "와냐.", "와냐! 와냐!", "와..냐", "와냐~", "와냐냐!", "와냐!!!!"]
endFlag = 0
print("와들디와 연결되었습니다.")
print("대화를 끝내고 싶으면 '잘 가!'라고 입력해 주세요!")
while(endFlag == 0):
    yourText = input("당신: ")
    if(yourText == "잘 가!"):
        endflag = 1
        break
    print("와들디: "+random_text(data))
print("와들디: 와냐와냐~")
