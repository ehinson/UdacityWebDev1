class MainHandler(webapp2.RequestHandler):
	def write_form(self, erroruser="", errorpass="",erroremail="", username="", password=""):
		self.response.out.write(form %{"error_user": erroruser,
										"error_pass": errorpass,
										"error_email": erroremail,
										"username":username,
										"password":password})
	def get(self):
		self.write_form()
		
	def post(self):
		user_name=self.request.get("username")
		pass_word=self.request.get("password")
		verify=self.request.get("verify")
		e_mail=self.request.get("email") 
		username=valid_username(user_name)
		email=valid_email(e_mail)
		
		errorpass=""
		erroruser=""
		erroremail=""
		
		if username == None:
			username=user_name
			erroruser="That's not a valid username."
		else:
			username=username.group()
		if (verify != pass_word or verify=="" and pass_word==""):
			errorpass="That wasn't a valid password." 
# if not(username):
# erroruser="That's not a valid username."
		if not (email or (not e_mail)):
			erroremail="That's not a valid email."
			self.write_form(erroruser, errorpass, erroremail, username, pass_word)
		if not (erroruser or errorpass or erroremail):
			self.redirect("/welcome")
			
class WelcomeHandler(webapp2.RequestHandler):
	def post(self):
		username=self.request.get("username")
		self.response.out.write("Welcome" +", " + username +"!")