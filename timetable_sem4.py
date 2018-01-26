#!/usr/bin/python

import random
import numpy
import math

subjects  = ['CO','DS','DMS','ADE','USP','M3']
subjects1 = ['CO','DS','DMS','ADE','USP','M3']
subjects2 = ['CO','DS','DMS','ADE','USP','M3']
subjects3 = ['CO','DS','DMS','ADE','USP','M3']
#subjects1 = []
#subjects2 = []
#subjects = []
teachers = ['T1','T2','T3','T4','T5','T6']
labs = ['L1','L2']
hours = [4,4,4,4,4,4]
lab_duration = 3
classes_per_day = 1
c, r = 7, 6
half_days = [3,1]

Table1 = [[0 for x in range(c)] for y in range(r)]
Table2 = [[0 for x in range(c)] for y in range(r)]
Table3 = [[0 for x in range(c)] for y in range(r)]

def markD4():
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
	while day != 6:
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
	lab_hour = [0,c-3]
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
		if Table[row].count(0) > 0 and ('L1' == Table[row][5] or 'L2' == Table[row][5] or 'L3' == Table[row][5]):
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
		if Table1[row].count(0) > 0 and Table1[row][5] not in labs and row !=3 and row !=1:
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
				
def removeGaps(Table1, Table2):
	TEMP = Table1
	for row in range(r):
		#print(TEMP[row])
		if 0 in TEMP[row] and TEMP[row].index(0) < 5:
			bad_row = row
			bad_col = TEMP[row].index(0)
			track_col = c-1
			track_row = 0
			while True:
				if track_col == 0:
					track_col = c-1
				if track_row == r:
					track_row = 0
					track_col -= 1
				#print('trackrow : ',track_row,'trackcol : ',track_col)
				if TEMP[track_row][track_col] not in labs and TEMP[track_row][track_col] != 0 and TEMP[track_row][track_col] != 'X':
					#SWAP
					TEMP[bad_row][bad_col] = TEMP[track_row][track_col]
					TEMP[track_row][track_col] = 0
					if checkConflict(TEMP, Table2) == 0:
						Table1 = TEMP
						#print("MOVE SUCCESSFUL")
						#printTables(Table1, Table2)
						break
					else:
						#print("MOVE NOT PERMITTED. SKIPPING")
						break
				track_row += 1
			#track_col -= 1
			#print(bad_row,bad_col)
	return Table1

def badRowCheck(Table1):
	for row in range(r):
			if 0 in Table1[row] and Table1[row].index(0) < 5:
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
def printTeacherTable(sub):
	TEACHER = [[0 for x in range(c)] for y in range(r)]
	for row in range(r):
		for col in range(c):
			if Table1[row][col] == sub:
				TEACHER[row][col] = sub + '-A'
			if Table2[row][col] == sub:
				TEACHER[row][col] = sub + '-B'
			if Table3[row][col] == sub:
				TEACHER[row][col] = sub + '-C'
	return TEACHER
		
def buildTables(Table1, Table2, Table3):
	markD4()
	firstHour()
	placeLabs()	
	distributeClasses()
	distributeClasses3()
	Table1 = fixLabRows(Table1, Table2, findFaultyLabRows(Table1))
	Table2 = fixLabRows(Table2, Table1, findFaultyLabRows(Table2))
	Table3 = fixLabRows(Table3, Table1, findFaultyLabRows(Table3))
	Table3 = fixLabRows(Table3, Table2, findFaultyLabRows(Table3))
	Table1 = fixFaultyRows(Table1, Table2)
	Table2 = fixFaultyRows(Table2, Table1)
	Table3 = fixFaultyRows(Table3, Table2)
	Table3 = fixFaultyRows(Table3, Table1)
	#printTables(Table1, Table2)
	#printTables(Table1, Table2)
	for i in range(1):
		while badRowCheck(Table1) != 0:
			Table1 = removeGaps(Table1, Table2)
		while badRowCheck(Table2) != 0:	
			Table2 = removeGaps(Table2, Table1)
		while badRowCheck(Table3) != 0:	
			Table3 = removeGaps(Table3, Table1)
		while badRowCheck(Table3) != 0:	
			Table3 = removeGaps(Table3, Table2)
		for i in range(5):
			Table1 = fixConflicts(Table1, Table2)
			Table2 = fixConflicts(Table2, Table1)
			Table3 = fixConflicts(Table3, Table1)
			Table3 = fixConflicts(Table3, Table2)
			while checkDoubleFullTable(Table1) != -1:
				fixDoubleClasses(Table1, Table2)
			while checkDoubleFullTable(Table2) != -1:
				fixDoubleClasses(Table2, Table1)
			while checkDoubleFullTable(Table3) != -1:
				fixDoubleClasses(Table3, Table1)
			while checkDoubleFullTable(Table3) != -1:
				fixDoubleClasses(Table3, Table2)
	if checkConflict(Table1, Table2) == 0 and checkConflict(Table1, Table3) == 0 and checkConflict(Table2, Table3) == 0:
		printTables(Table1, Table2, Table3)
		print(numpy.matrix(printTeacherTable(str('DMS'))))
	else:
		print("Please retry. Error!")
	
buildTables(Table1, Table2, Table3)

