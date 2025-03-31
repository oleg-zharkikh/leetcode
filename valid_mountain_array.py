def valid_mountain_array(array):
    if len(array) < 3:
        return False
    i = 1
    prev_item = int(array[0])
    up_trend = False
    down_trend = False
    while i <= len(array)-1:
        if int(array[i]) > prev_item:
            up_trend = True
            if down_trend:  # если уже был спуск, то гора неправильная
                return False
        elif int(array[i]) < prev_item:
            down_trend = True
            if not up_trend:
                return False
        elif int(array[i]) == prev_item:
            return False
        prev_item = int(array[i])
        i += 1
    return up_trend and down_trend
       

in_array = input().split()
print(valid_mountain_array(in_array))