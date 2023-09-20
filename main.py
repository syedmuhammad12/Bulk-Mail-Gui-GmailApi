from tkinter import *
from tkinter.messagebox import showinfo,showerror,askyesno,askokcancel,showwarning
from tkinter import ttk
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename
import pickle
import os
from datetime import datetime
import google.auth
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import psycopg
import pandas
import requests
from bs4 import BeautifulSoup
from random import randint, choices
import datetime
from datetime import date as datee
import pdfkit
import uuid


class ProxyList:

    def __init__(self, url='https://free-proxy-list.net'):
        self.url = url

    def get_random_proxy(self):
        table = self.scrape_list()
        ip = (list(zip(map(lambda td: td.text, table.findAll(
            "td")[::8]), map(lambda td: td.text, table.findAll("td")[1::8]))))
        return {'https': (':'.join(choice(ip)))}

    def get_all_proxies(self):
        table = self.scrape_list()
        ips = list(zip(map(lambda td: td.text, table.findAll(
            "td")[::8]), map(lambda td: td.text, table.findAll("td")[1::8]), map(lambda td: td.text, table.findAll("td")[5::8]), map(lambda td: td.text, table.findAll("td")[6::8])))
        ips = [("proxy", "port", "google", "https")] + ips
        return ips

    def scrape_list(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, 'lxml')
        table = soup.findAll('table')[0]
        return table


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
           
        conn = psycopg.connect("postgres://fcmyqzlp:lGTV9BNw__XkNHIu_W0xNe7ahiOjDq4z@rain.db.elephantsql.com/fcmyqzlp")
        cur = conn.cursor()
        conn.autocommit = True
        a = cur.execute(f"SELECT * FROM Users WHERE user_id='{userid}' and password='{userpass}' and is_available=TRUE")
        if len(a.fetchall())>0:
            # cur.execute(f""" UPDATE Users SET is_available=FALSE WHERE user_id='{userid}' """)
            file = open("cred.txt", "w+")
            file.write(f"user_id={userid}\tpassword={userpass}")
            with open(f'{os.path.expanduser("~")}/cred.pkl', "wb") as pkl:
                pickle.dump(file.read(), pkl)
            file.close()
            os.remove("cred.txt")
            self.destroy()
            SoftwareScreen()
        else:
           showerror("Error","Write correct credentials")
        #     self.destroy()
        #     SoftwareScreen()
        # else:
        #     showerror("Error","Write correct credentials")

class SoftwareScreen(Tk):
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    def __init__(self, bg_color="#121212", fg_color="white"):
        # ================================ Main Screen ========================================
        
        super().__init__()
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.entry_bg = "light yellow"
        self.button_bg = "light blue"
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
        self.config(bg=self.bg_color)
        
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
        self.l1 = Label(self,text="Blaze Mailer",font=("Times New Roman","30","bold",),bg="dark blue", fg="yellow").place(x=0,y=0,relwidth=1)  
        
        # ===========================================================================================
        self.uploads_info = LabelFrame(self, text="Uploads Info",font=("Times New Roman","20"), width="450", height="300", borderwidth="2", bg=self.bg_color, labelanchor='n', foreground=self.fg_color)
        
            # -----------------------------------------------------------
        
        self.recipients_upload_frame = Frame(self.uploads_info, bg=self.bg_color)
        
        self.recipients_upload_label = Label(self.recipients_upload_frame, text="Upload Recipients File", font=("Times New Roman", "15"), bg=self.bg_color, foreground=self.fg_color)
        self.recipients_upload_label.grid(row=0, column=0, columnspan=1)
        
        self.recipients_upload_entry = Entry(self.recipients_upload_frame, textvariable=self.recipients_file_name, font=("Times New Roman", "15"), width="30", bg=self.entry_bg, state='disabled', disabledbackground=self.entry_bg, disabledforeground="black")
        self.recipients_upload_entry.grid(row=1, column=0, columnspan=1, padx=15, pady=10)
        
        self.recipients_upload_button = Button(self.recipients_upload_frame, text="Upload", font=("Times New Roman", "12"), width="10", bg=self.button_bg, activebackground=self.button_bg, command=self.recipient_upload_button_click)
        self.recipients_upload_button.grid(row=1, column=1)
        
        self.recipients_upload_frame.place(x=5, y=5) 
        
            # ---------------------------------------------------------------
            
        self.html_upload_frame = Frame(self.uploads_info, bg=self.bg_color)        
        
        self.html_upload_label = Label(self.html_upload_frame, text="Upload HTML File", font=("Times New Roman", "15"), bg=self.bg_color, foreground=self.fg_color)
        self.html_upload_label.grid(row=0, column=0, columnspan=1)
        
        self.html_upload_entry = Entry(self.html_upload_frame, textvariable=self.html_file_name, font=("Times New Roman", "15"), width="30", bg=self.entry_bg, state='disabled', disabledbackground=self.entry_bg, disabledforeground="black")
        self.html_upload_entry.grid(row=1, column=0, columnspan=1, padx=15, pady=10)
        
        self.html_upload_button = Button(self.html_upload_frame, text="Upload", font=("Times New Roman", "12"), width="10", bg=self.button_bg, activebackground=self.button_bg, command=self.html_upload_button_click)
        self.html_upload_button.grid(row=1, column=1)
        
        self.html_upload_frame.place(x=5, y=80)    
        
            # ---------------------------------------------------------------
            
        self.token_json_upload_frame = Frame(self.uploads_info, bg=self.bg_color)
        
        self.token_json_upload_label = Label(self.token_json_upload_frame, text="Upload Token(JSON) File", font=("Times New Roman", "15"), bg=self.bg_color, foreground=self.fg_color)
        self.token_json_upload_label.grid(row=0, column=0, columnspan=1)
        
        self.token_json_upload_entry = Entry(self.token_json_upload_frame, textvariable=self.token_json_file_name, font=("Times New Roman", "15"), width="30", bg=self.entry_bg, state='disabled', disabledbackground=self.entry_bg, disabledforeground="black")
        self.token_json_upload_entry.grid(row=1, column=0, columnspan=1, padx=15, pady=10)
        
        self.token_json_upload_button = Button(self.token_json_upload_frame, text="Upload", font=("Times New Roman", "12"), width="10", bg=self.button_bg, activebackground=self.button_bg, command=self.token_upload_button_click)
        self.token_json_upload_button.grid(row=1, column=1)
        
        self.token_json_upload_frame.place(x=5, y=160)    
            
            # ---------------------------------------------------------------------------------------------------------------
            
        self.uploads_info.place(x=30, y=80)  
        
        # =============================================================================================================================
        
        self.desc_info = LabelFrame(self, text="Descriptions Info",font=("Times New Roman","20"), width="450", height="300", borderwidth="2", bg=self.bg_color, fg=self.fg_color, labelanchor='n')
        
            # ----------------------------------------------------------------------------------------------------------------
            
        self.subject_info_frame = Frame(self.desc_info, bg=self.bg_color)
        
        self.subject_info_label = Label(self.subject_info_frame, text="Subject:", font=("Times New Roman", "15"), bg=self.bg_color, fg=self.fg_color)
        self.subject_info_label.grid(row=0, column=0, padx=8)
        
        self.subject_info_entry = Entry(self.subject_info_frame, textvariable = self.subject_mail, font=("Times New Roman", "15"), borderwidth=1, background=self.entry_bg, width="33" )
        self.subject_info_entry.grid(row=0, column=1, padx=8)
        
        self.subject_info_frame.place(x=5, y=5)
        
            # ---------------------------------------------------------------------------------------------------------------
            
        self.spoof_name_frame = Frame(self.desc_info, bg=self.bg_color)
        
        self.spoof_name_label = Label(self.spoof_name_frame, text="Name(Spoof):", font=("Times New Roman", "15"), bg=self.bg_color, fg=self.fg_color)
        self.spoof_name_label.grid(row=0, column=0, padx=8)
        
        self.spoof_name_entry = Entry(self.spoof_name_frame, textvariable = self.spoof_name, font=("Times New Roman", "15"), borderwidth=1, background=self.entry_bg, width="29" )
        self.spoof_name_entry.grid(row=0, column=1)
        
        self.spoof_name_frame.place(x=5, y=50)
            
            # ----------------------------------------------------------------------------------------------------------------
        
        self.description_mail_frame = Frame(self.desc_info, bg=self.bg_color)
        
        self.description_mail_label = Label(self.description_mail_frame, text="Mail Description", font=("Times New Roman", "15"), bg=self.bg_color, fg=self.fg_color, justify="center")
        self.description_mail_label.grid(row=0, column=0, padx=8)
        
        self.description_mail_text = scrolledtext.ScrolledText(self.description_mail_frame, font=("Times New Roman", "15"), borderwidth=1, background=self.entry_bg, width="41", height="5", wrap='word', undo=True)
        self.description_mail_text.grid(row=1, column=0, padx=5, pady=10)
        
        self.description_mail_frame.place(x=5, y=100)
            
            # ----------------------------------------------------------------------------------------------------------------
        
        self.desc_info.place(x=520, y=80)  
        
        # ======================================== Email Structure and Send Button ===========================================
        
        self.submit_mail_frame = Frame(self, borderwidth="2", width=940, bg=self.bg_color)
        
            # -------------------------------------------------------------------------------------------------------
        
        self.write_mail_label = Label(self.submit_mail_frame, text="Enter Your Email:", font=("Times New Roman", 15), bg=self.bg_color, fg=self.fg_color) 
        self.write_mail_label.grid(row=0, column=0)

        self.write_mail_entry = Entry(self.submit_mail_frame, textvariable = self.sending_mail, font=("Times New Roman", 16), bg=self.entry_bg, width=30) 
        self.write_mail_entry.grid(row=0, column=1, padx=10)

        self.send_mail_button = Button(self.submit_mail_frame, text="Submit Mail", font=("Times New Roman", 15), bg=self.button_bg, activebackground=self.button_bg) 
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
        
        
    def recipient_upload_button_click(self):
        recipient_file_path = askopenfilename(parent=self, title='Choose Recipient File', initialdir='./',
                                        filetypes=(("TEXT File (*.txt)", "*.txt"), ("CSV File (*.csv)", "*.csv"), ("Excel File (*.xlsx)", "*.xlsx")))
        if recipient_file_path != "":
            self.recipients_file_name.set(recipient_file_path)
            
    def html_upload_button_click(self):
        html_file_path = askopenfilename(parent=self, title='Choose HTML File', initialdir='./',
                                        filetypes=[("HTML File (*.html)", "*.html")])
        if html_file_path != "":
            self.html_file_name.set(html_file_path)
            
    def token_upload_button_click(self):
        token_file_path = askopenfilename(parent=self, title='Choose Credential File', initialdir='./',
                                        filetypes=[("JSON File (*.json)", "*.json")])
        if token_file_path != "":
            self.token_json_file_name.set(token_file_path)
            
    def submit_mail_button(self):
        
        recipient_file = self.recipients_file_name.get()
        html_file = self.html_file_name.get()
        token_file = self.token_json_file_name.get()
        subject_mail = self.subject_mail.get()
        spoof_name = self.spoof_name.get()
        sending_email = self.sending_mail.get()
        
        if recipient_file == "":
            showerror("Error", "Please Select Recipients file")
        elif html_file == "":
            showerror("Error", "Please Select HTML file")
        elif token_file == "":
            showerror("Error", "Please Select Crediential file")
        elif sending_email == "":
            showerror("Error", "Please Enter Sender's Email Address")
        
        else:
            
            try:
                SCOPES = ['https://www.googleapis.com/auth/gmail.send']
                creds = None
                # The file token.json stores the user's access and refresh tokens, and is
                # created automatically when the authorization flow completes for the first
                # time.
                if os.path.exists('token.json'):
                    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
                # If there are no (valid) credentials available, let the user log in.
                if not creds or not creds.valid:
                    if creds and creds.expired and creds.refresh_token:
                        creds.refresh(Request())
                    else:
                        flow = InstalledAppFlow.from_client_secrets_file(
                            token_file, SCOPES)
                        creds = flow.run_local_server(host='localhost', port=50001)
                    # Save the credentials for the next run
                    with open('token.json', 'w') as token:
                        token.write(creds.to_json())
            except Exception as e:
                showerror("Error", f"error is: {e}")
                return 
            
            proxy_list = ProxyList()
            ips = proxy_list.get_all_proxies()
            ips_1 = list(filter(lambda x: x[2]=='yes' and x[3]=='no', ips))
            ips_2 = list(filter(lambda x: x[2]=='yes', ips))
            if len(ips_1)>0:
                ips = list(map(lambda x: f"http://{x[0]}:{x[1]}", proxy_list.get_all_proxies()))
            elif len(ips_2)>0:
                ips = list(map(lambda x: f"https://{x[0]}:{x[1]}", proxy_list.get_all_proxies()))
            mail_list = []
            if recipient_file.endswith(".txt"):
                with open(recipient_file, "r") as f:
                    mail_list = f.readlines()
            else: 
                ip_per_mails = int(len(mail_list)/len(ips))
                if ip_per_mails<1:
                    ip_per_mails = 1
                    ips = ips[:len(mail_list)]
                count_mails_sent = 0
                for i in range(len(ips)):
                    
                    if i == len(ips)-1:
                        pass
                    else:
                        for j in range(ip_per_mails):
                            pass
    
    
    
    def send_mail(self, name, customer_name, email, emailId, description, subjectWord, file_exe_name):
    
        #=======================================================================================================================
        current_time = datetime.datetime.now()
        date = str(current_time.day) + "-" + str(current_time.month) + "-" + str(current_time.year)
        newMessage = MIMEMultipart()
        #=======================================================================================================================
        # [Invoice Number and Subject]
        #=======================================================================================================================
        invoiceNo = randint(1000000, 9999999)
        transaction_id = randint(10000000000, 99999999999)
        rand_string = ''.join(choices(string.ascii_uppercase, k=5))
        num = randint(111111111, 999999999)
        subject = subjectWord + " TID_" + str(invoiceNo)
        # subject = subjectWord
        num = randint(111111111, 999999999)
        newMessage['Subject'] = subject
        newMessage['From'] = f"{name}<{emailId}>"
        #newMessage['From'] = name
        newMessage['To'] = email
        # newMessage['bcc'] = ",".join(email)
        transaction_id = randint(100000000, 999999999)
        random_id = randint(100000000, 999999999)
        xyz_id = (uuid.uuid4())
        #=======================================================================================================================
        # Mail Body Content
        # body = open(bodyFile, 'r').read()
        # body = body.replace('$email', email)
        # body = body.replace('$name', name)
        # body = body.replace('$product_no', rand_string + str(randint(10000, 99999)))
        # body = body.replace('$invoice_no', str(transaction_id))
        # body = body.replace('$digi_no', str(xyz_id))
        # body = body.replace('$date', str(date))
        #=======================================================================================================================
            # Mail PDF File
        html = open('html_code.html', 'r').read()
        # html = html.replace('$email', email)
        html = html.replace('$invoice_no', str(transaction_id))
        html = html.replace('$cus_name', customer_name)
        # html = html.replace('$cus_email', email)
        html = html.replace('$digi_no', str(xyz_id))
        # html = html.replace('$tfn', tfn)
        html = html.replace('$date', date)
        #==========================================================================================================================
        
        customer_tags = datetime.datetime.now().strftime('%d %B %Y')
        customer_tags += "<br>"
        if customer_name != "Customer":
            customer_tags += f"Name: {customer_name}"
            customer_tags += "<br>"
        customer_tags += f"Customer ID: {email}"
        customer_tags += "<br>"
        customer_tags += "<br>"
            
        description = "<br>".join(list(description.splitlines()))
        description = f"<p1 style='font-family: Lucida Sans Typewriter; font-size: 17pt'><b>{customer_tags}{description}</b></p1>"
        
        #========================================================================================================================
        newMessage.attach(MIMEText(description, 'html'))
        # newMessage.attach(MIMEText(html, 'html'))
        #=======================================================================================================================
        # saving the changes to html_code.html
        try:
            with open('html_code_1.html', 'w') as f:
                f.write(html)
                f.close
        #=======================================================================================================================
            file = str(file_exe_name) + str(invoiceNo) + ".pdf"
            pdfkit.from_file('html_code_1.html', file, configuration=SoftwareScreen.config)
        #=======================================================================================================================
            # html = open('html_code.html', 'r').read()
            # html = html.replace(str(transaction_id), '$invoice_no')
            # html = html.replace(name, '$cus_name')
            # html = html.replace(email, '$cus_email')
            # html = html.replace(str(xyz_id), '$digi_no')
            # html = html.replace(email, '$email')
            # with open('html_code.html', 'w') as f:
            #     f.write(html)
            #     f.close
        #=======================================================================================================================
        except PermissionError as e:
            print(e)
            #remove_email(emailId, password)
        #=======================================================================================================================
        
        #=======================================================================================================================
        try:
            service = build('gmail', 'v1', credentials=creds)
            with open(file, 'rb') as f:
                payload = MIMEBase('application', 'octet-stream', Name=file)
                # payload = MIMEBase('application', 'pdf', Name=pdfname)
                payload.set_payload(f.read())
            #=======================================================================================================================
                # enconding the binary into base64
                encoders.encode_base64(payload)
            #=======================================================================================================================
                # add header with pdf name
                payload.add_header('Content-Decomposition',
                                'attachment', filename=file)
                newMessage.attach(payload)
            #=======================================================================================================================
            # mailserver = smtplib.SMTP_SSL('mail.privateemail.com', 465)
            # mailserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            # mailserver.login(emailId, password)
            # mailserver.sendmail(emailId, email, newMessage.as_string())
            encoded_message = base64.urlsafe_b64encode(newMessage.as_bytes()).decode()

            create_message = {
                'raw': encoded_message
            }
    #=======================================================================================================================
            # mailserver.quit()
            send_message = (service.users().messages().send
                            (userId="me", body=create_message).execute())
            print(F'Message Id: {send_message["id"]}')
    #=======================================================================================================================
            os.remove(file)
            os.remove("html_code_1.html")
    #=======================================================================================================================
            
    #=======================================================================================================================
        # except UnboundLocalError as fileerror:
        #     print(fileerror)
            # remove_email(emailId, password)
    #=======================================================================================================================
        # except smtplib.SMTPResponseException as e:
        #     print(e)
        #     error_code = e.smtp_code
        #     error_message = e.smtp_error
        #     print(f"send to {email} by {emailId} failed")
            
        #     print(f"error code: {error_code}")
        #     print(f"error message: {error_message}")
        except HttpError as error:
            print(F'An error occurred: {error}')
            send_message = None
            os.remove(file)
            os.remove("html_code_1.html")

                    
if __name__ == "__main__":
    if os.path.exists(f'{os.path.expanduser("~")}/cred.pkl'):
        SoftwareScreen()
    else:
        Main()
    # SoftwareScreen()
    # SCOPES = ['https://www.googleapis.com/auth/gmail.send']
    # creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # service = build('gmail', 'v1', credentials=creds)
    # print(type(service))
    # print(service)
    # print(dir(service.users().getProfile()))