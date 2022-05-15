users={"1":["Bassant Ahmed Elmokadem", "1" , 20000], 
       "215321701332":["Ahmed Abdelrazek Mohamed", "1783" , 3500166], 
       "203659302214":["Salma Mohamed Foaad", "1390" , 520001],
       "126355700193":["Adel Khaled Abdelrahman", "1214" , 111000],
       "201455998011":["Amir Salama Elgendy", "8935" , 178933],
       "201356788002":["Wael Mohamed khairy", "3420" , 55000],
       "203366789564":["Mina Sameh Bishoy", "1179" , 18000], 
       "201236787812":["Omnia Ahmed Awad", "1430" , 180350]}

def login():
    #-------------------------------Exit-----------------------------------------------------#
    def Exit():
        main_window.destroy()
    #----------------------------------------------------------------------------------------#
    
    #-------------------------------Cash_Withdraw-----------------------------------------------------#
    def Cash_Withdraw():
        def ATM_Actuator_Out():
            amount_valid = int(Cash_Withdraw_Entery.get())
            if(amount_valid > 5000):
                pop_amount_check=tkinter.Toplevel()
                pop_amount_check.title("Max_Actuator_Out")
                Max_Actuator_Out=tkinter.Label(pop_amount_check, text="Maximum allowed value per transaction is 5000 L.E ").grid()
            elif((amount_valid%100) != 0):
                pop_amount_check=tkinter.Toplevel()
                pop_amount_check.title("Allowed values")
                Max_Actuator_Out=tkinter.Label(pop_amount_check, text="The allowed values are multiple of 100L.E").grid()
            else:
                pop_amount_check=tkinter.Toplevel()
                pop_amount_check.title("Actuator_Out_Success")
                users[accountNumber][2]=users[accountNumber][2]-amount_valid
                Max_Actuator_Out=tkinter.Label(pop_amount_check, text="operation accomplished successfully").grid()
            
            
        def amount_check():
            amount_valid=int(Cash_Withdraw_Entery.get())
            if( amount_valid > users.get(accountNumber)[2]):
                pop_amount_check=tkinter.Toplevel()
                pop_amount_check.title("messeage")
                label_pop_amount_check=tkinter.Label(pop_amount_check, text = "Sorry no sufficient balance").grid()
            else:
                ATM_Actuator_Out()


        pop_Cash_Withdraw = tkinter.Toplevel()
        pop_Cash_Withdraw.title("Cash_Withdraw")
        pop_Cash_Withdraw.geometry("500x300")
        Cash_Withdraw_Label=tkinter.Label(pop_Cash_Withdraw, text="Please enter the desired amount to withdraw " )
        Cash_Withdraw_Entery=tkinter.Entry(pop_Cash_Withdraw)
        Cash_Withdraw_Ok=tkinter.Button(pop_Cash_Withdraw, text="OK",command=amount_check ,bg="green")
        Cash_Withdraw_Label.grid()
        Cash_Withdraw_Entery.grid()
        Cash_Withdraw_Ok.grid()
    #------------------------------------------------------------------------------------------------------------#
    
    
    
    #----------------------------------------------------Balance_Inquiry---------------------------------------# 
    def Balance_Inquiry():
        def Balance_Inquiry_Ok():
            pop_Balance_Inquiry.destroy()
        
        
        pop_Balance_Inquiry = tkinter.Toplevel()
        pop_Balance_Inquiry.title("Balance_Inquiry")
        pop_Balance_Inquiry.geometry("400x200")
        text = "Acount User Name : "+ users.get(accountNumber)[0]+"  "+"balance : "+str(users.get(accountNumber)[2])
        Balance_Inquiry_Label=tkinter.Label(pop_Balance_Inquiry, text = text ).grid()
        Balance_Inquiry_Ok_BT=tkinter.Button(pop_Balance_Inquiry, text="Ok", command= Balance_Inquiry_Ok).grid()
      #--------------------------------------------------------------------------------------------------------------# 
    
    
       #-------------------------------Change_password-----------------------------------------------------#
        
    
    
    def Password_Change():
        def Check_passwd():
            passwd1=passwd1_Entry.get()
            passwd2=passwd2_Entry.get()
            if(len(passwd1)!=4):
                pop_Check_passwd=tkinter.Toplevel()
                pop_Check_passwd.title("Incorrect password")
                pop_Check_passwd.geometry("400x200")
                pop_Check_passwd_label = tkinter.Label(pop_Check_passwd, 
                                text="The system shall accept only a password with a length four, Please tyr again").grid()
            elif(passwd1!=passwd2):
                pop_Check_passwd=tkinter.Toplevel()
                pop_Check_passwd.title("Incorrect password")
                pop_Check_passwd.geometry("400x200")
                pop_Check_passwd_label = tkinter.Label(pop_Check_passwd, 
                                                       text="Two password not matched, Please tyr again").grid()
            else:
                pop_Check_passwd=tkinter.Toplevel()
                pop_Check_passwd.title("Incorrect password")
                pop_Check_passwd.geometry("400x200")
                pop_Check_passwd_label = tkinter.Label(pop_Check_passwd, 
                                                       text="Change Password Done").grid() 
                users.get(accountNumber)[1]=passwd1
            
        
        
        
        pop_Password_Change=tkinter.Toplevel()
        pop_Password_Change.title("Password Change")
        pop_Password_Change.geometry("400x200")
        passwd1_label = tkinter.Label(pop_Password_Change, text="Enter new password").grid()
        passwd1_Entry = tkinter.Entry(pop_Password_Change, show="*")
        passwd1_Entry.grid()
        passwd2_label = tkinter.Label(pop_Password_Change, text="Enter new password again ").grid()
        passwd2_Entry = tkinter.Entry(pop_Password_Change,  show="*")
        passwd2_Entry.grid()
        Password_Change_BT = tkinter.Button(pop_Password_Change, text="Change Password", command = Check_passwd)
        Password_Change_BT.grid()
    
    
    
    
    #------------------------------------------Fawry_Service-----------------------------------------------------#
    
    def Fawry_Service ():
        
        def charge():
            def Check_Amount():
                check_amount = int(amount_entry.get())
                check_phone = phone_entry.get()
                if(len(check_phone)==0):
                    pop_check_phone = tkinter.Toplevel()
                    pop_check_phone.title("Check_Phone")
                    pop_check_phone.geometry('400x300')
                    check_amount_label = tkinter.Label(pop_check_phone, text="Please enter phone number").grid()
                elif(check_amount> users.get(accountNumber)[2]):
                    pop_check_amount = tkinter.Toplevel()
                    pop_check_amount.title("Check_Amount")
                    pop_check_amount.geometry('400x300')
                    check_amount_label = tkinter.Label(pop_check_amount, text="Sorry no sufficient balance").grid()
                else:
                    pop_check_amount = tkinter.Toplevel()
                    pop_check_amount.title("Check_Amount")
                    pop_check_amount.geometry('400x300')
                    check_amount_label = tkinter.Label(pop_check_amount, text="operation accomplished successfully").grid()
                    users[accountNumber][2]=users[accountNumber][2]-check_amount
                    
            
            pop_charge = tkinter.Toplevel()
            pop_charge.title("Charge")
            pop_charge.geometry('400x300')
            phone_label = tkinter.Label(pop_charge, text="Enter phone number")
            phone_entry = tkinter.Entry(pop_charge)
            amount_label = tkinter.Label(pop_charge, text="Enter amount charge")
            amount_entry = tkinter.Entry(pop_charge)
            charge_BT = tkinter.Button(pop_charge, text="Charge", command=Check_Amount)
            phone_label.grid()
            phone_entry.grid()
            amount_label.grid()
            amount_entry.grid()
            charge_BT.grid()
            
            
            
        
        pop_Fawry_Service = tkinter.Toplevel()
        pop_Fawry_Service.title("Fawry_Service")
        pop_Fawry_Service.geometry("400x200")
        Orange_BT=tkinter.Button(pop_Fawry_Service, text="Orange", width=30, height=2,bg="orange",command=charge).grid()
        Etisalat_BT=tkinter.Button(pop_Fawry_Service, text="Etisalat", width=30, height=2,bg="green",command=charge).grid()
        Vodafone_BT=tkinter.Button(pop_Fawry_Service, text="Vodafone", width=30, height=2,bg="red",command=charge).grid()
        We_BT=tkinter.Button(pop_Fawry_Service, text="We", width=30, height=2, bg="purple",command=charge).grid()
        
    
    
    
    
    
    
    
    
    
        
    
    

    
    
    
    #----------------------------------------------------------------------------------------------------#
    accountNumber = user_entry.get()
    passwd=passwd_entry.get()
    if((accountNumber in users) and users.get(accountNumber)[1]=="This account is locked, please go to the branch"):
        pop=tkinter.Toplevel()
        pop.title("messeage")
        label_pop=tkinter.Label(pop, text = "This account is locked, please go to the branch")
        label_pop.grid()
    elif(accountNumber not in users):
        pop=tkinter.Toplevel()
        pop.title("Error ")
        label_pop=tkinter.Label(pop, text= "NOt found")
        label_pop.grid()
    elif( passwd!=users[accountNumber][1]):
        global i
        i=i+1
        pop=tkinter.Toplevel()
        pop.title("Wrong passwd")
        label_pop=tkinter.Label(pop, text= "Wrong password")
        label_pop.grid()
    else:
        passwd=passwd_entry.get()
        if (users.get(accountNumber)[1]==passwd):
            pop=tkinter.Toplevel()
            pop.geometry("500x300")
            pop.title("Welcome ")
            Cash_Withdraw_BT= tkinter.Button(pop, text = "Cash Withdraw", height=4, width=15 ,command = Cash_Withdraw).grid(row=2, column=0 )
            Balance_Inquiry_BT= tkinter.Button(pop, text = "Balance Inquiry", height=4, width=15, command=Balance_Inquiry ).grid(row=2, column=8 )
            Password_Change_BT= tkinter.Button(pop, text = "Password Change", height=4, width=15, command=Password_Change ).grid(row=3, column=0 )
            Fawry_Service_BT= tkinter.Button(pop, text = "Fawry Service", height=4, width=15,command=Fawry_Service).grid(row=3, column=8 )
            Exit_BT= tkinter.Button(pop, text = "Exit",command =Exit, height=4, width=15,bg="red").grid(row=4, column=4)
            
            Btn = tkinter.Button(main_window,text = "Log In",command=login).grid(row = 3, column = 1)
            x ="welcome "+ users.get(accountNumber)[0]
            label_pop=tkinter.Label(pop, text= x )
            label_pop.grid() 
               
    if (i==3):
        pop=tkinter.Toplevel()
        pop.title("Error ")
        label_pop=tkinter.Label(pop, text= "Sorry you enter wrong password many time, account is locked" )
        label_pop.grid() 
        accountNumber = user_entry.get()
        users[accountNumber][1] = "This account is locked, please go to the branch" 
                    
import tkinter
main_window=tkinter.Tk()
main_window.title("User Login")
main_window.geometry("400x300+100+100")


user_entry=tkinter.Entry(main_window, width=50)
user_label=tkinter.Label(main_window, width=9, text="user")
passwd_entry=tkinter.Entry(main_window, width=50, show="*")
passwd_label=tkinter.Label(main_window, width=9, text="password")




i=0

Btn = tkinter.Button(main_window,text = "Log In",
                     command=login,fg="white",bg="#4a7abc").grid(row = 3, column = 1)

user_label.grid(row = 0, column = 0)
user_entry.grid(row = 0, column = 1)
passwd_label.grid(row = 1, column = 0)
passwd_entry.grid(row = 1, column = 1)

main_window.mainloop()