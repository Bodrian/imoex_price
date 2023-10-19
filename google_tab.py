import gspread #модуль для работы с google таблицами
import time

#функция на вход получает словарь "название акции : значение", и должна записать котировку акции в ячейку справа
def print_price(dic_price):
	gc = gspread.service_account(filename='название JSON файла ключа для работы с гугл таблицами.json') 	# Ключь для работы с Гугл таблицами
	sh = gc.open_by_url('ссылка на вашу гугл таблицу - бемем из строки браузера')   #Открываем нужную таблицу по ссылке
	worksheet = sh.worksheet("test") 												#выбор рабочего листа
	
	n = 8
	while True:
		name = worksheet.cell(n, 3).value 											#читаем ячейку с координатами n - строка, 3 столбец
		if name is not None:
			worksheet.update_cell(n, 4, dic_price.get(name)) 							#пишем ячейку с координатами n - строка, 4 столбец
			print(f'Пишу котировку {name} - {dic_price.get(name)} в гугл таблицу')
		else:
			print('Выполнение записи котировок акций в гугл таблицу - завершено') 
			break 																	#пустая ячейка прерывает цикл
		n += 1
		time.sleep(1) #максимум 60 запросов в минуту к гугл таблицам
