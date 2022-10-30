def get_season(month_number):
    winter = [12, 1, 2, "12", "1", "2"]
    spring = [3, 4, 5, "3", "4", "5"]
    summer = [6, 7, 8, "6", "7", "8"]
    fall = [9, 10, 11, "9", "10", "11"]

    if month_number in winter:
        return "Winter"
    elif month_number in spring:
        return "Spring"
    elif month_number in summer:
        return "Summer"
    elif month_number in fall:
        return "Fall"
    else:
        return "Your month number does not belong to any season or is not a number!"
