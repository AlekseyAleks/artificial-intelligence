users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}

user1 = users.get("+55555555")
print(user1)  # Alice
user2 = users.get("+33333333", "Unknown user")
print(user2)  # Bob
user3 = users.get("+44444444", "Unknown user")
print(user3)  # Unknown user