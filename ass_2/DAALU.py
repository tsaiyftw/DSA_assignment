import tkinter as tk
import os, platform

#####################################################################################
filename = os.path.join("./warehouse", "game_canvas.py")
exec(open(filename, "r", encoding="utf-8").read(), globals())
# define the functions
def DAALUButton1RUN():
    global DAALUText1
    global DAALUButton2
    global DAALUCanvas1
    sss = """<html><head><title>DAALU</title></head><body><!--CONTENTSCONTENTSCONTENS--></body></html>"""
    sss = sss.replace(
        "<!--CONTENTSCONTENTSCONTENS-->",
        DAALUText1.get(1.0, tk.END) + "\n" + "<!--CONTENTSCONTENTSCONTENS-->",
    )
    for i in range(100):
        s4, t4 = PAGES(i)  ### strings
        if s4 != []:
            sss = sss.replace(
                "<!--CONTENTSCONTENTSCONTENS-->",
                "<BR><li>" + s4 + "</li><BR>\n" + "<!--CONTENTSCONTENTSCONTENS-->",
            )
            if t4 != []:
                sss = sss.replace(
                    "<!--CONTENTSCONTENTSCONTENS-->",
                    "<BR><img src=./warehouse/"
                    + t4
                    + ' width="50%" height="50%">\n'
                    + "<!--CONTENTSCONTENTSCONTENS-->",
                )
    filename = os.path.join("./warehouse", "NEW106.csv")
    ccc = [[] for i in range(6)]  ### 2-D list

    import csv

    sss = sss.replace(
        "<!--CONTENTSCONTENTSCONTENS-->",
        "<BR><table border=1>\n" + "<!--CONTENTSCONTENTSCONTENS-->",
    )
    with open(filename, newline="", encoding="utf-8") as csvfile:
        rows = csv.reader(csvfile)
        i = 0
        for row in rows:
            uuu = "<tr>"
            for j in range(6):
                ccc[j].append(row[j])
                uuu = uuu + "<td>" + row[j] + "</td>"
            i = i + 1
            uuu = uuu + "</tr>"
            sss = sss.replace(
                "<!--CONTENTSCONTENTSCONTENS-->",
                uuu + "\n" + "<!--CONTENTSCONTENTSCONTENS-->",
            )

    ### ccc[2] list
    ### set
    ### set -> list

    cflag = list(set(ccc[2]))
    for i in range(len(cflag)):
        indices = [j for j, x in enumerate(ccc[2]) if x == cflag[i]]

    sss = sss.replace(
        "<!--CONTENTSCONTENTSCONTENS-->",
        "<table><BR>\n" + "<!--CONTENTSCONTENTSCONTENS-->",
    )

    ### Trafic
    filename = os.path.join("./warehouse", "Trafic.csv")
    sss = sss.replace(
        "<!--CONTENTSCONTENTSCONTENS-->",
        "<BR><center>traffic accident</center>\n" + "<!--CONTENTSCONTENTSCONTENS-->",
    )
    sss = sss.replace(
        "<!--CONTENTSCONTENTSCONTENS-->",
        "<BR><table border=1>\n" + "<!--CONTENTSCONTENTSCONTENS-->",
    )
    with open(filename, newline="", encoding="utf-8") as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            uuu = "<tr>"
            for j in range(len(row)):
                uuu = uuu + "<td>" + row[j] + "</td>"
            uuu = uuu + "</tr>"
            sss = sss.replace(
                "<!--CONTENTSCONTENTSCONTENS-->",
                uuu + "\n" + "<!--CONTENTSCONTENTSCONTENS-->",
            )
    sss = sss.replace(
        "<!--CONTENTSCONTENTSCONTENS-->",
        "<table><BR>\n" + "<!--CONTENTSCONTENTSCONTENS-->",
    )

    csv_reader = csv.reader(open(filename, "r", encoding="utf-8"))
    ddd = []
    for row in csv_reader:
        ddd.append(row)
    dddT = [[row[i] for row in ddd] for i in range(len(ddd[0]))]
    ibeg = 1
    jbeg = 2
    for i in range(ibeg, len(dddT)):
        for j in range(jbeg, len(dddT[0])):
            dddT[i][j] = int(dddT[i][j])
    ### plot the graph
    import matplotlib.pyplot as plt

    plt.rcParams["font.sans-serif"] = ["Kai"]  # Or any other Chinese characters
    plt.rcParams["axes.unicode_minus"] = False
    jbeg = 2
    x = range(jbeg, len(dddT[0]))
    labels = dddT[0][jbeg:]
    for i in range(ibeg, len(dddT)):
        y = dddT[i][jbeg:]
        plt.plot(x, y, label=dddT[i][0])
    plt.xticks(x, labels, rotation="vertical")
    plt.margins(0.2)
    plt.subplots_adjust(bottom=0.15)
    plt.title("traffic accident")
    plt.legend()
    plt.ioff()
    plt.savefig(os.path.join("warehouse", "Display001.png"))
    ###
    sss = sss.replace(
        "<!--CONTENTSCONTENTSCONTENS-->",
        '<BR><center><img src="./warehouse/Display001.png"></center><BR>\n'
        + "<!--CONTENTSCONTENTSCONTENS-->",
    )

    for i in range(2, len(dddT)):
        y = dddT[i][jbeg:]
        plt.clf()
        plt.bar(x, y)
        plt.savefig(os.path.join("warehouse", "Display00" + str(i) + ".png"))
        sss = sss.replace(
            "<!--CONTENTSCONTENTSCONTENS-->",
            '<BR><center><img src="./warehouse/Display00'
            + str(i)
            + '.png"></center><BR>\n'
            + "<!--CONTENTSCONTENTSCONTENS-->",
        )

    fid = open("DAALU.html", "w", encoding="utf-8")
    fid.write(sss)
    fid.close()
    DAALUCanvas1.delete("all")
    DAALUCanvas1.create_text(
        100,
        20,
        fill="white",
        font="Times 20 italic bold",
        text=DAALUText1.get(1.0, tk.END),
    )
    DAALUButton2.invoke()
    DAALUText1.delete(1.0, tk.END)
    DAALUText1.insert(1.0, "A html has been generated.")


###
def DAALUButton2RUN():
    if platform.system() in ["Darwin", "Linux"]:
        os.system("open DAALU.html")
    else:
        os.system("DAALU.html")


###
def DAALUButton3RUN():
    DAALUWIN.destroy()


###
def DAALUButton4RUN():
    filename = os.path.join("warehouse", "TextbookDA.pdf")
    if platform.system() in ["Darwin", "Linux"]:
        os.system("open " + filename)
    else:
        os.system(filename)


###
def DAALUCanvas1_resize():
    global DAALUCanvas1
    global text_id
    font = "Times %i italic bold"
    fontsize = 20
    x0 = DAALUCanvas1.bbox(text_id)[0]  # x-coordinate of the left side of the text
    DAALUCanvas1.itemconfigure(
        text_id, width=DAALUCanvas1.winfo_width() - x0, font=font % fontsize
    )
    # shrink to fit
    height = DAALUCanvas1.winfo_height()  # canvas height
    y1 = DAALUCanvas1.bbox(text_id)[3]  # y-coordinate of the bottom of the text
    while y1 > height and fontsize > 1:
        fontsize -= 1
        DAALUCanvas1.itemconfigure(text_id, font=font % fontsize)
        y1 = DAALUCanvas1.bbox(text_id)[3]


# ----
def DAALUButton5RUN():
    global DAALULabel1
    global text_id
    s = DAALULabel1.cget("text")
    if int(s) > 0:
        ii = int(s) - 1
        DAALULabel1.configure(text=str(ii))
        sss, ttt = PAGES(ii)
        DAALUCanvas1.delete("all")
        text_id = DAALUCanvas1.create_text(
            30, 30, anchor="nw", fill="white", font="Times 20 italic bold", text=sss
        )
        DAALUCanvas1_resize()
        ###
        if ttt != []:
            from PIL import ImageTk, Image
            import os

            x0 = DAALUWIN.winfo_rootx() + DAALUCanvas1.winfo_x()
            y0 = DAALUWIN.winfo_rooty() + DAALUCanvas1.winfo_y()
            x1 = x0 + int(DAALUCanvas1.winfo_width())
            y1 = y0 + int(DAALUCanvas1.winfo_height())
            if not os.path.exists("warehouse"):
                import platform

                if platform.system() in ["Darwin", "Linux"]:
                    os.system("mkdir warehouse")
                else:
                    os.system("mkdir warehouse")
            filename = os.path.join("warehouse", ttt)
            im = Image.open(filename)
            imResized = im.resize((x1 - x0, y1 - y0), Image.ANTIALIAS)
            DAALUCanvas1.image = ImageTk.PhotoImage(imResized)
            DAALUCanvas1.create_image(0, 0, image=DAALUCanvas1.image, anchor="nw")


###
def DAALUOptionMenu1RUN(x):
    OMenu1Var.set(x)
    exec(open(os.path.join("warehouse", x), encoding="utf-8").read(), globals())


def DAALUButton6RUN():
    global DAALULabel1
    global text_id
    s = DAALULabel1.cget("text")

    sss, ttt = PAGES(int(s) + 1)
    if sss != []:
        ii = int(s) + 1
        DAALULabel1.configure(text=str(ii))
        sss, ttt = PAGES(ii)
        DAALUCanvas1.delete("all")
        text_id = DAALUCanvas1.create_text(
            30, 30, anchor="nw", fill="white", font="Times 20 italic bold", text=sss
        )
        DAALUCanvas1_resize()
        if ttt != []:
            from PIL import ImageTk, Image
            import os

            x0 = DAALUWIN.winfo_rootx() + DAALUCanvas1.winfo_x()
            y0 = DAALUWIN.winfo_rooty() + DAALUCanvas1.winfo_y()
            x1 = x0 + int(DAALUCanvas1.winfo_width())
            y1 = y0 + int(DAALUCanvas1.winfo_height())
            filename = os.path.join("./warehouse", ttt)
            im = Image.open(filename)
            imResized = im.resize((x1 - x0, y1 - y0), Image.ANTIALIAS)
            DAALUCanvas1.image = ImageTk.PhotoImage(imResized)
            DAALUCanvas1.create_image(0, 0, image=DAALUCanvas1.image, anchor="nw")


def DAALUButton7RUN():
    ii = int(DAALULabel1.cget("text"))
    sss, ttt = PAGES(ii)
    myPWD = os.getcwd()
    exec(sss, globals())
    print("DONE")


#####################################################################################
#####################################################################################
### GUI: Graphic User Interface 使用者圖形介面
DAALUWIN = tk.Tk()
DAALUWIN.title("Data Structure and Algorithm")
DAALUWIN.geometry("1000x700+100+100")
### create the objects
iOBJ = 0
iOBJ = iOBJ + 1
DAALUText1 = tk.Text(DAALUWIN)
iOBJ = iOBJ + 1
DAALUCanvas1 = tk.Canvas(DAALUWIN)
iOBJ = iOBJ + 1
DAALULabelFrame1 = tk.LabelFrame(DAALUWIN)
iOBJ = iOBJ + 1
DAALULabelFrame2 = tk.LabelFrame(DAALUWIN)
###
jOBJ = 0
OMenu1Var = tk.StringVar()
CHC = []
jOBJ = jOBJ + 1
DAALUOptionMenu1 = tk.OptionMenu(DAALULabelFrame1, variable=OMenu1Var, value=CHC)
jOBJ = jOBJ + 1
DAALUCheckbutton1 = tk.Checkbutton(DAALULabelFrame1)
jOBJ = jOBJ + 1
DAALUButton1 = tk.Button(DAALULabelFrame1)
jOBJ = jOBJ + 1
DAALUButton2 = tk.Button(DAALULabelFrame1)
jOBJ = jOBJ + 1
DAALUButton3 = tk.Button(DAALULabelFrame1)
jOBJ = jOBJ + 1
DAALUButton4 = tk.Button(DAALULabelFrame1)
jOBJ = jOBJ + 1
DAALUButton7 = tk.Button(DAALULabelFrame1)
###
### Initial Set for OMenu1Var
OMenu1Var.set("DATA-FILE")
CHC = [x for x in os.listdir(os.path.join(".", "warehouse")) if x.endswith(".py") == 1]
DAALUOptionMenu1["menu"].delete(0, tk.END)
for i in range(len(CHC)):
    DAALUOptionMenu1["menu"].add_command(
        label=CHC[i], command=lambda x=CHC[i]: DAALUOptionMenu1RUN(x)
    )
###
kOBJ = 0
kOBJ = kOBJ + 1
DAALUButton5 = tk.Button(DAALULabelFrame2)
kOBJ = kOBJ + 1
DAALULabel1 = tk.Label(DAALULabelFrame2)
kOBJ = kOBJ + 1
DAALUButton6 = tk.Button(DAALULabelFrame2)
### pack the objects
xx = 0
yy = 0
xwd = 1
ywd = 1
ywd = 0.8
DAALUCanvas1.place(relx=xx, rely=yy, relwidth=xwd, relheight=ywd)
yy = yy + ywd
ywd = 0.1
DAALUText1.place(relx=xx, rely=yy, relwidth=xwd, relheight=ywd)
yy = yy + ywd
ywd = 0.05
DAALULabelFrame1.place(relx=xx, rely=yy, relwidth=xwd, relheight=ywd)
yy = yy + ywd
ywd = 0.05
DAALULabelFrame2.place(relx=xx, rely=yy, relwidth=xwd, relheight=ywd)
###
xx = 0
yy = 0
xwd = 1
ywd = 1
xwd = xwd / float(jOBJ)
DAALUOptionMenu1.place(relx=xx, rely=yy, relwidth=xwd, relheight=ywd)
xx = xx + xwd
DAALUCheckbutton1.place(relx=xx, rely=yy, relwidth=xwd, relheight=ywd)
zz = [1, 2, 3, 4, 7]
for i in range(len(zz)):
    cmds = (
        "xx=xx+xwd;DAALUButton"
        + str(zz[i])
        + ".place(relx=xx,rely=yy,relwidth=xwd,relheight=ywd)"
    )
    exec(cmds, globals())
###
xx = 0
yy = 0
xwd = 1
ywd = 1
xwd = xwd / float(kOBJ)
DAALUButton5.place(relx=xx, rely=yy, relwidth=xwd, relheight=ywd)
xx = xx + xwd
DAALULabel1.place(relx=xx, rely=yy, relwidth=xwd, relheight=ywd)
xx = xx + xwd
DAALUButton6.place(relx=xx, rely=yy, relwidth=xwd, relheight=ywd)
#### Set the property
E2CVar = tk.IntVar()
DAALUCheckbutton1.configure(text="E2C")
DAALUCheckbutton1.configure(variable=E2CVar)
E2CVar.set(1)
TEMP = ["RUN", "OPEN", "QUIT", "Textbook", "<<", ">>", "EXEC"]
for i in range(len(TEMP)):
    cmds = "DAALUButton" + str(i + 1) + '.configure(text="' + TEMP[i] + '")'
    exec(cmds, globals())
    cmds = (
        "DAALUButton"
        + str(i + 1)
        + ".configure(command=DAALUButton"
        + str(i + 1)
        + "RUN)"
    )
    exec(cmds, globals())
DAALULabel1.configure(text="0")
#### Set the initial
DAALUText1.delete(1.0, tk.END)
sss = """Game of Life"""
DAALUText1.insert(1.0, sss)
DAALUCanvas1.create_text(
    100, 10, fill="white", font="Times 20 italic bold", text="Lecture 0923."
)
#####################################################################################
#####################################################################################
DAALUWIN.mainloop()
