import tkinter

# 글꼴 설정
FNT1 = ("@Yu Gothic", 12)  # 글꼴 사용, 크기 12
FNT2 = ("Times New Roman", 24)  # 글꼴 사용, 크기 24

# 영어와 한국어 단어 목록
WORDS = ["apple", "사과", "book", "책", "cat", "고양이", "dog", "개",
         "elephant", "코끼리", "flower", "꽃", "giraffe", "기린", "house", "집",
         "ice cream", "아이스크림", "juice", "주스", "kite", "연", "lion", "사자",
         "monkey", "원숭이", "nose", "코", "orange", "오렌지", "pencil", "연필",
         "queen", "여왕", "rabbit", "토끼", "sun", "태양", "ear", "귀"]

MAX = int(len(WORDS)/2)  # 단어 쌍의 총 개수 계산 (20개)
score = 0  # 점수 초기화
word_num = 0  # 현재 단어 인덱스 초기화
yourword = ""  # 사용자 입력 단어 초기화
koff = False  # 키 입력 플래그, 키가 눌린 후 올라옴을 감지하기 위함
incorrect_attempts = 0  # 틀린 시도 횟수

# 게임 종료 함수
def end_game():
    global root
    root.destroy()  # Tkinter 창 닫기

# 게임 중단 함수
def pause_game():
    global score
    message_label["text"] = f"게임 중단!\n총 점수: {score}\n[Enter] 키를 눌러서 게임을 종료해 주세요."
    root.bind("<KeyPress>", lambda e: end_game() if e.keysym == "Return" else None)  # Enter 키 이벤트 바인딩으로 게임 종료 조건 설정

# 키 입력 처리 함수
def key_down(e):
    global score, word_num, yourword, koff, incorrect_attempts
    kcode = e.keycode  # 눌린 키의 코드
    ksym = e.keysym  # 눌린 키의 심볼
    if ksym in ["Escape", "Pause"]:  # ESC 또는 Pause 키 처리
        pause_game()
    else:
        if 65 <= kcode <= 90:  # 대문자 알파벳
            yourword += chr(kcode + 32)  # 소문자로 변환하여 추가
        elif 97 <= kcode <= 122:  # 소문자 알파벳
            yourword += chr(kcode)  # 그대로 추가
        elif ksym == "space":  # 공백 처리
            yourword += " "
        elif ksym in ["Delete", "BackSpace"]:  # 삭제 키 처리
            yourword = yourword[:-1]  # 마지막 문자 삭제
        input_label["text"] = yourword  # 입력 라벨 업데이트
        if ksym == "Return":  # Enter 키 처리
            if incorrect_attempts >= 3:  # 3번 이상 틀린 경우
                message_label["text"] = f"게임 종료!\n총 점수: {score}\n[Enter] 키를 눌러서 게임을 종료해 주세요."
                root.bind("<KeyPress>", lambda e: end_game() if e.keysym == "Return" else None)
            else:
                if input_label["text"] == WORDS[word_num * 2]:  # 정답 확인
                    score += 1
                    incorrect_attempts = 0
                    word_num += 1
                    set_label()  # 라벨 업데이트
                else:
                    incorrect_attempts += 1
                    message_label["text"] = "응? 눈 감고 입력했어? 다시 입력해봐!"
                    yourword = ""
                    input_label["text"] = ""

# 키 해제 처리 함수
def key_up(e):
    global koff
    koff = True  # 키가 올라왔음을 표시

# 라벨 설정 함수
def set_label():
    global word_num, yourword
    if word_num >= MAX:  # 모든 단어를 입력한 경우
        message_label["text"] = f"모든 단어를 입력했습니다!\n총 점수: {score}\n[Enter] 키를 눌러서 게임을 종료해 주세요."
        root.bind("<KeyPress>", lambda e: end_game() if e.keysym == "Return" else None)
    else:
        score_label["text"] = f"점수: {score}"
        english_label["text"] = WORDS[word_num * 2]  # 현재 영어 단어
        korean_label["text"] = WORDS[word_num * 2 + 1]  # 해당 한국어 단어
        input_label["text"] = ""
        message_label["text"] = ""
        yourword = ""

# Tkinter GUI 설정
root = tkinter.Tk()
root.title("Voca Game For Beginner")  # 창 제목 설정
root.geometry("450x350")  # 창 크기 설정
root.resizable(False, False)  # 창 크기 조절 비활성화
root.bind("<KeyPress>", key_down)  # 키 입력 이벤트 바인딩
root.bind("<KeyRelease>", key_up)  # 키 해제 이벤트 바인딩
root["bg"] = "#DEF"  # 배경색 설정

# 점수 라벨 설정
score_label = tkinter.Label(font=FNT1, bg="#DEF", fg="#4C0")
score_label.pack()

# 영어 단어 라벨 설정
english_label = tkinter.Label(font=FNT2, bg="#DEF")
english_label.pack()

# 한국어 단어 라벨 설정
korean_label = tkinter.Label(font=FNT1, bg="#DEF", fg="#444")
korean_label.pack()

# 사용자 입력 라벨 설정
input_label = tkinter.Label(font=FNT2, bg="#DEF")
input_label.pack()

# 메시지 라벨 설정
message_label = tkinter.Label(font=FNT1, bg="#DEF", fg="#af0000")
message_label.pack()

# 설명 라벨 설정
howto_label = tkinter.Label(text="[실행방법]\n1. 영어 단어를 입력하고 [Enter] 키를 누릅니다.\n2. 입력을 수정할 때는 [Delete] 또는 [BackSpace]을 누릅니다.\n3. 게임 중단을 원하면 [Escape] 키 또는 [Pause] 키를 누릅니다.\n4. 단어를 3번 넘게 틀릴 경우, 게임 종료!", font=FNT1, bg="#FFF", fg="#00af5f")
howto_label.pack()

# 초기 라벨 설정
set_label()

# Tkinter 이벤트 루프 시작
root.mainloop()
