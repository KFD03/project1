# barmicva kalkulacka

from pyluach import dates, parshios, hebrewcal

"""count of the bar/bat mitzvah date, Shabbat followingthe date and the corresponding parasha using pyluach"""
class Bmicva:
    #year, month and day of birth of the person
    def __init__(self, year, month, day, sex, sunset):
        self.year=year
        self.month=month
        self.day=day
        self.sex=sex #boy==False, girl==True
        self.sunset=sunset

    #conversion of the day of birth to hebrew calendar
    def to_hebcal(self):
        if self.sunset==False:
            dategreg=dates.GregorianDate(self.year, self.month, self.day)
            self.dateheb=dategreg.to_heb()
        else:
            dategreg=dates.GregorianDate(self.year, self.month, self.day)
            self.dateheb=(dategreg+1).to_heb()

    
    #hebrew date of birth + 12 years (girls) or + 13 years (boys)    
    def bmicva_date(self):
        
        y,m,d=self.dateheb.tuple()
        
        if self.sex==False:             #boy

            leapyear=hebrewcal.Year(y+13)                           #check if the year of bar mitzvah is leap
            leapyear=leapyear.leap
            if leapyear==True and m==13:                        #born on Adar II and barmitzvah on Adar II                        
                self.date=dates.HebrewDate(y+13, 13, d)
            elif leapyear==True and m==12:                     #born on Adar and barmitzvah on Adar II
                self.date=dates.HebrewDate(y+13, 13, d)
            elif leapyear==False and m==13:
                self.date=dates.HebrewDate(y+13, 12, d)         #born on Adar II and barmitzvah on Adar
            else:
                self.date=dates.HebrewDate(y+13,m,d)         #born on any other date

            
        else:
            leapyear=hebrewcal.Year(y+12)                           #check if the year of bat mitzvah is leap
            leapyear=leapyear.leap
            if leapyear==True and m==13:                        #born on Adar II and batmitzvah on Adar II                        
                self.date=dates.HebrewDate(y+12, 13, d)
            elif leapyear==True and m==12:                     #born on Adar and batmitzvah on Adar II
                self.date=dates.HebrewDate(y+12, 13, d)
            elif leapyear==False and m==13:
                self.date=dates.HebrewDate(y+12, 12, d)         #born on Adar II and batmitzvah on Adar
            else:
                self.date=dates.HebrewDate(y+12,m,d)         #born on any other date
        
    #print date
    def printing(self):
        return self.date.to_greg().to_pydate().strftime("%d/%m/%Y")
        
    #shabbat following the bar/bat mitzvah
    def bmicva(self):
        return self.date.shabbos().to_greg().to_pydate().strftime("%d/%m/%Y")
        

    #parasha in english
    def parasha(self):
        cteni=parshios.getparsha_string(self.date)
        if cteni==None:
            return self.date.holiday()
        else:
            return (cteni)
"""
barmicva=Bmicva(1999,4,3,False, False)
barmicva.to_hebcal()
barmicva.bmicva_date()
print (barmicva.printing())
print (barmicva.bmicva())
print (barmicva.parasha())
"""