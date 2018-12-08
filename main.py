def list_infomation(file):
    """The function extracts from the file all the
    necessary information about the students to build."""
    with open(file, "r") as file:
        text = file.readlines()
        list_info = []
        for note in text:
            list_info.append(note.split())
    return list_info


def sort_list(text, column, order):
    """The function compiles a list based on information
    or 'text' and sorts it based on the parameters 'column' and 'row'."""
    name = []
    for word in text:
        word[3], word[4] = int(word[3]), int(word[4])
        add = word[column]
        word.remove(word[column])
        word.insert(0, add)
        name.append(word)
    name.sort()
    list_name_new = []
    for lists in name:
        add = lists[0]
        lists.remove(lists[0])
        lists.insert(column, add)
        list_name_new.append(lists)
    if order == "<":
        list_name_new.reverse()
        for post in list_name_new:
            print("{:12} {:13} {:12} {:>5} {:13}".format(
                post[0], post[1], post[2],
                post[3], post[4]))
            print('-' * 62)
    elif order in ">, none":
        for post in list_name_new:
            print("{:12} {:13} {:12} {:>5} {:13}".format(
                post[0], post[1], post[2],
                post[3], post[4]))
            print('-' * 62)


def condition_constructor():
    """The function constructs necessary and sufficient conditions for
    the correct sorting of list data."""
    condition = input("Sort the list (name, surname, group, points, year): ")
    while condition != "name" and condition != "surname" and condition != "group"\
            and condition != "points" and condition != "year" or condition == "":
        condition = input("No! name, surname, group, points, year: ")

    if condition == "group" or condition == "points" or condition == "year":
        communication = input("Ascending or descending order ( > or < ): ")
        while communication not in "<>" or communication == "":
            communication = input("No! > or < : ")
    print("\n{:14} {:11} {:9} {:15} {:10}".format("Фамилия", "Имя", "Группа",
                                                  "Текущие быллы", "Год рожд."))
    print('-' * 62)
    info = list_infomation("input.txt")

    if condition == "name":
        sort_list(info, 1, "none")
    if condition == "surname":
        sort_list(info, 0, "none")
    if condition == "group":
        sort_list(info, 2, communication)
    if condition == "points":
        sort_list(info, 3, communication)
    if condition == "year":
        sort_list(info, 4, communication)
    print()


def main():
    """The main function that leads the functions for the program."""
    while True:
        condition_constructor()
        ques = input("Build another table? (go or stop)\n")
        while ques != "go" and ques != "stop" or ques == "":
            ques = input("No! go or stop:")
        if ques == "go":
            continue
        if ques == "stop":
            print("Goodbye!")
            break


if __name__ == '__main__':
    main()
