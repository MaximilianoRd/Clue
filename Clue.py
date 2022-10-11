#Librerias
from tkinter import *  
import random
#creacion de ventana
root=Tk()
root.title("Clue")
root.geometry("1280x720")
root.resizable(0,0)
#fondos a utlizar
Plaza=PhotoImage(file="Plaza.png")
Cine=PhotoImage(file="Cine.png")
comedor=PhotoImage(file="Comedor.png")
Tienda=PhotoImage(file="Tienda.png")
Estacionamiento=PhotoImage(file="Estacionamiento.png")
Banio=PhotoImage(file="Banio.png")
#personajes buenos
Morgan=PhotoImage(file="MorganDialogo.png")
Sherlock=PhotoImage(file="SherlockDialogo.png")
Mike=PhotoImage(file="MikeDialogo.png")
Lucifer=PhotoImage(file="LuciferDialogo.png")
Hopper=PhotoImage(file="HopperDialogo.png")
#personajes sospechosos
Bruce=PhotoImage(file="BruceDialogo.png")
Rachel=PhotoImage(file="RachelDialogo.png")
Ross=PhotoImage(file="RossDialogo.png")
Heisenberg=PhotoImage(file="HeisenbergDialogo.png")
Jesse=PhotoImage(file="JesseDialogo.png")
#lugar donde va el dialogo
BarraDialogo=PhotoImage(file="Dialogo.png")
#listas
nombres=['Bruce','Rachel','Ross','Heisenberg','Jesse']
imagenes=[Bruce,Rachel,Ross,Heisenberg,Jesse]
lugar=['Cine','Comedor','Tienda','Estacionamiento','Banio']
arma=['Manopla con cuchillas','Navaja con forma de labial','Navaja con forma de dinosaurio','Veneno a base de ricino','Pistola robada']
#random del asesino
a=random.randint(0,4)
asesino=[nombres[a],lugar[random.randint(0,4)],arma[random.randint(0,4)],imagenes[a]]
#creacion de mapa
Mapa=[] 
Conclusion=[]
AccionesCount=0
for z in range(5):
    a=random.randint(0,(len(nombres)-1))
    Mapa.append([nombres[a],lugar[random.randint(0,len(lugar)-1)],arma[random.randint(0,len(arma)-1)],imagenes[a]])
    nombres.remove(Mapa[z][0])
    lugar.remove(Mapa[z][1])
    arma.remove(Mapa[z][2])
    imagenes.remove(Mapa[z][3])
#creacion del canvas
canvas=Canvas(root,width=1280,height=720)
canvas.pack(fill="both",expand=True)
canvas.pack()
canvas.create_image(0,0,image=Plaza,anchor="nw")
canvas.create_text(600,660,text="Selecciona un lugar para investigar",fill="Black",font=("Helvetica",26)) 
canvas.create_text(600,700,text=f"Acciones restantes: {5-AccionesCount}", fill="Black",font=("Helvetica",26)) 
#cambiar a la Cine
def cambia_Cine():
    canvas.pack(fill="both",expand=True) 
    canvas.pack()
    canvas.create_image(0,0,image=Cine,anchor="nw")
    ocultar_botones()
    global nombre_lugar
    nombre_lugar="Cine"
    global zmapa
    zmapa=ubicar_mapa(nombre_lugar)
    destino(nombre_lugar)
#cambiar al comedor
def cambia_comedor():
    canvas.pack(fill="both",expand=True)
    canvas.pack()
    canvas.create_image(0,0,image=comedor,anchor="nw")
    ocultar_botones()
    global nombre_lugar
    nombre_lugar="Comedor"
    global zmapa
    zmapa=ubicar_mapa(nombre_lugar)
    destino(nombre_lugar)
#cambiar al baño
def cambia_Banio():
    canvas.pack(fill="both",expand=True) 
    canvas.pack()
    canvas.create_image(0,0,image=Banio,anchor="nw")
    ocultar_botones()
    global nombre_lugar
    nombre_lugar="Banio"
    global zmapa
    zmapa=ubicar_mapa(nombre_lugar)
    destino(nombre_lugar)
#cambiar a la Estacionamiento
def cambia_Estacionamiento():
    canvas.pack(fill="both",expand=True)
    canvas.pack()
    canvas.create_image(0,0,image=Estacionamiento,anchor="nw")
    ocultar_botones()
    global nombre_lugar
    nombre_lugar="Estacionamiento"
    global zmapa
    zmapa=ubicar_mapa(nombre_lugar)
    destino(nombre_lugar)
#cambiar al Tienda
def cambia_Tienda():
    canvas.pack(fill="both",expand=True) 
    canvas.pack()
    canvas.create_image(0,0,image=Tienda,anchor="nw")
    ocultar_botones()
    global nombre_lugar
    nombre_lugar="Tienda"
    global zmapa
    zmapa=ubicar_mapa(nombre_lugar)
    destino(nombre_lugar)
#ocultar botones
def ocultar_botones():
    boton_Estacionamiento.place_forget()
    boton_comedor.place_forget()
    boton_Cine.place_forget()
    boton_Tienda.place_forget()
    boton_Banio.place_forget()
    global EnLugar
    global DialogCount
    EnLugar=1
    DialogCount=0
#mostrar botones    
def mostrar_botones():
    boton_investigar.place_forget()
    boton_preguntar.place_forget()
    boton_Estacionamiento.place(x=1050,y=200)
    boton_comedor.place(x=350,y=450)
    boton_Cine.place(x=600,y=100)
    boton_Tienda.place(x=1050,y=450)
    boton_Banio.place(x=600,y=300)
#mostrar opciones
def mostrar_opciones():
    boton_uno.place(x=600,y=280)
    boton_dos.place(x=600,y=320)
    boton_tres.place(x=600,y=360)
    boton_cuatro.place(x=600,y=400)
    boton_cinco.place(x=600,y=440)
#destino
def destino(lugar):
    texto=["Morgan\n\nListo, llegamos a "+lugar+ "\nBusquemos si hay algo que indique quien mató a Hopper",
           "Sherlock\n\nMe temo que no estamos solos...\n*"+Mapa[zmapa][0]+" hace acto de presencia*",
           "Morgan\n\nQué hacemos?"]
    Imagen_texto=[Morgan,Sherlock,Morgan]
    global dialogo
    global Imagen
    if DialogCount>0 and DialogCount<len(texto):  
        canvas.itemconfig(Imagen,image=Imagen_texto[DialogCount])
        canvas.itemconfig(dialogo,text=texto[DialogCount])
        if DialogCount==2:
            boton_investigar.place(x=750,y=500)
            boton_preguntar.place(x=950,y=500)    
    elif DialogCount>=len(texto):
        boton_siguiente.place_forget()
    else:
        Imagen=canvas.create_image(0,0,image=Morgan,anchor="nw")
        dialogo=canvas.create_text(200,440,fill="White",text=texto[DialogCount],anchor="nw",font=("Helvetica",20))
#funcion para interrogar       
def interrogar():
    boton_investigar.place_forget()
    boton_preguntar.place_forget()
    boton_siguiente.place(x=1000,y=680)
    global AccionesCount
    global DialogCount
    global EnLugar
    global num_dialogo 
    global dialogo  
    global Imagen
    canvas.delete(Imagen)
    canvas.delete(dialogo)
    AccionesCount+=1
    EnLugar=4
    DialogCount=0
    boton_menu.place_forget()
    num_dialogo=random.randint(0,2) 
    conversacion()
#funcion para observar el area
def observar():
    boton_investigar.place_forget()
    boton_preguntar.place_forget()
    boton_siguiente.place(x=1000,y=680)
    global AccionesCount
    global EnLugar
    global DialogCount
    global dialogo  
    global Imagen
    canvas.delete(Imagen)
    canvas.delete(dialogo)
    AccionesCount+=1
    EnLugar=2
    DialogCount=0
    boton_menu.place_forget()
    encontrarpista()
#funcion para conversar
def conversacion():
    global dialogo
    global Imagen
    lugar_random=random.randint(0,4)
    nombre_random=random.randint(0,4)
    if Mapa[nombre_random][0]==Mapa[zmapa][0] or Mapa[nombre_random][0]==asesino[0]:  
        nombre_random=random.randint(0,4)
    if lugar_random==zmapa:
        lugar_random=random.randint(0,4)
    dialogo1=[f"Sherlock \n\nHola {Mapa[zmapa][0]}.",
             f"{Mapa[zmapa][0]} \n\nBuen día, qué hacen por aquí?",
             f"Lucifer \n\nHopper ha sido asesinado, y estamos buscando pistas acerca de ello, \nquisiera saber donde has estado las ultimas horas?.",
             f"{Mapa[zmapa][0]} \n\nHe estado en {Mapa[lugar_random][1]},\n y si sirve de ayuda, creo haber visto a {Mapa[nombre_random][0]} rondando por el lugar.\nSi yo fuera ustedes investigaria por ahi...",
             f"Sherlock \n\nInteresante... Tal vez vayamos a echar un vistazo, {Mapa[zmapa][0]}",
             f"{Mapa[zmapa][0]} \n\nClaro, solo digo lo que creo que puede ser de ayuda"]
    image=[Sherlock,Mapa[zmapa][3],Lucifer,Mapa[zmapa][3],Sherlock,Mapa[zmapa][3]]
   
    dialogos=[[f"{Mapa[zmapa][0]} \n\nHola!\nOigan, y Hopper?",
                 "Mike \n\nHa sido asesinado, estamos buscando pistas sobre ello\nPuedes decirnos en donde has estado las ultimas horas?",
                 f"{Mapa[zmapa][0]} \n\n¡QUE! Hopper muerto?\nDemonios! Espero que encuentren al culpable\nYo he estado en la tienda probandome ropa",
                 "Mike \n\nNo pudo haber estado ahi, Hopper solo va a la ropa de paca",
                 f"Morgan \n\nGracias por la informacion {Mapa[zmapa][0]}",
                 f"{Mapa[zmapa][0]} \n\nDe nada, espero que puedan encontrar quien lo hizo"],
            [f"Morgan \n\nQue onda, {Mapa[zmapa][0]}? \nChicos, acerquense",
                 f"{Mapa[zmapa][0]} \n\nQue onda chicos, ¿Donde esta Hopper?",
                 f"Sherlock \n\nAlguien ha matado a Hopper y estamos investigando\ntenemos que saber quien lo mató. \nDinos donde estuviste estas ultimas horas",
                 f"{Mapa[zmapa][0]} \n\nEs un poco vergonzoso, pero he estado en el Miniso\n¿Quieren el recibo de compra?",
                 "Sherlock \n\nNo te preocupes, sabemos que Hopper odia ese lugar \npor lo que es imposible que estuviera ahí",
                 f"{Mapa[zmapa][0]} \n\nOK, nos vemos luego, que tengo cosas que hacer. \nEspero encuentren al asesino pronto."],
            [f"{Mapa[zmapa][0]} \n\nHola chicos, ¿puedo ayudarles en algo?",
                 f"Lucifer \n\nHola! {Mapa[zmapa][0]}, de hecho si que puedes ayudarnos\nestamos buscando al cabron que mato a Hopper, asi que dinos\n ¿donde has estado las ultimas horas?",
                 f"{Mapa[zmapa][0]} \n\nEeeeh... no recuerdo...",
                 f"{Mapa[zmapa][0]} \n\nAh si!, ya recuerdo \nEstaba con {Mapa[nombre_random][0]} en el Estacionamiento, fui por algo que olvide en mi carro \nluego me dirigí al comedor",
                 f"Sherlock \n\nEntiendo...\nGracias, {Mapa[zmapa][0]}"]]
    image2 =[[Mapa[zmapa][3],Mike,Mapa[zmapa][3],Mike,Morgan,Mapa[zmapa][3]],[Morgan,Mapa[zmapa][3],Sherlock,Mapa[zmapa][3],Sherlock,Mapa[zmapa][3]],[Mapa[zmapa][3],Lucifer,Mapa[zmapa][3],Mapa[zmapa][3],Sherlock]]
    if asesino[0]==Mapa[zmapa][0]:
        if DialogCount>0 and DialogCount<len(dialogo1): 
            canvas.itemconfig(Imagen,image=image[DialogCount])
            canvas.itemconfig(dialogo,text=dialogo1[DialogCount])
        elif DialogCount>=len(dialogo1):  
            volver_menu()
        else:             
            Imagen=canvas.create_image(0,0,image=image[DialogCount],anchor="nw")
            dialogo=canvas.create_text(200,440,fill="White",text=dialogo1[DialogCount],anchor="nw",font=("Helvetica",20))
    else:  
        if DialogCount>0 and DialogCount<len(dialogos[num_dialogo]):  
            canvas.itemconfig(Imagen,image=image2[num_dialogo][DialogCount])
            canvas.itemconfig(dialogo,text=dialogos[num_dialogo][DialogCount])
        elif DialogCount>=len(dialogos[num_dialogo]): 
            volver_menu()
        else:            
            Imagen=canvas.create_image(0,0,image=image2[num_dialogo][DialogCount],anchor = "nw")
            dialogo=canvas.create_text(200,440,fill="White",text=dialogos[num_dialogo][DialogCount],anchor="nw",font=("Helvetica",20))
#encontrar objeto importante
def encontrarcapa():  
    global dialogo
    global Imagen
    dialogo1=["Mike \n\nHey, he encontrado la placa de Hopper. Fue aqui donde lo mataron.",  
            "Lucifer \n\nHijos de puta!",
             "Mike \n\nNo parare hasta encontrar al culpable.",
             "Morgan \n\nMantengamos la calma, lo encontraremos y lo haremos pagar"]
    ImgTex1=[Mike,Lucifer,Mike,Morgan]
    
    dialogo2=["Sherlock \n\nNo hay nada por aqui, dudo que Hopper haya estado por \nesta area", 
             "Morgan \n\nLo mas seguro es que no estuvo aqui",
             "Mike \n\nDescuida Hopper, te vengare muy pronto..."]
    ImgTex2=[Sherlock,Morgan,Mike]
    
    if asesino[1]==Mapa[zmapa][1]: 
        if DialogCount>0 and DialogCount<len(dialogo1):  
            canvas.itemconfig(Imagen,image=ImgTex1[DialogCount])
            canvas.itemconfig(dialogo,text=dialogo1[DialogCount])
        elif DialogCount>=len(dialogo1):
            volver_menu()
        else:            
            Imagen=canvas.create_image(0,0,image=ImgTex1[DialogCount],anchor="nw")
            dialogo=canvas.create_text(200,440,fill="White",text=dialogo1[DialogCount],anchor="nw",font=("Helvetica",20))
    else:  
        if DialogCount>0 and DialogCount<len(dialogo2): 
            canvas.itemconfig(Imagen,image=ImgTex2[DialogCount])
            canvas.itemconfig(dialogo,text=dialogo2[DialogCount])
        elif DialogCount>=len(dialogo2): 
            volver_menu()
        else:            
            Imagen=canvas.create_image(0,0,image=ImgTex2[DialogCount],anchor="nw")
            dialogo=canvas.create_text(200,440,fill="White",text=dialogo2[DialogCount],anchor="nw",font=("Helvetica",20))
#encontrar pista en las areas
def encontrarpista():
    global dialogo
    global EnLugar
    global DialogCount
    global Imagen
    dialogo1=["Morgan \n\nOk, hay que dividirnos y busquemos cualquier cosa que nos pueda \nindicar quien asesino a Hopper.",
             "Sherlock \n\nHey! Acabo de encontrar algo...",
             "Sherlock \n\nEncontre "+asesino[2]+", \npero no estoy seguro de a quien le pertenece.",
             "Lucifer \n\nQuizas se le cayo al asesino"]
    ImgTex1=[Morgan,Sherlock,Sherlock,Lucifer]
    
    dialogo2=["Morgan \n\nOk, hay que dividirnos y busquemos cualquier cosa que nos pueda \nindicar quien asesino a Hopper.",
             "...",
             "Mike \n\nNo hay nada por aquí que nos indique que aquí hayan matado a Hopper",
             "Sherlock \n\nTenemos que seguir buscando, vayamos a otro lugar..."]
    ImgTex2=[Morgan,BarraDialogo,Mike,Sherlock]
    
    if asesino[2]==Mapa[zmapa][2]:
        if DialogCount>0 and DialogCount<len(dialogo1):  
            canvas.itemconfig(Imagen,image=ImgTex1[DialogCount])
            canvas.itemconfig(dialogo,text=dialogo1[DialogCount])
        elif DialogCount>=len(dialogo1):
            DialogCount=0
            EnLugar=3
            canvas.delete(dialogo)
            canvas.delete(Imagen)
            encontrarcapa()
        else:             
            Imagen=canvas.create_image(0,0,image=ImgTex1[DialogCount],anchor="nw")
            dialogo=canvas.create_text(200,440,fill="White",text=dialogo1[DialogCount],anchor="nw",font=("Helvetica",20))
    else:  
        if DialogCount>0 and DialogCount<len(dialogo2): 
            canvas.itemconfig(Imagen,image =ImgTex2[DialogCount])
            canvas.itemconfig(dialogo,text=dialogo2[DialogCount])
        elif DialogCount>=len(dialogo2): 
            DialogCount=0
            EnLugar=3
            canvas.delete(dialogo)
            canvas.delete(Imagen)
            encontrarcapa()
        else:             
            Imagen=canvas.create_image(0,0,image=ImgTex2[DialogCount],anchor="nw")
            dialogo=canvas.create_text(200,440,fill="White",text=dialogo2[DialogCount],anchor="nw",font=("Helvetica",20))
#ubicar mapa
def ubicar_mapa(lugar): 
    for i in range(5):
        if lugar==Mapa[i][1]:
            return i       
#volver al menu para seleccionar los lugares
def volver_menu():
    global dialogo
    global DialogCount
    global EnLugar
    EnLugar=0
    if AccionesCount==5:
        canvas.delete(dialogo)
        DialogCount=0
        EnLugar=5
        resolvermisterio()
    else:
        canvas.pack(fill="both",expand=True) 
        canvas.pack() 
        canvas.create_image(0,0,image=Plaza,anchor="nw") 
        mostrar_botones()
        boton_menu.place(x=5,y=680)
        canvas.create_text(600,660,text="Selecciona un lugar para investigar",fill="Black",font=("Helvetica",26)) 
        canvas.create_text(600,700,text=f"Acciones restantes: {5-AccionesCount}",fill="Black",font=("Helvetica",26)) 
#funcion para continuar el dialogo
def siguiente():
    global DialogCount
    global AnswerBien
    DialogCount+=1
    if EnLugar==1:
        destino(nombre_lugar)
    elif EnLugar==2: 
        encontrarpista()
    elif EnLugar==3: 
        encontrarcapa()
    elif EnLugar==4: 
        conversacion()
    elif EnLugar==5: 
        if DialogCount==1: 
            boton_siguiente.place_forget()
            mostrar_opciones()
        resolvermisterio()
    elif EnLugar==6: 
        Final(AnswerBien)
    elif EnLugar==7:
        root.destroy()
#funcion para resolver el misterio
def resolvermisterio():
    global dialogo
    global DialogCount
    global ans
    global AnswerBien
    global EnLugar
    global Imagen
    
    DialogFinal=["Morgan \n\nExcelente, ya es hora de encontrar al cerdo que mató a Hopper",
                "Morgan \n\nQuien es el asesino?",
                "Morgan \n\nEn donde fué asesinado Hopper?",
                "Morgan \n\nPor último, con que arma fue?"]
    if DialogCount>0 and DialogCount<len(DialogFinal):
        canvas.itemconfig(dialogo,text=DialogFinal[DialogCount])
        boton_uno.configure(text=Mapa[0][DialogCount-1])
        boton_dos.configure(text=Mapa[1][DialogCount-1])
        boton_tres.configure(text=Mapa[2][DialogCount-1])
        boton_cuatro.configure(text=Mapa[3][DialogCount-1])
        boton_cinco.configure(text=Mapa[4][DialogCount-1])
    elif DialogCount>=len(DialogFinal): 
        DialogCount=0
        EnLugar=6
        canvas.delete(dialogo)
        canvas.delete(Imagen)
        ans=0
        for a in 'Manopla con cuchillas','Navaja con forma de labial','Navaja con forma de dinosaurio','Veneno a base de ricino','Pistola robada':
            if asesino[2]==a:
                break
            ans+=1
        AnswerBien=True
        for i in range(3):
            if asesino[i]!=Conclusion[i]:
                AnswerBien=False
        boton_uno.place_forget()
        boton_dos.place_forget()
        boton_tres.place_forget()
        boton_cuatro.place_forget()
        boton_cinco.place_forget()
        boton_siguiente.place(x=1000,y=680) 
        Final(AnswerBien)
    else:             
        canvas.create_image(0,0,image=Plaza,anchor="nw")
        Imagen=canvas.create_image(0,0,image=Morgan,anchor="nw")
        dialogo=canvas.create_text(200,440,fill="White",text=DialogFinal[DialogCount],anchor="nw",font=("Helvetica",20))
#dfuncion para el ir al resultado   
def resultado(respuesta):
    global DialogCount
    global Conclusion
    Conclusion.append(respuesta)
    DialogCount+=1  
    resolvermisterio()
#dialogo final
def Final(r):
    global ans
    global DialogCount
    global dialogo
    global Imagen, EnLugar
    if r==True: 
        objetivos=[f"la {asesino[2]} que encontramos como pista? \nBueno, resulta que esa manopla con cuchillas es de que Bruce Lee \nMaldito camorrista sin cerebro.",
                  f"el {asesino[2]} que encontramos como pista? \nBueno, resulta que esa navaja con forma de labial le pertenece a Rachel \nLa belleza no es sinonimo de inteligencia.",
                  f"la {asesino[2]} que encontramos como pista? \nBueno, resulta que la navaja con forma de dinosaurio le pertenece a Ross \nEse paleontologo si que es descuidado.",
                  f"el {asesino[2]} que encontramos como pista? \nBueno, recorde que ese veneno de ricino es obra de Heisenberg \nSorprende que se le haya escapado algo tan importante.\nEse tipo es implacable",
                  f"la {asesino[2]} que encontramos como pista? \nBueno, la pistola fue robada por Jesse \nEste cabron nunca fue muy inteligente"]
        
        Dialogo_Final=["Sherlock \n\nMuy bien, al fin tenemos al asesino de Hopper.\nFue...",
                     f"Mike \n\n{asesino[0]}, cierto?",
                     f"Sherlock \n\nEfectivamente, {asesino[0]} mato a Hopper porque estaba interfiriendo con asuntos turbios",
                     "Lucifer \n\nTiene sentido, cuando fuimos a hablar con el, claramente \nse noto que estaba nervioso e intento culpar a otra persona",
                     "Morgan \n\nLogrando así que el dejara de parecer un sospechoso para poder lograr su \ncometido y salirse con la suya",
                     "Mike \n\n¿Porque ese imbécil asesinaría a Hopper?",
                     f"Sherlock \n\nRecuerdas {objetivos[ans]}",
                      "Mike \n\nPues fue gracias a ello que logramos encontrarte.Pero, donde está su cuerpo?",
                      f"{asesino[0]} \n\nNunca les diré donde está el cuerpo de su estúpido ami.....",
                      "Hopper \n\nHola chicos que estan haciendo?",
                      "Morgan \n\nHopper? Que pedo cabron, como es que sigues vivo?",
                      f"Hopper \n\nPues {asesino[0]} intento matarme pero solo consiguio \herirme y penso que estaba muerto el imbecil",
                      "Mike \n\nTiene que ser una broma, ¿acaso no puedes morir?",
                      "Hopper \n\nLa verdad no se, siempre me protege el guion alv",
                      "Morgan \n\nMaldita se Hopper, estabamos tan preocupados por ti.",
                       f"{asesino[0]} \n\nmaldita sea, si hubiera sabido que eras tan fuerte \nte hubiera descuartizado",
                      "Hopper \n\nLo siento por ti, tenias una buena vida pero decidiste\nmeterte en negocios turbios, ahora te chingaste"]
        ImgFinal=[Sherlock,Mike,Sherlock,Lucifer,Morgan,Mike,Sherlock,Mike,asesino[3],
                 Hopper,Morgan,Hopper,Mike,Hopper,Morgan,asesino[3],Hopper]
        
        if DialogCount>0 and DialogCount<len(Dialogo_Final):  
            canvas.itemconfig(Imagen,image=ImgFinal[DialogCount])
            canvas.itemconfig(dialogo,text=Dialogo_Final[DialogCount])
        elif DialogCount>=len(Dialogo_Final): 
            DialogCount=0
            EnLugar=0
            canvas.delete(dialogo)
            canvas.delete(Imagen)
            boton_siguiente.place_forget()
            root.destroy()
        else:            
            Imagen=canvas.create_image(0,0,image=ImgFinal[DialogCount],anchor="nw")
            dialogo=canvas.create_text(200,440,fill="White",text=Dialogo_Final[DialogCount],anchor="nw",font=("Helvetica",20))
    else:
        Imagen=canvas.create_image(0,0,image=Morgan,anchor="nw")
        dialogo=canvas.create_text(200,440,fill="White",text=f"Morgan \n\nTe falta investigar mejor.\nCulpable:{asesino[0]}\nLugar:{asesino[1]}\narma:{asesino[2]}",anchor="nw",font=("Helvetica",20)) 
        EnLugar=7
#boton Estacionamiento
boton_Estacionamiento=Button(canvas,text="Estacionamiento",width=12,command=cambia_Estacionamiento)  
boton_Estacionamiento.place(x=1050,y=200)
#boton Cine
boton_Cine=Button(canvas,text="Cine",width=12,command=cambia_Cine)
boton_Cine.place(x=600,y=100)
#boton comedor
boton_comedor=Button(canvas,text="Comedor",width=12,command=cambia_comedor)
boton_comedor.place(x=350,y=450)
#boton Tienda
boton_Tienda=Button(canvas,text="Tienda",width=12,command=cambia_Tienda)
boton_Tienda.place(x=1050,y=450)
#boton Banio
boton_Banio=Button(canvas,text="Banio",width=12,command=cambia_Banio)
boton_Banio.place(x=600,y=300)
#boton menu
boton_menu=Button(canvas,text="menu",width=12,command=volver_menu)
boton_menu.place(x=5,y=680)
#botn siguiente
boton_siguiente=Button(canvas, text="siguiente", width=12, command=siguiente)
boton_siguiente.place(x=1000,y=680)
#boton para checar lugares
boton_preguntar=Button(canvas,text="Interrogar a la persona",width="20",command=interrogar,font=("Helveltica",12))
boton_investigar=Button(canvas,text="Analizar el lugar",width="20",command=observar,font=("Helveltica",12))
#botones para las respuestas del asesinato
boton_uno=Button(canvas,text="",width="28",command= lambda:resultado(Mapa[0][DialogCount-1]),font=("Helveltica",12))
boton_dos=Button(canvas,text="",width="28",command=lambda:resultado(Mapa[1][DialogCount-1]),font=("Helveltica",12))
boton_tres=Button(canvas,text="",width="28",command=lambda:resultado(Mapa[2][DialogCount-1]),font=("Helveltica",12))
boton_cuatro=Button(canvas,text="",width="28",command=lambda:resultado(Mapa[3][DialogCount-1]),font=("Helveltica",12))
boton_cinco=Button(canvas,text="",width="28",command=lambda:resultado(Mapa[4][DialogCount-1]),font=("Helveltica",12))
root.mainloop() 