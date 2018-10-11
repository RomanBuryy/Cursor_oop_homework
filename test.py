some_list = [('Roman', 2, 'Python'), ('Igor', 12, 'Java'), ('Ira', 4, 'Ruby'), ('Roman', 3, 'Python')]

sec_list  = sorted(some_list, key=lambda x: x[1])


def some_print(slist):
    new_list = []
    for i in sec_list:
        new_list.append(f"{i[0]} - {i[1]} years, {i[2]}")

    return new_list



def fired_empl(key_name):
    for i in some_list:
        if i[0] == key_name:
            some_list.remove(i)
            break
        else:
            if i[0] != key_name:
                print("an employee with such name not found!")
                break









#print(some_print(sec_list))

print(some_list)
print(fired_empl("Roman"))
print(some_list)



