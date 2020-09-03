from random import randint

lunch=breakfast=dinner=snacks = [40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
70, 71, 72, 73, 74, 75, 76, 77, 78, 79 ]

cal_Count = 250
limit = 1000
best = 250
best_b = best_l = best_s = best_d = 0
found= 0

while limit > 0: # to prevent infinite loop we take the best 
    limit-=1
    random1 = randint(0, 39)
    cal_Count -= breakfast[random1]

    random2 = randint(0,39)
    cal_Count -= lunch[random2]

    random3 = randint(0,39)
    cal_Count -= snacks[random3]

    random4 = randint(0,39)
    cal_Count -= dinner[random4]

    if -1 < cal_Count < 1: #allowed change from requiremet
        found = 1
        print("found")
        break

    if abs(250 - cal_Count) < best:
        best_b = random1
        best_l = random2
        best_s = random3
        best_d = random4
        best = abs(250 - cal_Count)
    
    cal_Count = 250
if found == 1:
    print("calcount is {}".format(250-cal_Count))
    print("lunch {} \nbreakfast {} \nsnacks {} \ndinner {}".format(random1,random2,random3,random4))
else:
    print("calcount is {}".format(best))
    print("lunch {} \nbreakfast {} \nsnacks {} \ndinner {} ".format(best_b,best_l,best_s,best_d))
