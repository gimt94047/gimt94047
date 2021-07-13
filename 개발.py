
import tkinter.messagebox as msgbox # import TK
import tkinter.ttk as ttk
from tkinter import *

root = Tk() # 제목, 해상도
root.title("오늘할일") 
root.geometry("370x370") 

def btncmd(): # 버튼
    print(combobox.get()) # 선택된 갚 표시
    print(readonly_combobox.get())
    txt.delete("1.0", END)

def info(): # 정보창
    msgbox.showinfo("정보", "메모장")

menu = Menu(root)

# File 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="새로운 파일", command=btncmd)
menu_file.add_command(label="새로운 창", state="disable")
menu_file.add_separator()
menu_file.add_command(label="파일 열기...", state="disable")
menu_file.add_separator()
menu_file.add_command(label="모두 저장", state="disable") # 비활성화
menu_file.add_separator()
menu_file.add_command(label="나가기", command=root.quit)

menu.add_cascade(label="파일", menu=menu_file)

menu.add_cascade(label="설정")

menu_lang = Menu(menu, tearoff=0) # 언어 설정
menu_lang.add_radiobutton(label="한국어")
menu.add_cascade(label="언어", menu=menu_lang)

menu_file.add_separator()

menu_help = Menu(menu, tearoff=0) # 정보창
menu_help.add_command(label="정보", command=info)
menu.add_cascade(label="도움말", menu=menu_help)


label1 = Label(root, text="오늘 할일")
label1.pack()

values1 = [str(i) + "월" for i in range(1,13)] # 월, 일 선택

values = [str(i) + "일" for i in range(1,32)] # 1 ~ 31 까지의 숫자

combobox = ttk.Combobox(root, height=10, values=values1, state="combobox") #읽기 전용
combobox.current(0) # 0번째 인덱스 값 선택
combobox.pack()

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly") #읽기 전용
readonly_combobox.current(0) # 0번째 인덱스 값 선택
readonly_combobox.pack()

txt = Text(root, width=45, height=20) # 텍스트창 사이즈
txt.insert(END, "오늘 할일은?")
txt.pack()



root.config(menu=menu)
root.mainloop()

