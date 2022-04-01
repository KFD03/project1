# barmicva kalkulacka

from pyluach import dates, parshios, hebrewcal, gematria, utils

#translations to czech
parasa_cesky = {
    'Bereishis':'Berešit', 
    'Noach':'Noach', 
    'Lech Lecha':'Lech Lecha', 
    'Vayeira':'Vajera', 
    'Chayei Sarah':'Chajej Sara', 
    'Toldos':'Toldot',
    'Vayeitzei':'Vajece', 
    'Vayishlach':'Vajišlach', 
    'Vayeishev':'Vaješev', 
    'Mikeitz':'Mikec', 
    'Vayigash':'Vajigaš', 
    'Vayechi':'Vajechi',
    'Shemos':'Šemot', 
    "Va'eira":"Va'era", 
    'Bo':'Bo', 
    'Beshalach':'Bešalach', 
    'Yisro':'Yitro', 
    'Mishpatim':'Mišpatim', 
    'Terumah':'Teruma',
    'Tetzaveh':'Tecave', 
    'Ki Sisa':'Ki Tisa', 
    'Vayakhel':'Vajakhel', 
    'Pekudei':'Pekudej', 
    'Vayikra':'Vajikra', 
    'Tzav':'Cav', 
    'Shemini':'Šemini',
    'Tazria':'Tazria', 
    'Metzora':'Mecora', 
    'Acharei Mos':'Acharej Mot', 
    'Kedoshim':'Kedošim', 
    'Emor':'Emor', 
    'Behar':'Behar',
    'Bechukosai':'Bechukotaj', 
    'Bamidbar':'Bamidbar', 
    'Nasso':'Naso', 
    "Beha'aloscha":"Beha'alotecha", 
    'Shelach':'Šlach', 
    'Korach':'Korach',
    'Chukas':'Chukat', 
    'Balak':'Balak', 
    'Pinchas':'Pinchas', 
    'Mattos':'Matot', 
    'Masei':'Masej', 
    'Devarim':'Devarim', 
    "Va'eschanan":"Va'etchanan",
    'Eikev':'Ekev', 
    "Re'eh":"Re'e", 
    'Shoftim':'Šoftim', 
    'Ki Seitzei':'Ki Tece', 
    'Ki Savo':'Ki Tavo', 
    'Nitzavim':'Nicavim',
    'Vayeilech':'Vajelech', 
    'Haazinu':'Haazinu', 
    'Vezos Haberachah':'Vezot Habracha',
    'Vayakhel, Pekudei':'Vajakhel-Pekudej', 
    'Tazria, Metzora':'Tazria-Mecora', 
    'Acharei Mos, Kedoshim':'Acharej Mot-Kedošim', 
    'Behar, Bechukosai':'Behar-Bechukotaj',
    'Chukas, Balak':'Chukat-Balak', 
    'Mattos, Masei':'Matot-Masej', 
    'Nitzavim, Vayeilech':'Nicavim-Vajelech' 
}

mesic_cesky={
    'Nissan':'Nisan', 
    'Iyar':'Iyar', 
    'Sivan':'Sivan', 
    'Tammuz':'Tamuz', 
    'Av':'Av', 
    'Elul':'Elul', 
    'Tishrei':'Tišri', 
    'Cheshvan':'Chešvan',
    'Kislev':'Kislev', 
    'Teves':'Tevet', 
    'Shevat':'Švat', 
    'Adar':'Adar', 
    'Adar 1':'Adar 1', 
    'Adar 2':'Adar 2'
}

svatek_cesky={
     'Rosh Hashana':'Roš Hašana', 
     'Yom Kippur':'Jom Kipur', 
     'Succos':'Sukot', 
     'Shmini Atzeres':'Šmini Aceret', 
     'Simchas Torah':'Simchat Tora',
    'Chanuka':'Chanuka', 
    "Tu B'shvat":"Tu Bišvat", 
    'Purim Katan':'Purim Katan', 
    'Purim':'Purim', 
    'Shushan Purim':'Šušan Purim',
    'Pesach':'Pesach', 
    'Pesach Sheni':'Pesach šeni', 
    "Lag Ba'omer":"Lag Ba'omer", 
    'Shavuos':'Šavuot', 
    "Tu B'av":"Tu B'av"
}

pust_cesky={
    'Tzom Gedalia':'Com Gedalja', 
    '10 of Teves':'10. Tevet', 
    'Taanis Esther':'Taanit Esther', 
    '17 of Tamuz':'17. Tamuz', 
    '9 of Av':'9. Av'
}

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
            reading=self.date.holiday()
            return (svatek_cesky.get(reading))
        else:
            return (parasa_cesky.get(cteni))
"""
barmicva=Bmicva(1999,4,3,False, False)
barmicva.to_hebcal()
barmicva.bmicva_date()
print (barmicva.printing())
print (barmicva.bmicva())
print (barmicva.parasha())
"""