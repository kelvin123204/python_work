unconfirmed_users = ["alice", "brian", "candase"]
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user :" + current_user.title())
    confirmed_users.append(current_user.title())
print("\nThe following user have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user)
