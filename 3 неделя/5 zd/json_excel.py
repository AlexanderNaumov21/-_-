import json
from pandas import DataFrame
def Create_excel_fail(dictionary): # функция по созданию эксель файла
    df = DataFrame(dictionary)
    str_path = "./" + "Список_пользователей_ящиков" + ".xlsx"#имя будущего эксель файла
    df.to_excel(str_path, index=False)
with open('o_res_orgs.json', encoding="utf-8") as json_file: # из джейсона парсим данные организаций
    data_orgs = json.load(json_file)
    json_file.close()
n = 2 #количество файлов o_res_users!!!
data_users = []
for i in range(1,n+1): # из джейсонов парсим данные по каждому ящику и записываем в список
	with open(f'o_res_users_00{i}.json', encoding="utf-8") as json_file: # имена джейсон файлов должны быть одинаковые, 
		data_users.append(json.load(json_file))							 # кроме порядкового номера в конце
		json_file.close()
# три массива для почт, фио и есть ли права админа
arr_mailbox = []
arr_FIO = []
arr_admin = []
# записываем полученные данные в списки 
for i in range(n):
	for j in range(len(data_users[0]["Users"])):
		arr_mailbox.append(data_orgs["Organizations"][i]['Boxes'][0]['BoxId']) 
		arr_FIO.append(data_users[i]["Users"][j]["Name"])
		arr_admin.append(data_users[i]["Users"][j]["Permissions"]["IsAdministrator"])
# создаём словарь "Название столбца" : [элементы столбца в виде списка]
dictionary1 ={'Ящик': arr_mailbox,
              'ФИО': arr_FIO,
              'Администратор': arr_admin}
# передаём наш словарь в функцию создания эксель файла
Create_excel_fail( dictionary1)  