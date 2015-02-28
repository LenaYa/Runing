# coding: utf_8 

# m - для манежа и стадиона
# t - есть темп и км, за какое время пробегу?
# p - есть время и км, какой нужен темп?

zapros = raw_input('m - for manej, t - for time and p - for pace: ')


#за сколько секунд нужно пробежать круг для получения требуемого темпа
if zapros == 'm':
	temp = map(int, list(str(raw_input('Pace(mss): ')))) #нужный темп на километр, вида мсс
	a = float(raw_input('L of stad: ')) #длина круга стадиона
	l = round(1000/a, 2) #кругов в километре
	def krugi(temp, l):
		sec = 0
		for i in range(0, 2): #переводим темп в секунды на километр
			if i == 0:
				sec = sec + temp[i]*60;
			elif i == 1:
				sec = sec + temp[i]*10;
			else:
				sec = sec + temp[i];
		sec = sec/l; #делим полученные секунды на количество кругов стадиона
		if sec > 59:
			time = str(int(sec / 60)) + ':' + str(int(sec % 60))
		else:
			time = str(sec)

		return 'Time per round should be ' + time
	print krugi(temp, l)


# есть темп и км, за какое время пробегу?	
elif zapros == 't': 	
	temp = map(int, list(str(raw_input('Pace (mss): ')))) #нужный темп на километр, вида мсс
	km = int(raw_input("Distance: ")) 

	def vremia(temp, km):
		sec = 0
		for i in range(0, 3): #переводим темп в секунды на километр
			if i == 0:
				sec = sec + temp[i]*60;
			elif i == 1:
				sec = sec + temp[i]*10;
			else:
				sec = sec + temp[i];
		all_sec = sec * km
		mm = str(int(all_sec / 60))
		if int(mm) > 59: #добавляем часы
			hh = str(int(mm) / 60) + ':'
			mm = str(int(mm) - int(hh) * 60)
		else:
			hh = ''
		ss = str(int(all_sec % 60))
		if int(mm) < 10:
			mm = '0' + mm
		if int(ss) < 10:
			ss = '0' + ss
		b = 'time will be ' + hh + mm + ':' + ss
		return b	
	print vremia(temp, km)


# есть время и км, какой нужен темп?
# время в формате чммсс

elif zapros == 'p':
	time = map(int, list(str(raw_input('Time (hmmss): '))))
	km = int(raw_input("Distance: "))
	if len(time) == 4:
		time.insert(0, 0)
	elif len(time) == 3:
		time.insert(0, 0)
		time.insert(1, 0)
	def pace(time, km):
		# добавить нули слева, если length(time) < 5 !!!!
		# а вдруг сработает?
		sec = time[0] * 60 * 60 + time[1] * 600 + time[2] * 60 + time[3] * 10 + time[4]
		sek_km = int(sec / km) # секунд на километр
		# а теперь магия - получаем минуты на километры, милисекунды в жопу
		mm = str(sek_km / 60)
		ss = str(sek_km % 60)
		if int(ss) < 10:
			ss = '0' + ss
		p = 'Pace should be: ' + mm + ':' + ss + ' min/km'
		return p
	print pace(time, km)

