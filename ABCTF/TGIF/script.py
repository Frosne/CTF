import datetime
from datetime import datetime
from datetime import date, timedelta

def main():
	f = open('date.txt','r')
	text = f.read().split('\n')
	text = text[0:len(text)]
	text = map(lambda x :datetime.strptime(x, "%B %d, %Y"), text)
	today = date.today()
	today = datetime(int(getattr(today,'year')),int(getattr(today,'month')),int(getattr(today,'day')),0,0,0)	
	sumyear = 0
	frdy = 0;
	for el in text:
		newYear = newDate(el)
		if (newYear < today):
			delta = today - newYear-timedelta(days = 3)
			num = delta.days /7
			sumyear = sumyear + num
		if (newYear.isoweekday()==5):
			frdy = frdy+1
	print(frdy)

	
	
			
		
		
def Vis(date):
	if ((int(getattr(date,'year')))%4 ==0):
		return 1
	else:
		return 0

def newDate(date):
	y = int(getattr(date,'year'))
	m = int(getattr(date,'month'))
	d = int(getattr(date,'day'))
	y = y+1
	try:
		date =  datetime(y,m,d,0,0,0)
	except:
		date = datetime(y,3,1,0,0,0)
		
	return date

main()
	
