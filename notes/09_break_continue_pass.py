# loop control statements - changes loop execution from its normal sequence

# break         =   terminate loop entirely
# continue      =   skip to next iteration of the loop
# pass          =   does nothing (placeholder)

for i in range(0,10):
    if i == 2:
        continue    # skip number 2 and go to the next loop
    if i == 4:
        pass        # does nothing
    if i == 6:
        break       # stop the loop completely
    print(i)
    