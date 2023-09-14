from tkinter import *
from tkinter.messagebox import showinfo,showerror,askyesno,askokcancel,showwarning
from tkinter import ttk
import tkinter.scrolledtext as scrolledtext
from datetime import datetime
from tkinter.filedialog import askopenfilename
import google.auth
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError

class Main(Tk):
    
    # ================================= Login System ========================================
    
    def __init__(self):
        
        # ================================ Main Screen ========================================
        
        super().__init__()
        self.overrideredirect(True)
        self.iconbitmap('')
        #===========================================================================================
        
        # window_width = 750
        # window_height = 500
        window_width = 650
        window_height = 300
        
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        
        super().geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        
        # ================================================================================================
        
        # super().state("zoomed")
        # super().title("Retail Management System")
        self.config(bg="white")
        
        # =============================== Back Ground ==========================
        #Credits
        self.credit = Label(self,text="IMS - Inventory Management Syestem | Developed By: Syed Muhammad",fg="white",bg="grey").place(x=0,y=685,relwidth=1)
        
        # Management Label
        self.l1 = Label(self,text="Login",font=("Times New Roman","30","bold",),bg="light blue", fg="yellow").place(x=0,y=0,relwidth=1)
        
        # Create a canvas with a blue background (top border)
        # border_color = 'blue'
        # border_height = 5  # You can adjust the border height as needed
        # canvas = Canvas(self, width=self.winfo_screenwidth(), height=border_height, bg=border_color)
        # canvas.pack()


        
        
        # ========================== Setting Variables =============================
    
        self.user_id = StringVar()
        self.user_pass = StringVar()
       
        # ======================= Setting Entries ==============================
       
        # self.f = Frame(self,background="white")
        
        # self.l1 = Label(self.f,bg="white").pack(anchor=CENTER,pady=10)
        
        self.f2 = Frame(self, bg="white")
        self.l2 = Label(self.f2, text="User ID", compound=LEFT, font=("Times New Roman", 14), bg="white")
        self.e1 = Entry(self.f2, bg="white", textvar=self.user_id, font=("Times New Roman", 12), relief=SOLID, width="30")
        self.l3 = Label(self.f2, text="Password", compound=LEFT, font=("Times New Roman", 14), bg="white")
        self.e2 = Entry(self.f2, bg="white", textvar=self.user_pass, show="*", font="lucida 11", relief=SOLID, width="30")

        # Grid layout for the widgets within self.f2
        self.l2.grid(padx=20, pady=25, row=1, column=0)
        self.e1.grid(padx=30, pady=25, row=1, column=4)
        self.l3.grid(padx=20, row=2, column=0)
        self.e2.grid(padx=30, row=2, column=4)

        # Place self.f2 at the center of the screen
        self.f2.place(x=100, y=70)

        
        self.button = Button(self,text = "Login",font=("Times New Roman",12,"bold"),relief = "raised",borderwidth=2, activebackground='green', bg='green',width=12, command=self.login_check).place(x=280, y=200)
        
        self.exit_button = Button(self,text = "Exit",font=("Times New Roman",12,"bold"),relief = "raised",borderwidth=2,bg='green', activebackground='green',width=12, command=self.exit_screen).place(x=500, y=250)
        
        # self.f.pack(x=,y=)
       
        # ======================= Comman attributes ==============================
       
        self.date = datetime.now()
        self.date_today = f"{self.date.day}/{self.date.month}/{self.date.year}"
       
        # ========================================================================
        self.mainloop()
        
    def exit_screen(self):
        self.destroy()
    
    def login_check(self):
        userid = self.user_id.get()
        userpass = self.user_pass.get()
        if userid == "user" and userpass == "user":
            self.destroy()
        else:
            showerror("Error","Write correct credentials")

class SoftwareScreen(Tk):
    
    def __init__(self):
        # ================================ Main Screen ========================================
        
        super().__init__()
        # self.overrideredirect(True)
        # self.iconbitmap('')
        #===========================================================================================
        
        # window_width = 750
        # window_height = 500
        window_width = 1000
        window_height = 650
        
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        
        super().geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        
        # ================================================================================================
        
        # super().state("zoomed")
        # super().title("Retail Management System")
        self.config(bg="white")
        
        # ================================= Variables ========================================================
        
        self.recipients_file_name = StringVar()
        self.html_file_name = StringVar()
        self.token_json_file_name = StringVar()
        
        self.subject_mail = StringVar()
        self.spoof_name = StringVar()
        
        self.sending_mail = StringVar()
        
        # =============================== Back Ground ==========================
        #Credits
        # self.credit = Label(self,text="IMS - Inventory Management Syestem | Developed By: Syed Muhammad",fg="white",bg="grey").place(x=0,y=685,relwidth=1)
            
        #=======================================================================
        self.l1 = Label(self,text="Bulk Mailer",font=("Times New Roman","30","bold",),bg="light blue", fg="yellow").place(x=0,y=0,relwidth=1)  
        
        # ===========================================================================================
        self.uploads_info = LabelFrame(self, text="Uploads Info",font=("Times New Roman","20"), width="450", height="300", borderwidth="2", bg="white", labelanchor='n')
        
            # -----------------------------------------------------------
        
        self.recipients_upload_frame = Frame(self.uploads_info, bg="white")
        
        self.recipients_upload_label = Label(self.recipients_upload_frame, text="Upload Recipients File", font=("Times New Roman", "15"), bg="white")
        self.recipients_upload_label.grid(row=0, column=0, columnspan=1)
        
        self.recipients_upload_entry = Entry(self.recipients_upload_frame, textvariable=self.recipients_file_name, font=("Times New Roman", "15"), width="30", bg="white")
        self.recipients_upload_entry.grid(row=1, column=0, columnspan=1, padx=15, pady=10)
        
        self.recipients_upload_button = Button(self.recipients_upload_frame, text="Upload", font=("Times New Roman", "12"), width="10", bg="light blue")
        self.recipients_upload_button.grid(row=1, column=1)
        
        self.recipients_upload_frame.place(x=5, y=5) 
        
            # ---------------------------------------------------------------
            
        self.html_upload_frame = Frame(self.uploads_info, bg="white")        
        
        self.html_upload_label = Label(self.html_upload_frame, text="Upload HTML File", font=("Times New Roman", "15"), bg="white")
        self.html_upload_label.grid(row=0, column=0, columnspan=1)
        
        self.html_upload_entry = Entry(self.html_upload_frame, textvariable=self.html_file_name, font=("Times New Roman", "15"), width="30", bg="white")
        self.html_upload_entry.grid(row=1, column=0, columnspan=1, padx=15, pady=10)
        
        self.html_upload_button = Button(self.html_upload_frame, text="Upload", font=("Times New Roman", "12"), width="10", bg="light blue")
        self.html_upload_button.grid(row=1, column=1)
        
        self.html_upload_frame.place(x=5, y=80)    
        
            # ---------------------------------------------------------------
            
        self.token_json_upload_frame = Frame(self.uploads_info, bg="white")
        
        self.token_json_upload_label = Label(self.token_json_upload_frame, text="Upload Token(JSON) File", font=("Times New Roman", "15"), bg="white")
        self.token_json_upload_label.grid(row=0, column=0, columnspan=1)
        
        self.token_json_upload_entry = Entry(self.token_json_upload_frame, textvariable=self.token_json_file_name, font=("Times New Roman", "15"), width="30", bg="white")
        self.token_json_upload_entry.grid(row=1, column=0, columnspan=1, padx=15, pady=10)
        
        self.token_json_upload_button = Button(self.token_json_upload_frame, text="Upload", font=("Times New Roman", "12"), width="10", bg="light blue")
        self.token_json_upload_button.grid(row=1, column=1)
        
        self.token_json_upload_frame.place(x=5, y=160)    
            
            # ---------------------------------------------------------------------------------------------------------------
            
        self.uploads_info.place(x=30, y=80)  
        
        # =============================================================================================================================
        
        self.desc_info = LabelFrame(self, text="Descriptions Info",font=("Times New Roman","20"), width="450", height="300", borderwidth="2", bg="white", labelanchor='n')
        
            # ----------------------------------------------------------------------------------------------------------------
            
        self.subject_info_frame = Frame(self.desc_info, bg="white")
        
        self.subject_info_label = Label(self.subject_info_frame, text="Subject:", font=("Times New Roman", "15"), bg="white")
        self.subject_info_label.grid(row=0, column=0, padx=8)
        
        self.subject_info_entry = Entry(self.subject_info_frame, textvariable = self.subject_mail, font=("Times New Roman", "15"), borderwidth=1, background="light yellow", width="33" )
        self.subject_info_entry.grid(row=0, column=1, padx=8)
        
        self.subject_info_frame.place(x=5, y=5)
        
            # ---------------------------------------------------------------------------------------------------------------
            
        self.spoof_name_frame = Frame(self.desc_info, bg="white")
        
        self.spoof_name_label = Label(self.spoof_name_frame, text="Name(Spoof):", font=("Times New Roman", "15"), bg="white")
        self.spoof_name_label.grid(row=0, column=0, padx=8)
        
        self.spoof_name_entry = Entry(self.spoof_name_frame, textvariable = self.spoof_name, font=("Times New Roman", "15"), borderwidth=1, background="light yellow", width="29" )
        self.spoof_name_entry.grid(row=0, column=1)
        
        self.spoof_name_frame.place(x=5, y=50)
            
            # ----------------------------------------------------------------------------------------------------------------
        
        self.description_mail_frame = Frame(self.desc_info, bg="white")
        
        self.description_mail_label = Label(self.description_mail_frame, text="Mail Description", font=("Times New Roman", "15"), bg="white", justify="center")
        self.description_mail_label.grid(row=0, column=0, padx=8)
        
        self.description_mail_text = scrolledtext.ScrolledText(self.description_mail_frame, font=("Times New Roman", "15"), borderwidth=1, background="light yellow", width="41", height="5", wrap='word', undo=True)
        self.description_mail_text.grid(row=1, column=0, padx=5, pady=10)
        
        self.description_mail_frame.place(x=5, y=100)
            
            # ----------------------------------------------------------------------------------------------------------------
        
        self.desc_info.place(x=520, y=80)  
        
        # ======================================== Email Structure and Send Button ===========================================
        
        self.submit_mail_frame = Frame(self, borderwidth="2", width=940, bg="white")
        
            # -------------------------------------------------------------------------------------------------------
        
        self.write_mail_label = Label(self.submit_mail_frame, text="Enter Your Email:", font=("Times New Roman", 15), bg="white") 
        self.write_mail_label.grid(row=0, column=0)

        self.write_mail_entry = Entry(self.submit_mail_frame, textvariable = self.sending_mail, font=("Times New Roman", 16), bg="light yellow", width=30) 
        self.write_mail_entry.grid(row=0, column=1, padx=10)

        self.send_mail_button = Button(self.submit_mail_frame, text="Submit Mail", font=("Times New Roman", 15), bg="light green") 
        self.send_mail_button.grid(row=0, column=2, padx=60)        
        
        self.submit_mail_frame.place(x=30, y=400)
        
        # ======================================== Treeview ======================================================================
        
        self.treeview_frame = Frame(self)
        
        # ----------------------------------    ------------------------------
        
        self.style = ttk.Style()
        self.style.configure("Treeview", background="#D3D3D3", foreground="black", fieldbackground="white", rowheight=25)
        self.style.theme_use("default")
        self.style.configure("Treeview.Heading", font=("Times", 15))
        self.style.configure(".", font="Times 12")
        # ---------------------------------   ----------------------------
            
        self.yscrollbar = Scrollbar(self.treeview_frame)
        self.yscrollbar.pack(side=RIGHT,fill=Y)
        
        # -----------------------------------    ------------------------------------------
        
        #
        col = ("S.No", "Mail ID", "Sent To")
        
        #
        self.treeview = ttk.Treeview(self.treeview_frame, height=8, show="headings", columns=col, yscrollcommand=self.yscrollbar.set)
        
        #
        
        # for i in range(len(col)):
        #     self.treeview.column(col[i], width=len(col[i])+2, anchor=W)
        
        self.treeview.column(col[0], width=100, anchor=W)
        self.treeview.column(col[1], width=300, anchor=W)
        self.treeview.column(col[2], width=500, anchor=W)
            
        #
        for i in range(len(col)):
            self.treeview.heading(col[i], text=col[i], anchor=CENTER)

        #
        # if os.path.exists(f"Products/{self.seller_info[2]}.csv"):
        #     self.products = Filing.file_read(dir_name="Products", file_name=self.seller_info[2])
        #     if len(self.products) > 1:
        #         for i in self.products[1:]:
        #             self.treeview.insert(parent="", index="end", iid=self.count, text="", values=(self.count, i[1], i[2], i[3], i[4], i[5], i[6]))
        #             self.count += 1
        
        #
        self.treeview.pack(fill=BOTH)
        #
        self.yscrollbar.config(command=self.treeview.yview)

        #
        self.treeview_frame.place(x=25, y=460, width=950)

        
        # =============================================================================================================================
            
        self.mainloop()
        
        
if __name__ == "__main__":
    SoftwareScreen()
    # SCOPES = ['https://www.googleapis.com/auth/gmail.send']
    # creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # service = build('gmail', 'v1', credentials=creds)
    # print(type(service))
    # print(service)
    # print(dir(service.users().getProfile()))