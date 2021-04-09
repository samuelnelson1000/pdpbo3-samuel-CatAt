from tkinter import *
from tkinter import messagebox
from Penduduk import Penduduk
#from PIL import ImageTk

root = Tk()
root.geometry("550x400")
root.title("Tugas Praktikum 3 DPBO")
inputframe = Frame(root)
inputframe.pack(side = LEFT)
buttonframe = Frame(root)
buttonframe.pack(side = LEFT)
titlelabel = Label(inputframe, text = "Input Data Diri").grid(row= 0, column = 0, pady = 10)

# list data penduduk
penduduk  = []

# fungsi send data
def send_data():
    nama = namebox.get("1.0", "end-1c")
    jk = var.get()
    peran = role.get()
    alamat = addressbox.get("1.0", "end-1c")
    ttl = dobbox.get("1.0", "end-1c")
    som = Checkresult.get() #status of marriage
    if((len(nama) != 0) and (len(alamat)!=0) and (len(ttl) != 0) and (som)):
        #jika sudah lengkap semua
        penduduk.append(Penduduk(nama,jk,peran,alamat,ttl,som))
    else:
        mb =  messagebox.showinfo("Data Invalid", message = "Ada yang belum lengkap!")

# tampilkan data
def show_data():
    top = Toplevel()
    frame = LabelFrame(top, text="Data Penduduk", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    for index, p in enumerate(penduduk):
        idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        name = Label(frame, text=" " + p.get_nama(), width=10, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=1)
        name = Label(frame, text=" " + p.get_peran(), width=40,  borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)
        b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
        b_detail.grid(row=index, column=3)

# detail data
def details(index):
    top = Toplevel()
    top.title("Detail Penduduk")

    d_frame = LabelFrame(top, text="Data Penduduk", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    d_summary = Label(d_frame, text="Summary: " + penduduk[index].get_summary() + ".", anchor="w").grid(row=0, column=0, sticky="w")

# delete data
def delete_data():
    mb =  messagebox.askyesno("Data Deletion", message = "Yakin Hapus?")
    if(mb == "yes"):
        penduduk = [""]

    

#textbox
namevar = StringVar()
namelabel = Label(inputframe, text = "Nama ").grid(row=1, column=0, sticky="w")
namebox = Text(inputframe, height = 1, width = 32,)
namebox.grid(row=1, column=1, sticky="w")
#radiobutton
jklabel = Label(inputframe, text = "Jenis Kelamin").grid(row=2, column=0,sticky="w")
var = StringVar()#variable for radiobutton
var.set("Laki-Laki")
jkbox1 = Radiobutton(inputframe, text = "Laki-laki", variable = var, value="Laki-laki")
jkbox1.grid(row=2, column=1,sticky="w")
jkbox1.select()
jkbox2 = Radiobutton(inputframe, text = "Perempuan", variable = var, value="Perempuan")
jkbox2.grid(row = 3, column=1,sticky="w")
#dropdown
role = StringVar(inputframe)
roleoption = [ "Kepala Keluarga", "Istri", "Anak"]
rolelabel = Label(inputframe, text = "Peran ").grid(row = 4, column=0, sticky="nw")
rolebox = OptionMenu(inputframe, role, *roleoption )
role.set("Kepala Keluarga")
rolebox.grid(row = 4, column=1, sticky="w")

addresslabel = Label(inputframe, text = "Alamat ").grid(row = 5, column=0, sticky="nw")
addressbox = Text(inputframe, height = 4, width = 32)
addressbox.grid(row = 5, column=1, sticky="w")

doblabel = Label(inputframe, text = "Tempat, Tanggal Lahir").grid(row = 6, column=0,sticky="w")
dobbox = Text(inputframe, height = 1, width = 32)
dobbox.grid(row = 6, column = 1)

#checkbox
Checkresult = StringVar()
somlabel = Label(inputframe, text = "Status Pernikahan").grid(row = 7, column = 0, sticky="w")
sombutton1 = Checkbutton(inputframe, text = "Belum Menikah", variable = Checkresult , onvalue="Belum Menikah", offvalue="" )
sombutton1.grid(row = 7, column = 1, sticky = "w")  
sombutton2 = Checkbutton(inputframe, text = "Sudah Menikah", variable = Checkresult , onvalue="Sudah Menikah", offvalue="" )
sombutton2.grid(row = 8, column = 1, sticky = "w")

# save data
savebutton = Button(inputframe, text = "Save Data", width = 24, command = send_data).grid(row = 9, column = 1)

#logopic = ImageTk.PhotoImage(file="20749479.jpg")
appname = Label(buttonframe, text = "CatAt")
descname = Label(buttonframe, text = "Aplikasi Sensus Penduduk")
appname.pack(padx =10)
descname.pack(padx =10)

# show data
showbutton = Button(buttonframe, text = "Show All ", width = 24, command = show_data)
showbutton.pack(padx =10)

# delete data
delbutton = Button(buttonframe, text = "Delete All", width = 24, command = delete_data)
delbutton.pack(padx =10)

# exit button
exitbutton = Button(buttonframe, text="Exit", command=root.destroy, width = 24)
exitbutton.pack(padx =10)


root.mainloop()