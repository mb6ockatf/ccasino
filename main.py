from datetime import datetime
from sys import exit
from random import randint
from json import load, dump

	
won, lost, length = 0, 0, 0
print("casino game\n\
For register press nn\n\
For login, press y\n\
Otherwise, press n")
login_decision = input("y/n/nn: ")
user = input("Account name: ")
if login_decision == "y":
	with open(user + ".json") as account:
		data = load(account)
		data["all_log-ins"] += 1
		show_data = input("\nShow your data? (y/n): ")
		if show_data == "y":
			print(*data)
	if input("Start (y/n): ") != "y":
		exit()
elif login_decision == "nn":
	start_time = datetime.now()
	created_file_name = user + ".json"
	with open(created_file_name, "x") as account:
		contents = {"name": user, "all_log-ins": 1, "longest_game": "0",
					"most_wins": 0, "most_lost": 0, "best_game": "0",
					"worst_game": "0", "rating": 0,}
		dump(contents, account, ensure_ascii=False)
	print(f"Data stored in {created_file_name}\n\
Created in {start_time - datetime.now()} seconds")
	decision_after_registering = int(
		input("Print 1 to play, otherwise 0: "))
	if decision_after_registering == 0:
		exit()
print("\nYou're playing casino. You can choose: \n\
- 1 to 18 or 19 to 36\n\
- odd or not odd\n\
- red or black\n\
- any number from 1 to 36, 0 and 00\n\
- print ! to quit\n")
choice = input("Your choice: ")
while choice != "!":
	print(f'This is {length + 1} turn')
	if choice in ("red", "black"):
		ans = ["red", "black"][randint(0, 1)]
	elif choice in ("odd", "not odd"):
		ans = ["odd", "not odd"][randint(0, 1)]
	elif choice in ("1 to 18", "19 to 36"):
		ans = ["1 to 18", "19 to 36"][randint(0, 1)]
	elif choice == "!":
		exit()
	else:
		if 0 <= int(choice) <= 36 or int(choice) == 00:
			ans = ([str(j) for j in range(0, 37)] + ["00"])[randint(0, 37)]
	print(ans, 'won')
	length += 1
	if ans != choice:
		print("Your choice is wrong")
		lost += 1
	else:
		print("Your choice is right")
		won += 1
	print(f"Won: {won}\nLost: {lost}")
	choice = input("Your choice: ")
with open(user + ".json") as fh:
	data = load(fh)
	if data["most_wins"] < won:
		data["most_wins"] = won
	if data["most_lost"] < lost:
		data["most_lost"] = lost
	if int(data["longest_game"]) < length:
		data["longest_game"] = length
	if int(data['longest_game']) != 1:
		if float(data["best_game"]) < won / (lost if lost != 0 else 1):
			data["best_game"] = won / (lost if lost != 0 else 1)
			print("You have a record: it was your luckiest game ever\nCongratulations!")
		elif float(data["worst_game"]) < lost / (won if won != 0 else 1):
			data["worst_game"] = lost / (won if won != 0 else 1)
			print("You have a record: it was your unluckiest game ever\nBetter luck next time")
	data["rating"] = (data["most_wins"] - data["most_lost"]) / data["all_log-ins"]
with open(user + ".json", "w") as f:
	dump(data, f)
print("Bye")
exit()
