#!/usr/bin/python
print "Content-type:text/html\n\n"
# Import modules for CGI handling 
import cgi, codecs 

# Create instances of FieldStorage 
form = cgi.FieldStorage()

# Get data from fields
#if form.getvalue("text"):
	#text = form.getvalue("text")
	#print '<h1> Hello, Your reverse test is '+  + '! Thanks for using my script! </h1> <br/>'
   
user_input = form.getvalue('user_input') #using form to user_input
cipher = form.getvalue('cipher')
original = user_input   #decare orginal as user_input


#if  len(user_input) !=0:
	
if 	cipher== "dummy":
	output =  user_input #printout dummy

elif	cipher== "lower":
	output = user_input.lower() #printout lower
elif	cipher  == "upper":
	output = user_input.upper() #printout  upper
elif    cipher== "reverse":
	output = user_input[::-1] #print out reverse
	
elif   cipher == "rot13":
	#Got help from Stackoverflow.com
	enc = codecs.getencoder( "rot-13" ) 
	output = enc(user_input)[0];	#print out rot13 
		
	
	#elif   len(user_input)==0: # reconixe if ling is empty
	#	print (" Sorry, We are uable to generate  your selected cipher, please try again....")
	

	# here is the print section which'll display in the webpage as user entered valid text


print "<html>"
print "<head>"
print " <h3>"
print ("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print ("<h3>  Hello, Your "+cipher +" text of  "+ original  + "  : <br/> " +  output + "<br><br/> Thanks for using my script! </h3> ")
print "</head>"
print "<body>"
print ("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print "</body>"
print "</html>"

#else:
 #print "wrong message"

	











