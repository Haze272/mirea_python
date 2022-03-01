def generate_groups():
    all_groups = []

    ivbo = []
    for i in range(1, 10):
        if i == 9:
            ivbo.append("ИВБО-" + "13" + "-20")
            continue
        if i < 10:
            ivbo.append("ИВБО-0" + str(i) + "-20")
    all_groups.append(ivbo)

    ikbo = []
    for i in range(1, 29):
        if i == 28:
            ikbo.append("ИКБО-" + "30" + "-20")
            continue
        if i < 10:
            ikbo.append("ИКБО-0" + str(i) + "-20")
        else:
            ikbo.append("ИКБО-" + str(i) + "-20")
    all_groups.append(ikbo)

    inbo = []
    for i in range(1, 14):
        if i == 12:
            inbo.append("ИНБО-" + "13" + "-20")
            continue
        if i == 13:
            inbo.append("ИНБО-" + "15" + "-20")
            continue
        if i < 10:
            inbo.append("ИНБО-0" + str(i) + "-20")
        else:
            inbo.append("ИНБО-" + str(i) + "-20")
    all_groups.append(inbo)

    imbo = []
    for i in range(1, 3):
        if i < 10:
            imbo.append("ИМБО-0" + str(i) + "-20")
    all_groups.append(imbo)


    for elem in range(len(all_groups)):
        print(all_groups[elem])


generate_groups()