#!/usr/bin/python

import random
import numpy

subjects  = ['SE','DAA','MP','OOPS','DC','M4']
subjects1 = ['SE','DAA','MP','OOPS','DC','M4']
subjects2 = ['SE','DAA','MP','OOPS','DC','M4']
subjects3 = ['SE','DAA','MP','OOPS','DC','M4']
			
			#NAME,      SUB, CLASS, LAB
teachers = [['Daminder','SE' ,'ABC',''],
			['Bharati',  'M4' ,'AB',''],
			['Vijay Baskar', 'DAA','A',''],
			['Bhumika',	'MP','AB','AB'],
			['Sudhakar','DC','AB',''],
			['Sudhakar','MP','','C'],
			['Poornima', 'OOPS' ,'AB',''],
			['Poornima', 'DAA', '', 'AB'],
			['Gopika','DAA','','AB'],
			['Reshma','DAA','','ABC'],
			['Sudha','DAA','', 'AB'],
			['Meenakshi', 'MP', '', 'ABC'],
			['Anand', 'MP', '', 'ABC'],
			['Jhansi', 'DAA', 'B', ''],
			['Pinchu','DAA', '', 'BC'],
			['Sonali', 'DAA', '', 'BC'],
			['Preeti', 'MP', 'C', 'BC'],
			['Usha', 'M4', 'C', ''],
			['Premkumar', 'DAA', 'C', ''],
			['Navneetha', 'OOPS', 'C', 'C'],
			['Savitha', 'DC', 'C', 'C']]

			
labs = ['MP-L','DAA-L']
hours = [4,4,4,4,4,4]
lab_duration = 3
classes_per_day = 1
c, r = 7, 6
half_days = [3,1]
number_of_sections = 3

Table1 = [[0 for x in range(c)] for y in range(r)]
Table2 = [[0 for x in range(c)] for y in range(r)]
Table3 = [[0 for x in range(c)] for y in range(r)]

def freehoursperweek():
	freehours = 0
	for hour in hours:
		freehours = freehours + hour
	freehours = freehours + (len(labs)*lab_duration)
	freehours = (r*c)-freehours
	return freehours-6

#print(freehoursperweek())

def markhalfdays():
	for i in range(4,c):
		Table1[3][i] = 'X'
		Table2[3][i] = 'X'
		Table3[3][i] = 'X'
		Table1[1][i] = 'X'
		Table2[1][i] = 'X'
		Table3[1][i] = 'X'

def firstHour():
	used1 = []
	used2 = []
	day = 0
	while day != r:
		val1 = random.randrange(len(subjects1))
		val2 = random.randrange(len(subjects2))
		if subjects1[val1] not in used1 and subjects2[val2] not in used2 and val1 != val2:
			used1.append(subjects1[val1])
			Table1[day][0] = subjects1[val1]
			used2.append(subjects1[val2])
			Table2[day][0] = subjects2[val2]
			day += 1
			#print(used,day)
			
def placeLabs():
	used_labs = []
	labs_placed = 0
	lab_hour = [0,c-lab_duration]
	lab_hour_picked = []
	days_picked = []
	
	while labs_placed != len(labs):
		day_pick = random.randrange(r)
		lab_hour_pick1 = random.choice(lab_hour)
		lab_hour_pick2 = random.choice(lab_hour)
		if Table1[day_pick][lab_hour_pick1] != 'X' and Table2[day_pick][lab_hour_pick2] != 'X' and lab_hour_pick1 != lab_hour_pick2:
			lab_pick = random.choice(labs)
			if day_pick not in days_picked and lab_pick not in used_labs:
				for i in range(lab_duration):
					Table1[day_pick][lab_hour_pick1+i] = lab_pick
					Table2[day_pick][lab_hour_pick2+i] = lab_pick
				used_labs.append(lab_pick)
				lab_hour_picked.append(lab_hour_pick1)
				days_picked.append(day_pick)
				labs_placed += 1
	used_labs = []
	lab_hour_picked = []
	days_picked = []
	labs_placed = 0
	while labs_placed != len(labs):
			day_pick = random.randrange(r)
			lab_hour_pick3 = random.choice(lab_hour)	
			lab_pick = random.choice(labs)		
			if Table3[day_pick][lab_hour_pick3] != 'X' and lab_pick != Table2[day_pick][lab_hour_pick3] and lab_pick != Table1[day_pick][lab_hour_pick3]:
				if day_pick not in days_picked and lab_pick not in used_labs:
					for i in range(lab_duration):
						Table3[day_pick][lab_hour_pick3+i] = lab_pick
					used_labs.append(lab_pick)
					lab_hour_picked.append(lab_hour_pick3)
					days_picked.append(day_pick)
					labs_placed += 1

def count(Table, key):
	count = 0
	for row in range(r):
		for col in range(c):
			if Table[row][col] == key:
				count +=1
	return count

def distributeClasses():
	class_count1 = []
	class_count2 = []
	#print('reference -> [CO, DS, DMS, ADE, USP, M3]')
	for i in range(len(subjects1)):
		class_count1.append(count(Table1,subjects[i]))
		class_count2.append(count(Table2,subjects[i]))
		
	pick_hour = -1
	pick_day = 0
	#print(class_count1,'\n',class_count2)
	while True:
		if class_count1 == hours and class_count2 == hours:
			break
		for i in range(len(subjects1)):
			if class_count1[i] == hours[i]:
				subjects1[i] = 0
		for i in range(len(subjects2)):
			if class_count2[i] == hours[i]:
				subjects2[i] = 0
		pick_hour += 1
		if pick_hour == c:
			pick_hour = 0
			pick_day += 1
		if pick_day == c-2 and pick_hour == c or pick_day == r:
			pick_hour = 0
			pick_day = 0			
		#print("DAY",pick_day)
		#print("HOUR",pick_hour)
		pick_subject1 = random.randrange(len(subjects1))
		pick_subject2 = random.randrange(len(subjects2))
		if pick_subject1 == pick_subject2 or (subjects1[pick_subject1] == 0 and subjects2[pick_subject2] == 0):
			while pick_subject1 == pick_subject2 or (subjects1[pick_subject1] == 0 and subjects2[pick_subject2] == 0):
				pick_subject1 = random.randrange(len(subjects1))
				pick_subject2 = random.randrange(len(subjects2))
		#print('1:',subjects1,'\n\n','2:',subjects2)

		if Table1[pick_day][pick_hour] == 0 and subjects1[pick_subject1] != 0 and Table1[pick_day].count(subjects1[pick_subject1]) < classes_per_day:
			Table1[pick_day][pick_hour] = subjects1[pick_subject1]
			class_count1[subjects1.index(subjects1[pick_subject1])] += 1
			#printTables(Table1, Table2)
			#print(class_count1,'\n',class_count2)
			#print('1:',subjects1,'\n\n','2:',subjects2)

		if Table2[pick_day][pick_hour] == 0 and subjects2[pick_subject2] != 0 and Table2[pick_day].count(subjects2[pick_subject2]) < classes_per_day:
			Table2[pick_day][pick_hour] = subjects2[pick_subject2]
			class_count2[subjects2.index(subjects2[pick_subject2])] += 1
			#printTables(Table1, Table2)
			#print(class_count1,'\n',class_count2)
			#print('1:',subjects1,'\n\n','2:',subjects2)

def distributeClasses3():
	class_count3 = []
	for i in range(len(subjects1)):
		class_count3.append(count(Table3,subjects[i]))
	pick_hour = -1
	pick_day = 0
	while True:
			if class_count3 == hours:
				break
			for i in range(len(subjects3)):
				if class_count3[i] == hours[i]:
					subjects3[i] = 0
			pick_hour += 1
			if pick_hour == c:
				pick_hour = 0
				pick_day += 1
			if pick_day == c-2 and pick_hour == c or pick_day == r:
				pick_hour = 0
				pick_day = 0
			pick_subject3 = random.randrange(len(subjects3))
			if Table3[pick_day][pick_hour] == 0 and subjects3[pick_subject3] != 0 and Table3[pick_day].count(subjects3[pick_subject3]) < classes_per_day:
				Table3[pick_day][pick_hour] = subjects3[pick_subject3]
				class_count3[subjects3.index(subjects3[pick_subject3])] += 1
				
def findFaultyLabRows(Table):
	rows_to_fix1 = []
	for row in range(r):
		if Table[row].count(0) > 0 and (Table[row][c-lab_duration] in labs):
			rows_to_fix1.append(row)
			#print('found row',row)
	#print("to fix ->",rows_to_fix1)
	return rows_to_fix1

def fixLabRows(Table1, Table2, rows_to_fix1):
	if len(rows_to_fix1) > 0:
		temp = Table1
		for row in rows_to_fix1:
			while True:
				if Table1[row].count(0) > 0:
					n = Table1[row].index(0)
					tracker = n
					while temp[row][tracker] == 0 and tracker < c-lab_duration:
						tracker += 1
					if temp[row][tracker] in labs:
						break
					else:
						temp[row][n] = temp[row][tracker]
						temp[row][tracker] = 0
						n += 1
						if checkConflict(temp, Table2) == 0:
							#print('Successful!')
							Table1 = temp
							#print(numpy.matrix(Table1))
						else:
							continue	
	#else:
		#print('No faulty lab rows')	
	return Table1
			


def printTables(Table1, Table2, Table3):
	print(numpy.matrix(Table1))
	print('\n')
	print(numpy.matrix(Table2))
	print('\n')
	print(numpy.matrix(Table3))
	print('\n')
	print(numpy.matrix(teachers))
	print('\n')
	
def checkConflict(Table1, Table2):
	res = []
	for row in range(r):
		for col in range(c):
			if Table1[row][col] == Table2[row][col] and Table1[row][col] != 'X' and Table1[row][col] != 0 and Table1[row][col] not in labs:
				res.append(row)
				res.append(col)
				return res
	return 0

def fixFaultyRows(Table1, Table2):
	temp = Table1
	offset = 0
	t = 0
	for row in range(r):
		if Table1[row].count(0) > 0 and Table1[row][c-lab_duration] not in labs and row !=3 and row !=1:
			#print('fixing row',row)
			while True:
				pos = Table1[row].index(0)
				tracker = pos
				#print('pos -> ',pos)
				while True:
					if temp[row][tracker] != 0 or tracker == c-1:
						break
					else:
						tracker += 1
				#print('tracker -> ',tracker)
				temp[row][pos] = temp[row][tracker]
				temp[row][tracker] = 0
				if Table1[row][pos:c-1] == [0 for x in range((c-1)-pos)]:
					break
				if checkConflict(temp, Table2) == 0:
					#print('Successful!')
					Table1 = temp
					#print(numpy.matrix(Table1))
				else:
					#print('Move not permitted!')
					offset += 1
					continue	
		#else:
		#	print('Not a faulty row')	
	return Table1
				
def removeGaps(Table):
	for row in range(r):
		if 0 in Table[row] and Table[row].index(0) < c-2:
			bad_row = row
			bad_col = Table[row].index(0)
			track_col = c-1
			track_row = 0
			while True:
				if track_col == 0:
					track_col = c-1
				if track_row == r:
					track_row = 0
					track_col -= 1
				#print('trackrow : ',track_row,'trackcol : ',track_col)
				if Table[track_row][track_col] not in labs and Table[track_row][track_col] != 0 and Table[track_row][track_col] != 'X':
					#SWAP
					Table[bad_row][bad_col] = Table[track_row][track_col]
					Table[track_row][track_col] = 0
					return Table
				else:
					track_row += 1

def badRowCheck(Table1):
	for row in range(r):
			if 0 in Table1[row] and Table1[row].index(0) < c-2:
				return 1
	return 0
	
def checkDoubleClassesRow(Table):
	for i in range(1,c):
		if Table[i] == Table[i-1] and Table[i] not in labs and Table[i] != 0 and Table[i] != 'X':
			return i
	return -1
	
def checkDoubleFullTable(Table):
	for row in range(r):
		for i in range(1,c):
				if Table[row][i] == Table[row][i-1] and Table[row][i] not in labs and Table[row][i] != 0 and Table[row][i] != 'X':
					return i
	return -1
		
def fixDoubleClasses(Table1,Table2):
	track_row = 0
	for track_row in range(r):
		result = checkDoubleClassesRow(Table1[track_row])
		if result > 0:
			TEMP = Table1
			pick_row = random.randrange(r)
			pick_col = random.randrange(c)
			if TEMP[pick_row][pick_col] in labs or TEMP[pick_row][pick_col] == 'X' or TEMP[pick_row][pick_col] == 0:
				while TEMP[pick_row][pick_col] in labs or TEMP[pick_row][pick_col] == 'X' or TEMP[pick_row][pick_col] == 0:
					pick_row = random.randrange(r)
					pick_col = random.randrange(c)
			SUB = TEMP[track_row][result]
			TEMP[track_row][result] = TEMP[pick_row][pick_col]
			TEMP[pick_row][pick_col] = SUB
			if checkConflict(TEMP, Table2) != 0:
				#print(pick_row,pick_col,"to",track_row,result,"move not allowed. trying again")
				TEMP = Table1
				continue
			else:
				#print(pick_row,pick_col,"to",track_row,result,"was successful")
				Table1 = TEMP
				track_row += 1
		#if track_row == r:
		#	break
	return Table1

def fixConflicts(Table1,Table2):
	while True:
		result = checkConflict(Table1, Table2)
		if result == 0:
			return Table1
		else:
			TEMP = Table1
			pick_row = random.randrange(r)
			pick_col = random.randrange(c)
			bad_row = result[0]
			bad_col = result[1]
			if TEMP[pick_row][pick_col] in labs or TEMP[pick_row][pick_col] == 'X' or TEMP[pick_row][pick_col] == 0:
				while TEMP[pick_row][pick_col] in labs or TEMP[pick_row][pick_col] == 'X' or TEMP[pick_row][pick_col] == 0:
					pick_row = random.randrange(r)
					pick_col = random.randrange(c)
			SUB = TEMP[bad_row][bad_col]
			TEMP[bad_row][bad_col] = TEMP[pick_row][pick_col]
			TEMP[pick_row][pick_col] = SUB
			if checkConflict(TEMP, Table2) != 0:
				#print(pick_row,pick_col,"to",bad_row,bad_col,"move not allowed. trying again")
				#TEMP = Table1
				continue
			else:
				#print(pick_row,pick_col,"to",bad_row,bad_col,"was successful")
				Table1 = TEMP
				
def fixTableFH(Table1, Table2, Table3):
	#print(numpy.matrix(Table3))
	Table3 = numpy.asarray(Table3)
	first_hours = numpy.ndarray.tolist(Table3.T[0])
	Table3 = numpy.ndarray.tolist(Table3)
	#first_hours = list(first_hours)
	#print(first_hours)
	for subject in subjects:
		count = 0
		for i in range(len(first_hours)):
			if subject == first_hours[i]:
				count += 1
				if count > 1:
					break
		if count > 1:
			while True:
				pick_row = random.randrange(r)
				pick_col = random.randrange(c)
				if Table3[pick_row][pick_col] not in labs and Table3[pick_row][pick_col] != 'X' and Table3[pick_row][pick_col] != 0 and first_hours.count(Table3[pick_row][pick_col]) == 0:
					temp = Table3
					temp_sub = temp[pick_row][pick_col] 
					temp[pick_row][pick_col] = temp[i][0]
					temp[i][0] = temp_sub
					if checkConflict(Table1, Table3) == 0 and checkConflict(Table2, Table3) == 0:
						Table3 = temp
						break
	return Table3

def getcolumn(Table, pos):
	Table = numpy.asarray(Table)
	Table = numpy.ndarray.tolist(Table.T[pos])
	#Table = numpy.ndarray.tolist(Table)
	return Table

def fixTableFHv2(Table1, Table2, Table3, id):
	for i in range(len(subjects)):
		column = getcolumn(Table1, 0)
		if column.count(subjects[i]) > 1:
			Table1 = swapRandom(Table1, column.index(subjects[i]), 0)
	for i in range(len(subjects)):
		column = getcolumn(Table2, 0)
		if column.count(subjects[i]) > 1:
			Table2 = swapRandom(Table2, column.index(subjects[i]), 0)
	for i in range(len(subjects)):
		column = getcolumn(Table3, 0)
		if column.count(subjects[i]) > 1:
			Table3 = swapRandom(Table3, column.index(subjects[i]), 0)
	for row in range(r):
		for col in range(1):
			if Table1[row][col] == Table2[row][col] and Table1[row][col] in subjects:
				Table1 = swapRandom(Table1, row, col)
			if Table1[row][col] == Table3[row][col] and Table1[row][col] in subjects:
				Table1 = swapRandom(Table1, row, col)
			if Table2[row][col] == Table1[row][col] and Table2[row][col] in subjects:
				Table2 = swapRandom(Table2, row, col)
			if Table2[row][col] == Table3[row][col] and Table2[row][col] in subjects:
				Table2 = swapRandom(Table2, row, col)
			if Table3[row][col] == Table2[row][col] and Table3[row][col] in subjects:
				Table3 = swapRandom(Table3, row, col)
			if Table3[row][col] == Table1[row][col] and Table3[row][col] in subjects:
				Table3 = swapRandom(Table3, row, col)
	if id == 1:
		return Table1
	if id == 2:
		return Table2
	if id == 3:
		return Table3

					
def fixTableCounts(Table1, Table2, Table3):
	#print(numpy.matrix(Table3))
	for row in range(r):
		for col in range(1,c):
			if Table3[row].count(Table3[row][col]) > classes_per_day and Table3[row][col] in subjects:
				#while True:
				#for pick_row in range(r):
				#	for pick_col in range(1,c):
				while True:
					pick_row = random.randrange(r)
					pick_col = random.randrange(c)
				#pick_row = random.randrange(r)
				#pick_col = random.randrange(c)
					if Table3[pick_row][pick_col] not in labs and Table3[pick_row][pick_col] != 'X' and Table3[pick_row][pick_col] != 0 and pick_col != 0:
						temp = Table3
						temp_sub = temp[pick_row][pick_col] 
						temp[pick_row][pick_col] = temp[row][col]
						temp[row][col] = temp_sub
						if checkConflict(Table1, Table3) == 0 and checkConflict(Table2, Table3) == 0:
							Table3 = temp
							break
	return Table3
				
def checkHours(Table):
	for row in range(r):
			for col in range(1,c):
				if Table[row].count(Table[row][col]) > classes_per_day and Table[row][col] in subjects:
					print('Flaw detected!')	
					return -1
	return 0	

def printProfTable(SUB,SEC,LAB):
	PROF_TABLE = [[0 for x in range(c)] for y in range(r)]
	for row in range(r):
		for col in range(c):
			
			if Table1[row][col] == SUB and 'A' in SEC:
				PROF_TABLE[row][col] = SUB + '-A'
			if SUB in str(Table1[row][col]) and '-L' in str(Table1[row][col]) and 'A' in LAB:
				PROF_TABLE[row][col] = SUB + '-L' + '(A)'
				
			if Table2[row][col] == SUB and 'B' in SEC:
				PROF_TABLE[row][col] = SUB + '-B'
			if SUB in str(Table2[row][col]) and '-L' in str(Table2[row][col]) and 'A' in LAB:
				PROF_TABLE[row][col] = SUB + '-L' + '(B)'
				
			if Table3[row][col] == SUB and 'C' in SEC:
				PROF_TABLE[row][col] = SUB + '-C'
			if SUB in str(Table3[row][col]) and '-L' in str(Table3[row][col]) and 'A' in LAB:
				PROF_TABLE[row][col] = SUB + '-L' + '(C)'
	return PROF_TABLE

def createProfTable():
	table = numpy.asarray(teachers)
	table = numpy.array(table.T[0])
	table = numpy.ndarray.tolist(table)

	for i in range(len(table)):
		print('Prof. '+str(table[i]))
		print(numpy.matrix(printProfTable(teachers[i][1], teachers[i][2], teachers[i][3])))
		print('\n\n')

def clearLab(Table1, Table2, Table3):
	for row in range(r):
		for col in range(c):
			if isLab(Table1[r][c],Table2[r][c]) == 1:
				print("Found conflicting lab - 1\n")
				while True:
					pick_row = random.randrange(r)
					pick_col = random.randrange(c)
					if Table1[pick_row][pick_col] not in labs and Table1[pick_row][pick_col] != 'X' and Table1[pick_row][pick_col] != 0 and first_hours.count(Table1[pick_row][pick_col]) == 0:
						temp = Table1
						temp_sub = temp[pick_row][pick_col] 
						temp[pick_row][pick_col] = temp[i][0]
						temp[i][0] = temp_sub
						if checkConflict(Table1, Table3) == 0 and checkConflict(Table2, Table3) == 0:
							Table3 = temp
							break

def isLab(subject, lab):
	if str(subject) in str(lab) and '-L' in str(lab):
		return 1
	return 0

def checkLab(Table1, Table2, Table3):
	for row in range(r):
		for col in range(c):
				if isLab(Table1[row][col],Table2[row][col]) == 1:
					print("Move subject from table 1 (2)")
				if isLab(Table2[row][col],Table1[row][col]) == 1:
					print("Move subject from table 2 (1)")
				if isLab(Table3[row][col],Table1[row][col]) == 1:
					print("Move subject from table 3 (1)")
				if isLab(Table3[row][col],Table2[row][col]) == 1:
					print("Move subject from table 3 (2)")
				if isLab(Table2[row][col],Table3[row][col]) == 1:
					print("Move subject from table 2 (3)")
				if isLab(Table1[row][col],Table3[row][col]) == 1:
					print("Move subject from table 1 (3)")
	print("Lab conflicts checked")

def done():
	print('Done!')

def swapRandom(TableX, badrow, badcol):
	while True:
		pick_row = random.randrange(r)
		pick_col = random.randrange(c)
		if TableX[pick_row][pick_col] in subjects and pick_col > 0:
			temp = TableX[badrow][badcol]
			TableX[badrow][badcol] = TableX[pick_row][pick_col]
			TableX[pick_row][pick_col] = temp
			return TableX



def fixconflicts3tables(Table1, Table2, Table3, trig):
	for row in range(r):
		for col in range(1,c):
			if Table1[row][col] == Table2[row][col] and Table1[row][col] in subjects:
				Table1 = swapRandom(Table1, row, col)
			if Table1[row][col] == Table3[row][col] and Table1[row][col] in subjects:
				Table1 = swapRandom(Table1, row, col)
			if Table2[row][col] == Table1[row][col] and Table2[row][col] in subjects:
				Table2 = swapRandom(Table2, row, col)
			if Table2[row][col] == Table3[row][col] and Table2[row][col] in subjects:
				Table2 = swapRandom(Table2, row, col)
			if Table3[row][col] == Table2[row][col] and Table3[row][col] in subjects:
				Table3 = swapRandom(Table3, row, col)
			if Table3[row][col] == Table1[row][col] and Table3[row][col] in subjects:
				Table3 = swapRandom(Table3, row, col)
	if trig == 1:
		return Table1
	if trig == 2:
		return Table2
	if trig == 3:
		return Table3
		
def buildTables(Table1, Table2, Table3):
	print('Marking half days...')
	markhalfdays()
	done()
	print('Placing labs...')
	placeLabs()	
	done()
	print('Placing classes in A&B...')
	distributeClasses()
	done()
	print('Placing classes in C...')
	distributeClasses3()
	done()
	print('Fixing faulty rows...')
	print('Stage 1')
	Table1 = fixLabRows(Table1, Table2, findFaultyLabRows(Table1))
	print('Stage 2')
	Table2 = fixLabRows(Table2, Table1, findFaultyLabRows(Table2))
	print('Stage 3')
	Table3 = fixLabRows(Table3, Table1, findFaultyLabRows(Table3))
	print('Stage 4')
	Table3 = fixLabRows(Table3, Table2, findFaultyLabRows(Table3))
	print('Stage 5')
	Table1 = fixFaultyRows(Table1, Table2)
	print('Stage 6')
	Table2 = fixFaultyRows(Table2, Table1)
	print('Stage 7')
	Table3 = fixFaultyRows(Table3, Table2)
	print('Stage 8')
	Table3 = fixFaultyRows(Table3, Table1)
	done()
	print('Clearing free spaces...[Restart if stuck]')
	while badRowCheck(Table1) != 0:
		Table1 = removeGaps(Table1)
	while badRowCheck(Table2) != 0:
		Table2 = removeGaps(Table2)
	while badRowCheck(Table3) != 0:
		Table3 = removeGaps(Table3)
	while badRowCheck(Table3) != 0:
		Table3 = removeGaps(Table3)
	done()
	#printTables(Table1, Table2, Table3)
	print('Fixing conflicts...')
	for i in range(5):
		#Table1 = fixConflicts(Table1, Table2)
		#Table2 = fixConflicts(Table2, Table1)
		#Table3 = fixConflicts(Table3, Table1)
		#Table3 = fixConflicts(Table3, Table2)
		Table1 = fixconflicts3tables(Table1, Table2, Table3, 1)
		Table2 = fixconflicts3tables(Table1, Table2, Table3, 2)
		Table3 = fixconflicts3tables(Table1, Table2, Table3, 3)
		#printTables(Table1, Table2, Table3)
		while checkDoubleFullTable(Table1) != -1:
			fixDoubleClasses(Table1, Table2)
		while checkDoubleFullTable(Table2) != -1:
			fixDoubleClasses(Table2, Table1)
		while checkDoubleFullTable(Table3) != -1:
			fixDoubleClasses(Table3, Table1)
		while checkDoubleFullTable(Table3) != -1:
			fixDoubleClasses(Table3, Table2)
	done()
	print('Fixing first hours...')
	for i in range(5):
		Table1 = fixTableFHv2(Table1, Table2, Table3, 1)
		Table2 = fixTableFHv2(Table1, Table2, Table3, 2)
		Table3 = fixTableFHv2(Table1, Table2, Table3, 3)
	#printTables(Table1, Table2, Table3)
	while checkHours(Table3) != 0:
		Table3 = fixTableCounts(Table1, Table2, Table3)
		print('Flaw corrected!')
	while checkHours(Table2) != 0:
		Table2 = fixTableCounts(Table3, Table1, Table2)
		print('Flaw corrected!')
	while checkHours(Table1) != 0:
		Table1 = fixTableCounts(Table3, Table2, Table1)
		print('Flaw corrected!')
	done()
	print('Checking for conflicts...')
	if checkConflict(Table1, Table2) == 0 and checkConflict(Table1, Table3) == 0 and checkConflict(Table2, Table3) == 0:
		done()
		printTables(Table1, Table2, Table3)
		createProfTable()
		checkLab(Table1, Table2, Table3)
	else:
		print("Please retry. Error!")
	
def initialize():
	buildTables(Table1, Table2, Table3)

initialize()
