
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
import mysql.connector as mysql
win = tk.Tk() 
win.title('GUI-Tkinter-MySql')
win.geometry('1100x500') 


label_frame = ttk.LabelFrame(win, text='Enter Login Credentials')
label_frame.grid(row=0, column=0, padx=500,pady=200)


username_label = ttk.Label(label_frame, text = 'Username : ')
password_label = ttk.Label(label_frame, text = 'Password : ')


username_var = tk.StringVar()
password_var = tk.StringVar()


username_entry = ttk.Entry(label_frame, width=20, textvariable = username_var)
password_entry = ttk.Entry(label_frame, width=20, textvariable = password_var)

username_label.grid(row=0, column=0, padx=5, pady=5 )
password_label.grid(row=1 ,column=0, padx=5, pady=5 )
username_entry.grid(row=0, column=1, padx=5, pady=5 )
username_entry.focus()
password_entry .grid(row=1, column=1, padx=5, pady=5 )

def login():
    
    username = username_var.get()
    password = password_var.get()
    if username == '' or password == '':
        m_box.showerror('Login Error', 'Please fill both Username and Password !!! ')
           
    
    elif username == 'user' and password == 'pass':
        
        top1=tk.Toplevel()
        top1.title("GUI-1")
        top1.geometry('1100x500')
        
        label_frame1 = ttk.LabelFrame(top1, text='Enter Your Details')
        label_frame1.grid(row=0, column=0, padx=500,pady=200)


        name_label = ttk.Label(label_frame1, text = 'Name: ')
        branch_label = ttk.Label(label_frame1, text = 'Branch: ')
        regid_label = ttk.Label(label_frame1, text = 'Registration ID: ')


        name_var = tk.StringVar()
        branch_var = tk.StringVar()
        regid_var = tk.StringVar()


        name_entry = ttk.Entry(label_frame1, width=20, textvariable = name_var)
        branch_entry = ttk.Entry(label_frame1, width=20, textvariable = branch_var)
        regid_entry = ttk.Entry(label_frame1, width=20, textvariable = regid_var)

        name_label.grid(row=0, column=0, padx=5, pady=5 )
        branch_label.grid(row=1 ,column=0, padx=5, pady=5 )
        regid_label.grid(row=2 ,column=0, padx=5, pady=5 )

        name_entry.grid(row=0, column=1, padx=5, pady=5 )
        name_entry.focus()
        branch_entry .grid(row=1, column=1, padx=5, pady=5 )
        regid_entry .grid(row=2, column=1, padx=5, pady=5 )

        def submit():
            name = name_var.get()
            branch = branch_var.get()
            regid = regid_var.get()

            if name == '' or branch == ''or regid == '':
                m_box.showerror('Submit Error', 'Please fill every detail !!! ')
                name_entry.delete(0,tk.END)
                branch_entry.delete(0,tk.END) 
                regid_entry.delete(0,tk.END)    

           
            elif name == name_var.get() or branch == branch_var.get() or regid == regid_var.get():
                name_entry.delete(0,tk.END)
                branch_entry.delete(0,tk.END) 
                regid_entry.delete(0,tk.END)  
                
                top2=tk.Toplevel()
                top2.title("GUI-2")
                top2.geometry('1100x500')
                
                label_frame2 = ttk.LabelFrame(top2, text='Click on a subject')
                label_frame2.grid(row=0, column=0, padx=500,pady=10,sticky=tk.N)
                
                def physics():
                    physics_frame = ttk.LabelFrame(top2, text='Enter marks out of 100')
                    physics_frame.grid(row=0, column=0, padx=500,pady=200)

                    physics_label = ttk.Label(physics_frame, text = 'Physics   Marks  : ')
                    physics_var = tk.StringVar()
                    physics_entry = ttk.Entry(physics_frame ,width=20, textvariable = physics_var)
                    physics_label.grid(row=0, column=0, padx=6, pady=5 )
                    physics_entry.grid(row=0, column=1, padx=5, pady=5 )
                    physics_entry.focus()
                   
                    
                
                    
                    
            
                    name_entry.delete(0,tk.END)
                    branch_entry.delete(0,tk.END) 
                    regid_entry.delete(0,tk.END)   
                   
                    def psubmit():
                        physics=physics_var.get()
                        if physics == '':
                            m_box.showerror('Error', 'Please fill marks')
                        elif physics==physics_var.get():
                            try:
                            
                                physics= int(physics)
                            except ValueError: 
                                m_box.showerror('Field Error','Only digits are allowed in marks field')
                            else:
                                if physics<0:
                                    m_box.showwarning('Error', 'Marks cannot be less than 0')
                                elif physics>100:   
                                    m_box.showwarning('Error', 'Marks cannot be more than 100') 
                                else:
                                    phy=str(physics)
                                    con=mysql.connect(host="localhost",user="root",password="pass123",database="tkinter")
                                    cursor=con.cursor()
                                    sql = "INSERT INTO student_info (Name, Branch,Reg_ID,Subject_Marks) VALUES (%s, %s,%s,%s)"
                                    val = (name, branch,regid,"Physics : "+phy)
                                    cursor.execute(sql, val)
                                    con.commit()
                                    con.close()
                                    top3=tk.Toplevel()
                                    top3.title("GUI-3")
                                    top3.geometry('1100x500')
                        
                                    label_frame3 = ttk.LabelFrame(top3, text='Click on an option')
                                    label_frame3.grid(row=0, column=0, padx=500,pady=10,sticky=tk.N)
                                    
                                    def pcgpa():
                                        pcgpa1=physics/9.5
                                        if pcgpa1>10:
                                            pcgpa1=10
                                        pcgpa1="{:.2f}".format(pcgpa1)
                                        pcgpa1=str(pcgpa1)
                                        
                                        ptext = tk.Text(top3, height=2, width=25)
                                        ptext.grid(row=0, column=0, padx=500,pady=200)
                                        ptext.insert(tk.END, "Physics CGPA :"+pcgpa1)
                                        ptext.configure(state='disabled')

                                    cgpa_btn = ttk.Button(label_frame3, text = 'CGPA',command=pcgpa)
                                    cgpa_btn.grid(row=0, column=1,padx=20,pady=20)
                                    
                                    def pgrade():
                                        pcgpa1=physics/9.5
                                        if pcgpa1>10:
                                            pcgpa1=10
                                        pcgpa1="{:.2f}".format(pcgpa1)
                                        if 9<float(pcgpa1)<=10:
                                            pgrade1="O"
                                        elif 8<float(pcgpa1)<=9:
                                            pgrade1="E"   
                                        elif 7<float(pcgpa1)<=8:
                                            pgrade1="A"
                                        elif 6<float(pcgpa1)<=7:
                                            pgrade1="B"
                                        elif 5<float(pcgpa1)<=6:
                                            pgrade1="C"
                                        elif 4<float(pcgpa1)<=5:
                                            pgrade1="D"
                                        else:
                                            pgrade1="F"                     

                                        ptext1 = tk.Text(top3, height=2, width=25)
                                        ptext1.grid(row=0, column=0, padx=500,pady=200)
                                        ptext1.insert(tk.END, "Physics GRADE :"+pgrade1)
                                        ptext1.configure(state='disabled')

                                    grade_btn = ttk.Button(label_frame3, text = 'Grade',command=pgrade)
                                    grade_btn.grid(row=0, column=2,padx=20,pady=20)

                                    def newinput():
                                        top2.destroy()
                                        top3.destroy()

                                    newinput_btn = ttk.Button(label_frame3, text = 'New Input',command=newinput)
                                    newinput_btn.grid(row=0, column=3,padx=20,pady=20)
                        
                                    def close():
                                        win.destroy()
                                        top1.destroy()
                                        top2.destroy()
                                        top3.destroy()


                                    close_btn = ttk.Button(label_frame3, text = 'Close',command=close)
                                    close_btn.grid(row=0, column=4,padx=20,pady=20)
                        


                    psubmit_btn = ttk.Button(physics_frame, text = 'Submit',command=psubmit)
                    psubmit_btn.grid(row=1, column=1,padx=20,pady=20)

                physics_btn = ttk.Button(label_frame2, text = 'Physics',command=physics)
                physics_btn.grid(row=0, column=1,padx=20,pady=20)
                
                def maths():
                    maths_frame = ttk.LabelFrame(top2, text='Enter marks out of 100')
                    maths_frame.grid(row=0, column=0, padx=500,pady=200)

                    maths_label = ttk.Label(maths_frame, text = ' Maths   Marks  :  ')
                    maths_var = tk.StringVar()
                    maths_entry = ttk.Entry(maths_frame ,width=20, textvariable = maths_var)
                    maths_label.grid(row=0, column=0, padx=6, pady=5 )
                    maths_entry.grid(row=0, column=1, padx=5, pady=5 )
                    maths_entry.focus()
                    
                    def msubmit():
                        maths=maths_var.get()
                        if maths == '':
                            m_box.showerror('Error', 'Please fill marks')
                        elif maths==maths_var.get():
                            try:
                            
                                maths= int(maths)
                            except ValueError: 
                                m_box.showerror('Field Error','Only digits are allowed in marks field')
                            else:
                                if maths<0:
                                    m_box.showwarning('Error', 'Marks cannot be less than 0')
                                elif maths>100:   
                                    m_box.showwarning('Error', 'Marks cannot be more than 100') 
                                else:
                                    mat=str(maths)
                                    con=mysql.connect(host="localhost",user="root",password="pass123",database="tkinter")
                                    cursor=con.cursor()
                                    sql = "INSERT INTO student_info (Name, Branch,Reg_ID,Subject_Marks) VALUES (%s, %s,%s,%s)"
                                    val = (name, branch,regid,"Maths : "+mat)
                                    cursor.execute(sql, val)
                                    con.commit()
                                    con.close()
                                    top3=tk.Toplevel()
                                    top3.title("GUI-3")
                                    top3.geometry('1100x500')
                        
                                    label_frame3 = ttk.LabelFrame(top3, text='Click on an option')
                                    label_frame3.grid(row=0, column=0, padx=500,pady=10,sticky=tk.N)
                                    
                                    def mcgpa():
                                        mcgpa1=maths/9.5
                                        if mcgpa1>10:
                                            mcgpa1=10
                                        mcgpa1="{:.2f}".format(mcgpa1)
                                        mcgpa1=str(mcgpa1)
                                        
                                        mtext = tk.Text(top3, height=2, width=25)
                                        mtext.grid(row=0, column=0, padx=500,pady=200)
                                        mtext.insert(tk.END, "Maths CGPA :"+mcgpa1)
                                        mtext.configure(state='disabled') 

                                    cgpa_btn = ttk.Button(label_frame3, text = 'CGPA',command=mcgpa)
                                    cgpa_btn.grid(row=0, column=1,padx=20,pady=20)
                                     
                                    def mgrade():
                                        mcgpa1=maths/9.5
                                        if mcgpa1>10:
                                            mcgpa1=10
                                        mcgpa1="{:.2f}".format(mcgpa1)
                                        if 9<float(mcgpa1)<=10:
                                            mgrade1="O"
                                        elif 8<float(mcgpa1)<=9:
                                            mgrade1="E"   
                                        elif 7<float(mcgpa1)<=8:
                                            mgrade1="A"
                                        elif 6<float(mcgpa1)<=7:
                                            mgrade1="B"
                                        elif 5<float(mcgpa1)<=6:
                                            mgrade1="C"
                                        elif 4<float(mcgpa1)<=5:
                                            mgrade1="D"
                                        else:
                                            mgrade1="F"                     

                                        mtext1 = tk.Text(top3, height=2, width=25)
                                        mtext1.grid(row=0, column=0, padx=500,pady=200)
                                        mtext1.insert(tk.END, "Maths GRADE :"+mgrade1)
                                        mtext1.configure(state='disabled')
                                    
                                    

                                    grade_btn = ttk.Button(label_frame3, text = 'Grade',command=mgrade)
                                    grade_btn.grid(row=0, column=2,padx=20,pady=20)

                                    def newinput():
                                        top2.destroy()
                                        top3.destroy()

                                    newinput_btn = ttk.Button(label_frame3, text = 'New Input',command=newinput)
                                    newinput_btn.grid(row=0, column=3,padx=20,pady=20)
                        
                                    def close():
                                        win.destroy()
                                        top1.destroy()
                                        top2.destroy()
                                        top3.destroy()


                                    close_btn = ttk.Button(label_frame3, text = 'Close',command=close)
                                    close_btn.grid(row=0, column=4,padx=20,pady=20)
                        

                        

                    msubmit_btn = ttk.Button(maths_frame, text = 'Submit',command=msubmit)
                    msubmit_btn.grid(row=1, column=1,padx=20,pady=20)

                maths_btn = ttk.Button(label_frame2, text = 'Maths',command=maths)
                maths_btn.grid(row=0, column=2,padx=20,pady=20)
                
                def chemistry():
                    chemistry_frame = ttk.LabelFrame(top2, text='Enter marks out of 100')
                    chemistry_frame.grid(row=0, column=0, padx=500,pady=200)

                    chemistry_label = ttk.Label(chemistry_frame, text = 'Chemistry Marks: ')
                    chemistry_var = tk.StringVar()
                    chemistry_entry = ttk.Entry(chemistry_frame ,width=20, textvariable = chemistry_var)
                    chemistry_label.grid(row=0, column=0, padx=5, pady=5 )
                    chemistry_entry.grid(row=0, column=1, padx=5, pady=5 )
                    chemistry_entry.focus()

                    def csubmit():
                        chemistry=chemistry_var.get()
                        if chemistry == '':
                            m_box.showerror('Error', 'Please fill marks')
                        elif chemistry==chemistry_var.get():
                            try:
                            
                                chemistry= int(chemistry)
                            except ValueError: 
                                m_box.showerror('Field Error','Only digits are allowed in marks field')
                            else:
                                if chemistry<0:
                                    m_box.showwarning('Error', 'Marks cannot be less than 0')
                                elif chemistry>100:   
                                    m_box.showwarning('Error', 'Marks cannot be more than 100') 
                                else:
                                    chem=str(chemistry)
                                    con=mysql.connect(host="localhost",user="root",password="pass123",database="tkinter")
                                    cursor=con.cursor()
                                    sql = "INSERT INTO student_info (Name, Branch,Reg_ID,Subject_Marks) VALUES (%s, %s,%s,%s)"
                                    val = (name, branch,regid,"Chemistry : "+chem)
                                    cursor.execute(sql, val)
                                    con.commit()
                                    con.close()
                                    top3=tk.Toplevel()
                                    top3.title("GUI-3")
                                    top3.geometry('1100x500')
                        
                                    label_frame3 = ttk.LabelFrame(top3, text='Click on an option')
                                    label_frame3.grid(row=0, column=0, padx=500,pady=10,sticky=tk.N)

                                    def ccgpa():
                                        ccgpa1=chemistry/9.5
                                        
                                        if ccgpa1>10:
                                            ccgpa1=10
                                        ccgpa1="{:.2f}".format(ccgpa1)    
                                        
                                        ccgpa1=str(ccgpa1)
                                        
                                        ctext = tk.Text(top3, height=2, width=25)
                                        ctext.grid(row=0, column=0, padx=500,pady=200)
                                        ctext.insert(tk.END, "Chemistry CGPA :"+ccgpa1)
                                        ctext.configure(state='disabled') 

                                    
                                    cgpa_btn = ttk.Button(label_frame3, text = 'CGPA',command=ccgpa)
                                    cgpa_btn.grid(row=0, column=1,padx=20,pady=20)

                                    def cgrade():
                                        ccgpa1=chemistry/9.5
                                        if ccgpa1>10:
                                            ccgpa1=10
                                        ccgpa1="{:.2f}".format(ccgpa1)
                                        if 9<float(ccgpa1)<=10:
                                            cgrade1="O"
                                        elif 8<float(ccgpa1)<=9:
                                            cgrade1="E"   
                                        elif 7<float(ccgpa1)<=8:
                                            cgrade1="A"
                                        elif 6<float(ccgpa1)<=7:
                                            cgrade1="B"
                                        elif 5<float(ccgpa1)<=6:
                                            cgrade1="C"
                                        elif 4<float(ccgpa1)<=5:
                                            cgrade1="D"
                                        else:
                                            cgrade1="F"                     

                                        ctext1 = tk.Text(top3, height=2, width=25)
                                        ctext1.grid(row=0, column=0, padx=500,pady=200)
                                        ctext1.insert(tk.END, "Chemistry GRADE :"+cgrade1)
                                        ctext1.configure(state='disabled')
                                    

                                    grade_btn = ttk.Button(label_frame3, text = 'Grade',command=cgrade)
                                    grade_btn.grid(row=0, column=2,padx=20,pady=20)
                                    

                                    def newinput():
                                        top2.destroy()
                                        top3.destroy()

                                    newinput_btn = ttk.Button(label_frame3, text = 'New Input',command=newinput)
                                    newinput_btn.grid(row=0, column=3,padx=20,pady=20)
                        
                                    def close():
                                        win.destroy()
                                        top1.destroy()
                                        top2.destroy()
                                        top3.destroy()


                                    close_btn = ttk.Button(label_frame3, text = 'Close',command=close)
                                    close_btn.grid(row=0, column=4,padx=20,pady=20)
                        

                        

                    csubmit_btn = ttk.Button(chemistry_frame, text = 'Submit',command=csubmit)
                    csubmit_btn.grid(row=1, column=1,padx=20,pady=20)


                chemistry_btn = ttk.Button(label_frame2, text = 'Chemistry',command=chemistry)
                chemistry_btn.grid(row=0, column=3,padx=20,pady=20)
       

    

        submit_btn = ttk.Button(label_frame1, text='Submit', command=submit)
        submit_btn.grid(row=3, column=1,padx=1,pady=10)
       
    else:
        m_box.showerror('Login Unsuccessful', 'Invalid Username or Password')

    
    username_entry.delete(0,tk.END)
    password_entry.delete(0,tk.END)    
    top1.mainloop()


login_btn = ttk.Button(label_frame, text = 'Login', command=login)
login_btn.grid(row=2, column=1,padx=1,pady=10)

win.mainloop()

# create table student_info(Name varchar(50),Branch varchar(50),Reg_ID varchar(50),Subject_Marks varchar(50));
# select*from student_info;