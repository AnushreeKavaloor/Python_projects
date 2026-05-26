import datetime 
import os
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
if os.path.exists("streak.txt"):
	with open("streak.txt","r") as reading:
		lines=(reading.readlines())
		if lines:
			last_line = lines[-1].split(", ")
			last_date =datetime.date.fromisoformat(last_line[0])
			last_streak = int(last_line[1])
			if last_date==today:
				print("Already updated todays streak")
			elif last_date==yesterday:
				with open("streak.txt","a") as add:
					new_streak = last_streak + 1
					add.write(f"{today}, {new_streak}\n")
			else:
				with open("streak.txt","a") as add:
					new_streak = 1
					add.write(f"{today}, {new_streak}\n")
		else:
			with open("streak.txt","a") as add:
				new_streak = 1
				add.write(f"{today}, {new_streak}\n")
		
else:
	with open("streak.txt","a") as append:
		new_streak = 1
		append.write(f"{today}, {new_streak}\n")
