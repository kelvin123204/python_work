current_users = ["Tom","Eric","Tim","Sam","Mary","Sammy"]
#lower_current_users = current_users[:]
#x=0
#for lower_current_user in lower_current_users:
#	lower_current_users[x]=lower_current_user.lower()
#	x=x+1
#A better way to replace the codes upper is list comprehension
lower_current_users=[current_user.lower() for current_user in current_users]
new_users = ["Eli","Nick","TOM","Tommy","eric"]
for new_user in new_users:
	if new_user.lower() in lower_current_users:
		print(new_user + " has been used.")
	else:
		print(new_user + " is avaliable.")