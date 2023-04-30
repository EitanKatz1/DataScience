
def convert2sec(x, y):
    y.lower()
    if y == 'min' :
         time = x*60
    elif y == 'hours':
        time = x*60*60
    elif y == 'days':
        time = x*24*60*60
    print(time,"Seconds")


convert2sec(23,'hours')
