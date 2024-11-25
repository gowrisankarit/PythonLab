def sort_dictionary(d, by='key', ascending=True):
    
    if by == 'key':
        sorted_items = sorted(d.items(), reverse=not ascending)
    elif by == 'value':
        sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=not ascending)
    return dict(sorted_items)

n = int(input("Enter the number of items in the dictionary: "))
user_dict = {}
for _ in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    user_dict[key] = value 


print("Original Dictionary:", user_dict)
print("Sorted by key in ascending", sort_dictionary(user_dict, by='key', ascending=True))
print("Sorted by key in descending:", sort_dictionary(user_dict, by='key', ascending=False))
print("Sorted by valuesin ascending:", sort_dictionary(user_dict, by='value', ascending=True))
print("Sorted by values descending:", sort_dictionary(user_dict, by='value', ascending=False))
		
			
