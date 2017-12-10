from datetime import date

class Checker():

    def __init__(self,dtc,query,db,cex_user,cex_key,cex_secret,currency):
        self.query = query 
        self.db = db 
        self.cursor = db.cursor() 
        self.cex_user = cex_user
        self.cex_key = cex_key
        self.cex_secret = cex_secret
        self.currency = currency
        self.dtc = dtc

    def execute_check_data(self):
        today = date.today()        
        #sql_string = "SELECT AVG(last) FROM ticker date_created >= DATEADD(day,-"+self.dtc+", GETDATE())"
        #data = self.query.query_fetch_one(sql_string)
        print 'AVERAGE: '
        #print 'AVERAGE: ',data 
