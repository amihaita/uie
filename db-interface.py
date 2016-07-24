import Tkinter
import MySQLdb
from Tkinter import IntVar


class Begueradj(Tkinter.Frame):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Tkinter.Frame.__init__(self, parent)
        self.parent=parent
        self.initialize_user_interface()

    def initialize_user_interface(self):
        """Draw a user interface allowing the user to type
        MySQL server credentials
        """
        self.parent.title("DB operations")
        self.parent.grid_rowconfigure(0,weight=1)
        self.parent.grid_columnconfigure(0,weight=1)
        self.parent.config(background="lavender")

        self.label_user=Tkinter.Label(self.parent,text="DB User: ",anchor=Tkinter.W,background="dark slate gray",foreground="white", font="Helvetica 8  bold")
        self.label_password=Tkinter.Label(self.parent,text="DB Password:", anchor=Tkinter.W,background="dark slate gray",foreground="white", font="Helvetica 8  bold")

        self.label_user.grid(row=0,column=0,sticky=Tkinter.E+Tkinter.W)
        self.label_password.grid(row=1,column=0, sticky=Tkinter.E+Tkinter.W)

        self.dbuser=Tkinter.Entry(self.parent)
        self.dbpassword=Tkinter.Entry(self.parent,show="*")

        self.dbuser.grid(row=0,column=1,sticky=Tkinter.E+Tkinter.W)
        self.dbpassword.grid(row=1,column=1,sticky=Tkinter.E+Tkinter.W)

        self.connectb=Tkinter.Button(self.parent,text="Log in",font="Helvetica 10 bold",command=self.dbconnexion)
        self.cancelb=Tkinter.Button(self.parent,text="Cancel",command=self.parent.quit,font="Helvetica 10 bold")

        self.connectb.grid(row=2,column=1,sticky=Tkinter.W)
        self.cancelb.grid(row=2,column=2)

    def item_insertion_window(self):
        self.new_window=Tkinter.Toplevel(self)
        self.new_window.wm_title("Add my favorite stars")
        self.new_window.grid_rowconfigure(0, weight=1)
        self.new_window.grid_columnconfigure(0, weight=1)

        self.exitb=Tkinter.Button(self.new_window,text="Exit",command=self.new_window.quit)
        self.submitb=Tkinter.Button(self.new_window,text="Submit",command=self.increment_db)
        self.exitb.grid(row=8,column=1)
        self.submitb.grid(row=8,column=0,sticky=Tkinter.W)

        self.v=IntVar()
        self.tvstars=[('YOWERI KAGUTA MUSEVENI', 1), ('KIIZA BESIGYE', 2),
                      ('AMAAMA JOHN MBABAZI ', 3), ('KARUNGI SHARON', 4),
                      ('BYAMUKAMA OSCAR', 5), ('MATILDA MOREEN', 6),
                      ('DUNCANS', 7)]
        self.i=0
        for self.txt, star in self.tvstars:
            self.i=self.i+1
            self.rb=Tkinter.Radiobutton(self.new_window,text=self.txt,variable=self.v,value=star)
            self.rb.grid(row=self.i,column=0,sticky=Tkinter.W)


    def which_artist(self,radiob):
        self.artists = {
                        1:"YOWERI KAGUTA MUSEVENI",
                        2:"KIIZA BESIGYE",
                        3:"AMAAMA JOHN MBABAZI",
                        4:"KARUNGI SHARON",
                        5:"BYAMUKAMA OSCAR",
                        6:"MATILDA MOREEN",
                        7:"DUNCANS",
        }
        return self.artists.get(radiob,"Unknown")

    def increment_db(self):
        #print self.v.get()
        self.chosenartist=self.which_artist(self.v.get())
        print(self.chosenartist)

        self.config = {
                  'user': 'begueradj',
                  'passwd': 'begueradj',
                  'host': '127.0.0.1',
                  'db': 'begueradj',
        }
        try:
            self.connecttodb=MySQLdb.connect(**self.config)
        except MySQLdb.Error:
            print("Connexion error")

        self.cursor=self.connecttodb.cursor()

        self.cursor.execute("""INSERT INTO mystars(starname) VALUES(%s)""",self.chosenartist)

        self.connecttodb.commit()
        self.connecttodb.close()



    def dbconnexion(self):
        if self.dbuser.get()=="begueradj" and  self.dbpassword.get()=="begueradj":
            self.item_insertion_window()
        else:
            self.initialize_user_interface()



def main():
    root=Tkinter.Tk()
    d=Begueradj(root)
    root.mainloop()

if __name__=="__main__":
    main()