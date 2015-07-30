
import re, urllib

#If we want to use myurl (the real link) then we will have to append the pre string to get the real url
myurl = "https://en.wikipedia.org/wiki/List_of_high_schools_in_Virginia"
#mylocal was created in MSWord by copy pasting the desired links
mylocal = "file:///Users/bdcoe/Desktop/school_links.htm"

for i in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(mylocal).read(), re.I):
        #pre="http://en.wikipedia.org"
	#fullurl = pre + i;
	#print fullurl  
        print "#Opening:\t" + i
	try:
		for gg in re.findall('\d\d\d\d\d',re.findall('postal-code">\d\d\d\d\d', urllib.urlopen(i).read(), re.I)[0]):
			print gg

	#	for ee in re.findall('\d\d\d\d\d', urllib.urlopen(i).read(), re.I):
        #	        print ee
	except:
		print "lun ho gaya"
