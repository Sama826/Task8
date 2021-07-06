#!/usr/bin/python3

print("content-type: text/html")
print()

import cgi
import os
import subprocess as sp

f=cgi.FieldStorage()
cmd = f.getvalue("x")
	

if cmd == "MH 20 EE 0948":
	print('''<pre>
	Car Number: MH 20 EE 0948
	Car Model: skoda	
	Registration Name: abc
	Registration Date: X/X/20XX
	Fuel Type: CNG
	Location: Maharashtra, India
	Vehicle Class: SUV
	Insurance Upto: XX/XX/20XX
	</pre>''')
elif cmd == "KA 01 MS 2658":
	print('''<pre>
	Car Number: KA 01 MS 2658
	Car Model: BMW	
	Registration Name: xyz
	Registration Date:XX/X/20XX
	Fuel Type: CNG
	Location: Karnataka, India
	Vehicle Class: SUV
	Insurance Upto: 19/12/2026
	</pre>''')

elif cmd == "LR33 TEE":
	print('''<pre>
	Car Number:LR33 TEE 
	Car Model: Swift	
	Registration Name: abc
	Registration Date: XX/X/20XX
	Fuel Type: CNG
	Location: Out of India
	Vehicle Class: SUV
	Insurance Upto: xx/x/20xx
	</pre>''')
else:
print("Information not available")


