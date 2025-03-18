numbers = [3,5,6]
doubled = [num * 2 for num in numbers]

print(doubled)

friends = ["Rolf", "Subroto", "Shreya", "Shubham", "Robin"]
starts_s = [friend for friend in friends if friend.startswith("R")]

# for friend in friends:
#     if friend.startswith("S"):
#         starts_s.append(friend)

print(starts_s)