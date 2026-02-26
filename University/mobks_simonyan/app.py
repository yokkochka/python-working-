import tkinter as tk
import subprocess
import logging
import os

root = tk.Tk()
root.config(bg = "white")
root.geometry("650x650+600+300")
root.title("Программа проверки средств информационной безопасности")

check_internet = tk.StringVar(value="")
check_installed_fw = tk.StringVar(value="")
check_fw = tk.StringVar(value="")

check_installed_antivirus = tk.StringVar(value="")
check_antivirus = tk.StringVar(value='')
test_antivirus = tk.StringVar(value="")

FONT = ('Arial', 12, 'bold')

logging.basicConfig(
    filename='logs.log',
    level=logging.INFO,
    format = "%(asctime)s | %(levelname)s | %(message)s",
    datefmt = "%Y-%m-%d %H:%M:%S"
)

def function_check_internet():
    logging.info("internet connection check has begun")
    try:
        subprocess.check_output(['ping', '-n', '1', '8.8.8.8'])
        result = "Устройство подключено к интернету!"
        logging.info("device is connected to the internet")
    except:
        result = "Устройство не подключено к интернету!"
        logging.error("device is not connected to the internet")
    check_internet.set(result)
    return result

def function_check_installed_fw():
    logging.info("start checking the installed firewall")

    try:
        status = subprocess.check_output(
            ["powershell", "-Command", "Get-Service -Name MpsSvc"], 
            text=True
        )
        if "Running" in status:
            result = "Фаервол установлен и работает!"
        elif "Stopped" in status:
            result = "Фаервол установлен, но не запущен!"
        else:
            result = "Фаервол найден, но статус неизвестен."
    except subprocess.CalledProcessError:
        result = "Фаервол не найден!"
    except Exception as e:
        result = f"Ошибка проверки фаервола: {e}"

    check_installed_fw.set(result)
    return result


def function_check_fw():
    logging.info("start checking firewall status")
    try:
        output = subprocess.check_output(
            ["cmd", "/c", "netsh advfirewall show allprofiles | findstr /C:Состояние /C:State"],
            stderr=subprocess.STDOUT,
            text=True,
            encoding="cp866" 
        ) 
        
        output = output.split('\n')
        
        for i in range(len(output)):
            output[i] = output[i].replace(' ','*', 1).replace(' ', '')

        lst = ['Сеть домена:', "Частная сеть:", "Общедоступная:"]
        result = ""
        for i, j in zip(output, lst):
            result += f'{j} {(i[i.find('*')+1:])}\n'

        result = result[:-1]
        logging.info(f"firewall activation check result {result}")
        check_fw.set(result)
        return result  

    except Exception as e:
        print("Error", e)



def function_check_installed_antivirus():
    logging.info("start checking the installed antivirus")

    fw_path = r"C:\Program Files\Windows Defender\MpCmdRun.exe"
    if os.path.exists(fw_path):
        logging.info("antivirus isinstalled")
        result = "Антивирус установлен!"
    else:
        logging.error("antivirus is not installed")
        result = "Антивирус не установлен!"
    check_installed_antivirus.set(result)
    return result


def function_check_antivirus():
    logging.info("start checking antivirus status")
    try:
        output = subprocess.check_output(
            ["powershell", "-Command", 
             "Get-MpComputerStatus | Select-Object AMServiceEnabled, AntispywareEnabled, AntivirusEnabled, RealTimeProtectionEnabled"],
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8"
        )

        lines = output.strip().splitlines()
        values = []
        if len(lines) > 2:
            values = lines[2].split()
        
        lst = [
            "Запущена",
            "Антишпионская защита",
            "Антивирус функционирует",
            "Защита в реальном времени"
        ]

        result = ""
        for name, val in zip(lst, values):
            
            result += f"{name}: {val}\n"
        logging.info(f"antivirus activation check result {result}")
        result = result.strip()

    except Exception as e:
        logging.error(f"Error: {e}")

    check_antivirus.set(result)
    return result

def function_test_antivirus():
    logging.info("antivirus scan begins")
    target_path_file = r"./target_file.txt"
    if os.path.exists(target_path_file):
        try:
            os.remove(target_path_file)  
            logging.info(f"file {target_path_file} deleted successfully")
        except Exception as e:
            logging.error(f"error deleting file {target_path_file}: {e}")
    else:
        
        file = open(target_path_file, "w")
        file.write('X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*')
        file.close()
        logging.info(f"file {target_path_file} with virus created successfully")
    test_antivirus.set("Ожидайте...")
    try:
        logging.info(f"attempt to access an infected file {target_path_file}")
        file = open(target_path_file, 'r')
        file.close()
    except:
        logging.error("error opening infected file")
    root.after(20000, check_antivirus_file, target_path_file)

def check_antivirus_file(path):
    if os.path.exists(path):
        result = "Антивирус работает некорректно!"
        logging.info(f"the antivirus is not working correctly")
    else:
        result = "Антивирус работает корректно!"
        logging.info('the antivirus is working correctly')

    test_antivirus.set(result)
    if text_full_result.get("1.0", tk.END).strip() != "": text_full_result.insert(tk.END, result)


def report():
    result = function_check_internet() + '\n' + \
            function_check_installed_fw() + '\n' + \
            function_check_fw() + '\n' + \
            function_check_installed_antivirus() + '\n' +\
            function_check_antivirus() + '\n' 
    function_test_antivirus()

    logging.info('the report has been compiled')

    text_full_result.delete("1.0", tk.END)
    text_full_result.insert(tk.END, result)

    return result


def save_report_to_file():
    logging.info('saving the report to a file has started')
    file = open("./report.txt", 'w', encoding='utf-8')
    if text_full_result.get("1.0", tk.END).strip() == '':
        file.write(report())
    else:
        file.write(text_full_result.get("1.0", tk.END))
    

# ------------------ ЧАСТЬ 1 ------------------
frame1 = tk.Frame(root, bd=2, relief=tk.GROOVE, padx=10, pady=10)
frame1.pack(fill='x', pady=5, padx=5)

lbl_part_1 = tk.Label(frame1, text="Проверка межсетевого экрана", font=FONT)
lbl_part_1.grid(row=0, column=0, sticky='w', pady=5)

btn_check_internet = tk.Button(frame1, text="Проверка подключения к интернету", command = function_check_internet)
btn_check_internet.grid(row=1, column=0, sticky='ew', pady=2)

btn_check_installed_fw = tk.Button(frame1, text="Проверка наличия установленного межсетевого экрана", wraplength=200, \
                                   command = function_check_installed_fw)
btn_check_installed_fw.grid(row=2, column=0, sticky='ew', pady=2)

btn_check_fw = tk.Button(frame1, text="Проверка работоспособности межсетевого экрана", command = function_check_fw)
btn_check_fw.grid(row=3, column=0, sticky='ew', pady=2)

lbl_chek_internet = tk.Label(frame1, textvariable=check_internet, bd=1, relief=tk.SUNKEN, width=40, background='white')
lbl_chek_internet.grid(row=1, column=1, padx=10, pady=2, sticky='ew')

lbl_check_installed_fw = tk.Label(frame1, textvariable=check_installed_fw, bd=1, relief=tk.SUNKEN, width=40, background='white')
lbl_check_installed_fw.grid(row=2, column=1, padx=10, pady=2, sticky='ew')

lbl_check_fw = tk.Label(frame1, textvariable=check_fw, bd=1, relief=tk.SUNKEN, width=40, background='white')
lbl_check_fw.grid(row=3, column=1, padx=10, pady=2, sticky='ew')

frame1.grid_columnconfigure(0, weight=1)
frame1.grid_columnconfigure(1, weight=1)



# ------------------ ЧАСТЬ 2 ------------------
frame2 = tk.Frame(root, bd=2, relief=tk.GROOVE, padx=10, pady=10)
frame2.pack(fill='x', pady=5, padx=5)

lbl_part_2 = tk.Label(frame2, text="Проверка антивирусного ПО", font=FONT)
lbl_part_2.grid(row=0, column=0, sticky='w', pady=5)
btn_check_installed_antivirus = tk.Button(frame2, text="Проверка наличия установленного антивируса", \
                                          command = function_check_installed_antivirus)
btn_check_installed_antivirus.grid(row=1, column=0, sticky='ew', pady=2)
btn_check_antivirus = tk.Button(frame2, text="Проверка работоспособности антивирусного ПО", \
                                command = function_check_antivirus)
btn_check_antivirus.grid(row=2, column=0, sticky='ew', pady=2)
btn_test_antivirus = tk.Button(frame2, text="Тестирование антивирусного ПО", command = function_test_antivirus)
btn_test_antivirus.grid(row=3, column=0, sticky='ew', pady=2)
lbl_check_installed_antivirus = tk.Label(frame2, textvariable=check_installed_antivirus, bd=1, relief=tk.SUNKEN, width=40, \
                                         background='white')
lbl_check_installed_antivirus.grid(row=1, column=1, padx=10, pady=2, sticky='ew')
lbl_check_antivirus = tk.Label(frame2, textvariable=check_antivirus, bd=1, relief=tk.SUNKEN, width=40, background='white')
lbl_check_antivirus.grid(row=2, column=1, padx=10, pady=2, sticky='ew')
lbl_test_antivirus = tk.Label(frame2, textvariable=test_antivirus, bd=1, relief=tk.SUNKEN, width=40, background='white')
lbl_test_antivirus.grid(row=3, column=1, padx=10, pady=2, sticky='ew')
frame2.grid_columnconfigure(0, weight=1)
frame2.grid_columnconfigure(1, weight=1)



# ------------------ ЧАСТЬ 3 ------------------
frame3 = tk.Frame(root, bd=2, relief=tk.GROOVE, padx=10, pady=10)
frame3.pack(fill='both', pady=5, padx=5, expand=True)

lbl_part_3 = tk.Label(frame3, text="Результаты проверок и рекомендации", font=FONT)
lbl_part_3.grid(row=0, column=0, columnspan=2, sticky='w', pady=5)

text_full_result = tk.Text(frame3, bd=1, relief=tk.SUNKEN)
text_full_result.grid(row=1, column=0, sticky='nsew', padx=5, pady=2)

frame_buttons = tk.Frame(frame3)
frame_buttons.grid(row=1, column=1, sticky='ns', padx=5, pady=2)

btn_print_result = tk.Button(frame_buttons, text="Ввести результаты", width=30, command = report)
btn_print_result.pack(fill='x', pady=2)

btn_save_to_file = tk.Button(frame_buttons, text="Сохранить результаты в файл", width=30, wraplength=160, command=save_report_to_file)
btn_save_to_file.pack(fill='x', pady=2)

btn_exit = tk.Button(frame_buttons, text='Выход', command=root.destroy)
btn_exit.pack(fill='x', pady=2)

frame3.grid_columnconfigure(0, weight=3)
frame3.grid_columnconfigure(1, weight=1)
frame3.grid_rowconfigure(1, weight=1)




root.mainloop()


