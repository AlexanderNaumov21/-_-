from tkinter import Button as ButtonTk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from datetime import datetime
#from functools import partial
from re import match as re_match
import tkinter.messagebox as mb
from pandas import DataFrame

# фокус для 1ого фрейма
def focus1(event):
	widget = root.focus_get()
	
	if str(type(widget)) == "<class 'tkinter.ttk.Entry'>":
		cumma_1otv["text"] = " "
	ot_ex(btn_ex1, cumma_1otv)

def focus2(event):

	widget = root.focus_get()
	if str(type(widget)) == "<class 'tkinter.ttk.Entry'>":
		cumma_2otv["text"] = " "
	ot_ex(btn_ex2, cumma_2otv)

def focus3(event):
	
	focus1(event)
	focus2(event)
	widget = root.focus_get()
	
	if str(type(widget)) == "<class 'tkinter.ttk.Entry'>":
		cumma_3otv["text"] = " "
		ghz_3otv['text'] = " "
	ot_ex(btn_ex3, cumma_3otv)		

# проверка ответа на заполненность, для разблокировки кнопки отчёта	
def ot_ex(btn_ex, otv_label):
	if otv_label["text"] == " ":
		btn_ex['state'] = ttk.DISABLED
	else:
		btn_ex['state'] = ttk.NORMAL

def Create_excel_fail(dictionary, label):
    df = DataFrame(dictionary)
    str_path = "./" + label + ".xlsx"
    df.to_excel(str_path, index=False)

def Create_label(frame, txt):
	label = ttk.Label(frame,  text=txt, width=17, font=("Arial", 14), borderwidth=0, relief="ridge")
	return label
def Create_entry(frame):
	entry = ttk.Entry(frame, font=("Arial", 14))
	return entry
#def Create_button(frame, date_arr, proc_arr, num_arr):
	#btn = tkinter.Button(frame, text="Расчитать", font=("Arial", 14), command=partial(click_button, date_arr, proc_arr, num_arr)) 
	#return btn
def click_button(date_str_arr, proc_str_arr, num_str_arr):
   # проверка дат
   try:
      bul_data = True
      date_arr = []
      for i in date_str_arr:
         date1 = datetime.strptime(i, '%d.%m.%Y').date()
         if date1.year > 2100 or date1.year < 2000:
            bul_data = False
            break
         else:
            date_arr.append(date1)
      if len(date_arr) == 2:
         if date_arr[0] > date_arr[-1] :
            bul_data = False
      elif len(date_arr) < 2 or len(date_arr) > 4:
         bul_data = False
      else:
         if date_arr[0] > date_arr[-1] or date_arr[1]<date_arr[0] or date_arr[1]>date_arr[-1] or date_arr[-2]<date_arr[0] or date_arr[-2]>date_arr[-1]:
            bul_data = False
   except ValueError as err:
      bul_data = False
   
   global main_date_arr
   main_date_arr = date_arr
   
   #проверка процентов
   try:
      bul_proc = True
      proc_date = []
      for i in proc_str_arr:
         if re_match("^\d{1,2}[.]\d{1,2}$", i) is None:
            bul_proc = False
         if float(i) > 30.00 or float(i)< 0.01:
            bul_proc = False
         else:
            proc_date.append(float(i))
   except ValueError:
      bul_proc = False
   
   global main_proc_arr
   main_proc_arr = proc_date

   #проверка чисел
   try:
      bul_num = True
      num_arr = []
      for i in num_str_arr:
         if re_match("^\d{1,}[.]\d{1,2}$", i) is None:
            bul_num = False
         if float(i) > 1000000.00 or float(i)< 0.99:
            bul_num = False
         else:
            num_arr.append(float(i))
   except ValueError:
      bul_num = False

   
   global main_num_arr
   main_num_arr = num_arr

   # проверка наличия ошибок
   err_str = "Ошибки в заполнение!"
   if bul_data==True and bul_proc==True and bul_num==True:
      return True
   else:
      if bul_data == False:
         err_str += "\nФормат дат: ДД.ММ.ГГГГ, от 01.01.2000 до 31.12.2099 "
      if bul_proc == False:
         err_str += "\nФормат процентов: 0.08, от 0.01 до 30.00 "
      if bul_num == False:
         err_str += "\nФормат чисел: 123.00, от 1.00 до 1000000.00 "
      return err_str



root = ttk.Window()

root.title("Расчёт займа")
root.geometry("455x560+400+100") 
root.minsize(455, 560)
root.maxsize(455, 560)
# создаем набор вкладок
notebook = ttk.Notebook(bootstyle="light")
notebook.pack(expand=True, fill=BOTH)
 
# создаем пару фреймвов 
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)
 
frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)
frame3.pack(fill=BOTH, expand=True)
 
# добавляем фреймы в качестве вкладок
notebook.add(frame1, text="Займ1")
notebook.add(frame2, text="Займ2")
notebook.add(frame3, text="Займ3")

#======================frame1==========================
label_1 = Create_label(frame1, "  Срочный займ").grid(row=0, column=0, columnspan=2, ipadx=6, ipady=6, padx=4, pady=4)
date_give_1 = Create_label(frame1, "Дата выдачи").grid(row=1, column=0, ipadx=6, ipady=6, padx=4, pady=4)
date_take_1 = Create_label(frame1, "Дата гашения").grid(row=2, column=0, ipadx=6, ipady=6, padx=4, pady=4)
num_1 = Create_label(frame1, "Сумма займа").grid(row=3, column=0, ipadx=6, ipady=6, padx=4, pady=4)
proc_1 = Create_label(frame1, "Процентная ставка, %").grid(row=4, column=0, ipadx=6, ipady=6, padx=4, pady=4)
cumma_1 = Create_label(frame1, "Сумма % по займу").grid(row=5, column=0, ipadx=6, ipady=6, padx=4, pady=4)

cumma_1otv = Create_label(frame1, " ")
cumma_1otv.grid(row=5, column=1, ipadx=6, ipady=6, padx=4, pady=4)

date_give_1e = Create_entry(frame1)
date_give_1e.grid(row=1, column=1, ipadx=1, ipady=1)
date_take_1e = Create_entry(frame1)
date_take_1e.grid(row=2, column=1, ipadx=1, ipady=1)
num_1e = Create_entry(frame1)
num_1e.grid(row=3, column=1, ipadx=1, ipady=1)
proc_1e = Create_entry(frame1)
proc_1e.grid(row=4, column=1, ipadx=1, ipady=1)

def Cl1():
	root.focus_force()
	main_date_arr = [date_give_1e.get(), date_take_1e.get()]
	main_proc_arr = [proc_1e.get()]
	main_num_arr = [num_1e.get()]

	btn1 = click_button(main_date_arr, main_proc_arr, main_num_arr)
	if btn1==True:
   		#логика приложения
   		main_date_arr[0]=datetime.strptime(main_date_arr[0], '%d.%m.%Y')
   		main_date_arr[-1]=datetime.strptime(main_date_arr[-1], '%d.%m.%Y')
   		
   		date = str(main_date_arr[-1]-main_date_arr[0]).split(" ", 1)
   		date = int(date[0])
   		cum = float(main_num_arr[0])*date*float(main_proc_arr[0])/100/365
   		global cumma_1otv
   		cum = round(cum, 2)
   		cumma_1otv["text"] = cum
	else:
		# вывод окна с ошибкой 
		msg = btn1
		mb.showerror("Ошибка", msg)


	# проверка ответа на заполнение
	if cumma_1otv["text"] == " ":
		btn_ex1['state'] = ttk.DISABLED
	else:
		btn_ex1['state'] = ttk.NORMAL

def Cl1_ex():
	dictionary1 ={'Дата выдачи': [date_give_1e.get()],
              'Дата гашения': [date_take_1e.get()],
              'Сумма займа': [num_1e.get()],
              'Процентня ставка, в %':[proc_1e.get()],
              'Сумма % по займу':[cumma_1otv['text']]}
	Create_excel_fail( dictionary1, "Срочный займ")  

btn1 = ButtonTk(frame1, text="Расчитать", font=("Arial", 14), command=Cl1, width=21)
btn1.grid(row=6, column=1, ipadx=1, ipady=1)

btn_ex1 = ButtonTk(frame1, text="Отчёт", font=("Arial", 14), state="disabled", width=17, command=Cl1_ex )
btn_ex1.grid(row=6, column=0, ipadx=1, ipady=1)

#frame1.bind('<Button-1>', lambda e1: focus1(e1))
#====================================================================
#======================frame2==========================
label_2 = ttk.Label(frame2,  text="Займ с изменением процентной ставки", width=31, font=("Arial", 14)).grid(row=0, column=0, columnspan=2, ipadx=6, ipady=6, padx=4, pady=4)
date_give_2 = Create_label(frame2, "Дата выдачи").grid(row=1, column=0, ipadx=6, ipady=6, padx=4, pady=4)
date_take_2 = Create_label(frame2, "Дата гашения").grid(row=2, column=0, ipadx=6, ipady=6, padx=4, pady=4)
num_2 = Create_label(frame2, "Сумма займа").grid(row=3, column=0, ipadx=6, ipady=6, padx=4, pady=4)
proc_2 = Create_label(frame2, "Процентная ставка, %").grid(row=4, column=0, ipadx=6, ipady=6, padx=4, pady=4)
date_edit_2 = Create_label(frame2, "Дата изменения\nпроцентной ставки").grid(row=5, column=0, ipadx=6, ipady=6, padx=4, pady=4)
proc_2_new = Create_label(frame2, "Новая процентная\nставка, %").grid(row=6, column=0, ipadx=6, ipady=6, padx=4, pady=4)
cumma_2 = Create_label(frame2, "Сумма % по займу").grid(row=7, column=0, ipadx=6, ipady=6, padx=4, pady=4)

cumma_2otv = Create_label(frame2, " ")
cumma_2otv.grid(row=7, column=1, ipadx=6, ipady=6, padx=4, pady=4)

date_give_2e = Create_entry(frame2)
date_give_2e.grid(row=1, column=1, ipadx=1, ipady=1)
date_take_2e = Create_entry(frame2)
date_take_2e.grid(row=2, column=1, ipadx=1, ipady=1)
num_2e = Create_entry(frame2)
num_2e.grid(row=3, column=1, ipadx=1, ipady=1)
proc_2e = Create_entry(frame2)
proc_2e.grid(row=4, column=1, ipadx=1, ipady=1)
date_edit_2e = Create_entry(frame2)
date_edit_2e.grid(row=5, column=1,  ipadx=1, ipady=6)
proc_2_newe = Create_entry(frame2)
proc_2_newe.grid(row=6, column=1,  ipadx=1, ipady=6)

def Cl2():
	root.focus_force()
	main_date_arr = [date_give_2e.get(), date_edit_2e.get(), date_take_2e.get()]
	main_proc_arr = [proc_2e.get(), proc_2_newe.get()]
	main_num_arr = [num_2e.get()]

	btn2 = click_button(main_date_arr, main_proc_arr, main_num_arr)
	if btn2==True:
   		#логика приложения
   		main_date_arr[0]=datetime.strptime(main_date_arr[0], '%d.%m.%Y')
   		main_date_arr[-1]=datetime.strptime(main_date_arr[-1], '%d.%m.%Y')
   		main_date_arr[1]=datetime.strptime(main_date_arr[1], '%d.%m.%Y')
   		
   		col_dn1 = str(main_date_arr[1]-main_date_arr[0] ).split(" ", 1)
   		col_dn1 = int(col_dn1[0])-1
   		col_dn2 = str(main_date_arr[-1]-main_date_arr[1] ).split(" ", 1)
   		col_dn2 = int(col_dn2[0])+1

   		cum = float(main_num_arr[0])*(col_dn1*float(main_proc_arr[0])+col_dn2*float(main_proc_arr[-1]))/100/365

   		global cumma_2otv
   		cum = round(cum, 2)
   		cumma_2otv["text"] = cum
   		
	else:
		# вывод окна с ошибкой 
		msg = btn2
		mb.showerror("Ошибка", msg)


	# проверка ответа на заполнение
	if cumma_2otv["text"] == " ":
		btn_ex2['state'] = ttk.DISABLED
	else:
		btn_ex2['state'] = ttk.NORMAL

def Cl2_ex():
	dictionary2 ={'Дата выдачи': [date_give_2e.get()],
              'Дата гашения': [date_take_2e.get()],
              'Сумма займа': [num_2e.get()],
              'Процентня ставка, в %':[proc_2e.get()],
              'Дата изменения процентной ставки':[date_edit_2e.get()],
              'Навая процентная ставка, в %':[proc_2_newe.get()],
              'Сумма % по займу':[cumma_2otv['text']]}
	Create_excel_fail( dictionary2, "Займ с изменением процентной ставки")  

btn2 = ButtonTk(frame2, text="Расчитать", font=("Arial", 14), command=Cl2, width=21)
btn2.grid(row=8, column=1, ipadx=1, ipady=1)

btn_ex2 = ButtonTk(frame2, text="Отчёт", font=("Arial", 14), state="disabled", width=17, command=Cl2_ex )
btn_ex2.grid(row=8, column=0, ipadx=1, ipady=1)

#frame2.bind('<Button-1>', lambda e2: focus2(e2))
#====================================================================
#======================frame3==========================
label_3 = ttk.Label(frame3,  text="     Займ с досрочным гашением", width=31, font=("Arial", 14)).grid(row=0, column=0, columnspan=2, ipadx=6, ipady=6, padx=4, pady=4)
date_give_3 = Create_label(frame3, "Дата выдачи").grid(row=1, column=0, ipadx=6, ipady=2, padx=4, pady=3)
date_take_3 = Create_label(frame3, "Дата гашения").grid(row=2, column=0, ipadx=6, ipady=2, padx=4, pady=3)
num_3 = Create_label(frame3, "Сумма займа").grid(row=3, column=0, ipadx=6, ipady=2, padx=4, pady=3)
proc_3 = Create_label(frame3, "Процентная ставка, %").grid(row=4, column=0, ipadx=6, ipady=2, padx=4, pady=3)
date_edit_3 = Create_label(frame3, "Дата изменения\nпроцентной ставки").grid(row=5, column=0, ipadx=2, ipady=2, padx=4, pady=3)
proc_3_new = Create_label(frame3, "Новая процентная\nставка, %").grid(row=6, column=0, ipadx=2, ipady=2, padx=4, pady=3)
date_chg_3 = Create_label(frame3, "Дата част. гашения").grid(row=7, column=0, ipadx=2, ipady=2, padx=4, pady=3)
num_chg_3 = Create_label(frame3, "Сумма част. гашения").grid(row=8, column=0, ipadx=2, ipady=2, padx=4, pady=3)
cumma_3 = Create_label(frame3, "Сумма % по займу").grid(row=9, column=0, ipadx=2, ipady=2, padx=4, pady=3)
ghz_3 = Create_label(frame3, "Гашение займа").grid(row=10, column=0, ipadx=2, ipady=2, padx=4, pady=3)

cumma_3otv = Create_label(frame3, " ")
cumma_3otv.grid(row=9, column=1, ipadx=6, ipady=2, padx=4, pady=3)
ghz_3otv = Create_label(frame3, " ")
ghz_3otv.grid(row=10, column=1, ipadx=6, ipady=2, padx=4, pady=3)

date_give_3e = Create_entry(frame3)
date_give_3e.grid(row=1, column=1, ipadx=1, ipady=2, padx=4, pady=3)
date_take_3e = Create_entry(frame3)
date_take_3e.grid(row=2, column=1, ipadx=1, ipady=2, padx=4, pady=3)
num_3e = Create_entry(frame3)
num_3e.grid(row=3, column=1, ipadx=1, ipady=2, padx=4, pady=3)
proc_3e = Create_entry(frame3)
proc_3e.grid(row=4, column=1, ipadx=1, ipady=2, padx=4, pady=3)
date_edit_3e = Create_entry(frame3)
date_edit_3e.grid(row=5, column=1,  ipadx=1, ipady=6, padx=4, pady=3)
proc_3_newe = Create_entry(frame3)
proc_3_newe.grid(row=6, column=1,  ipadx=1, ipady=6, padx=4, pady=3)
date_chg_3e = Create_entry(frame3)
date_chg_3e.grid(row=7, column=1,  ipadx=1, ipady=2, padx=4, pady=3)
num_chg_3e = Create_entry(frame3)
num_chg_3e.grid(row=8, column=1,  ipadx=1, ipady=2, padx=4, pady=3)

def Cl3():
	
	root.focus_force()
	main_date_arr = [date_give_3e.get(), date_edit_3e.get(), date_chg_3e.get(), date_take_3e.get()]
	main_proc_arr = [proc_3e.get(), proc_3_newe.get()]
	main_num_arr = [num_3e.get(), num_chg_3e.get()]

	btn3 = click_button(main_date_arr, main_proc_arr, main_num_arr)
	if btn3==True:
   		#логика приложения
   		main_date_arr[0]=datetime.strptime(main_date_arr[0], '%d.%m.%Y')
   		main_date_arr[-1]=datetime.strptime(main_date_arr[-1], '%d.%m.%Y')
   		main_date_arr[1]=datetime.strptime(main_date_arr[1], '%d.%m.%Y')
   		main_date_arr[2]=datetime.strptime(main_date_arr[2], '%d.%m.%Y')

   		col_day1 = 0
   		col_day2 = 0
   		col_day3 = 0
   		if main_date_arr[2] >= main_date_arr[1]:
   			col_day1 = str(main_date_arr[1] - main_date_arr[0]).split(" ", 1)
   			col_day1 = int(col_day1[0])-1

   			col_day2 = str(main_date_arr[2] - main_date_arr[1]).split(" ", 1)
   			col_day2 = int(col_day2[0])+1

   			col_day3 = str(main_date_arr[3] - main_date_arr[2]).split(" ", 1)
   			col_day3 = int(col_day3[0])
   		else:
   			col_day1 = str(main_date_arr[2] - main_date_arr[0]).split(" ", 1)
   			col_day1 = int(col_day1[0])

   			col_day2 = str(main_date_arr[1] - main_date_arr[2]).split(" ", 1)
   			col_day2 = int(col_day2[0])-1

   			col_day3 = str(main_date_arr[3] - main_date_arr[1]).split(" ", 1)
   			col_day3 = int(col_day3[0])+1

   		cum1 = float(main_num_arr[0])*col_day1*float(main_proc_arr[0])/100/365
   		cum2 = 0
   		if main_date_arr[2] >= main_date_arr[1]:
   			cum2 = float(main_num_arr[0])*col_day2*float(main_proc_arr[1])/100/365
   		else:
   			cum2 = (float(main_num_arr[0]) - float(main_num_arr[1]))*col_day2*float(main_proc_arr[0])/100/365
   		cum3 = (float(main_num_arr[0])- float(main_num_arr[1]))*col_day3*float(main_proc_arr[1])/100/365

   		cum = cum1 + cum2 + cum3
   		ghz = float(main_num_arr[0]) - float(main_num_arr[1])
   		global cumma_3otv
   		cum = round(cum, 2)
   		cumma_3otv["text"] = cum
   		global ghz_3otv
   		ghz = round(ghz, 2)
   		ghz_3otv["text"] = ghz
	else:
		# вывод окна с ошибкой 
		msg = btn3
		mb.showerror("Ошибка", msg)


	# проверка ответа на заполнение
	if cumma_3otv["text"] == " ":
		btn_ex3['state'] = ttk.DISABLED
	else:
		btn_ex3['state'] = ttk.NORMAL
	

def Cl3_ex():
	
	dictionary3 ={'Дата выдачи': [date_give_3e.get()],
              'Дата гашения': [date_take_3e.get()],
              'Сумма займа': [num_3e.get()],
              'Процентня ставка, в %':[proc_3e.get()],
              'Дата изменения процентной ставки':[date_edit_3e.get()],
              'Навая процентная ставка, в %':[proc_3_newe.get()],
              'Дата частичного погашения':[date_chg_3e.get()],
              'Сумма частичного гашения':[num_chg_3e.get()],
              'Сумма % по займу':[cumma_3otv['text']],
              'Гашение займа':[ghz_3otv['text']]}
	Create_excel_fail( dictionary3, "«Займ с досрочным гашением") 
	 

btn3 = ButtonTk(frame3, text="Расчитать", font=("Arial", 14), command=Cl3, width=21)
btn3.grid(row=11, column=1, ipadx=1, ipady=1)

btn_ex3 = ButtonTk(frame3, text="Отчёт", font=("Arial", 14), state="disabled", width=17, command=Cl3_ex )
btn_ex3.grid(row=11, column=0, ipadx=1, ipady=1)

frame3.bind_all('<Button-1>', lambda e3: focus3(e3))

#====================================================================

root.mainloop()

