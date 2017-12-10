import data_info
import cexapi

#CLASS TO PRINT INFO
class Ticker():

    def __init__(self,query,cex_user,cex_key,cex_secret,currency):
        self.info_class = data_info.Info()
        self.query = query 
        self.cex_user = cex_user
        self.cex_key = cex_key
        self.cex_secret = cex_secret
        self.currency = currency

    def get_data(self):
        try:
            api_info = cexapi.API(self.cex_user, self.cex_key, self.cex_secret)
            data = api_info.ticker(self.currency)
            return data
        except:
            print "Request Timeout!"
            return 0

    def save_data(self,data):
        # PRINT INFO
        self.info_class.print_data(data)

        # COLUMNS
        column = "`timestamp`,"
        column += "`low`,"
        column += "`high`,"
        column += "`last`,"
        column += "`volume`,"
        column += "`volume30d`,"
        column += "`bid`,"
        column += "`ask`"
       
        # VALUES
        value = "'" + str(data['timestamp']) + "',"
        value += "'" + str(data['low']) + "',"
        value += "'" + str(data['high']) + "',"
        value += "'" + str(data['last']) + "',"
        value += "'" + str(data['volume']) + "',"
        value += "'" + str(data['volume30d']) + "',"
        value += "'" + str(data['bid']) + "',"
        value += "'" + str(data['ask']) + "'"

        # CREATE ENTRY
        sql_string = "INSERT INTO ticker ("
        sql_string += column
        sql_string += ") VALUES ("
        sql_string += value
        sql_string += ")"
        
        self.query.query_commit(sql_string)
        #print sql_string

    def execute_insert(self):
        data = self.get_data() 
        if data:
            self.save_data(data)
