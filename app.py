# Import modules
import locale
import os
from flask import Flask, request, render_template, Markup, flash


# Set locale
locale.setlocale(locale.LC_ALL, '')

# Flask constructor
app = Flask(__name__)  

# Program startup, menu utama
@app.route("/")
def startup():
    f = open("static/session.txt")
    f = f.read()
    f = f.split("\n")
    nama = f[0]
    isLogin = f[1]
    if (isLogin == "True"):
        return render_template("menu.html", nama = nama, isLogin = isLogin)
    else:
        return render_template("menu.html")

# Login
@app.route("/login", methods=["POST", "GET"])
def login():
    isLogin = False
    f = open("static/data.txt")
    f = f.read()
    f = f.split("\n")
    namaPengguna = [0] * len(f)
    PINPengguna = [0] * len(f)
    saldoPengguna = [0] * len(f)
    j = 0
    for i in f:
        i = i.split(" ")
        namaPengguna[j] = i[0]
        PINPengguna[j] = i[1]
        saldoPengguna[j] = i[2]
        j+=1
    inpNama = request.form.get("nama")
    inpPIN = request.form.get("pin")
    if (inpNama in namaPengguna and inpPIN in PINPengguna):
        nama = inpNama
        isLogin = True
    else:
        nama = ""
        isLogin = False
    f = open("static/session.txt", 'w')
    f = f.write(f"{nama}\n{isLogin}")
    if (request.method == "POST"):
        return render_template("menu.html", nama = nama, isLogin = isLogin)
    else:
        return render_template("menu.html")
    
# Logout
@app.route("/logout")
def logout():
    nama = ""
    isLogin = False
    f = open("static/session.txt", 'w')
    f = f.write(f"{nama}\n{isLogin}")
    return render_template("menu.html")

# Buka menu tarik tunai
@app.route("/menuTarik")
def bukaTarik():
    f = open("static/session.txt")
    f = f.read()
    f = f.split("\n")
    nama = f[0]
    isLogin = f[1]
    if (isLogin == "True"):
        return render_template("tarik.html", nama = nama, isLogin = isLogin)
    else:
        return render_template("menu.html")

# Buka menu setor 
@app.route("/menuSetor")
def bukaSetor():
    f = open("static/session.txt")
    f = f.read()
    f = f.split("\n")
    nama = f[0]
    isLogin = f[1]
    if (isLogin == "True"):
        return render_template("setor.html", nama = nama, isLogin = isLogin)
    else:
        return render_template("menu.html")

# Buka menu transfer
@app.route("/menuTransfer")
def bukaTransfer():
    f = open("static/session.txt")
    f = f.read()
    f = f.split("\n")
    nama = f[0]
    isLogin = f[1]
    if (isLogin == "True"):
        return render_template("transfer.html", nama = nama, isLogin = isLogin)
    else:
        return render_template("menu.html")

# Buka menu info nasabah
@app.route("/menuInfo")
def bukaInfo():
    f = open("static/session.txt")
    f = f.read()
    f = f.split("\n")
    nama = f[0]
    isLogin = f[1]
    if (isLogin == "True"):
        return render_template("info.html", nama = nama, isLogin = isLogin)
    else:
        return render_template("menu.html")

# Buka menu pembukaan rekening
@app.route("/menuBukaRek")
def bukaRekening():
    f = open("static/session.txt")
    f = f.read()
    f = f.split("\n")
    nama = f[0]
    isLogin = f[1]
    if (isLogin == "True"):
        return render_template("bukarek.html", nama = nama, isLogin = isLogin)
    else:
        return render_template("bukarek.html")
    
    
# Buka rekening baru
@app.route("/bukaRekening", methods = ["POST", "GET"])
def rekeningBaru():
    nama = (request.form.get("nama")).capitalize()
    pin = request.form.get("PIN")
    saldo = request.form.get("setor")
    f = open("static/data.txt")
    f = f.read()
    f = f.split("\n")
    namaPengguna = [0] * len(f)
    j = 0
    for i in f:
        i = i.split(" ")
        namaPengguna[j] = i[0]
        j+=1
    if (nama in namaPengguna):
        message = "Rekening sudah ada"
    else:
        f = open("static/data.txt", "a")
        f = f.write(f"\n{nama} {pin} {saldo}")
        f = open("static/session.txt", 'w')
        f = f.write(f"{nama}\n{True}")
        message = "Rekening berhasil dibuat"
    return render_template("bukarek.html", nama = nama, isLogin = True, message = message)
    

# Tarik tunai
@app.route("/tarik", methods = ["POST", "GET"])
def tarikTunai():
    nominalTarik = int(request.form.get("nominalTarik"))
    f = open("static/session.txt")
    f = f.read()
    f = f.split("\n")
    nama = f[0]
    f = open("static/data.txt")
    f = f.read()
    f = f.split("\n")
    namaPengguna = [0] * len(f)
    PINPengguna = [0] * len(f)
    saldoPengguna = [0] * len(f)
    j = 0
    for i in f:
        i = i.split(" ")
        namaPengguna[j] = i[0]
        PINPengguna[j] = i[1]
        saldoPengguna[j] = i[2]
        j+=1
    if (nominalTarik > int(saldoPengguna[namaPengguna.index(nama)])):
        message = "Saldo anda tidak cukup"
    else:
        message = "Tarik tunai berhasil"
        saldoPengguna[namaPengguna.index(nama)] = int(saldoPengguna[namaPengguna.index(nama)])
        saldoPengguna[namaPengguna.index(nama)]-=nominalTarik
        for i in range(len(f)):
            if (i == 0):
                dataUpdate = f"{namaPengguna[i]} {PINPengguna[i]} {saldoPengguna[i]}"
            else:
                dataUpdate += f"\n{namaPengguna[i]} {PINPengguna[i]} {saldoPengguna[i]}"
        f = open("static/data.txt", "w")
        f = f.write(dataUpdate)
    return render_template("tarik.html", nama = nama, isLogin = True, message = message)


# Setor tunai
@app.route("/setor", methods = ["POST", "GET"])
def setorTunai():
    nominalSetor = int(request.form.get("nominalSetor"))
    f = open("static/session.txt")
    f = f.read()
    f = f.split("\n")
    nama = f[0]
    f = open("static/data.txt")
    f = f.read()
    f = f.split("\n")
    namaPengguna = [0] * len(f)
    PINPengguna = [0] * len(f)
    saldoPengguna = [0] * len(f)
    j = 0
    for i in f:
        i = i.split(" ")
        namaPengguna[j] = i[0]
        PINPengguna[j] = i[1]
        saldoPengguna[j] = i[2]
        j+=1
    message = "Setor tunai berhasil"
    saldoPengguna[namaPengguna.index(nama)] = int(saldoPengguna[namaPengguna.index(nama)])
    saldoPengguna[namaPengguna.index(nama)]+=nominalSetor
    for i in range(len(f)):
        if (i == 0):
            dataUpdate = f"{namaPengguna[i]} {PINPengguna[i]} {saldoPengguna[i]}"
        else:
            dataUpdate += f"\n{namaPengguna[i]} {PINPengguna[i]} {saldoPengguna[i]}"
    f = open("static/data.txt", "w")
    f = f.write(dataUpdate)
    return render_template("setor.html", nama = nama, isLogin = True, message = message)
    

if __name__=='__main__':
    app.run(debug=True)