import pygeoip

gip= pygeoip.Geoip("GeoliteCity.dat")
res= gip.record_by_addr(' ')
for key, val in res.items():
    print('%s : %s'%(key,val))
    