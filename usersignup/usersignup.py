import webapp2
import cgi
import re

def escape_html(s):
    return cgi.escape(s, quote = True)

form = """
<form method = "post">
    <label> Username 
    <input type = "text" name = "username" value = "%(username)s">
	</label>
	<div style="color:red">%(username_error)s</div>
	<br>
	
	<label> Password 	
    <input type = "password" name = "password" value = "" placeholder = "Enter password">
	</label>
	<div style="color:red">%(password_error)s</div>
	<br>
	
	<label> Verify Password </label>	
    <input type = "password" name = "verify" value = "" >
    <div style="color:red">%(verify_error)s</div>
	<br>
	
	<label> Email(optional)</label>	
    <input type = "text" name = "email" value = "%(email)s" placeholder = "Enter an email">
	<div style="color:red">%(email_error)s</div>
	<br>
	
    <input type = "submit" value = "come in">
  </form>
  """
  
user_re = re.compile(r'^[a-zA-Z0-9_-]{3,20}$')
password_re = re.compile(r'^.{3,20}$')
email_re = re.compile(r'^[\S]+@[\S]+\.[\S]+$')

def valid_user(username):
	return username and user_re.match(username)

def valid_password(password):
    return password and password_re.match(password)
	
#def valid_verify(verify, password):
#	if (verify==password):
#	    return password_re.match(password)

def valid_email(email):
    return not email or email_re.match(email)
	
class MainPage(webapp2.RequestHandler):
	def post(self):
		self.response.out.write(form)
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(form)

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)