import datetime
import random
print(f"Today is: {datetime.date.today()}\n")
print(f"Day is: {datetime.date.today().strftime('%A')}\n")
print(f"Time is: {datetime.datetime.now().time()}\n")
quotes =[ "Code is like humor. When you have to explain it, it’s bad.- Cory House", "First, solve the problem. Then, write the code. - John Johnson", "Experience is the name everyone gives to their mistakes.- Oscar Wilde"]

choose_quote = random.choice(quotes)
print("The quote chose is:")
print(f"{choose_quote}\n")

with open("quotes_log.txt","a") as quotes_log:
	quotes_log.write(f"{choose_quote}\n")
	print("Quote saved to quotes_log.txt\n")
print("Quotes saved in quotes_log.txt are below: \n")
with open("quotes_log.txt","r") as quote:
	print(f"{quote.read()}")
