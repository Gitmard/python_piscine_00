def ft_water_reminder():
    time_last_watering = int(input("Days since last watering: "))
    if (time_last_watering > 2):
        print("Water the plant !")
    else:
        print("Plants are fine")
