from tkinter import *
import backend

help_text = '''
    DOCSTRING: It is a UI application which is student and teacher informations are stored in SQLite database system.
    
    INPUT: 
    For student side :
    • Name and Surname
    • School ID
    
    For teacher side:
    • Name and Surname
    • Lecture
    
    OUTPUT:
    Some information about students and teachers from  the database.(Name, Surname, School ID, Lecture)
'''

def command_help():
    help_window = Toplevel()
    help_window.geometry("450x350")
    help_window.title("Help")
    help_window.resizable(width=False,height=False)
    
    t_help = Text(help_window,height=300,width=300)
    t_help.insert(1.0,help_text)
    t_help.config(state=DISABLED)
    t_help.pack()
    
    help_window.mainloop()
    
def students_open():

    def get_selected_row(event):
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END,selected_tuple[2])
         
    def view_command():
        l3.configure(text="")
        list1.delete(0, END)
        for row in backend.view_student():
            list1.insert(END, row)

    def search_command():
        list1.delete(0, END)
        for row in backend.search_student(sc_id.get(), lectures.get()):
            list1.insert(END, row)
        l3.configure(text="Your value is searching.")

    def add_command():
        backend.insert_student(sc_id.get(), lectures.get())
        list1.delete(0, END)
        list1.insert(END, (sc_id.get(), lectures.get()))
        l3.configure(text="Your value is added.")

    def delete_command():
        backend.delete_student(selected_tuple[0])
        l3.configure(text="Your value is deleted.")
        
    def update_command():
        backend.update_student(selected_tuple[0], sc_id.get(), lectures.get())
        l3.configure(text="Your value is updated.")
        
        
    student = Toplevel()
    student.title("Student Database")
    student.geometry("400x400")
    student.resizable(width=False,height=False)

    l1 = Label(student, text="Name/Surname")
    l1.grid(row=0, column=0,pady=7)

    l2 = Label(student, text="School ID")
    l2.grid(row=0, column=2)
    
    l3 = Label(student)
    l3.grid(row=1,column=1)
    
    sc_id = StringVar()
    e1 = Entry(student, textvariable=sc_id)
    e1.grid(row=0, column=1)

    lectures = StringVar()
    e2 = Entry(student, textvariable=lectures)
    e2.grid(row=0, column=3)

    list1 = Listbox(student, height=20, width=35)
    list1.grid(row=8, column=0, rowspan=20, columnspan=2)

    sb1 = Scrollbar(student, orient=VERTICAL)
    sb1.grid(row=8, column=2, sticky=(N,S),rowspan=20)

    list1.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list1.yview)

    list1.bind("<<ListboxSelect>>", get_selected_row)

    b1 = Button(student, text="View all", width=12,command= view_command)
    b1.grid(row=14, column=3)

    b2 = Button(student, text="Search entry", width=12,command=search_command)
    b2.grid(row=15, column=3)

    b3 = Button(student, text="Add", width=12,command=add_command)
    b3.grid(row=16, column=3)

    b4 = Button(student, text="Delete selected", width=12,command=delete_command)
    b4.grid(row=17, column=3)

    b5 = Button(student, text="Update selected", width=12,command=update_command)
    b5.grid(row=18, column=3)

    student.mainloop()

def teachers_open():
    
    def get_selected_row(event):
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END,selected_tuple[2])
        
    def view_command():
        list1.delete(0, END)
        for row in backend.view_teacher():
            list1.insert(END, row)
    
    def search_command():
        list1.delete(0, END)
        for row in backend.search_teacher(names.get(), lecture.get()):
            list1.insert(END, row)
        l3.configure(text="Your value is searching.")
        
    def add_command():
        backend.insert_teacher(names.get(), lecture.get())
        list1.delete(0, END)
        list1.insert(END, (names.get(), lecture.get()))
        l3.configure(text="Your value is added.")
        
    def delete_command():
        backend.delete_teacher(selected_tuple[0])
        l3.configure(text="Your value is deleted.")
        
    def update_command():
        backend.update_teacher(selected_tuple[0], names.get(), lecture.get())
        l3.configure(text="Your value is updated.")
        
    teacher = Toplevel()
    teacher.title("Teacher Database")
    teacher.geometry("400x400")
    teacher.resizable(width=False,height=False)

    l1 = Label(teacher, text="Name/Surname")
    l1.grid(row=0, column=0, pady=7)

    l2 = Label(teacher, text="Lesson")
    l2.grid(row=0, column=2)
    
    l2 = Label(teacher)
    l2.grid(row=1, column=0)
    
    l3 = Label(teacher)
    l3.grid(row=1,column=1)
    
    names = StringVar()
    e1 = Entry(teacher, textvariable=names)
    e1.grid(row=0, column=1)

    lecture = StringVar()
    e2 = Entry(teacher, textvariable=lecture)
    e2.grid(row=0, column=3)

    list1 = Listbox(teacher, height=20, width=35)
    list1.grid(row=8, column=0, rowspan=20, columnspan=2)

    sb1 = Scrollbar(teacher)
    sb1.grid(row=8, column=2, rowspan=20)

    list1.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list1.yview)

    list1.bind('<<ListboxSelect>>', get_selected_row)

    b1 = Button(teacher, text="View all", width=12,command = view_command)
    b1.grid(row=14, column=3)

    b2 = Button(teacher, text="Search entry", width=12,command = search_command)
    b2.grid(row=15, column=3)

    b3 = Button(teacher, text="Add", width=12,command = add_command)
    b3.grid(row=16, column=3)

    b4 = Button(teacher, text="Delete selected", width=12,command = delete_command)
    b4.grid(row=17, column=3)

    b5 = Button(teacher, text="Update selected", width=12,command =update_command )
    b5.grid(row=18, column=3)

    teacher.mainloop()


window_main = Tk()
window_main.geometry("400x350")
window_main.title("Student and Teacher Database")
window_main.resizable(width=False,height=False)

l1 = Label(window_main, text= "Student and Teacher Database Application",width = 100,font = "10")
l1.pack(side=TOP,pady=10)

b1 = Button(window_main, text ="STUDENT",width = 20,height = 10,command = students_open)
b1.place(x=20, y=85)

b2 = Button(window_main, text ="TEACHER",width = 20,height = 10,command = teachers_open)
b2.place(x=230, y=85)

b3 = Button(window_main, text ="Help",width = 20,height = 1,command = command_help)
b3.place(x=125, y=300)

window_main.mainloop()