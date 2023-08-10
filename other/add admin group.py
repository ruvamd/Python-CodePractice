def groups_per_user(group_dictionary):
	user_groups = {}
	for group, users in group_dictionary.items():
		for user in users:
			user_groups.setdefault(user, []).append(group)

			# Now add the group to the the list of
			# groups for this user, creating the entry
			# in the dictionary if necessary
			

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],"public":  ["admin", "userB"],"administrator": ["admin"] }))