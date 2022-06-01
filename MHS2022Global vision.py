#2022年文化祭グローバルビジョンロボットの位置表示ソフトのプログラム
#USB.txtファイルをこのファイルと同様のディレクトリに配置し、「COM5」のようにポート番号を半角で入力し保存する
#シリアル通信は、",ボールのX座標,Y座標,ロボット1のX座標,Y座標,ロボット2のX座標,Y座標,"の形式でPCに送ること、
import serial #シリアル通信用ライブラリ
import tkinter as tk #UI用ライブラリ
import math #数値計算用ライブラリ
import time
with open("USB.txt", "r", encoding="utf_8") as b:
    usb1 = b.read()
ser = serial.Serial(usb1, 2400) #シリアル通信設定
class set:
    def drow(self,a,b,c): #UI描画
        self.can1.delete("all")
        self.can1.create_rectangle(0, 0, 972, 760, fill="#007700", outline="#007700")
        self.can1.create_rectangle(100, 100, 872, 108, fill="#FFFFFF", outline="#FFFFFF")
        self.can1.create_rectangle(100, 621, 872, 629, fill="#FFFFFF", outline="#FFFFFF")
        self.can1.create_rectangle(100, 100, 108, 628, fill="#FFFFFF", outline="#FFFFFF")
        self.can1.create_rectangle(865, 100, 873, 628, fill="#FFFFFF", outline="#FFFFFF")
        self.can1.create_rectangle(108, 224, 148, 232, fill="#FFFFFF", outline="#FFFFFF")
        self.can1.create_rectangle(108, 496, 148, 504, fill="#FFFFFF", outline="#FFFFFF")
        self.can1.create_rectangle(825, 224, 865, 232, fill="#FFFFFF", outline="#FFFFFF")
        self.can1.create_rectangle(825, 496, 865, 504, fill="#FFFFFF", outline="#FFFFFF")
        self.can1.create_rectangle(200, 284, 208, 444, fill="#FFFFFF", outline="#FFFFFF")
        self.can1.create_rectangle(765, 284, 773, 444, fill="#FFFFFF", outline="#FFFFFF")
        self.can1.create_arc(88, 224, 208, 344, fill="#FFFFFF", outline="#FFFFFF")
        self.can1.create_arc(88, 233, 199, 344, fill="#007700", outline="#007700")
        self.can1.create_arc(88, 504, 208, 384, start=270, fill="#FFFFFF", outline="#FFFFFF")
        self.can1.create_arc(88, 495, 199, 384, start=270, fill="#007700", outline="#007700")
        self.can1.create_arc(765, 224, 885, 344, start=90, fill="#FFFFFF", outline="#FFFFFF")
        self.can1.create_arc(774, 233, 885, 344, start=90, fill="#007700", outline="#007700")
        self.can1.create_arc(765, 386, 885, 504, start=180, fill="#FFFFFF", outline="#FFFFFF")
        self.can1.create_arc(774, 386, 885, 495, start=180, fill="#007700", outline="#007700")
        self.can1.create_oval(366, 244, 603, 484, width=2, outline="#000000", fill="#007700")
        self.can1.create_rectangle(280, 244, 286, 250, fill="#000000", outline="#000000") #中立点描画
        self.can1.create_rectangle(687, 244, 693, 250, fill="#000000", outline="#000000")
        self.can1.create_rectangle(280, 476, 286, 484, fill="#000000", outline="#000000")
        self.can1.create_rectangle(687, 476, 693, 484, fill="#000000", outline="#000000")
        self.can1.create_rectangle(483, 361, 489, 367, fill="#000000", outline="#000000")
        self.can1.create_rectangle(50, 244, 100, 484, fill="#0000FF", outline="#0000FF") #中心円描画
        self.can1.create_rectangle(873, 244, 922, 484, fill="#FFFF00", outline="#FFFF00")
        if self.countR[0] < 10:
            self.can1.create_oval(self.ballx - 12, self.bally - 12, self.ballx + 12, self.bally + 12, outline="#FF3300",fill="#FF3300", tag="ball")
        if self.countR[1] < 10:
            self.can1.create_arc(self.bot1x - 36, self.bot1y - 36, self.bot1x + 36, self.bot1y + 36,
                                 start=self.bot1r + 30, extent=300, fill="#00CCCC", outline="#00CCCC")
            #"#660066紫"
            x1 = self.bot1x + 20
            y1 = self.bot1y - 20
            x2 = self.bot1x + 20
            y2 = self.bot1y + 20
            self.can1.create_polygon(self.bot1x, self.bot1y, x1, y1, x2, y2, fill="#00CCCC", outline="#00CCCC"
                                                                                                     "")
        #[ self.can1.create_oval(self.bot1x - 36, self.bot1y - 36, self.bot1x + 36, self.bot1y + 36, outline="#444444",fill="#444444", tag="bot1")
        if self.countR[2] < 10:
            self.can1.create_arc(self.bot2x - 36, self.bot2y - 36, self.bot2x + 36, self.bot2y + 36,
                                 start=self.bot2r + 30, extent=300, outline="#FF0461", fill="#FF0461", tag="bot2")
            x1 = self.bot2x - 20
            y1 = self.bot2y - 20
            x2 = self.bot2x - 20
            y2 = self.bot2y + 20
            print("a")
            self.can1.create_polygon(self.bot2x, self.bot2y, x1, y1, x2, y2, fill="#FF0461", outline="#FF0461")
        #self.tan1 = math.atan()
    def test(self):
        while True:
            val_arduino = ser.readline()
            if len(self.label) == 44:
                self.label.pop(0)
            if len(str(val_arduino))<40:
                self.label.append(str(val_arduino) + "\n")
                self.la2["text"] = "".join(self.label)
                a = str(val_arduino)
                data = a.split(",")
                if len(data) == 8:
                    data.pop(0)
                    data.pop(-1)
                    data = list(map(int, data))
                    c1=c2=c3=0
                    if len(data) == 6:
                        self.ballx = 972-math.floor(data[0]*1.25 * 3.03)
                        self.bally = 728-math.floor(data[1] * 3.03)
                        self.bot1x = 952-math.floor(data[2]*1.25 * 3.03)
                        self.bot1y = 708-math.floor(data[3]* 3.03)
                        self.bot2x = 952-math.floor(data[4]*1.25 * 3.03)
                        self.bot2y = 708-math.floor(data[5]* 3.03)
                    if data[0] == 0 and data[1] == 0:
                        c1 = 1
                        self.countR[0]+=1
                        self.ballx = 972 - math.floor(self.databack[0] * 1.25 * 3.03)
                        self.bally = 728 - math.floor(self.databack[1] * 3.03)
                    else:
                        self.countR[0]=0
                        self.databack[0] = data[0]
                        self.databack[1] = data[1]
                    if data[2] == 0 and data[3] == 0:
                        c2 = 1
                        self.countR[1]+=1
                        self.bot1x = 952 - math.floor(self.databack[2] * 1.25 * 3.03)
                        self.bot1y = 708 - math.floor(self.databack[3] * 3.03)
                    else:
                        self.countR[1]=0
                        self.databack[2] = data[2]
                        self.databack[3] = data[3]
                    if data[4] == 0 and data[5] == 0:
                        c3 = 1
                        self.countR[2]+=1
                        self.bot2x = 952 - math.floor(self.databack[4] * 1.25 * 3.03)
                        self.bot2y = 708 - math.floor(self.databack[5] * 3.03)
                    else:
                        self.countR[2]=0
                        self.databack[4] = data[4]
                        self.databack[5] = data[5]
                    set.drow(self,c1,c2,c3)
                    self.can1.update()
                # self.win.after(1, self.test)


        #print(val_arduino)



    def __init__(self):
        self.countR=[0,0,0]
        self.databack = [0,0,0,0,0,0]
        self.tan1 = 0
        self.tan2 = 0
        self.tan3 = 0
        self.tan4 = 0
        self.label = []
        self.time1 = 0
        self.a = 1
        self.ballx = 500
        self.bally = 400
        self.bot1x = 300
        self.bot1y = 300
        self.bot2x = 400
        self.bot2y = 400
        self.bot1r = 0
        self.bot2r = 180
        self.win = tk.Tk()
        self.win.title("test")
        self.win.geometry("1360x728")
        self.win.configure(bg="#000000")
        self.can1 = tk.Canvas(width=972, height=760, bg="#007700")
        self.la1 = tk.Label(text="Arduino"+usb1,bg="#000000",fg="#FF69B4",font=("",10))
        self.la1.place(x=980,y=2)
        self.la2 = tk.Label(text="", bg="#000000", fg="#00ffff", font=("", 12),justify='left')
        self.la2.place(x=980, y=20)
        self.can1.place(x=-2, y=-2)
        self.can1.create_rectangle(0, 0, 972, 760, fill="#007700", outline="#007700")
        self.can1.create_rectangle(100, 100, 872, 108, fill="#FFFFFF", outline="#FFFFFF")
        self.can1.create_rectangle(100, 621, 872, 629, fill="#FFFFFF", outline="#FFFFFF")
        self.can1.create_rectangle(100, 100, 108, 628, fill="#FFFFFF", outline="#FFFFFF")
        self.can1.create_rectangle(865, 100, 873, 628, fill="#FFFFFF", outline="#FFFFFF")
        self.can1.create_rectangle(108, 224, 148, 232, fill="#FFFFFF", outline="#FFFFFF")
        self.can1.create_rectangle(108, 496, 148, 504, fill="#FFFFFF", outline="#FFFFFF")
        self.can1.create_rectangle(825, 224, 865, 232, fill="#FFFFFF", outline="#FFFFFF")
        self.can1.create_rectangle(825, 496, 865, 504, fill="#FFFFFF", outline="#FFFFFF")
        self.can1.create_rectangle(200, 284, 208, 444, fill="#FFFFFF", outline="#FFFFFF")
        self.can1.create_rectangle(765, 284, 773, 444, fill="#FFFFFF", outline="#FFFFFF")
        self.can1.create_arc(88, 224, 208, 344, fill="#FFFFFF", outline="#FFFFFF")
        self.can1.create_arc(88, 233, 199, 344, fill="#007700", outline="#007700")
        self.can1.create_arc(88, 504, 208, 384, start=270, fill="#FFFFFF", outline="#FFFFFF")
        self.can1.create_arc(88, 495, 199, 384, start=270, fill="#007700", outline="#007700")
        self.can1.create_arc(765, 224, 885, 344, start=90, fill="#FFFFFF", outline="#FFFFFF")
        self.can1.create_arc(774, 233, 885, 344, start=90, fill="#007700", outline="#007700")
        self.can1.create_arc(765, 386, 885, 504, start=180, fill="#FFFFFF", outline="#FFFFFF")
        self.can1.create_arc(774, 386, 885, 495, start=180, fill="#007700", outline="#007700")
        self.can1.create_oval(366, 244, 603, 484, width=2, outline="#000000", fill="#007700")
        self.can1.create_rectangle(280, 244, 286, 250, fill="#000000", outline="#000000")
        self.can1.create_rectangle(687, 244, 693, 250, fill="#000000", outline="#000000")
        self.can1.create_rectangle(280, 476, 286, 484, fill="#000000", outline="#000000")
        self.can1.create_rectangle(687, 476, 693, 484, fill="#000000", outline="#000000")
        self.can1.create_rectangle(483, 361, 489, 367, fill="#000000", outline="#000000")
        self.can1.create_rectangle(50, 244, 100, 484, fill="#0000FF", outline = "#0000FF")
        self.can1.create_rectangle(873, 244, 922, 484, fill="#FFFF00", outline="#FFFF00")
        self.can1.create_oval(self.ballx-12, self.bally-12, self.ballx+12, self.bally+12, outline="#FF3300", fill="#FF3300", tag="ball")
        #self.can1.create_oval(self.bot1x - 36, self.bot1y - 36, self.bot1x + 36, self.bot1y + 36, outline="#444444",fill="#444444", tag="bot1")
        self.can1.create_arc(self.bot1x - 36, self.bot1y - 36, self.bot1x + 36, self.bot1y + 36, start=self.bot1r+30, extent=300, fill="#444444", outline="#444444")
        x1 = self.bot1x - 20
        y1 = self.bot1y - 20
        x2 = self.bot1x - 20
        y2 = self.bot1y + 20
        self.can1.create_polygon(self.bot1x, self.bot1y,x1, y1, x2, y2, fill="#444444", outline="#444444")
        self.can1.create_arc(self.bot2x - 36, self.bot2y - 36, self.bot2x + 36, self.bot2y + 36, start=self.bot2r+30, extent=300, outline="#999999",fill="#999999", tag="bot2")
        x1 = self.bot2x + 20
        y1 = self.bot2y - 20
        x2 = self.bot2x + 20
        y2 = self.bot2y + 20
        self.can1.create_polygon(self.bot2x, self.bot2y, x1, y1, x2, y2, fill="#999999", outline="#999999")
        set.test(self)
        self.win.mainloop()
app = set()