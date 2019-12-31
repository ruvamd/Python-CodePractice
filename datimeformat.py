from datetime import datetime
def main():
  now=datetime.now()
  print(now.strftime('%a,%d %B,%y'))
  #print(now.strftime('locale date and time:%c'))
  #print(now.strftime('locale date: %x'))
  #print(now.strftime('locale date: %X'))
main()
