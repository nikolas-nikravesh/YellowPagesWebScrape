import ypData

info = ypData.get_yp_data('tacos', 'Albany', 'CA', '1')

for item in info:
   print item
   print
