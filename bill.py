from tkinter import *
import math
import random
from tkinter import messagebox
import os


class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title('BILLING SOFTWARE')
        bg_colour = "black"
        title= Label(self.root, text = "BILLING SOFTWARE",bd = 12,relief = GROOVE,bg = bg_colour
            ,fg = 'white', font = ('arial',30,'bold'),pady = 2).pack(fill = X)



# VARIABLES
### COSMETICS 
        self.soap = IntVar()
        self.face_crm = IntVar()
        self.face_wsh = IntVar()
        self.spray = IntVar()
        self.gel = IntVar()
        self.lotion = IntVar()

### GROCERY 
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()

### COLD DRINK

        self.maza = IntVar()
        self.coke = IntVar()
        self.frooti = IntVar()
        self.thumbsup = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()

###TOTAL PRODUCT PRICE AND TAX VARIABLE

        self.cosmetic_price = StringVar()    
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

###CUSTOMER
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()


# CUSTOMER DETAIL FRAME

        F1 = LabelFrame(self.root,text = 'Customer Details ',bd =10, relief= GROOVE 
            ,font =('arial',15,'bold'),fg = 'gold', bg = bg_colour)
        F1.place(x=0,y=80,relwidth = 1)

        cname_label = Label(F1, text= 'Customer Name',bg = bg_colour 
            , fg = 'white',font =('arial',18,'bold')).grid(row = 0, column = 0)
        cname_txt = Entry(F1, width = 15, font ='arial 15',textvariable = self.c_name, bd = 7
            , relief = SUNKEN).grid(row=0, column=1, pady = 5, padx =10)

        cphn_label = Label(F1, text= ' Phone No.',bg = bg_colour , fg = 'white',font =('arial',18,'bold')).grid(row = 0, column = 2)
        cphn_txt = Entry(F1, width = 15, font ='arial 15'
            ,textvariable = self.c_phone, bd = 7, relief = SUNKEN).grid(row=0, column=3, pady = 5, padx =10)

        cbill_label = Label(F1, text= 'Bill Number',bg = bg_colour 
            , fg = 'white',font =('arial',18,'bold')).grid(row = 0, column = 4)
        cbill_txt = Entry(F1, width = 15, font ='arial 15',textvariable = self.search_bill, bd = 7
            , relief = SUNKEN).grid(row=0, column=5, pady = 5, padx =10)

        bill_btn = Button(F1, text = 'Seach',command = self.find_bill, font = 'arial 12 bold',bd = 7,width = 10).grid(row=0, column=6, pady = 10, padx =10)



# COSMETICS FRAME

        F2 = LabelFrame(self.root,text = 'Cosmetics ',bd =10, relief= GROOVE ,font =('arial',15,'bold'),fg = 'gold', bg = bg_colour)
        F2.place(x=5,y=180,width = 325, height = 380 )

        bath_lbl = Label(F2,text = 'Bath soap',bg = bg_colour ,
         fg = 'lightgreen',font =('arial',16,'bold')).grid(row=0,column=0)
        batg_text = Entry(F2,width = 10,textvariable = self.soap, font =('arial', 15, 'bold')
            , bd = 5, relief = SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        face_cream_lbl = Label(F2,text = 'Face Cream',bg = bg_colour
         , fg = 'lightgreen',font =('arial',16,'bold')).grid(row=1,column=0)
        face_cream_lbl_text = Entry(F2,width = 10,textvariable = self.face_crm
            , font =('arial', 15, 'bold'), bd = 5, relief = SUNKEN).grid(row=1,column=1,pady=10,padx=10)

        facewash_lbl = Label(F2,text = 'Face Wash',bg = bg_colour 
            , fg = 'lightgreen',font =('arial',16,'bold')).grid(row=2,column=0)
        facewash_text = Entry(F2,width = 10,textvariable = self.face_wsh 
            , font =('arial', 15, 'bold'), bd = 5, relief = SUNKEN).grid(row=2,column=1,pady=10,padx=10)

        hairspray_lbl = Label(F2,text = 'Hair Spray',bg = bg_colour 
            , fg = 'lightgreen',font =('arial',16,'bold')).grid(row=3,column=0)
        hairspray_text = Entry(F2,width = 10,textvariable = self.spray
            , font =('arial', 15, 'bold'), bd = 5, relief = SUNKEN).grid(row=3,column=1,pady=10,padx=10)

        hairgel_lbl = Label(F2,text = 'Hair Gel',bg = bg_colour 
            , fg = 'lightgreen',font =('arial',16,'bold')).grid(row=4,column=0)
        hairgel_text = Entry(F2,width = 10,textvariable = self.gel
            , font =('arial', 15, 'bold'), bd = 5, relief = SUNKEN).grid(row=4,column=1,pady=10,padx=10)

        bodylotion_lbl = Label(F2,text = 'Body Lotion',bg = bg_colour
         , fg = 'lightgreen',font =('arial',16,'bold')).grid(row=5,column=0)
        bodylotion_text = Entry(F2,width = 10,textvariable = self.lotion
            , font =('arial', 15, 'bold'), bd = 5, relief = SUNKEN).grid(row=5,column=1,pady=10,padx=10)


#GROCERY FRAMEWORK
        
        F3 = LabelFrame(self.root,text = 'GROCERY ',bd =10, relief= GROOVE ,font =('arial',15,'bold'),fg = 'gold', bg = bg_colour)
        F3.place(x=340,y=180,width = 325, height = 380 )

        g1_lbl = Label(F3,text = 'Rice',bg = bg_colour 
            , fg = 'lightgreen',font =('arial',16,'bold')).grid(row=0,column=0)
        g1_text = Entry(F3,width = 10,textvariable = self.rice, font =('arial', 15, 'bold'), bd = 5, relief = SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        g2_cream_lbl = Label(F3,text = 'Food oil',bg = bg_colour 
            , fg = 'lightgreen',font =('arial',16,'bold')).grid(row=1,column=0)
        g2_cream_lbl_text = Entry(F3,width = 10,textvariable = self.food_oil
            , font =('arial', 15, 'bold'), bd = 5, relief = SUNKEN).grid(row=1,column=1,pady=10,padx=10)

        g3_lbl = Label(F3,text = 'Pulse',bg = bg_colour
         , fg = 'lightgreen',font =('arial',16,'bold')).grid(row=2,column=0)
        g3_text = Entry(F3,width = 10,textvariable = self.daal, font =('arial', 15, 'bold')
            , bd = 5, relief = SUNKEN).grid(row=2,column=1,pady=10,padx=10)

        g4_lbl = Label(F3,text = 'Wheat',bg = bg_colour 
            , fg = 'lightgreen',font =('arial',16,'bold')).grid(row=3,column=0)
        g4_text = Entry(F3,width = 10,textvariable = self.wheat
            , font =('arial', 15, 'bold'), bd = 5, relief = SUNKEN).grid(row=3,column=1,pady=10,padx=10)

        g5_lbl = Label(F3,text = 'Sugar',bg = bg_colour , fg = 'lightgreen',font =('arial',16,'bold')).grid(row=4,column=0)
        g5_text = Entry(F3,width = 10,textvariable = self.sugar
            , font =('arial', 15, 'bold'), bd = 5, relief = SUNKEN).grid(row=4,column=1,pady=10,padx=10)

        g6_lbl = Label(F3,text = 'Tea',bg = bg_colour
         , fg = 'lightgreen',font =('arial',16,'bold')).grid(row=5,column=0)
        g6_text = Entry(F3,width = 10,textvariable = self.tea, font =('arial', 15, 'bold')
            , bd = 5, relief = SUNKEN).grid(row=5,column=1,pady=10,padx=10)


#COLD DRINK FRAME

        F4 = LabelFrame(self.root,text = 'Cold Drink',bd =10, relief= GROOVE ,font =('arial',15,'bold'),fg = 'gold', bg = bg_colour)
        F4.place(x=670,y=180,width = 325, height = 380 )

        c1_lbl = Label(F4,text = 'Maza',bg = bg_colour , fg = 'lightgreen',font =('arial',16,'bold')).grid(row=0,column=0)
        c1_text = Entry(F4,width = 10,textvariable = self.maza, font =('arial', 15, 'bold')
            , bd = 5, relief = SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        c2_cream_lbl = Label(F4,text = 'coke',bg = bg_colour , fg = 'lightgreen'
            ,font =('arial',16,'bold')).grid(row=1,column=0)
        c2_cream_lbl_text = Entry(F4,width = 10,textvariable = self.coke
            , font =('arial', 15, 'bold'), bd = 5, relief = SUNKEN).grid(row=1,column=1,pady=10,padx=10)

        c3_lbl = Label(F4,text = 'Frooti',bg = bg_colour , fg = 'lightgreen'
            ,font =('arial',16,'bold')).grid(row=2,column=0)
        c3_text = Entry(F4,width = 10,textvariable = self.frooti, font =('arial', 15, 'bold')
            , bd = 5, relief = SUNKEN).grid(row=2,column=1,pady=10,padx=10)

        c4_lbl = Label(F4,text = 'Thumbs Up',bg = bg_colour , fg = 'lightgreen'
            ,font =('arial',16,'bold')).grid(row=3,column=0)
        c4_text = Entry(F4,width = 10,textvariable = self.thumbsup, font =('arial', 15, 'bold'), bd = 5, relief = SUNKEN).grid(row=3,column=1,pady=10,padx=10)

        c5_lbl = Label(F4,text = 'Limca',bg = bg_colour , fg = 'lightgreen'
            ,font =('arial',16,'bold')).grid(row=4,column=0)
        c5_text = Entry(F4,width = 10,textvariable = self.limca, font =('arial', 15, 'bold'), bd = 5, relief = SUNKEN).grid(row=4,column=1,pady=10,padx=10)

        c6_lbl = Label(F4,text = 'Sprite',bg = bg_colour , fg = 'lightgreen'
            ,font =('arial',16,'bold')).grid(row=5,column=0)
        c6_text = Entry(F4,width = 10,textvariable = self.sprite, font =('arial', 15, 'bold')
            , bd = 5, relief = SUNKEN).grid(row=5,column=1,pady=10,padx=10)

# BILL AREA

        F5 = Frame(self.root,bd=10,relief = GROOVE)
        F5.place(x=1010,y =180, width = 340,height=380)

        bill_title = Label(F5,text = 'Bill Area',font =('arial', 15, 'bold'),bd=7,relief= GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient = VERTICAL)
        self.txtarea = Text(F5, yscrollcommand = scrol_y.set)
        scrol_y.pack(side= RIGHT, fill=Y)
        scrol_y.config(command= self.txtarea.yview)
        self.txtarea.pack(fill = BOTH, expand = 1) 


#BUTTON FRAME


        F6 = LabelFrame(self.root,text = 'Bill Menu',bd =10, relief= GROOVE ,font =('arial',15,'bold'),fg = 'gold', bg = bg_colour)
        F6.place(x=0,y=560,relwidth = 1, height = 140 )

        m1 = Label(F6,text = 'Total Cosmetic Price',bg = bg_colour,fg = 'lightgreen', 
            font = ('arial',16,'bold')).grid(row = 0,column = 0,padx= 20,pady = 1, sticky = 'w')
        m1_txt = Entry(F6,width = 18,textvariable = self.cosmetic_price,
         font = 'arial 10 bold',bd = 7, relief= GROOVE).grid(row = 0,column=1,padx=10,pady=1)
 
        m2 = Label(F6,text = 'Total Grocery Price',bg = bg_colour,fg = 'lightgreen'
            , font = ('arial',16,'bold')).grid(row = 1,column = 0,padx= 20,pady = 1, sticky = 'w')
        m2_txt = Entry(F6,width = 18,textvariable = self.grocery_price, font = 'arial 10 bold'
            ,bd = 7, relief= GROOVE).grid(row = 1,column=1,padx=10,pady=1)
     
        m3 = Label(F6,text = 'Total Cold Drink Price',bg = bg_colour,fg = 'lightgreen'
            , font = ('arial',16,'bold')).grid(row = 2,column = 0,padx= 20,pady = 1, sticky = 'w')
        m3_txt = Entry(F6,width = 18,textvariable = self.cold_drink_price
            , font = 'arial 10 bold',bd = 7, relief= GROOVE).grid(row = 2,column=1,padx=10,pady=1)


        c1 = Label(F6,text = 'Cosmetic Tax',bg = bg_colour,fg = 'lightgreen'
            , font = ('arial',16,'bold')).grid(row = 0,column = 2,padx= 20,pady = 1, sticky = 'w')
        c1_txt = Entry(F6,width = 18,textvariable = self.cosmetic_tax, font = 'arial 10 bold'
            ,bd = 7, relief= GROOVE).grid(row = 0,column=3,padx=10,pady=1)
 
        c2 = Label(F6,text = 'Grocery Tax',bg = bg_colour,fg = 'lightgreen'
            , font = ('arial',16,'bold')).grid(row = 1,column = 2,padx= 20,pady = 1, sticky = 'w')
        c2_txt = Entry(F6,width = 18,textvariable = self.grocery_tax
            , font = 'arial 10 bold',bd = 7, relief= GROOVE).grid(row = 1,column=3,padx=10,pady=1)
     
        c3 = Label(F6,text = 'Cold Drink Tax',bg = bg_colour,fg = 'lightgreen',
         font = ('arial',16,'bold')).grid(row = 2,column = 2,padx= 20,pady = 1, sticky = 'w')
        c3_txt = Entry(F6,width = 18,textvariable = self.cold_drink_tax
            , font = 'arial 10 bold',bd = 7, relief= GROOVE).grid(row = 2,column=3,padx=10,pady=1)

        btn_F = Frame(F6, bd = 7,relief= GROOVE)
        btn_F.place(x = 750,width = 580,height = 105)

        total_btn = Button(btn_F,command = self.total, text = 'Total'
            , bg = 'cadetblue', fg = 'white',bd =2, pady = 15, width = 10
            ,font = 'arial 15 bold').grid(row=0,column=0, padx = 5, pady=5)
        gbill_btn = Button(btn_F, text = 'Gen Bill', bg = 'cadetblue'
            ,command= self.bill_area, fg = 'white',bd =2, pady = 15, width = 10
            ,font = 'arial 15 bold').grid(row=0,column=1, padx = 5, pady=5)
        clear_btn = Button(btn_F, text = 'Clear', command = self.clear_data
            ,bg = 'cadetblue', fg = 'white',bd =2, pady = 15, width = 10
            ,font = 'arial 15 bold').grid(row=0,column=2, padx = 5, pady=5)
        exit_btn = Button(btn_F, text = 'Exit', command = self.exit_sft
         ,  bg = 'cadetblue', fg = 'white',bd =2, pady = 15, width = 10
            ,font = 'arial 15 bold').grid(row=0,column=3, padx = 5, pady=5)
        self.welcome_bill()
 
    def total(self):
        self.c_s_p =  self.soap.get()*40
        self.c_fc_p = self.face_crm.get()*120
        self.c_fw_p = self.face_wsh.get()*60
        self.c_hs_p = self.spray.get()*180
        self.c_hg_p = self.gel.get()*140
        self.c_bl_p = self.lotion.get()*180



        self.total_cosmetic_price = float(  self.c_s_p +
                                       self.c_fc_p+
                                       self.c_fw_p+
                                       self.c_hs_p+
                                       self.c_hg_p+
                                       self.c_bl_p
                                       )

        self.cosmetic_price.set('Rs. '+str(self.total_cosmetic_price))
        self.c_tax = round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set('Rs. ' +str(self.c_tax))

        self.g_r_p =  self.rice.get()*40
        self.g_fo_p = self.food_oil.get()*120
        self.g_d_p = self.daal.get()*60
        self.g_w_p = self.wheat.get()*180
        self.g_s_p = self.sugar.get()*140
        self.g_t_p = self.tea.get()*180


        self.total_grocery_price = float(  
                                       self.g_r_p+ 
                                       self.g_fo_p+
                                       self.g_d_p+
                                       self.g_w_p+
                                       self.g_s_p+
                                       self.g_t_p
                                       )

        self.grocery_price.set('Rs. '+str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price*0.1),2)
        self.grocery_tax.set('Rs. ' +str(self.g_tax))

        self.d_m_p =  self.maza.get()*60
        self.d_c_p = self.coke.get()*60
        self.d_f_p = self.frooti.get()*50
        self.d_t_p = self.thumbsup.get()*45
        self.d_l_p = self.limca.get()*40
        self.d_s_p = self.sprite.get()*60



        self.total_cold_price =    float(  
                                       self.d_m_p+
                                       self.d_c_p+
                                       self.d_f_p+
                                       self.d_t_p+
                                       self.d_l_p+
                                       self.d_s_p
                                       )

        self.cold_drink_price.set('Rs. '+str(self.total_cold_price))
        self.d_tax =round((self.total_cold_price*0.05),2)
        self.cold_drink_tax.set('Rs. '+str(self.d_tax))

        self.total_bill = float(self.total_cosmetic_price + self.total_grocery_price +self.total_cold_price+self.c_tax+self.g_tax+self.d_tax)



    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END,f'\tWelcome to Webcode Retail')
        self.txtarea.insert(END,f'\n Bill No. : {self.bill_no.get()}')
        self.txtarea.insert(END,f'\n Customer Name: {self.c_name.get()}')
        self.txtarea.insert(END,f'\n Phone Number: {self.c_phone.get()}')
        self.txtarea.insert(END,f'\n ====================================')
        self.txtarea.insert(END,f'\n Products\t\t QTY\tPrice')
        self.txtarea.insert(END,f'\n ====================================')



    def bill_area(self):
        if self.c_name.get() == '' or self.c_phone.get() == '':
            messagebox.showerror('Error',"Customer Details are must")

        elif self.cosmetic_price.get() == 'Rs. 0.0' and self.grocery_price.get() == 'Rs, 0.0' and self.cold_drink_price.get() == 'Rs. 0.0':
            messagebox.showerror('Error', 'No product Purchased')
            
        else:    


            self.welcome_bill()
    #COSMETICS IN BILL        
            if self.soap.get() != 0:
                self.txtarea.insert(END,f'\n Bath soap\t\t{self.soap.get()}\t\t{self.c_s_p}')

            if self.face_crm.get() != 0:
                self.txtarea.insert(END,f'\n Face Cream\t\t{self.face_crm.get()}\t\t{self.c_fc_p}')
                
            if self.face_wsh.get() != 0:
                self.txtarea.insert(END,f'\n Face Wash\t\t{self.face_wsh.get()}\t\t{self.c_fw_p}')

            if self.spray.get() != 0:
                self.txtarea.insert(END,f'\n Hair Spray\t\t{self.spray.get()}\t\t{self.c_hs_p}')
                
            if self.gel.get() != 0:
                self.txtarea.insert(END,f'\n Hair Gel\t\t{self.gel.get()}\t\t{self.c_hg_p}')
                
            if self.lotion.get() != 0:
                self.txtarea.insert(END,f'\n Body Lotion\t\t{self.spray.get()}\t\t{self.c_bl_p}')
                

    #GROCERIES IN BILL        
            if self.rice.get() != 0:
                self.txtarea.insert(END,f'\n Rice\t\t{self.soap.get()}\t\t{self.g_r_p}')

            if self.food_oil.get() != 0:
                self.txtarea.insert(END,f'\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_fo_p}')
                
            if self.daal.get() != 0:
                self.txtarea.insert(END,f'\n Pulses\t\t{self.daal.get()}\t\t{self.g_d_p}')

            if self.wheat.get() != 0:
                self.txtarea.insert(END,f'\n Wheat\t\t{self.spray.get()}\t\t{self.g_w_p}')
                
            if self.sugar.get() != 0:
                self.txtarea.insert(END,f'\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}')
                
            if self.tea.get() != 0:
                self.txtarea.insert(END,f'\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}')


    #COLD DRINK IN BILL        
            if self.maza.get() != 0:
                self.txtarea.insert(END,f'\n Maza\t\t{self.soap.get()}\t\t{self.d_m_p}')

            if self.coke.get() != 0:
                self.txtarea.insert(END,f'\n Coke\t\t{self.coke.get()}\t\t{self.d_c_p}')
                
            if self.frooti.get() != 0:
                self.txtarea.insert(END,f'\n Frooti\t\t{self.frooti.get()}\t\t{self.d_f_p}')

            if self.thumbsup.get() != 0:
                self.txtarea.insert(END,f'\n Thumbs Up\t\t{self.thumbsup.get()}\t\t{self.d_t_p}')
                
            if self.limca.get() != 0:
                self.txtarea.insert(END,f'\n Limca\t\t{self.limca.get()}\t\t{self.d_l_p}')
                
            if self.sprite.get() != 0:
                self.txtarea.insert(END,f'\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}')


            self.txtarea.insert(END,f'\n -----------------------------------')
            if self.cosmetic_tax.get()!= 'Rs. 0.0':
                self.txtarea.insert(END,f'\n Cosmetic Tax\t\t\t\t\t{self.cosmetic_tax.get()}')

            if self.grocery_tax.get()!= 'Rs. 0.0':
                self.txtarea.insert(END,f'\n Grocery Tax\t\t\t\t\t{self.grocery_tax.get()}')

            if self.cold_drink_tax.get()!= 'Rs. 0.0':
                self.txtarea.insert(END,f'\n Cold Drink Tax\t\t\t\t\t{self.cold_drink_tax.get()}')

            self.txtarea.insert(END,f'\n Total Bill : \t\t\t\t\t{self.total_bill}')     
            self.txtarea.insert(END,f'\n ------------------------------------')
            self.save_bill()


    def save_bill(self):
        op = messagebox.askyesno('Save Bill', 'Do you want to save the bill?')
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open('bills/'+ str(self.bill_no.get())+ '.txt','w')
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo('Saved', f'Bill No. :{self.bill_no.get()} saved successfully ')

        else:
            return 

    def find_bill(self):
        present = 'no'
        for i in os.listdir('bills/'):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f'bills/{i}', 'r')
                self.txtarea.delete('1.0', END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present = 'yes'

        if present == 'no':
            messagebox.shoywerror("Error", "Invalid Bill No.")

    def clear_data(self):
        op = messagebox.askyesno('Clear', "Do you really want to Clear Data?")
        if op>0 : 
    ### COSMETICS 
            self.soap.set(0)
            self.face_crm.set(0)
            self.face_wsh.set(0)
            self.spray.set(0)
            self.gel.set(0)
            self.lotion.set(0)

    ### GROCERY 
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

    ### COLD DRINK

            self.maza.set(0)
            self.coke.set(0)
            self.frooti.set(0)
            self.thumbsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)

    ###TOTAL PRODUCT PRICE AND TAX VARIABLE

            self.cosmetic_price.set('') 
            self.grocery_price.set('') 
            self.cold_drink_price.set('')

            self.cosmetic_tax.set('')
            self.grocery_tax.set('')
            self.cold_drink_tax.set('')

    ###CUSTOMER
            self.c_name.set('')
            self.c_phone.set('')
            self.bill_no.set('')
            x = random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill.set('')
            self.welcome_bill()

        else:
            return
            

    def exit_sft(self):
        op = messagebox.askyesno('Exit', "Do you really want to exit?")
        if op>0:
            self.root.destroy()
        else:
            return

        

root = Tk()
obj = Bill_App(root)
root.mainloop()        