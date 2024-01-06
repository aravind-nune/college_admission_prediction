import webbrowser
from tkinter import *
import csv
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
import numpy as np
##from sklearn.neighbors import KNeighborsClassifier
##from sklearn.linear_model import LogisticRegression
##from sklearn.svm import SVC
##from sklearn.naive_bayes import GaussianNB
##from sklearn.ensemble import RandomForestClassifier
import os
import pandas as pd

filename = 'testing.csv'
x=[]
y=[]
##df = pd.read_csv("dataset.csv")
##y1 = df.iloc[:,0].values
##y1 = ["name", "Bachelors Aggregate", "IELTS", "TOEFL", "Duolingo", "Backlogs", "Research Papers", "LOR", "Work experience in years", "GRE", "Prediction"]

count=0
a = open("dataset.csv","r")
new = a.readline()
new = a.readline()
while new!='':
    data=new.split(",")
    y.append(data[-1][:-1])
    z=[(float(data[1])),(float(data[2])),(int(data[3])),(int(data[4])),(int(data[5])),(int(data[6])),(int(data[7])),(int(data[8])),(int(data[9]))]
    x.append(z)
    new = a.readline()


a.close()
#print(x,y)
##print(str(data)+ ": data" )
##print(str(y)+ ":y" )
##print(str(z)+ ":z" )
##print(str(x)+ ":x" )

def uab_website():
    webbrowser.open("https://www.uab.edu/home/")

##def draw_decision_tree(clf):
##    dot_data = tree.export_graphviz(clf, out_file=None, feature_names=['Aggregate', 'IELTS', 'Duolingo', 'TOEFL', 'Backlogs', 'Research Paper', 'LOR', 'Work Experience', 'GRE'], class_names=['0', '1', '2', '3', '4'], filled=True, rounded=True, special_characters=True)
##    graph = graphviz.Source(dot_data)
##    graph.render("decision_tree")  # Saves the tree as a PDF file named "decision_tree.pdf"
##    graph.view("decision_tree")

def cleartxtbox():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e9.delete(0, END)
    txt.delete(1.0, END)

##def calculate_metrics(true_labels, predicted_labels):
##    accuracy = accuracy_score(true_labels, predicted_labels)
##    f1 = f1_score(true_labels, predicted_labels, average='weighted')
##    print("Accuracy is : " +str(accuracy))
##    print("F1 score is : " +str(f1))
##    return accuracy, f1

def viewdata():
    top=Toplevel()
    top.title("Group Information")
    top.geometry('500x500')
    canvas.create_image(0,0,image=photo2,anchor=NW)
    label=Label(top,text='Design of Classification Model for Admission Prediction',width=40,bg="light blue",font=("bold",10))
    label.pack()
    label4=Label(top,text='Guide',width=20,bg="light blue",font=("bold",10))
    label4.place(x=50,y=100)
    label5=Label(top,text='XYZ',width=20,bg="light blue",font=("bold",10))
    label5.place(x=250,y=100)
    label6=Label(top,text='Projectees',width=20,bg="light blue",font=("bold",10))
    label6.place(x=50,y=200)
    label7=Label(top,text='Ritish Nedunoori  CT15121',width=20,bg="light blue",font=("bold",10))
    label7.place(x=250,y=200)
    label7=Label(top,text='',width=20,bg="light blue",font=("bold",10))
    label7.place(x=250,y=220)
    label7=Label(top,text='',width=20,bg="light blue",font=("bold",10))
    label7.place(x=250,y=240)
    label7=Label(top,text='',width=20,bg="light blue",font=("bold",10))
    label7.place(x=250,y=260)


##x_train, x_test, y_train, y_test = train_test_split(x, y1, test_size=0.2, random_state=42)

def convert_to_4_scale(h):
    mapscores = {
        100:4.0,
        90:4.0,
        80:3.0,
        70:2.0,
        60:1.0,
        50:0.0
        }
    h = float(h)
    if 5<=h<=10:
        aggcal = 4.0/100
        agg = h*aggcal*10
    elif 50<=h<=100:
        aggcal = 4.0/100
        agg = h*aggcal
    return round(agg,2)

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def is_string(value):
    return isinstance(value, str)

def printClasses():
    global x,y
    txt.delete(0.0,'end')
    clf=tree.DecisionTreeClassifier()
    clf=clf.fit(x,y)

    g = e1.get()        #g contains name
    h=e2.get()          #h contains the Bachelors aggregate 
    r=e3.get()          #r contains ielts
    
    t=e4.get()          #t toefl
    w=e5.get()          #w duolingo
    i=e6.get()          #i is backlogs
    
    s=var.get()         #s is research paper
    l=e7.get()          #l is lor
    m=e8.get()          #work experience
    n=e9.get()          #gre


    # Train the model on the training set
##    clf.fit(x_train, y_train)
##
##    # Make predictions on the test set
##    predictions = clf.predict(x_test)
##
##    # Calculate accuracy and f-measure
##    accuracy, f1 = calculate_metrics(y_test, predictions)

    # Display accuracy and f-measure
    #txt.insert(0.0, f"Accuracy: {accuracy}\nF-measure: {f1}")

    if g== '' or h=='' or (r=='' and  w=='' and t=='')or i=='' or l=='' or m=='' or n =='':
        txt.insert(0.0,"Please fill data")
        
    elif not is_string(g) or not is_float(h) or not is_float(r) or not is_float(m) or not is_integer(w) or not is_integer(t) or not is_integer(i) or not is_integer(s) or not is_integer(l) or not is_integer(n):
        txt.insert(0.0, "Enter correct input")
        

    elif 6.0 <= float(r) <= 9.0 or 70 <= float(w) <= 140 or 80 <= float(t) <= 120:
        h = convert_to_4_scale(h)
        prediction = clf.predict([[h,r,w,t,i,s,l,m,n]])
        print(prediction)
        if prediction=='':
            txt.insert(0.0,'Unfortunately, you are not eligible. Better luck next time.')
        else:
            z=e1.get()
            if prediction == 'Yes':
                pred = "Congratulations " + z + " you are eligible for UAB"
            elif prediction == 'No':
                pred = "Unfortunately " + z + " you are not eligible for UAB"
            txt.insert(0.0,pred)
            entry=str(z)+","+str(h)+","+str(r)+","+str(w)+","+str(t)+","+str(i)+","+str(s)+","+str(l)+","+str(m)+","+str(n)+","+prediction[0]+"\n"
            fp.write(entry)
##        draw_decision_tree(clf)
    else:
        txt.insert(0.0,'English Proficiency test score is low')

         

if os.path.exists(filename):
    fp = open(filename,'a')
else:
    fp = open(filename,'w')
    fp.write('Name, Aggregate, IELTS, Duolingo, TOEFL, Backlogs, Research Paper, LOR, Work Experience, GRE')
#GUI part
    
main=Tk()

main.geometry('1500x1500')
canvas=Canvas(width=1500,height=1800,bg='lightblue')
canvas.pack()

main.title('BlazerNet')
label0=Label(main,text='UAB admission portal',bg="light blue",fg="black",width=20,font=("bold",25))
label0.place(x=475,y=70)
l3=Label(main,text='Name',width=20,bg="light blue",font=("bold",10))
l3.place(x=100,y=110)

label1=Label(main,text=' Bachelors Aggregate',width=20,bg="light blue",font=("bold",10))
label1.place(x=100,y=150)
label2=Label(main,text=' IELTS',width=20,bg="light blue",font=("bold",10))
label2.place(x=100,y=190)

label3=Label(main,text="UAB"
             "\n Department of Computer Science",bg="light blue",fg="black",width=50,font=("bold",15))
label3.place(x=400,y=10)

label8=Label(main,text=' TOEFL',width=20,bg="light blue",font=("bold",10))
label8.place(x=100,y=230)

label9=Label(main,text='Duolingo ',width=20,bg="light blue",font=("bold",10))
label9.place(x=100,y=270)

label10=Label(main,text=' Backlogs',width=20,bg="light blue",font=("bold",10))
label10.place(x=100,y=310)

label11=Label(main,text=' Research Papers ',width=20,bg="light blue",font=("bold",10))
label11.place(x=100,y=350)

label12=Label(main,text=' LOR ',width=20,bg="light blue",font=("bold",10))
label12.place(x=100,y=390)

label12=Label(main,text=' Years of Exp ',width=20,bg="light blue",font=("bold",10))
label12.place(x=100,y=430)

label12=Label(main,text=' GRE ',width=20,bg="light blue",font=("bold",10))
label12.place(x=100,y=470)

e1=Entry(main)
e1.place(x=300,y=110)

e2=Entry(main)
e2.place(x=300,y=150)

e3=Entry(main)
e3.place(x=300,y=190)

e4=Entry(main)
e4.place(x=300,y=230)

e5=Entry(main)
e5.place(x=300,y=270)

var=IntVar()

e6 = Entry(main)
e6.place(x=300,y=310)

e7 = Entry(main)
e7.place(x=300, y=390)

e8 = Entry(main)
e8.place(x=300, y=430)

e9=Entry(main)
e9.place(x=300,y=470)

rb1=Radiobutton(main,text='0',variable=var,value=0)
rb2=Radiobutton(main,text='1',variable=var,value=1)

rb1.place(x=300,y=350)
rb2.place(x=350,y=350)

b1=Button(main,text='Submit',bg="light blue",fg="black",command=printClasses)
b1.place(x=300,y=610)

clr = Button(main, text='Clear',bg="light blue",fg="black", command = cleartxtbox)
clr.place(x = 370,y = 610)

txt=Text(main,width=15,height=5,bg="light yellow",wrap=WORD)
txt.place(x=300,y=510)
#button1.pack()

label13 = Label(main, text = "UAB Portal", fg="blue")
label13.bind("<Button-1>", lambda e:uab_website())

label13.place(x= 350, y = 650)
main.mainloop()

fp.close()


