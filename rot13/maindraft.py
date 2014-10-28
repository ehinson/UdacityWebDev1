import webapp2

form = """
<form method = "post" >
	  
	  <p>Enter some text to encode: </p>
	  
	  <textarea placeholder ="Enter some text to encode..." name = "text" rows = "10" cols= "50" ></textarea>
	  <p><input type = "submit"></p>
</form>
"""

def shift_n_letters(letter, n):
     offset=ord(letter)-ord('a')
     offset= offset+n
     offset=offset%26
     offset= ord('a')+ offset
     value= chr(offset)
     return value

def shift_m_letters(letter, m):
     offset=ord(letter)-ord('A')
     offset= offset+m
     offset=offset%26
     offset= ord('A')+ offset
     value= chr(offset)
     return value

def rotate(s, n):
    # Your code here
    p=""
    for letter in s:
         if ord(letter)>= ord('a') and ord(letter)<= ord('z'):
             p = p + shift_n_letters(letter, n)
         elif ord(letter) >= ord('A') and ord(letter)<= ord('Z'):
              p = p + shift_m_letters(letter, n)
         else:
             p = p + letter
    return p

class MainHandler(webapp2.RequestHandler):
    def get(self):
	    self.response.out.write(form)
	
	def post(self):
        self.response.out.write("Thanks! That's a totally valid day!")
		
app = webapp2.WSGIApplication([('/', MainHandler)], debug = True)