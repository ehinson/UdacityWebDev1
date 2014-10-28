#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law (or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
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
	<br>
	
	<label> Email(optional)</label>	
    <input type = "text" name = "email" value = "%(email)s" placeholder = "Email(optional)">
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
	
	
class MainHandler(webapp2.RequestHandler):
   def write_form(self, username ="", email = "", username_error="", password_error="", email_error=""):
        self.response.out.write(form % {"username":username,
										"email":email,
										"username_error": username_error}
										"password_error": password_error,
										"email_error":email_error})
    def get(self):
        self.write_form()
		
	def post(self):
	    username = self.request.get('username')
		userpass= self.request.get('password')
		verify = self.request.get('verify')
		email = self.request.get('email')
		
		user_name= valid_user(username)
		user_pass = valid_password(password)
		user_email = valid_email(email)
		
		username_error = ""
		password_error=""
		email_error = ""
		
		
		if not(username):
			username = user_name
			username_error = "Please enter a valid username."
		else:
			username = username.group()
			
		if verify!= password or verify == "" and password = ""):
			password_error = "Please enter a valid password."
		
		if not(email or (not user_email)):
			email_error = "Please enter a valid email."
			self.write_form(username, email, username_error, password_error, email_error
		else:
			self.redirect("/welcome")
			
	    #self.write_form(username, email, username_error, password_error,email_error)

class WelcomeHandler(webapp2.RequestHandler):
	def post(self):
		username = self.request.get("username")
		self.response.out.write("Welcome " + username)
    


		
		
app = webapp2.WSGIApplication([('/', MainHandler)], [('/welcome', WelcomeHandler)], debug=True)
