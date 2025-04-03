Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ########## AND OPERATORS ######
>>> if 1>2 and 1<2:
	print("TRUE!!!!!!!!!")
else:
	print("FALSE!!!!!!!!")

	
FALSE!!!!!!!!
>>> if 1>2 and 1>2:
	print("TRUE!!!!!!!!")
else:
	print("FALSE!!!!!!!")

	
FALSE!!!!!!!
>>> if 1<2 and 1<2:
	print("TRUE!!!!!!!!")
else:
	print("FALSE!!!!!!!")

	
TRUE!!!!!!!!
>>> ############## OR OPERATOR #######
>>> if 1>2 or 1<2:
	print("TRUE!!!!!!")
else:
	print("FALSE!!!!!")

	
TRUE!!!!!!
>>> if 1>2 or 1>2:
	print("TRUE!!!!!!!!")
else:
	print("FALSE!!!!!!!")

	
FALSE!!!!!!!
>>> if 1==1 or 2==2:
	print("TRUE!!!!!!!!")
else:
	print("FALSE!!!!!!!")

	
TRUE!!!!!!!!
>>> ######## NOT OPERTAOR ###########
>>> if 1==1 not 2==2:
	print("TRUE!!!!!!!!")
else:
	print("FALSE!!!!!!!")
	
SyntaxError: invalid syntax
>>> if 1>1 not 2>2:
	print("TRUE!!!!!!!!")
else:
	print("FALSE!!!!!!!")
	
SyntaxError: invalid syntax
>>> if 1 not 2:
	print("TRUE!!!!!!!!")
else:
	print("FALSE!!!!!!!")
	
SyntaxError: invalid syntax
>>> if 1==1:
	print("TRUE!!!!!!!!")
else:
	print("FALSE!!!!!!!")

	
TRUE!!!!!!!!
>>> 
