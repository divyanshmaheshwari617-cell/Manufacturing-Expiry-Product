import datetime
class Product:
    def __init__(self,manf_year,manf_month,manf_date,exp_year,exp_month,exp_date):
        self.manf_date=datetime.date(manf_year,manf_month,manf_date)
        self.exp_date=datetime.date(exp_year,exp_month,exp_date)
    def __str__(self):
        return f"MANUFACTURING DATE:{self.manf_date} and EXPIRY DATE:{self.exp_date}"
    def get_time(self):
        now=datetime.date.today()
        if self.exp_date<now:
            return "The product has expired."
        else:
            difference=self.exp_date-now
            years=difference.days//365
            remaining_days=difference.days%365
            months=remaining_days//30
            days=remaining_days%30
            return f"THE PRODUCT EXPIRE IN {years} YEARS,{months}MONTHS AND {days}DAYS"
obj=Product(2022,1,15,2027,12,31)
print(obj)
print(obj.get_time())
