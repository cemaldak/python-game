from tkinter import *
import random

words = ['Hüzün','Yaprak','Yağmur','Heves','Berrak','Merhamet','İrfan','Esrar',
         'İstanbul','Evren','Gizem','Anne','Nefes','Gerçek','Özgürlük','Umut','Pencere','Güven',
         'Kelebek','Yazgı','Ufuk','Merdiven','Anadolu','Duru','Yakamoz','Toprak','Birlik','Üstad','Hazan','Işıl','Başak','Vatan',
         'Gönenç','Hayat','Gökyüzü','Deniz','Gönül','Kutlu','Barış','Mor','Sarı','Kırmızı','Kahverengi','Kapı','Lezzetli','Mağdur',
         'Göçebe','Bardak','Üzülmek','Jandarma','Şemsiye','Kar','Yağmur','Kütüphane','Çanta','cemaldak','Çimento','Masa','Mavi',
         'Yeşil','Gri','Perde','Palto','Terlik','Valiz','Modem','Çorap','Ütü','Poşet','Torba','Pantolon','Kış','Yaz','Sonbahar',
         'İlkbahar','Bant','Telefon','Televizyon','Şapka','Kitap','Dergi','Kurban','Hakim','Avukat','Polis','Mühendis','Doktor',
         'Dünya','Mars','Jüpiter','Satürn','Güneş','Ay','Kalp','Beyin','Parmak','Mide','Kulak','Cam','Kum','Taş','Sandalye',
         'Klavye','Fare','Aslan','Kedi','Köpek','Maymun','Böcek','Örümcek','Metal','Demir','Bakır','Saklambaç','Sözlük','İngilizce',
         'Almanca','Aydınlık','Karanlık','Gece','Gündüz','Asker','Su','Hava','Halı','Bal','Peynir','Balık','Çay','Kahve','Şeker',
         'Lale','Gül','Çürük','Bıyık','Sakal','Zemin','Bulut','Çorap','Gömlek','Bayburt','Elazığ','Sivas','Çorum','Hatay','İl',
         'Şehir','İlçe','Sokak','Apartman','Edebiyat','Okul','Biyoloji','Matematik','Kalem','Silgi','Gazete','Fare','Lastik','Araba']


score = 0
timeleft = 30
bestScore = 0

def startgame(event):
    global score
    global timeleft
    global bestScore
    if timeleft == 30:
        entryLabel.delete(0, END)
        countdown()
    elif timeleft == 0:
        timeleft = 30
        score = 0
        scoreLabel.config(text="Skor(Score) : "+ str(score))
        bestscoreLabel.config(text="Rekor(Best Score) : " + str(bestScore))
        entryLabel.delete(0,END)
        countdown()
    random.shuffle(words)
    label.config(text=words[0],font=('Helvetica', 60),padx=400)


def countdown():
    global timeleft
    global bestScore
    global score
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text=(">>> Zaman(Timeleft) : " + str(timeleft)+" <<<"))
        timeLabel.after(1000,countdown)
    else:
        label.config(text="Tekrar Başlamak İçin Boşluk Tuşuna Basın\n(Press Spacebar to Restart)",
                     font=('Helvetica', 25))


def getWord(event):
        wrd = ''
        wrd = entryLabel.get() + wrd
        checkWord(wrd)


def checkWord(event):
    global timeleft
    global score
    global bestScore
    if timeleft > 0:
            if event.lower() == label['text'].lower():
                score += 1
                entryLabel.delete(0, END)
                scoreLabel.config(text="Skor(Score) : "+ str(score))
                random.shuffle(words)
                label.config(text=words[0],font=('Helvetica', 60),padx=400)
                if score > bestScore:
                    bestScore = score
                    bestscoreLabel.config(text="Rekor(Best Score) : " + str(bestScore))
                else:
                    bestScore = bestScore
                    bestscoreLabel.config(text="Rekor(Best Score) : " + str(bestScore))
            else:
                entryLabel.delete(0, END)
                scoreLabel.config(text="Skor(Score) : "+ str(score))
                random.shuffle(words)
                label.config(text=words[0],font=('Helvetica', 60),padx=400)
                if score > bestScore:
                    bestScore = score
                    bestscoreLabel.config(text="Rekor(Best Score) : " + str(bestScore))
                else:
                    bestScore = bestScore
                    bestscoreLabel.config(text="Rekor(Best Score) : " + str(bestScore))


wndw = Tk()
wndw.geometry("700x630")
wndw.resizable(0, 0)
wndw.title("Tell Megatron, Let's Tango(by cmldk)")
wndw.configure(background="#B3A812")

infoLabel = Label(wndw,text="Büyük yada Küçük Harf Yazdığınız Etkilememektedir\n(Doesn't Matter Upper or Lower Case)",
                  font=('Tahoma 17 bold'),background="#052626",fg="#B3A812",padx=300,pady=11,relief=RAISED,borderwidth=10)
infoLabel.pack()

bestscoreLabel = Label(wndw,text="Rekor(Best Score) : "+ str(bestScore),font=('Tahoma 25 bold'),background="#B3A812",fg="black",
                       padx=250,pady=10,relief=RAISED,borderwidth=10)
bestscoreLabel.pack()

scoreLabel = Label(wndw,text="Skor(Score) : "+ str(score),font=('Tahoma 25 bold'),background="#B3A812",fg="black",
                    padx=280,pady=10,relief=RAISED,borderwidth=10)
scoreLabel.pack()

timeLabel = Label(wndw,text=(">>> Zaman(Timeleft) : " + str(timeleft)+" <<<"),font=('Tahoma 25 bold'),background="#052626",fg="#B3A812",
                                relief=RAISED,borderwidth=10,padx=300,pady=30)
timeLabel.pack()

label = Label(wndw,text="Hoşgeldin\nBaşlamak İçin Boşluk Tuşuna Basın\n(Press Spacebar to Restart)"
              ,font=('Helvetica 25 bold'),background="#052626",fg="#B3A812",padx=200,pady=30,relief=RAISED,borderwidth=10)
label.pack()

entryLabel = Entry(wndw,borderwidth=6)
wndw.bind('<space>',startgame)
wndw.bind('<Return>',getWord)
entryLabel.pack()
entryLabel.focus_set()
entryLabel.place(x=265,y=570)



wndw.mainloop()

