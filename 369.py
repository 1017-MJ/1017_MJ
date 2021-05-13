for i in range(1, 101):
        str_i = str(i)
        count_str = 0
        for j in str_i:
            if (j =='3') or (j =='6') or (j =='9'):
                count_str = count_str+1
        if count_str == 0:
            print(str_i+':', i)
        else:
            print(str_i+':', count_str * '짝')