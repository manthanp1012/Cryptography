import tkinter.messagebox

from cryptography.fernet import Fernet

class System(object):

    def __init__(self):
        self.m = "Hello There!"
    def rps(self):
        import rock_paper_scissor as rps

    def quiz(self):
        import quiz_game

    def number_guess(self):
        import number_guess


    # def adv(self):
    #     import adventure_game
    def rtd(self):
        import roll_the_dice
    def snake(self):
        import snake
    def pacman(self):
        import pacman
    # def pong(self):
    #     import pong
    def email(self):
        import mail
    def time(self):
        import clock

    def login(self):
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                a = user
                b = fer.decrypt(passw.encode()).decode()


        username = input("Write your username: ")
        password = input("Put your password: ")
        if a == username and b  == password:
            b1 = Button(ob,text='Select Game to play? ',command = '')
            b1.place(x=310,y=100)

            b1 = Button(ob,text = 'Rock/Paper/Scissor',command = things.rps ,fg='green')
            b1.place(x=120,y=160)
            b1 = Button(ob, text='Quiz Game', command=things.quiz,fg='green')
            b1.place(x=300, y=160)
            b1 = Button(ob, text='Number Guess', command=things.number_guess,fg='green')
            b1.place(x=480, y=160)
            # b1 = Button(ob, text='Adventure Game', command=things.adv,fg='green')
            # b1.place(x=550, y=160)
            b1 = Button(ob,text = 'Roll the Dice',command= things.rtd,fg = 'green')
            b1.place(x=120,y=200)
            b1 = Button(ob,text='snake game',command=things.snake,fg='green')
            b1.place(x=300,y=200)
            b1 = Button(ob, text='pacman game', command=things.pacman, fg='green')
            b1.place(x=480, y=200)
            # b1 = Button(ob, text='pong game', command=things.pong, fg='green')
            # b1.place(x=550, y=200)
            # b1 = Button(ob, text='Mail to manthanpatil912@gmail.com for support', command=things.email, fg='red')
            # b1.place(x=340, y=300)


            #things.implement()
        else:
            print("Incorrect details!")
            things.main()
    '''
    def implement(self):
        print("""
        Welcome to Gaming!
        Which Game you wanna play?
        type rps to play rock paper scissor
        type quiz for Computer Quiz
        type ng to play number guess game
        type adv to play adventure game
        """)
        game = input().lower()

        if game == 'rps':
            import rock_paper_scissor
        elif game == 'quiz':
            from quiz_game import quiz
        elif game == 'ng':
            import number_guess
        elif game == 'adv':
            import adventure_game
        else:
            print("Wrong choice!")
            things.implement()'''

    def main(self):
       print("""
        Welcome to Gaming
        click to login and register
        """)
    '''
        choice = int (input())
        if choice == 1:
            things.login()
        elif choice == 2:
            things.registration()
        else:
            print("Wrong choice! Be precise")
            things.main()'''

    def registration(self):
        print("Register to learn programming languages")
        username = input("Write your username: ")

        '''
        def get_username():
            username = e.get()
            label1 = Label(ob, text=username)
            label1.pack()

        def get_password():
            password = e.get()
            label1 = Label(ob,text= password)
            label1.place()


        b3 = Button(ob,text='Username: ',command = get_username)
        b3.place(x=250,y=90)
        b4 = Button(ob,text='Password: ',command = get_password)
        b4.place(x=250,y=130)
        e = Entry(ob, width=50)
        e.pack()
        '''
        with open('passwords.txt','r') as r:
            for line in r.readlines():
                data = line.rstrip()
                u , p = data.split("|")
        if u == username:
            print("Try other username!")
            things.registration()
        else:
            print("Set your password: ")
        password = input()
        print('You have successfully registered!')

        with open("passwords.txt",'a') as file:
            file.write(username + "|" + fer.encrypt(password.encode()).decode() + "\n") #use encrypt to convert password into bytes and encode also converts normal string into bytes string  and decode does convert bytes string into normal string
        things.main()




'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
write_key()'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

things = System()
#things.main()

from tkinter import *
#import tkinter as tk
ob = Tk()
ob.title("Gaming")
ob.geometry("700x400")

def exit():
    response = tkinter.messagebox.askyesno('', 'Do you want to exit?')
    if response > 0:
        ob.destroy()
        return


b1 = Button(ob,text='Welcome to Gaming!', fg = 'red')
b1.place(x=310, y=0)
b2 = Button(ob,text='Register',command = things.registration,fg = 'blue')
b2.place(x=250,y=50)
b1 = Button(ob,text='Login',command = things.login,fg ='blue')
b1.place(x=450,y=50)
# b1 = Button(ob,text='EXIT ',command = exit ,fg ='red')
# b1.place(x=340,y=350)


reg = Frame(ob)
menubar = Menu(reg)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Dashboard', menu=filemenu)

filemenu.add_command(label='mail to manthanpatil912@gmail.com for help', command = things.email)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit)
ob.config(menu=menubar)


ob.mainloop()








