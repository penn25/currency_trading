class Info():
    def print_data(self,data):
        print "---------- INFO ----------"
        print "bid - highest buy order"
        print "ask - lowest sell order"
        print "low - last 24 hours price low"
        print "high - last 24 hours price high"
        print "last - last BTC price"
        print "volume - last 24 hours volume"
        print "volume30d - last 30 days volume"
        print "--------------------------"
        
        
        print "---------- DATA ----------"
        print "bid = ", data['bid']
        print "ask = ",data['ask']
        print "low = ",data['low']
        print "high = ",data['high'] 
        print "last = ",data['last']
        print "volume = ",data['volume']
        print "volume30d = ",data['volume30d']
        print "--------------------------"
