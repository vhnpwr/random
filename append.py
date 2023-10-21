from tkinter import *
import random
root=Tk()

root.title("lucky friend")
root.geometry("600x400")
root.configure(bg='blue')

luckyFriend=Label(root,text="lucky friend",font='arial')
luckyFriend.place(relx=0.5,rely=0.2,anchor=CENTER)

friend=Entry(root)
friend.place(relx=0.5,rely=0.4,anchor=CENTER)

friendList=Label(root)
friendList.place(relx=0.5,rely=0.6,anchor=CENTER)

list1=[]
def addFriend():
    name=friend.get()
    list1.append(name)
    friendList["text"]='your friend list: '+str(list1)
    
    

showList=Button(root,text="show list",command=addFriend)
showList.place(relx=0.5,rely=0.5,anchor=CENTER)

lucky=Label(root)
lucky.place(relx=0.5,rely=0.9,anchor=CENTER)

def randomNumber():
    l=len(list1)
    r=random.randint(0,l)
    friend_name=list1[r]
    lucky["text"]="your lucky friend is: "+str(friend_name)
    

chooseFriend=Button(root,text="choose friend",command=randomNumber)
chooseFriend.place(relx=0.5,rely=0.8,anchor=CENTER)


root.mainloop()