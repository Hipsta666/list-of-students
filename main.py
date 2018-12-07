

def list_infomation(file):
    with open(file, "r") as file:
        text = file.readlines()
        list_info = []
        for note in text:
            list_info.append(note.split())
    return list_info


def sort_list(func, x):
    name = []
    for word in func:
        word[3], word[4] = int(word[3]), int(word[4])
        add = word[x + 1]
        word.remove(word[x + 1])
        word.insert(0, add)
        name.append(word)
    name.sort()
    list_name_new = []
    for lists_ in name:
        add = lists_[0]
        lists_.remove(lists_[0])
        lists_.insert(x + 1, add)
        list_name_new.append(lists_)
        print("{:12} {:13} {:10} {:>5} {:^10}".format(
            lists_[0], lists_[1], lists_[2],
            lists_[3], lists_[4]))


def main():
    condition = input()
    while condition not in "name, last name, group, points, year":
        print("no!")
        condition = input()
    else:
        info = list_infomation("input.txt")
        if condition == "name":
                sort_list(info, 0)
        if condition == "last name":
                sort_list(info, -1)
        if condition == "group":
                sort_list(info, 1)
        if condition == "points":
                sort_list(info, 2)
        if condition == "year":
                sort_list(info, 3)


if __name__ == '__main__':
    main()
