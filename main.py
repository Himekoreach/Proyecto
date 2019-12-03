from flask import Flask,render_template
from flask_email import Mail,Message
from flask_socketio import SocketIO,send
from io import BytesIO
import os
#configuracion para enviar correos con flask
app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'
app.config['MAIL_SERVER']= 'mail.prettyprinted.com'
app.config['MAIL_PORT']= 465
app.config['MAIL_USE_SSL']= True
app.config.from_pyfile('config.cfg')

socketio = SocketIO(app)
@app.route('/')
#ruta predeterminada

def index():
    return render_template('index.html')

    # conexion con el index html para poder conectarme y usar su estilo verguitas

def handleMessage(msg):
    print("Message: "+ msg)
#mensaje para saber si se conecto

@socketio.on('message')
#todos los def con las funciones para poder hacer los comandos y para enviarlos por correo
def ifconfig():
    correo2 = input("Cual es tu correo")
    correo = input("Cual es el correo al que quieres enviar")
    os.system('ifconfig > ifconfig.txt')
    #envio lo que el usuario escribio y envio el txt
    msg = Message('ifconfig.txt', sender=correo,recipients=[correo2])

def ls():

    correo2 = input("Cual es tu correo")
    correo = input("Cual es el correo al que quieres enviar")
    os.system('ls > ls.txt')
    msg = Message('ls.txt', sender=correo,recipients=[correo2])

def iwconfig():
    correo2 = input("Cual es tu correo")
    correo = input("Cual es el correo al que quieres enviar")
    os.system('iwconfig > iwconfig.txt')
    msg = Message('iwconfig.txt', sender=correo,recipients=[correo2])

def cualquiera(resp2):
    correo2 = input("Cual es tu correo")
    correo = input("Cual es el correo al que quieres enviar")
    os.system( resp2 + '> cualquiera.txt')
    msg = Message('cualquiera.txt', sender=correo,recipients=[correo2])


#todo esto es para hacer archivos pdf y excel
#@app.route('/pdf/<arch>',methods=['GET'])
#def archivo_pdf(arch):
#    if arch == "ifconfig":
#        cs = "el archivo es:"+arch
#        archivo=open('ifconfig.txt','r')
#        repuesta=archivo.read()
#    elif arch == "ls":
#        cs = "el archivo es:"+arch
#        archivo = open ('ls.txt','r')
#        repuesta=archivos.read()
#    elif arch == "iwconfig":
#        cs = "el archivo es:"+arch
#        archivo = open ('iwconfig.txt','r')
#        repuesta=archivos.read()

#    w,h = A4
#    c = canvas.Canvas(arch+".pdf",pagesize=A4)
#    c.drawString(50, h - 50,""+respuesta)
#    c.showPage()
#    c.save()

#    return cs

#@app.route('/excel/<arch>',methods=["GET"])
#def archivo_excel(arch):
#    if arch == "ifconfig":
#        cs = "el archivo es:"+arch
#        archivo = open('ifconfig.txt','r')
#        repuesta=archivos.read()
#    elif arch == "ls":
#        cs = "el archivo es:"+arch
#        archivo = open ('ls.txt','r')
#        repuesta=archivos.read()
#    elif arch == "iwconfig":
#        cs = "el archivo es:"+arch
#        archivo = open ('iwconfig.txt','r')
#        repuesta=archivos.read()
#    elif arch != resp2:
#        cs = "el archivo es:"+arch
#        archivo = open (arch+'.txt','r')
#        repuesta=archivos.read()

#    datos = pd.read_csv(arch+'txt',error_bad_lines=False,engine="python",index_col=false,header=None)
#    datos.to_excel(arch+".xlsx",index=False,header=False)
#    return cs

#para el boton que tengo en el html

@app.route('/test2',methods=['GET','POST'])
def test2():
    if request.method == "POST":
        if request.form['submit']=='submit':
            print(request.args.get('check'))
    return render_template('index.html')

#abro la todo
if __name__ == '__main__':
    socketio.run(app)

#pregunto lo que el usuario quiere hacer para probar que funcione todo bien
print("Que comando quieres utilizar 1)ls 2)ifconfig 3)iwconfig 4)que comando quieres utilizar")

res = int(input("Cual es su respuesta"))

if res==1:
    ls()
#    arch='ls'
#    resp1 = input("En que formato quieres exportarlo 1pdf o excel")
#    cualquiera(resp1)
#    if resp1==1:
#        archivo_pdf(arch)
#    else:
#        archivo_excel(arch)

else:
    if res==2:
        ifconfig()
#        arch='ifconfig'
#        resp1 = input("En que formato quieres exportarlo 1pdf o excel")
#        cualquiera(resp1)
#        if resp1==1:
#            archivo_pdf(arch)
#        else:
#            archivo_excel(arch)

    else:
        if res==3:
            iwconfig()
#            arch='iwconfig'
#            resp1 = input("En que formato quieres exportarlo 1pdf o excel")
#            cualquiera(resp1)
#            if resp1==1:
#                archivo_pdf(arch)
#            else:
#                archivo_excel(arch)

        else:
            if res==4:
                resp2 = input("Que comando quieres")
                cualquiera(resp2)
#                arch=resp2
#                resp1 = input("En que formato quieres exportarlo 1pdf o excel")
#                cualquiera(resp1)
#                if resp1==1:
#                    archivo_pdf(arch)
#                else:
#                    archivo_excel(arch)
