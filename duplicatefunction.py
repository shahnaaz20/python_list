def unique(main_list):
    main_list = [1,2,2,3,3,4]
    index = 0
    list1 = []
    while index < len(main_list):
        if main_list[index]  not in list1:
            list1.append(main_list[index])
        index = index + 1
    return(list1)
print(unique([1,2,3,3,4,4]))
