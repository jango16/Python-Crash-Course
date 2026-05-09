current_users = ["Alpha_one", "byte_ninjA",
                 "signal_pro", "debug_king", "root_user"]
new_users = ["alpha_one", "byte_ninja",
             "data_wizard", "logic_builder", "net_hacker"]
current_users_lower = [user.lower() for user in current_users]

for users in new_users:
    if users in current_users_lower:
        print(f"Hi {users}, this username has been taken.")
    else:
        print(f"Hi {users}, this username is available.")
