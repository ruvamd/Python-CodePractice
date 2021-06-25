class router(object):
    def __init__(self,name,interface_number,vendor):
        self.name=name
        self.interface_number=interface_number
        self.vendor=vendor
r1=router('sfo1-r1',64,'cisco')

print(r1.name,r1.interface_number,r1.vendor,sep='\n')
# print(r1.interface_number)
# print(r1.vendor)