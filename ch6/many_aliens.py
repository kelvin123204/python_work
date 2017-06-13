aliens = []
alien = {"color": "green", "score": "5"}
for number_of_aliens in range(30):
    aliens.append(alien)
for alien in aliens[:5]:
    print(alien)
print("...")
print("Number of aliens :" + str(len(aliens)))
print(number_of_aliens)
