import random 
def Znaesh_li_t6l_vdol_nochnix_dorog_shla_bacekom_ne_gale9_nog(x1,x2):
	return random.randint(0,1)

list_fio = ["fio1","fio2","fio3","fio4","fio5" ]
list_0 = []
for i in range(len(list_fio)):
	list_0.append([])
	
# кто знает i-того, все = [1,1,1,1,1] 
for i in range(len(list_fio)):
	for j in range(len(list_fio)):
		x = Znaesh_li_t6l_vdol_nochnix_dorog_shla_bacekom_ne_gale9_nog(list_0[i],list_0[j])#знает ли итого, житый?
		if x == 1:
			list_0[i].append(1)
		else:
			list_0[i].append(0)

#list_0 = [[1,1,1,1,1],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]

#print(list_0)
nov_1 = [] #проверяем, есть ли человек которого нают все
for i in range(len(list_fio)):
	bul = True 
	for j in range(len(list_fio)):
		if list_0[i][j] != 1:
			bul = False
	if bul == True:
		nov_1.append(i)
#print(nov_1) # 0
nov_2 = [] #проверяем, человек из прошлого пункта знает кого то? 
for i in nov_1:
	bul = True
	for j in range(len(list_fio)):
		if j != i:
			if list_0[j][i] != 0:
				bul = False
	if bul == True:
		nov_2.append(i)

try:
	print("Новенький, в списке под номером: ",nov_2[0]+1)
except IndexError:
	print("Нет новеньких")

