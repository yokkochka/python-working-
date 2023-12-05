
year = 0
days = 0
hours = 0
mines = 0
seconds = 0

vvod = int(input('введите'))
def perevod(sec):
    global year, days, hours, mines, seconds
    ostatok = sec
    if ostatok != 0:
        years = ostatok // 31536000
        ostatok -= (31536000 * years)
        days = ostatok // 86400
        ostatok -= (86400 * days)
        hours = ostatok // 3600
        ostatok -= (3600 * hours)
        mines = ostatok // 60
        ostatok -= (60 * mines)
        seconds = ostatok            
        
    else:
        print('now')


perevod(vvod)
