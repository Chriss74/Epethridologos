from tkinter import *
from tkinter import ttk
import ttkbootstrap as tb
import tkinter as tk
from ttkbootstrap.scrolled import ScrolledFrame
from tkinter import filedialog
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.dialogs import Messagebox
import random
import re

root = tb.Window(themename="superhero")
root.resizable(False,False)
root.title("Επετηριδολόγος")
root.geometry('1900x1300')

#initial data
    #standard lists
data_array = []
    #standard data
file_path="" #user input file in computer/standard file
ranks=["<Χωρίς επιλογή>", "Πρόεδρος Εφετών", "Εφέτης", "Πρόεδρος Πρωτοδικών", "Πρωτοδίκης"]

    #changing input data
countList=[75, 268, 110] # plhthos user input array, max words 3Xyears only ints min 0 max 400 for all
cyear=2022 #user input input box only ints min 2022 max 2035
ksouList= [0,0,0,0] #user input array, max words 4Xyears, only ints min 0 max 100 for all random
agelimit=[67, 65, 65, 65]
    # changing lists
templist=[]
ProedroiEfetwn=0 #onomata
Efetes=0 #onomata
ProedroiProtodikwn=0 #onomata
Prwtodikes=0 #onomata
myrank=0
name=[0,0]
years=0 #optional if rank is chosen user input slider max 30


#DEFS
#GUI DEFS
def select_file():
    if countList[0]==None or countList[1]==None or countList[2]==None:
        Messagebox.ok("Δεν έχετε εισάγει το πλήθος των θέσεων για κάθε βαθμό")
    else:
        reloadFile()
        global file_path
        file_path= filedialog.askopenfilename(title="Select a File", filetype=(('text files','*.txt'),('all files','*.*')))
        openFile(file_path)
    

def openFile (filepath):
    global ProedroiEfetwn
    global Efetes
    global ProedroiProtodikwn
    global Prwtodikes
    global data_array
    
    if countList[0]==None or countList[1]==None or countList[2]==None:
        Messagebox.ok("Δεν έχετε εισάγει το πλήθος των θέσεων για κάθε βαθμό")
        return
    if filepath=="":
        Messagebox.ok("Δεν έχετε επιλέξει αρχείο")
        return
    reloadFile()
    data_array=[]
    global ProedroiEfetwn
    ProedroiEfetwn=0
    global Efetes
    Efetes=0
    global ProedroiProtodikwn
    ProedroiProtodikwn=0
    global Prwtodikes
    Prwtodikes=0
    fileName=re.search(r'[^/\\]+$', filepath).group()
    with open(filepath, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, start=1):
            parts = line.strip().split()
            if len(parts) != 3:
                clearAll()
                file_label.config(text=f"{fileName} ERROR in line {line_num}", bootstyle="danger")
                file_path=""
                Messagebox.ok(f"1. Το αρχείο που επιλέξατε δεν έχει τη σωστή μορφή (εντοπίστηκε λάθος στη γραμμή {line_num})")
                return
            else:
                try:
                    dob=int(parts[2])
                    if dob>1955 and dob<1995:
                        full_name = ' '.join(parts[:2])
                        data_array.append([full_name, dob])
                    else:
                        clearAll()
                        Messagebox.ok(f"2. Το αρχείο που επιλέξατε δεν έχει τη σωστή μορφή (εντοπίστηκε λάθος στη γραμμή {line_num})")
                        return
                except:
                    clearAll()
                    Messagebox.ok(f"3. Το αρχείο που επιλέξατε δεν έχει τη σωστή μορφή (εντοπίστηκε λάθος στη γραμμή {line_num})")
                    return     
    formatted_data = [f"{item[0]} {item[1]}" for item in data_array] 
    formatted_data.insert(0,None)
    chose_name.config(values=formatted_data)
    chose_name.current(0)
    pe=countList[0]
    e=countList[1]
    pp=countList[2]
    ProedroiEfetwn=data_array[:pe]
    Efetes=data_array[pe:pe+e]
    ProedroiProtodikwn=data_array[pe+e:pe+e+pp]
    Prwtodikes=data_array[pe+e+pp:]
    add_content_to_tab(0, ProedroiEfetwn)
    add_content_to_tab(1, Efetes)
    add_content_to_tab(2, ProedroiProtodikwn)
    add_content_to_tab(3, Prwtodikes)
    file_label.config(text=fileName, bootstyle="success")
    
  

def add_content_to_tab(tab_index, mydata):
    selected_tab = nb.tabs()[tab_index]
    frame = nb.nametowidget(selected_tab)

    # Create a Text widget within the frame
    text_widget = Text(frame, wrap="word",font=('Helvetica', 12), height=20, width=50)
    text_widget.grid(row=0, column=0, sticky="ew", pady=my_pady, padx=my_padx)

    # Create a vertical scrollbar for the Text widget
    scrollbar = Scrollbar(frame, command=text_widget.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")

    # Configure weights for the rows and columns within the frame
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # Connect the Text widget to the scrollbar
    text_widget.config(yscrollcommand=scrollbar.set)

    # Insert content into the Text widget
    for index, element in enumerate(mydata):
        formatted_text = f"{index + 1}. {element[0]} {element[1]}\n\n"
        text_widget.insert("end", formatted_text)

def add_content_to_ksou(tab_index, mydata):
    selected_tab = nb.tabs()[tab_index]
    frame = nb.nametowidget(selected_tab)

    # Create a Text widget within the frame
    text_widget = Text(frame, wrap="word",font=('Helvetica', 12), height=20, width=50)
    text_widget.grid(row=0, column=0, sticky="ew", pady=my_pady, padx=my_padx)

    # Create a vertical scrollbar for the Text widget
    scrollbar = Scrollbar(frame, command=text_widget.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")

    # Configure weights for the rows and columns within the frame
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # Connect the Text widget to the scrollbar
    text_widget.config(yscrollcommand=scrollbar.set)

    # Insert content into the Text widget
    for index, element in enumerate(mydata):
        formatted_text = f"{int(index) + 1}. {element[0]} {element[1]} {element[2]} {element[3]} {element[4]} {element[5]}\n\n"
        text_widget.insert("end", formatted_text)

def delete_content_from_tab(notebook):
    for tab_index in range(notebook.index("end")):
        selected_tab = notebook.tabs()[tab_index]
        frame = notebook.nametowidget(selected_tab)
        for widget in frame.winfo_children():
            widget.destroy()
def reload():
    if file_path:
        openFile(file_path)
    else:
        Messagebox.ok("Δεν έχετε ήδη επιλεγμένο κάποιο έγκυρο αρχείο")
    
def clearAll():
    reloadFile()
    global countList
    countList=[75, 268, 110]
    global file_path
    file_path="" 
    global ksouList
    ksouList=[0,0,0,0]
    global cyear
    cyear=2022 
    global agelimit
    agelimit=[67, 65, 65, 65]
    global templist
    templist=[]
    global ProedroiEfetwn
    ProedroiEfetwn=0
    global Efetes
    Efetes=0
    global ProedroiProtodikwn
    ProedroiProtodikwn=0
    global Prwtodikes
    Prwtodikes=0
    global myrank
    myrank=0
    global name
    name=[0,0]
    global years
    years=0 #optional if rank is chosen user input slider max 30
    chose_name.config(values=[""])
    chose_rank.set(ranks[0])
    clear_entry_value(chose_countrank_PE)
    clear_entry_value(chose_countrank_E)
    clear_entry_value(chose_countrank_PP)
    chose_countrank_PE.insert(0,"75")
    chose_countrank_E.insert(0,"268")
    chose_countrank_PP.insert(0,"110")
    chose_countrank_PE.config(state="normal")
    chose_countrank_E.config(state="normal")
    chose_countrank_PP.config(state="normal")
    file_label.config(text="", bootstyle="info")
    infoLabel.config(text="")
    clear_entry_value(chose_ksou_PE)
    clear_entry_value(chose_ksou_E)
    clear_entry_value(chose_ksou_PP)
    clear_entry_value(chose_ksou_P)
    clear_entry_value(chose_age_PE)
    clear_entry_value(chose_age_E)
    clear_entry_value(chose_age_PP)
    clear_entry_value(chose_age_P)
    clear_entry_value(chose_name_entry)  
    year_slider.set(0)
    file_year_slider.set(cyear)   
    chose_age_PE.insert(0, "67")
    chose_age_E.insert(0, "65")
    chose_age_PP.insert(0, "65")
    chose_age_P.insert(0, "65")
    chose_ksou_PE.insert(0, "0")
    chose_ksou_E.insert(0, "0")
    chose_ksou_PP.insert(0, "0")
    chose_ksou_P.insert(0, "0")


def clear_entry_value(entry):
    entry.delete(0, END)

#Otan anoigei kainourio arxeio, to file_path kanei update giati prwta trexei to select_file, opote kanei clearAll kai arxikopoiei to file_path kai meta trexei to openFile
#Otan kanei reload trexei mono to openFile, kratwntas idia osa fainontai sthn othonh. Auta pou evale o xrhsths stiw listes ana xrono klp, allazoun

def reloadFile():
    global countList
    countList=countList[:3]
    global agelimit
    agelimit=agelimit[:4]
        # changing lists
    global templist
    templist=[]
    global ksouList
    ksouList=ksouList[:4]
    global ksou_onomata
    ksou_onomata=[]
    Prwtodikes=0 #onomata
    delete_content_from_tab(nb)
    [button.destroy() for button in mainFrame4.winfo_children() if isinstance(button, ttk.Button)]
    infoLabel.config(text="")
    chose_age_PE.config(state="normal")
    chose_age_E.config(state="normal")
    chose_age_PP.config(state="normal")
    chose_age_P.config(state="normal")
    chose_ksou_PE.config(state="normal")
    chose_ksou_E.config(state="normal")
    chose_ksou_PP.config(state="normal")
    chose_ksou_P.config(state="normal")
    year_slider.config(state="normal")
    file_year_slider.config(stat="normal")
  
  
def chose_name_bind(e):
    global name
    data=chose_name.get()
    if data and data!=[0,0]:
        data=data.split(" ")
        name=[]
        name.append(f"{data[0]} {data[1]}")
        name.append(int(data[2]))
        
    
def chose_rank_bind(e):
    chosen=chose_rank.get()
    global myrank
    if chosen=="<Χωρίς Επιλογή>":
        myrank=0
    elif chosen=="Πρόεδρος Εφετών":
        myrank=1
    elif chosen=="Εφέτης":
        myrank=2
    elif chosen=="Πρόεδρος Πρωτοδικών":
        myrank=3
    

#find the name in the long list/very practical
def chose_name_entry_bind(e):
    text=chose_name_entry.get()
    values = chose_name['values']
    if len(text)>100:
        chose_name_entry.delete(0,END)
    else:
        mytext=text.strip().lower()
        for i, value in enumerate (values):
            myvalue=value.strip().lower()
            if mytext in myvalue:
                chose_name.current(i)
                break

#####COUNTRANK####
#rythmizei thn symperifora tou pediou gia thn eisagwgh tou arithmou twn thesewn ana vathmo
def focusout_countrank(e):
    caller=e.widget
    caller_name = caller.chosen_name
    try:
        entry=caller.get()
        #this is redudndant because it is already checked on keystroke
        if int(entry)>500 or int(entry)<-1:
            caller.delete(0, END)
            caller.config(bootstyle="danger")       
        else:
            caller.config(bootstyle="success")
            if caller_name=="chose_countrank_PE":
                countList[0]=int(entry)
            elif caller_name=="chose_countrank_E":
                countList[1]=int(entry)
            elif caller_name=="chose_countrank_PP":
                countList[2]=int(entry)
        
                
    except:
            caller.config(bootstyle="danger")
            caller.delete(0, END)
            if caller_name=="chose_countrank_PE":
                countList[0]=None
            elif caller_name=="chose_countrank_E":
                countList[1]=None
            elif caller_name=="chose_countrank_PP":
                countList[2]=None
        
def key_countrank(e):
    caller=e.widget
    entry=caller.get()
    if entry.isdigit()==False:
       caller.delete(0, END)
       caller.config(bootstyle="danger")
    elif len(entry)>3:
        caller.delete(0, END)
        caller.config(bootstyle="danger")
    elif int(entry)>500 or int(entry)<-1:
        caller.delete(0, END)
        caller.config(bootstyle="danger")
    else:
        caller.config(bootstyle="success")
    
    #Gia th lista ana etos
def confirmCountRank(parent):
    global countList
    countList=countList[:3]
    chose_countrank_PE.config(state="readonly")
    chose_countrank_E.config(state="readonly")
    chose_countrank_PP.config(state="readonly")
    # year_slider.config(state="disabled")
    file_year_slider.config(state="disabled")
    entry_widgets = list(parent.children.values())

    c=0
    for i in range (len(entry_widgets)):
        if isinstance(entry_widgets[i], tb.Entry):
            entry_value = entry_widgets[i].get()
            if entry_value=="":
                entry_value=countList[i-c]
                countList.append(entry_value)
            else:
                entry_value=int(entry_value)
                countList.append(entry_value)
        else:
            c+=1
    
    
    ###AGE###
def focusout_age(e):
    caller=e.widget
    caller_name = caller.chosen_name
    global agelimit
    try:
        entry=caller.get()
        if int(entry)>80 or int(entry)<60:
            caller.delete(0, END)
            caller.config(bootstyle="danger")
        else:
            caller.config(bootstyle="success")
            if caller_name=="chose_age_PE":
                agelimit[0]=int(entry)
            elif caller_name=="chose_age_E":
                agelimit[1]=int(entry)
            elif caller_name=="chose_age_PP":
                agelimit[2]=int(entry)
            elif caller_name=="chose_age_P":
                agelimit[3]=int(entry)
       
                
    except:
            caller.config(bootstyle="success")
            caller.delete(0, END)
            entry="65"
            if caller_name=="chose_age_PE":
                entry="67"
                agelimit[0]=67
            elif caller_name=="chose_age_E":
                agelimit[1]=65
            elif caller_name=="chose_age_PP":
                agelimit[2]=65
            elif caller_name=="chose_age_P":
                agelimit[3]=65
            caller.insert(0, entry)
        
def key_age(e):
    caller=e.widget
    entry=caller.get()
    if entry.isdigit()==False:
       caller.delete(0, END)
       caller.config(bootstyle="danger")
    elif len(entry)>2:
        caller.delete(0, END)
        caller.config(bootstyle="danger")
    elif int(entry)>80 or int(entry)<0:
        caller.delete(0, END)
        caller.config(bootstyle="danger")
    else:
        caller.config(bootstyle="success")

#ayto xreiazetai giati den ginetai na elegxthei sto keystroke an einai mikrotero apo 60
def focusout_list_age(e):
    caller=e.widget
    entry=caller.get()
    if int(entry)<60:
        caller.delete(0, END)
        caller.config(bootstyle="danger")
    
def confirmAge(parent):
    global agelimit
    agelimit=agelimit[:4]
    chose_age_PE.config(state="readonly")
    chose_age_E.config(state="readonly")
    chose_age_PP.config(state="readonly")
    chose_age_P.config(state="readonly")
    entry_widgets = list(parent.children.values())
    c=0
    for i in range (len(entry_widgets)):
        if isinstance(entry_widgets[i], tb.Entry):
            entry_value = entry_widgets[i].get()
            if entry_value=="":
                entry_value=agelimit[i-c]
                agelimit.append(entry_value)
            else:
                entry_value=int(entry_value)
                agelimit.append(entry_value)
        else:
            c+=1
    
    #new window for inputs for each year
    
def openNewWindowCountrank():
    if countList[0] and countList[1] and countList[2]:
        newWindow = Toplevel(root)
        newWindow.title("New Window")
        newWindow.geometry("500x500")
        sf = ScrolledFrame(newWindow,autohide=False)
        sf.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        tb.Label(sf,text="Εισάγεται τις θέσεις ανά βαθμό κατ' έτος (Πρόεδροι Εφετών, Εφέτες, Πρόεδροι Πρωτοδικών). Εάν παραλείψετε τη συμπλήρωση ορισμένων ετών, αυτά θα συμπληρωθούν από τo ακριβώς προηγούμενο συμπληρωμένο έτος", wraplength=400).pack()
        count_confirm_button = tb.Button(sf, text="Enter", command=lambda: confirmCountRank(sf)).pack(pady=20)
        
        for i in range(1,years+1):
            etos=str(cyear+i)
            lb=tb.Label(sf,text=etos)
            lb.pack()
            
            en1=tb.Entry(sf)
            en1.pack()
            en1.chosen_name = "chose_countrank_PE"
            en1.bind("<KeyRelease>",key_countrank)
            en1.bind('<Control-v>', lambda _:'break')
            
            en2=tb.Entry(sf)
            en2.pack()
            en2.chosen_name = "chose_countrank_PE"
            en2.bind("<KeyRelease>",key_countrank)
            en2.bind('<Control-v>', lambda _:'break')
            
            en3=tb.Entry(sf)
            en3.pack()
            en3.chosen_name = "chose_countrank_PE"
            en3.bind("<KeyRelease>",key_countrank)
            en3.bind('<Control-v>', lambda _:'break')
            
            if i*3<len(countList)-2:
                en1.insert(0, str(countList[i*3]))
                en2.insert(0, str(countList[i*3+1]))
                en3.insert(0, str(countList[i*3+2]))
                

        newWindow.grab_set()
    else:
        Messagebox.ok("Πρέπει να συμπληρώσετε πρώτα όλα τα αρχικά πεδία για το πλήθος σε κάθε βαθμό")


def openNewWindowKsou():
    if ksouList[0]>-1 and ksouList[1]>-1 and ksouList[2]>-1 and ksouList[3]>-1:
        newWindow = Toplevel(root)
        newWindow.title("New Window")
        newWindow.geometry("500x500")
        sf = ScrolledFrame(newWindow,autohide=False)
        sf.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        tb.Label(sf,text="Εισάγεται τις θέσεις ανά βαθμό κατ' έτος (Πρόεδροι Εφετών, Εφέτες, Πρόεδροι Πρωτοδικών). Εάν παραλείψετε τη συμπλήρωση ορισμένων ετών, αυτά θα συμπληρωθούν από τo ακριβώς προηγούμενο συμπληρωμένο έτος", wraplength=400).pack()
        count_confirm_button = tb.Button(sf, text="Enter", command=lambda: confirmKsou(sf)).pack(pady=20)
        
        for i in range(1, years+1):
            etos=str(cyear+i)
            lb=tb.Label(sf,text=etos)
            lb.pack()
            
            en1=tb.Entry(sf)
            en1.pack()
            en1.chosen_name = "chose_ksou_PE"
            en1.bind("<KeyRelease>",key_ksou)
            en1.bind('<Control-v>', lambda _:'break')
            
            en2=tb.Entry(sf)
            en2.pack()
            en2.chosen_name = "chose_countrank_PE"
            en2.bind("<KeyRelease>",key_ksou)
            en2.bind('<Control-v>', lambda _:'break')
            
            en3=tb.Entry(sf)
            en3.pack()
            en3.chosen_name = "chose_ksou_PE"
            en3.bind("<KeyRelease>",key_ksou)
            en3.bind('<Control-v>', lambda _:'break')
            
            en4=tb.Entry(sf)
            en4.pack()
            en4.chosen_name = "chose_ksou_PE"
            en4.bind("<KeyRelease>",key_ksou)
            en4.bind('<Control-v>', lambda _:'break')
            
            if i*4<len(ksouList)-3:
                en1.insert(0, str(ksouList[i*4]))
                en2.insert(0, str(ksouList[i*4+1]))
                en3.insert(0, str(ksouList[i*4+2]))
                en4.insert(0, str(ksouList[i*4+3]))
                
        newWindow.grab_set()
    else:
        Messagebox.ok("Πρέπει να συμπληρώσετε πρώτα όλα τα αρχικά πεδία για το πλήθος των αποχωρήσεων σε κάθε βαθμό")
    
    
    
def openNewWindowAge():
    if agelimit[0] and agelimit[1] and agelimit[2] and agelimit[3]:
        newWindow = Toplevel(root)
        newWindow.title("New Window")
        newWindow.geometry("500x500")
        sfAge = ScrolledFrame(newWindow,autohide=False)
        sfAge.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        tb.Label(sfAge,text="Εισάγεται τα όρια ηλικίας συνταξιοδότησης για κάθε βαθμό (Πρόεδροι Εφετών, Εφέτες, Πρόεδροι Πρωτοδικών). Εάν παραλείψετε τη συμπλήρωση ορισμένων ετών, αυτά θα συμπληρωθούν από τo ακριβώς προηγούμενο συμπληρωμένο έτος", wraplength=400).pack()
        count_confirm_button = tb.Button(sfAge, text="Enter", command=lambda: confirmAge(sfAge)).pack(pady=20)
        
        for i in range(1, years+1):
            etos=str(cyear+i)
            lb=tb.Label(sfAge,text=etos)
            lb.pack()
            en1=tb.Entry(sfAge)
            en1.pack()
            en1.chosen_name = "chose_age_PE"
            en1.bind("<KeyRelease>",key_age)
            en1.bind("<FocusOut>", focusout_list_age)
            en1.bind('<Control-v>', lambda _:'break')
            
            en2=tb.Entry(sfAge)
            en2.pack()
            en2.chosen_name = "chose_age_E"
            en2.bind("<KeyRelease>",key_age)
            en2.bind("<FocusOut>", focusout_list_age)
            en2.bind('<Control-v>', lambda _:'break')
            
            en3=tb.Entry(sfAge)
            en3.pack()
            en3.chosen_name = "chose_age_PP"
            en3.bind("<KeyRelease>",key_age)
            en3.bind("<FocusOut>", focusout_list_age)
            en3.bind('<Control-v>', lambda _:'break')
            
            en4=tb.Entry(sfAge)
            en4.pack()
            en4.chosen_name = "chose_age_P"
            en4.bind("<KeyRelease>",key_age)
            en1.bind("<FocusOut>", focusout_list_age)
            en4.bind('<Control-v>', lambda _:'break')
            
            if i*4<len(agelimit)-3:
                en1.insert(0, str(agelimit[i*4]))
                en2.insert(0, str(agelimit[i*4+1]))
                en3.insert(0, str(agelimit[i*4+2]))
                en4.insert(0, str(agelimit[i*4+3]))

        newWindow.grab_set()
    else:
        Messagebox.ok("Πρέπει να συμπληρώσετε πρώτα όλα τα αρχικά πεδία για το όριο ηλικίας σε κάθε βαθμό")

def designGraph(yearCountList, PEDataRet, PEDataRand, EDataRet, EDataRand, PPDataRet, PPDataRand): 
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    #yearCountList and PEData and EData and PPData:
        newWindow = tk.Toplevel(root)
        newWindow.title("Graph Window")
        newWindow.geometry("1000x1000")
        newWindow.grab_set()


        # Create a VerticalScrolledFrame to hold the graphs
        sfGraph = ScrolledFrame(newWindow)
        sfGraph.pack(fill=tk.BOTH, expand=tk.YES, padx=10, pady=10)

       # Calculate the total number of years
        num_years = len(yearCountList)

        # Create a figure and axes for PEData
        fig1, ax1 = plt.subplots(figsize=(10, 6))

        # Create a list of indices for the x-axis
        x_indices = list(range(num_years))

        # Create a stacked bar plot for PEData
        ax1.bar(x_indices, PEDataRet, label='Ηλικίας', color='red', alpha=0.5)
        ax1.bar(x_indices, PEDataRand, label='Τυχαία', color='blue', alpha=0.5, bottom=PEDataRet)

        # Set x-axis labels to be the years
        ax1.set_xticks(x_indices)
        # ax1.set_xticklabels(yearCountList)
        custom_labels = [str(yearCountList[i]) if i % 2 == 0 else '' for i in x_indices]
        ax1.set_xticklabels(custom_labels, fontsize=10)  # Adjust the font size (e.g., 10)
        ax1.set_xlabel("Έτος")
        ax1.set_ylabel("Αποχωρήσεις")
        ax1.set_title('Πρόεδροι Εφετών')
        ax1.legend()

        # Embed the PEData plot in the frame
        canvas1 = FigureCanvasTkAgg(fig1, master=sfGraph)
        canvas1.get_tk_widget().pack(padx=10, pady=10)

        # Create a figure and axes for EData
        fig2, ax2 = plt.subplots(figsize=(10, 6))

        # Create a stacked bar plot for EData
        ax2.bar(x_indices, EDataRet, label='Ηλικίας', color='red', alpha=0.5)
        ax2.bar(x_indices, EDataRand, label='Τυχαία', color='blue', alpha=0.5, bottom=EDataRet)

        # Set x-axis labels to be the years
        ax2.set_xticks(x_indices)
        custom_labels = [str(yearCountList[i]) if i % 5 == 0 else '' for i in x_indices]
        ax2.set_xticklabels(custom_labels, fontsize=10)  # Adjust the font size (e.g., 10)
        ax2.set_xlabel("Έτος")
        ax2.set_ylabel("Αποχωρήσεις")
        ax2.set_title('Εφέτες')
        ax2.legend()

        # Embed the EData plot in the frame
        canvas2 = FigureCanvasTkAgg(fig2, master=sfGraph)
        canvas2.get_tk_widget().pack(padx=10, pady=10)

        # Create a figure and axes for PPData
        fig3, ax3 = plt.subplots(figsize=(10, 6))

        # Create a stacked bar plot for PPData
        ax3.bar(x_indices, PPDataRet, label='Ηλικίας', color='red', alpha=0.5)
        ax3.bar(x_indices, PPDataRand, label='Τυχαία', color='blue', alpha=0.5, bottom=PPDataRet)

        # Set x-axis labels to be the years
        ax3.set_xticks(x_indices)
        custom_labels = [str(yearCountList[i]) if i % 2 == 0 else '' for i in x_indices]
        ax1.set_xticklabels(custom_labels, fontsize=10)  # Adjust the font size (e.g., 10)
        ax3.set_xlabel("Έτος")
        ax3.set_ylabel("Αποχωρήσεις")
        ax3.set_title('Πρόεδροι Πρωτοδικών')
        ax3.legend()

        # Embed the PPData plot in the frame
        canvas3 = FigureCanvasTkAgg(fig3, master=sfGraph)
        canvas3.get_tk_widget().pack(padx=10, pady=10)
        plt.close('all')
#slider
def slider(e):
    global years
    year_slider_label.config(text=f'{int(year_slider.get())}')
    years=int(year_slider.get())

def slider2(e):
    global cyear
    file_year_slider_label.config(text=f'{int(file_year_slider.get())}')
    cyear=int(file_year_slider.get())


#ksouList
def focusout_ksou(e):
    caller=e.widget
    caller_name = caller.chosen_name
    try:
        entry=int(caller.get())
        if entry>20 or entry<-1:
            caller.delete(0, END)
            caller.config(bootstyle="warning")       
        else:
            caller.config(bootstyle="success")
            if caller_name=="chose_ksou_PE":
                ksouList[0]=entry
            elif caller_name=="chose_ksou_E":
                ksouList[1]=entry
            elif caller_name=="chose_ksou_PP":
                ksouList[2]=entry
            elif caller_name=="chose_ksou_P":
                ksouList[3]=entry
        
                
    except:
            caller.config(bootstyle="warning")
            caller.delete(0, END)
            entry=0
            caller.insert(0, entry)
            if caller_name=="chose_ksou_PE":
                ksouList[0]=entry
            elif caller_name=="chose_ksou_E":
                ksouList[1]=entry
            elif caller_name=="chose_ksou_PP":
                ksouList[2]=entry
            elif caller_name=="chose_ksou_P":
                ksouList[3]=entry
                
        
def key_ksou(e):
    caller=e.widget
    entry=caller.get()
    if entry.isdigit()==False:
       caller.delete(0, END)
       caller.config(bootstyle="warning")
    elif len(entry)>2:
        caller.delete(0, END)
        caller.config(bootstyle="warning")
    elif int(entry)>20 or int(entry)<-1:
        caller.config(bootstyle="warning")
        caller.delete(0, END)
    else:
        caller.config(bootstyle="success")
        
def confirmKsou(parent):
    entry_widgets = list(parent.children.values())
    global ksouList
    ksouList=ksouList[:4]
    chose_ksou_PE.config(state="readonly")
    chose_ksou_E.config(state="readonly")
    chose_ksou_PP.config(state="readonly")
    c=0
    for i in range (len(entry_widgets)):
        if isinstance(entry_widgets[i], tb.Entry):
            entry_value = entry_widgets[i].get()
            if entry_value=="":
                entry_value=ksouList[i-c]
                ksouList.append(int(entry_value))
            else:
                ksouList.append(int(entry_value))
        else:
            c+=1
    
    
    #ksouList new window for inputs for each year

    
    for i in range(years):
        etos=str(cyear+1+i)
        lb=tb.Label(sfKsou,text=etos)
        lb.pack()
        en1=tb.Entry(sfKsou)
        en1.pack()
        en1.bind('<Control-v>', lambda _:'break')
        en2=tb.Entry(sfKsou)
        en2.pack()
        en2.bind('<Control-v>', lambda _:'break')
        en3=tb.Entry(sfKsou)
        en3.pack()
        en3.bind('<Control-v>', lambda _:'break')
        en4=tb.Entry(sfKsou)
        en4.pack()
        en4.bind('<Control-v>', lambda _:'break')
    

#MAIN DEFS
def loop(firstlist, year, ksoucount, age, name, rank):
    temp=[]
    temp2=[]
    ksou_onomata=[] #onomata
    retirementCount=0
    randomCount=0
    
 
    for index, x in enumerate(firstlist):
        if year-x[1]<age:
            temp.append(x)           
        else:
            k=[]
            k+=x
            k.append(year-x[1])
            k.append(year)
            k.append(rank)
            k.append("Οριο Ηλικίας")
            ksou_onomata.append(k)
            retirementCount+=1
    #Meta tha elegxw thn ksoulist gia to onoma
    index=None
    add=0
    unlucky=None
    if name:
        index = next((i for i, sublist in enumerate(temp) if sublist == name), None)
        add=1
    if ksoucount>len(temp)-1-add:
        ksoucount=len(temp)-1-add
    if ksoucount>0:
        lottery=random.sample(range(0, len(temp)), ksoucount)
        if index==None:
            lottery=random.sample(range(0, len(temp)), ksoucount)
        else:
            while index in lottery:
                lottery=random.sample(range(0, len(temp)), ksoucount)
        
        for y in lottery:
            unlucky=[]
            unlucky+=temp[y]
            unlucky.append(year-x[1])
            unlucky.append(year)
            unlucky.append(rank)
            unlucky.append("random")
            ksou_onomata.append(unlucky)
            randomCount+=1
    if unlucky and ksoucount>0:
        
        temp2 = [temp[i] for i in range(len(temp)) if i not in lottery]
        
        
    else:
        temp2=temp
    return temp2, [retirementCount, randomCount], ksou_onomata

def sliceList(firstlist, pe, e, pp):
    PEList=[]
    EList=[]
    PPList=[]
    PList=[]
    #adeia arxikh lista
    if len(firstlist) == 0:
        return PEList, EList, PPList, PList
    #PE
    if pe>len(firstlist):
        pe=len(firstlist)
        PEList=firstlist[:pe]
    else:
         PEList=firstlist[:pe]
    #E
    if len(firstlist)-len(PEList)>0:
        e=min(e,len(firstlist)-len(PEList))
        EList=firstlist[pe:pe+e]
    else:
        return PEList, EList, PPList, PList
    #PP
    if len(firstlist)-len(PEList)-len(EList)>0:
        p=min(pp,len(firstlist)-len(PEList)-len(EList))
        PPList=firstlist[pe+e:pe+e+pp]
    else:
        return PEList, EList, PPList, PList
    
    if len(firstlist)-len(PEList)-len(EList)>0:
        PList=firstlist[pe+e+pp:]
    else:
        return PEList, EList, PPList, PList
   
    return PEList, EList, PPList, PList
    
def combineList(PE, E, PP, P):
        finlist=[]
        if PE:
            finlist+=PE
        if E:
            finlist+=E
        if PP:
            finlist+=PP
        if P:
            finlist+=P
        if len(finlist):
            return finlist
        else:
            finlist=None
            return finlist


def fill_plhrofories(textIndex,yearEnd, indexInRank, rankIndex, yearCountList, PEDataRet, PEDataRand, EDataRet, EDataRand, PPDataRet, PPDataRand):
    
    global ranks
    try:
        myrank=ranks[rankIndex]
    except:
        myrank=0
    [button.destroy() for button in mainFrame4.winfo_children() if isinstance(button, ttk.Button)]
    infoLabel.config(text="")
    FMIRankReached=f'Δικαστής: {name[0]}\nΈτος Γέννησης: {name[1]}\n Προαγωγή στο βαθμό "{myrank}" σε {yearEnd-cyear} έτη από το έτος της επετηρίδας δηλαδή το έτος {yearEnd}.\nΣειρά στον βαθμό: {indexInRank+1} \nHλικία: {yearEnd-name[1]}'
    FMSyntaksi=f"Δικαστής: {name[0]}\nΈτος Γέννησης: {name[1]}\n Συνταξιοδότηση σε {yearEnd-cyear} έτη από το έτος της επετηρίδας, δηλαδή το έτος {yearEnd} Βαθμός: {ranks[rankIndex]} \nΗλικία {yearEnd-name[1]}"
    FMEinaiHdh=f'Δικαστής: {name[0]}\nΈτος Γέννησης: {name[1]}\n Στην επετηρίδα του έτους {yearEnd} είχε ήδη τον βαθμό "{ranks[rankIndex]}" και σειρά στο βαθμό {indexInRank+1} σύμφωνα με τα στοιχεία που δώσατε'
    FMNoName=f'Ετος: {yearEnd} \n'
    FMName=f'Δικαστής: {name[0]}\nΈτος Γέννησης: {name[1]}\n Σε {yearEnd-cyear} έτη από το έτος της επετηρίδας {cyear} δηλαδή το έτος {yearEnd} και σε ηλικία {yearEnd-name[1]} έχει τον βαθμό "{ranks[rankIndex]}" και σειρά στον βαθμό αυτό {indexInRank+1}'
    Error="Error"
    arr=[FMIRankReached, FMSyntaksi, FMEinaiHdh, FMNoName, FMName, Error]
    infoLabel.config(text=arr[textIndex])   
    global graphButton
    graphButton = ttk.Button(mainFrame4, text="Graph")
    graphButton.pack(side="bottom", pady=15)
    graphButton.config(command=lambda: designGraph(yearCountList, PEDataRet, PEDataRand, EDataRet, EDataRand, PPDataRet, PPDataRand))

    
def enter():
    global countList
    global agelimit
    global ksouList
    global templist
    global years
    global myrank
    global name      
  
    
    #Arxikopoihseis
    templist=[]
    templist+=data_array
    pe=countList[0]
    e=countList[1]
    pp=countList[2]
    PEList=data_array[:pe]
    EList=data_array[pe:pe+e]
    PPList=data_array[pe+e:pe+e+pp]
    PList=data_array[pe+e+pp:]
    ksou_onomata_all=[]
    indexInRank=-1
    indexRank=-1
    yearsKsouCountList=[]
    PERetCountList=[]
    PERandCountList=[]
    ERetCountList=[]
    ERandCountList=[]
    PPRetCountList=[]
    PPRandCountList=[]
    PRetCountList=[]
    PRandCountList=[]
    
    #recreate lists
    element1=countList[-3]
    element2=countList[-2]
    element3=countList[-1]
    while len(countList)<years*4:
        countList.append(element1)
        countList.append(element2)
        countList.append(element3)
    element1=agelimit[-4]
    element2=agelimit[-3]
    element3=agelimit[-2]
    element4=agelimit[-1]
    while len(agelimit)<years*5:
        agelimit.append(element1)
        agelimit.append(element2)
        agelimit.append(element3)
        agelimit.append(element4)
    element1=ksouList[-4]
    element2=ksouList[-3]
    element3=ksouList[-2]
    element4=ksouList[-1]
    while len(ksouList)<years*5:
        ksouList.append(element1)
        ksouList.append(element2)
        ksouList.append(element3)
        ksouList.append(element4)
         
    #delete tabs and infoLabel
    delete_content_from_tab(nb)
    [button.destroy() for button in mainFrame4.winfo_children() if isinstance(button, ttk.Button)]
    infoLabel.config(text="") 
    
    #Elegxoi
    if name==[0,0]:
        myrank=0
        chose_rank.set(ranks[0])
    
    #no file_path    
    if file_path=="":
        Messagebox.ok("Δεν έχει επιλέξει αρχείο")
        return
    
    #0 years chosen by user
    if years==0:
        openFile(file_path)
        if name in ProedroiEfetwn:
            indexInRank = next((i for i, sublist in enumerate(ProedroiEfetwn) if sublist == name), None)
            fill_plhrofories(4, cyear, indexInRank, 2, [0],[0],[0],[0],[0],[0],[0])
            return
        elif name in Efetes:
            indexInRank = next((i for i, sublist in enumerate(Efetes) if sublist == name), None)
            fill_plhrofories(4, cyear, indexInRank, 2, [0],[0],[0],[0],[0],[0],[0])
            return
        elif name in ProedroiProtodikwn:
            indexInRank = next((i for i, sublist in enumerate(ProedroiProtodikwn) if sublist == name), None)
           
            fill_plhrofories(4, cyear, indexInRank, 3, [0],[0],[0],[0],[0],[0],[0])
            return
        elif name in Prwtodikes:
            indexInRank = next((i for i, sublist in enumerate(Prwtodikes) if sublist == name), None)
            fill_plhrofories(4, cyear, indexInRank, 4,[0],[0],[0],[0],[0],[0],[0])
            return
        else:
            return
    
    
    #tsek ean to onoma katexei hdh ton vathmo
    
    if myrank==1 and name in ProedroiEfetwn:
        openFile(file_path)
        indexInRank = next((i for i, sublist in enumerate(ProedroiEfetwn) if sublist == name), None)
        fill_plhrofories(2, cyear, indexInRank, 1, [0],[0],[0],[0],[0],[0],[0])
        return
    elif myrank==2 and name in Efetes:
        openFile(file_path)
        indexInRank = next((i for i, sublist in enumerate(Efetes) if sublist == name), None)
        fill_plhrofories(2, cyear, indexInRank, 2, [0],[0],[0],[0],[0],[0],[0])
        return
    elif myrank==3 and name in ProedroiProtodikwn:
        openFile(file_path)
        indexInRank = next((i for i, sublist in enumerate(ProedroiProtodikwn) if sublist == name), None)
        fill_plhrofories(2, cyear, indexInRank, 3, [0],[0],[0],[0],[0],[0],[0])
        return
    
    
    
    #sliced list
    countPE=countList[0]
    countE=countList[1]
    countPP=countList[2]
    allList=sliceList(templist,countPE, countE, countPP)
    PEList=allList[0]
    EList=allList[1]
    PPList=allList[2]
    PList=allList[3]
    
    #loop
    for i in range(1,years+1):
            yearsKsouCountList.append(cyear+i)
        #count
            if len(countList)>3:
                count=(3*i)
            else:
                count=(i*3)%3
            countPE=countList[count]
            countE=countList[count+1]
            countPP=countList[count+2]
            
        #ksou
            if len(ksouList)>4:
                rand=4*i
            else:
                rand=(4*i)%4
            ksouPE=ksouList[rand]
            ksouE=ksouList[rand+1]
            ksouPP=ksouList[rand+2]
            ksouP=ksouList[rand+3]
            
        #age
            if len(agelimit)>4:
                age=4*i
            else:
                age=(i*4)%4
            agePE=agelimit[age]
            ageE=agelimit[age+1]
            agePP=agelimit[age+2]
            ageP=agelimit[age+3]
            
        # main loop
            PEListAll=loop(PEList, cyear+i, ksouPE, agePE, name, "Πρόεδρος Εφετών")
            EListAll=loop(EList, cyear+i, ksouE, ageE, name, "Εφέτης")
            PPListAll=loop(PPList, cyear+i, ksouPP, agePP, name, "Πρόεδρος Πρωτοδικών")
            PListAll=loop(PList, cyear+i, ksouP, ageP, name, "Πρωτοδίκης")
            
            PEList=PEListAll[0]
            EList=EListAll[0]
            PPList=PPListAll[0]
            PList=PListAll[0]
            
            #recreate templist
            templist=[]
            if PEList:
                templist+=PEList
            if EList:
                templist+=EList
            if PPList:
                templist+=PPList
            if PList:   
                templist+=PList     
                pe=countList[-3]
            e=countList[-2]
            pp=countList[-1]
            allList=sliceList(templist,pe, e, pp)
            PEList=allList[0]
            EList=allList[1]
            PPList=allList[2]
            PList=allList[3]   
            
            for x in PEListAll[2]:
                ksou_onomata_all.append(x)
            for x in EListAll[2]:
                ksou_onomata_all.append(x)
            for x in PPListAll[2]:
                ksou_onomata_all.append(x)
            for x in PListAll[2]:
                ksou_onomata_all.append(x)
 
            #elegxos syntaksh
            if any(sublist[:2] == name for sublist in PEListAll[2]):
                add_content_to_tab(0, PEList)
                add_content_to_tab(1, EList)
                add_content_to_tab(2, PPList)
                add_content_to_tab(3, PList)
                add_content_to_ksou(4, ksou_onomata_all)
                indexInRank=next((i for i, sublist in enumerate(PEListAll[2]) if sublist[:2] == name), None)
                fill_plhrofories(1, cyear+i, indexInRank, 1, yearsKsouCountList, PERetCountList, PERandCountList, ERetCountList, ERandCountList,PPRetCountList, PPRandCountList)
                templist=[]
                ksou_onomata_all=[]
                yearsKsouCountList=[]
                PERetCountList=[]
                PERandCountList=[]
                ERetCountList=[]
                ERandCountList=[]
                PPRetCountList=[]
                PPRandCountList=[]
                PRetCountList=[]
                PRandCountList=[]
                indexInRank=-1
                indexRank=-1
                return
            elif any(sublist[:2] == name for sublist in EListAll[2]):
                add_content_to_tab(0, PEList)
                add_content_to_tab(1, EList)
                add_content_to_tab(2, PPList)
                add_content_to_tab(3, PList)
                add_content_to_ksou(4, ksou_onomata_all)
                indexInRank=next((i for i, sublist in enumerate(EListAll[2]) if sublist[:2] == name), None)
                fill_plhrofories(1, cyear+i, indexInRank, 2, yearsKsouCountList, PERetCountList, PERandCountList, ERetCountList, ERandCountList,PPRetCountList, PPRandCountList)
                templist=[]
                ksou_onomata_all=[]
                yearsKsouCountList=[]
                PERetCountList=[]
                PERandCountList=[]
                ERetCountList=[]
                ERandCountList=[]
                PPRetCountList=[]
                PPRandCountList=[]
                PRetCountList=[]
                PRandCountList=[]
                indexInRank=-1
                indexRank=None
                return
            elif any(sublist[:2] == name for sublist in PPListAll[2]):
                add_content_to_tab(0, PEList)
                add_content_to_tab(1, EList)
                add_content_to_tab(2, PPList)
                add_content_to_tab(3, PList)
                add_content_to_ksou(4, ksou_onomata_all)
                indexInRank=next((i for i, sublist in enumerate(PPListAll[2]) if sublist [:2]== name), None)
                fill_plhrofories(1, cyear+i, indexInRank, 3, yearsKsouCountList, PERetCountList, PERandCountList, ERetCountList, ERandCountList,PPRetCountList, PPRandCountList)
                templist=[]
                ksou_onomata_all=[]
                yearsKsouCountList=[]
                PERetCountList=[]
                PERandCountList=[]
                ERetCountList=[]
                ERandCountList=[]
                PPRetCountList=[]
                PPRandCountList=[]
                PRetCountList=[]
                PRandCountList=[]
                indexInRank=-1
                indexRank=None
                return
            elif any(sublist[:2] == name for sublist in PListAll[2]):
                add_content_to_tab(0, PEList)
                add_content_to_tab(1, EList)
                add_content_to_tab(2, PPList)
                add_content_to_tab(3, PList)
                add_content_to_ksou(4, ksou_onomata_all)
                indexInRank=next((i for i, sublist in enumerate(PListAll[2]) if sublist == name), None)
                fill_plhrofories(1, cyear+i, indexInRank, 4, yearsKsouCountList, PERetCountList, PERandCountList, ERetCountList, ERandCountList,PPRetCountList, PPRandCountList)
                templist=[]
                ksou_onomata_all=[]
                yearsKsouCountList=[]
                PERetCountList=[]
                PERandCountList=[]
                ERetCountList=[]
                ERandCountList=[]
                PPRetCountList=[]
                PPRandCountList=[]
                PRetCountList=[]
                PRandCountList=[]
                indexInRank=-1
                indexRank=-1
                return
            
                
        
        #Graph Data    
            PERetCountList.append(PEListAll[1][0])
            PERandCountList.append(PEListAll[1][1])
            ERetCountList.append(EListAll[1][0])
            ERandCountList.append(EListAll[1][1])
            PPRetCountList.append(PPListAll[1][0])
            PPRandCountList.append(PEListAll[1][1])
            PRetCountList.append(PListAll[1][0])
            PRandCountList.append(PListAll[1][1])
               
          
            
        #Elegxos an exei hdh ftasei ston vathmo
            if myrank==1 and name in PEList:
                add_content_to_tab(0, PEList)
                add_content_to_tab(1, EList)
                add_content_to_tab(2, PPList)
                add_content_to_tab(3, PList)
                add_content_to_ksou(4, ksou_onomata_all)
                indexInRank=next((i for i, sublist in enumerate(PEList) if sublist == name), None)
                fill_plhrofories(0, cyear+i, indexInRank, 1, yearsKsouCountList, PERetCountList, PERandCountList, ERetCountList, ERandCountList,PPRetCountList, PPRandCountList)
                templist=[]
                ksou_onomata_all=[]
                yearsKsouCountList=[]
                PERetCountList=[]
                PERandCountList=[]
                ERetCountList=[]
                ERandCountList=[]
                PPRetCountList=[]
                PPRandCountList=[]
                PRetCountList=[]
                PRandCountList=[]
                indexInRank=-1
                indexRank=-1
                return
            if myrank==2 and name in EList:
                
                add_content_to_tab(0, PEList)
                add_content_to_tab(1, EList)
                add_content_to_tab(2, PPList)
                add_content_to_tab(3, PList)
                add_content_to_ksou(4, ksou_onomata_all)
                indexInRank = next((i for i, sublist in enumerate(EList) if sublist == name), None)
                fill_plhrofories(0, cyear+i, indexInRank, 2, yearsKsouCountList, PERetCountList, PERandCountList, ERetCountList, ERandCountList,PPRetCountList, PPRandCountList)
                templist=[]
                ksou_onomata_all=[]
                yearsKsouCountList=[]
                PERetCountList=[]
                PERandCountList=[]
                ERetCountList=[]
                ERandCountList=[]
                PPRetCountList=[]
                PPRandCountList=[]
                PRetCountList=[]
                PRandCountList=[]
                indexInRank=-1
                indexRank=-1
                return
            if myrank==3 and name in PPList:
               
                add_content_to_tab(0, PEList)
                add_content_to_tab(1, EList)
                add_content_to_tab(2, PPList)
                add_content_to_tab(3, PList)
                add_content_to_ksou(4, ksou_onomata_all)
                indexInRank = next((i for i, sublist in enumerate(PPList) if sublist == name), None)
                fill_plhrofories(0, cyear+i, indexInRank, 3, yearsKsouCountList, PERetCountList, PERandCountList, ERetCountList, ERandCountList,PPRetCountList, PPRandCountList)
                templist=[]
                ksou_onomata_all=[]
                yearsKsouCountList=[]
                PERetCountList=[]
                PERandCountList=[]
                ERetCountList=[]
                ERandCountList=[]
                PPRetCountList=[]
                PPRandCountList=[]
                PRetCountList=[]
                PRandCountList=[]
                indexInRank=-1
                indexRank=-1
                return
                      

    
#addcontent to tab   
    add_content_to_tab(0, PEList)
    add_content_to_tab(1, EList)
    add_content_to_tab(2, PPList)
    add_content_to_tab(3, PList)
    add_content_to_ksou(4, ksou_onomata_all)
    

#Telikos elegxos 
    if name in PEList:
        print("successPE")
        indexInRank = next((i for i, sublist in enumerate(PEList) if sublist == name), None)
        indexRank=1
    elif name in EList:
        print("success")
        indexInRank = next((i for i, sublist in enumerate(EList) if sublist == name), None)
        indexRank=2
    elif name in PPList:
        indexInRank = next((i for i, sublist in enumerate(PPList) if sublist == name), None)
        indexRank=3
    elif name in PList:
        indexInRank = next((i for i, sublist in enumerate(PList) if sublist == name), None)
        indexRank=4
    if indexRank>-1 and indexInRank>-1:
        fill_plhrofories(4,cyear+i,indexInRank,indexRank, yearsKsouCountList, PERetCountList, PERandCountList, ERetCountList, ERandCountList,PPRetCountList, PPRandCountList)
    else:
        print(indexInRank, indexRank)
        fill_plhrofories(3,cyear+i,0,0,yearsKsouCountList, PERetCountList,PERandCountList, ERetCountList, ERandCountList,PPRetCountList, PPRandCountList)
    
#arxikopoihsh metavlhtwn, kalou kakou
    templist=[]
    ksou_onomata_all=[]
    yearsKsouCountList=[]
    PERetCountList=[]
    PERandCountList=[]
    ERetCountList=[]
    ERandCountList=[]
    PPRetCountList=[]
    PPRandCountList=[]
    PRetCountList=[]
    PRandCountList=[]
    indexInRank=-1
    indexRank=-1
    

       
#styles
style = ttk.Style(root)
style.configure('TButton', font=('Helvetica', 10))
style.configure('TNotebookTab', font=('Helvetica', 10))

my_padx=30
my_pady=15

#GUI
    #Frames
mainFrame1=tb.Frame(root, bootstyle="secondary")
mainFrame1.grid(row=1, column=0, rowspan=5, sticky="ns", pady=my_pady, padx=my_padx)
mainFrame2=tb.Frame(root, bootstyle="secondary")
mainFrame2.grid(row=6, column=0, rowspan=3, sticky="ns", pady=my_pady, padx=my_padx)
mainFrame3=tb.Frame(root,bootstyle="dark")
mainFrame3.grid(row=10, column=0, rowspan=2, sticky="nsew", pady=my_pady, padx=my_padx)
nb = tb.Notebook(root)
nb.grid(row=0, column=1, rowspan=5, sticky="n", padx=my_padx, pady=my_pady)
mainFrame4=LabelFrame(root)
mainFrame4.grid(row=5, rowspan=4, column=1,  sticky="nsew", pady=my_pady, padx=my_padx)
credit=tb.Label(root, text="made by @Chris 2023", font=("Helvetica", 12))
credit.grid(row=10, rowspan=2, column=1, padx=10, pady=10)
f1 = Frame(mainFrame1)
f1.pack(pady=my_pady, padx=my_padx)
f2=tb.Frame(mainFrame1)
f2.pack(fill=BOTH)
f3 =tb.Frame(mainFrame2)
f3.pack(pady=my_pady, padx=my_padx)

#TITLE
my_label=tb.Label(root, text="Επετηριδολόγος",  font=("Helvetica", 18), bootstyle="default")
my_label.grid(row=0, column=0,pady=20)

#MAINFRAME1
    #chosefile
file_button= tb.Button(f1, width=20,text="\nΑρχείο\n", command= select_file)
file_button.grid(row=0, column=0, pady=my_pady, padx=my_padx)
tt_file_button=ToolTip(file_button, text="Επιλέξτε το αρχείο που περιέχει την επετηρίδα. Η επετηρίδα πρέπει να έχει την μορφή όνομα <κενό> επίθετο <κενό> χρονολογία γέννησης. Εάν υπάρχουν περισσότερα ονόματα ή περισσότερα επίθετα, δεν θα πρέπει να διαχωρίζονται με κενό, αλλά με άλλο τρόπο, πχ. παύλες", bootstyle="warning")

file_label=tb.Label(f1, width=20, bootstyle="info")
file_label.grid(row=1, column=0, pady=my_pady, padx=my_padx)
# tt_file_label=ToolTip(file_label, text=f"{}", bootstyle="warning")

reload_button=tb.Button(f1, width=20, bootstyle="warning", text="\nRELOAD\n", compound="right", command= reload)
reload_button.grid(row=2, column=0, pady=my_pady, padx=my_padx)
tt_reload_button=ToolTip(reload_button, text="Επαναφόρτωση του τρέχοντος αρχείου", bootstyle="warning")


 
demo_media = tb.PhotoImage(file="justice.png")
media = tb.Label(f1, image=demo_media)
media.grid(column=1, row=0, rowspan=3)

    #Enter number in each rank gui
chose_countrank_PE=tb.Entry(f1, width=20, bootstyle="success")
chose_countrank_PE.chosen_name = "chose_countrank_PE"
chose_countrank_PE.insert(0,"75")
chose_countrank_PE.grid(row=0, column=2, pady=my_pady, padx=my_padx, sticky="ne")
chose_countrank_PE.bind("<FocusOut>",focusout_countrank)
tt_ccPE=ToolTip(chose_countrank_PE, text="Πλήθος θέσεων Προέδρων Εφετών. Ακέραιοι αριθμοί 0-500", bootstyle="warning")
chose_countrank_PE.bind("<KeyRelease>",key_countrank)
chose_countrank_PE.bind('<Control-v>', lambda _:'break')

chose_countrank_E=tb.Entry(f1,bootstyle="success", width=20)
chose_countrank_E.chosen_name = "chose_countrank_E"
chose_countrank_E.insert(0,"268")
chose_countrank_E.grid(row=1, column=2, padx=my_padx)
tt_ccE=ToolTip(chose_countrank_E, text="Πλήθος θέσεων Εφετών. Ακέραιοι αριθμοί 0-500", bootstyle="warning")
chose_countrank_E.bind("<FocusOut>",focusout_countrank)
chose_countrank_E.bind("<KeyRelease>",key_countrank)
chose_countrank_E.bind('<Control-v>', lambda _:'break')

chose_countrank_PP=tb.Entry(f1,bootstyle="success", width=20)
chose_countrank_PP.chosen_name = "chose_countrank_PP"
chose_countrank_PP.insert(0,"110")
chose_countrank_PP.grid(row=2, column=2, pady=my_pady, padx=my_padx)
tt_ccPP=ToolTip(chose_countrank_PP, text="Πλήθος θέσεων Προέδρων Πρωτοδικών. Ακέραιοι αριθμοί 0-500", bootstyle="warning")
chose_countrank_PP.bind("<FocusOut>",focusout_countrank)
chose_countrank_PP.bind("<KeyRelease>",key_countrank)
chose_countrank_PP.bind('<Control-v>', lambda _:'break')

#########AGE#####
chose_age_PE=tb.Entry(f2, width=20, bootstyle="success")
chose_age_PE.chosen_name = "chose_age_PE"
chose_age_PE.grid(pady=my_pady, padx=my_padx, row=0, column=0, rowspan=2)
chose_age_PE.insert(0, "67")
chose_age_PE.bind("<FocusOut>",focusout_age)
tt_caPE=ToolTip(chose_age_PE, text="Ηλικία συνταξιοδότησης Προέδρων Εφετών. Ακέραιοι αριθμοί 60-80", bootstyle="warning")
chose_age_PE.bind("<KeyRelease>",key_age)
chose_age_PE.bind('<Control-v>', lambda _:'break')

chose_age_E=tb.Entry(f2,bootstyle="success", width=20)
chose_age_E.chosen_name = "chose_age_E"
chose_age_E.grid(pady=my_pady, padx=my_padx, row=2, column=0, rowspan=2)
chose_age_E.insert(0, "65")
tt_caE=ToolTip(chose_age_E, text="Ηλικία συνταξιοδότησης Εφετών. Ακέραιοι αριθμοί 60-80", bootstyle="warning")
chose_age_E.bind("<FocusOut>",focusout_age)
chose_age_E.bind("<KeyRelease>",key_age)
chose_age_E.bind('<Control-v>', lambda _:'break')

chose_age_PP=tb.Entry(f2,bootstyle="success", width=20)
chose_age_PP.chosen_name = "chose_age_PP"
chose_age_PP.grid(pady=my_pady, padx=my_padx, row=4, column=0, rowspan=2)
chose_age_PP.insert(0, "65")
tt_caPP=ToolTip(chose_age_PP, text="Ηλικία συνταξιοδότησης Προέδρων Πρωτοδικών. Ακέραιοι αριθμοί 60-80", bootstyle="warning")
chose_age_PP.bind("<FocusOut>",focusout_age)
chose_age_PP.bind("<KeyRelease>",key_age)
chose_age_PP.bind('<Control-v>', lambda _:'break')

chose_age_P=tb.Entry(f2,bootstyle="success", width=20)
chose_age_P.chosen_name = "chose_age_P"
chose_age_P.insert(0, "65")
chose_age_P.grid(pady=my_pady, padx=my_padx, row=6, column=0, rowspan=2)
tt_caP=ToolTip(chose_age_P, text="Ηλικία συνταξιοδότησης Πρωτοδικών. Ακέραιοι αριθμοί 60-80", bootstyle="warning")
chose_age_P.bind("<FocusOut>",focusout_age)
chose_age_P.bind("<KeyRelease>",key_age)
chose_age_P.bind('<Control-v>', lambda _:'break')

    #Slider
year_slider=tb.Scale(f2, bootstyle="success", length=600, orient="horizontal", from_=0, to=30, command=slider)
year_slider.grid(pady=my_pady, padx=my_padx, row=2, column=2, columnspan=3)
tt_year_slider=ToolTip(year_slider, text="Εισάγετε το πλήθος των ετών που θέλετε να ψάξετε", bootstyle="warning")
year_slider_label=tb.Label(f2, text="0", font=("Helvetica", 18))
year_slider_label.grid(pady=0, row=3, column=3)

file_year_slider=tb.Scale(f2, bootstyle="success", length=600, orient="horizontal", from_=2022, to=2030, command=slider2)
file_year_slider.grid(pady=my_pady, padx=my_padx, row=5, column=2, columnspan=3)
tt_file_year_slider=ToolTip(file_year_slider, text="Εισάγετε το έτος έκδοσης της επετηρίδας που χρησιμοποιείτε", bootstyle="warning")
file_year_slider_label=tb.Label(f2, text="2022", font=("Helvetica", 18))
file_year_slider_label.grid(pady=0, row=6, column=3)
#MAINFRAME2
    #chose name gui
chose_name_entry=tb.Entry(f3, width=30)
chose_name_entry.grid(row=0, column=0, pady=my_pady, padx=my_padx)
tt1_chose_name=ToolTip(chose_name_entry, text="Γράψτε το όνομα το οποίο αναζητάτε στη λίστα", bootstyle="warning")
chose_name_entry.bind("<KeyRelease>",chose_name_entry_bind)
chose_name_entry.bind('<Control-v>', lambda _:'break')

    #name list gui
chose_name=tb.Combobox(f3, width=30, bootstyle="default", values=[""], state="readonly")
chose_name.grid(row=1, column=0, pady=my_pady, padx=my_padx)
chose_name.bind("<<ComboboxSelected>>",chose_name_bind)


    #Chose Rank gui
chose_rank=tb.Combobox(f3, width=30, bootstyle="default", values=ranks[:4])
chose_rank.grid(row=2, column=0, pady=my_pady, padx=my_padx)
chose_rank.current(0)
chose_rank.bind("<<ComboboxSelected>>",chose_rank_bind)

#Enter ksou gui
chose_ksou_PE=tb.Entry(f3, bootstyle="warning")
chose_ksou_PE.chosen_name = "chose_ksou_PE"
chose_ksou_PE.grid(row=0, column=2, pady=my_pady, padx=my_padx)
chose_ksou_PE.insert(0, "0")
chose_ksou_PE.bind("<FocusOut>",focusout_ksou)
tt_ckPE=ToolTip(chose_ksou_PE, text="Πλήθος Προέδρων Εφετών που πιθανολογείτe ότι θα αποχωρούν κάθε έτος από την υπηρεσία, πλην αυτών λόγω ορίου ηλικίας. Ακέραιοι αριθμοί 0-20", bootstyle="warning")
chose_ksou_PE.bind("<KeyRelease>",key_ksou)
chose_ksou_PE.bind('<Control-v>', lambda _:'break')

chose_ksou_E=tb.Entry(f3,bootstyle="warning")
chose_ksou_E.chosen_name = "chose_ksou_E"
chose_ksou_E.grid(row=1, column=2, pady=my_pady, padx=my_padx)
chose_ksou_E.insert(0, "0")
tt_ckE=ToolTip(chose_ksou_E, text="Πλήθος Εφετών που πιθανολογείτε ότι θα αποχωρούν κάθε έτος από την υπηρεσία, πλην αυτών λόγω ορίου ηλικίας. Ακέραιοι αριθμοί 0-20", bootstyle="warning")
chose_ksou_E.bind("<FocusOut>",focusout_ksou)
chose_ksou_E.bind("<KeyRelease>",key_ksou)
chose_ksou_E.bind('<Control-v>', lambda _:'break')

chose_ksou_PP=tb.Entry(f3,bootstyle="warning")
chose_ksou_PP.chosen_name = "chose_ksou_PP"
chose_ksou_PP.grid(row=2, column=2, pady=my_pady, padx=my_padx)
chose_ksou_PP.insert(0, "0")
tt_ccPP=ToolTip(chose_ksou_PP, text="Πλήθος Προέδρων Πρωτοδικών που πιθανολογείτε ότι θα αποχωρούν κάθε έτος από την υπηρεσία, πλην αυτών λόγω ορίου ηλικίας. Ακέραιοι αριθμοί 0-20", bootstyle="warning")
chose_ksou_PP.bind("<FocusOut>",focusout_ksou)
chose_ksou_PP.bind("<KeyRelease>",key_ksou)
chose_ksou_PP.bind('<Control-v>', lambda _:'break')

chose_ksou_P=tb.Entry(f3, bootstyle="warning")
chose_ksou_P.chosen_name = "chose_ksou_P"
chose_ksou_P.grid(row=3, column=2, pady=my_pady, padx=my_padx)
chose_ksou_P.insert(0, "0")
tt_ccP=ToolTip(chose_ksou_P, text="Πλήθος Πρωτοδικών που πιθανολογείτε ότι θα αποχωρούν κάθε έτος από την υπηρεσία, πλην αυτών λόγω ορίου ηλικίας. Ακέραιοι αριθμοί 0-20", bootstyle="warning")
chose_ksou_P.bind("<FocusOut>",focusout_ksou)
chose_ksou_P.bind("<KeyRelease>",key_ksou)
chose_ksou_P.bind('<Control-v>', lambda _:'break')

    #count rank for each seperate year
count_button= ttk.Button(f3,width=20,text ="Βαθμοί κατ' έτος",command = openNewWindowCountrank)
count_button.grid(row=0, column=3, pady=my_pady, padx=my_padx)

    #count ksou for each seperate year
ksou_button= ttk.Button(f3,width=20,text ="Αποχωρήσεις κατ' έτος",command = openNewWindowKsou)
ksou_button.grid(row=1, column=3, pady=my_pady, padx=my_padx)

    #count retirement age for each seperate year
age_button= ttk.Button(f3,width=20,text ="Ηλικία συνταξιοδότησης\n          κατ' έτος",command = openNewWindowAge)
age_button.grid(row=2, column=3, pady=my_pady, padx=my_padx)

#MAINFRAME 3
clear_all_button1=tb.Button(mainFrame3, width=20, bootstyle="danger", text="\nCLEAR ALL\n", compound="right", command= clearAll)
clear_all_button1.pack(pady=my_pady, padx=my_padx, side=RIGHT)
clear_all_button=tb.Button(mainFrame3, width=20, compound="left", bootstyle="success", text="\nENTER\n", command= enter)
clear_all_button.pack(pady=my_pady, padx=my_padx, side=LEFT)


#TAB gui#   

arr=["Πρόεδροι Εφετών", "Εφέτες", "Πρόεδροι Πρωτοδικών", "Πρωτοδίκες", "Αποχωρήσαντες"]
for i in range(5):
    tab = Frame(nb)  # Use tb.ttk.Frame
    tab.chosen_name = f"tab{i+1}"
    nb.add(tab, text=f"{arr[i]}")

    # Configure weights for rows and columns within each tab
    tab.grid_rowconfigure(0, weight=1)
    tab.grid_columnconfigure(0, weight=1)

    # Create a frame within each tab
    frame = Frame(tab)  # Use tb.ttk.Frame
    frame.grid(row=0, column=0, sticky="n")

 
messageArea=tb.Label(mainFrame4, text="Πληροφορίες", font=("Helvetica", 12))
messageArea.pack(pady=my_pady, padx=my_padx)

infoLabel=tb.Label(mainFrame4, wraplength=700)
infoLabel.pack()
root.mainloop() 