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
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2
import cgi

def escape_html(s):
	return cgi.escape(s, quote = True)

form = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Rot13 </title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
	
	
	<style type="text/css">
    body {
        padding-top: 40px;
        padding-bottom: 40px;
        background-color: #f5f5f5;
      }

      .form-signin {
        max-width: 600px;
        padding: 19px 29px 29px;
        margin: 0 auto 20px;
        background-color: #fff;
        border: 1px solid #e5e5e5;
        -webkit-border-radius: 5px;
           -moz-border-radius: 5px;
                border-radius: 5px;
        -webkit-box-shadow: 0 1px 2px rgba(0,0,0,.05);
           -moz-box-shadow: 0 1px 2px rgba(0,0,0,.05);
                box-shadow: 0 1px 2px rgba(0,0,0,.05);
      }
      .form-signin .form-signin-heading {
        margin-bottom: 10px;
      }
      .form-signin textarea {
        font-size: 16px;
        height: auto;
		width: auto;
        margin-bottom: 15px;
        padding: 7px 9px;
      }

    </style>
	  </head>
	  <body>
	  <div class="container">
		<form class="form-signin" method="post" >
				<h2 class="form-signin-heading">ROT13</h2>
				<br>
				<textarea class="form-control" type="text" name = "text" placeholder = "Enter some text to ROT13" rows = "10" cols="50" >%(text)s  </textarea>
				<br><br>
				<button class="btn btn-large btn-success" type="submit" >DOMINATE</button>
		</form>
	  </div>
	  </body>
</html>
"""

# takes as input a lowercase letter and an integer n 
# returns a letter n steps in the alphabet after the letter
# wraps around at 'z'

def shift_n_letters(letter, n):
     offset= ord(letter)-ord('a')
     offset= offset+n
     offset= offset%26
     offset= ord('a')+ offset
     value= chr(offset)
     return value

# takes as input an Uppercase letter and an integer m 
# returns a letter m steps in the alphabet after the letter
# wraps around at 'Z'

def shift_m_letters(letter, m):
     offset= ord(letter)-ord('A')
     offset= offset+m
     offset= offset%26
     offset= ord('A')+ offset
     value= chr(offset)
     return value

# takes in a string s and int n
# returns a string of letters 
# where each letter is n steps after each letter in s

def rotate(s, n):
    p=""
    for letter in s:
         if ord(letter)>= ord('a') and ord(letter)<= ord('z'):
             p = p + shift_n_letters(letter, n)
         elif ord(letter) >= ord('A') and ord(letter)<= ord('Z'):
             p = p + shift_m_letters(letter, n)
         else:
             p = p + letter
    return p
	
class MainPage(webapp2.RequestHandler):
	def render_form(self, text = ""):
		self.response.out.write(form % {"text" : escape_html(text)})
	def post(self):
		input= self.request.get('text')
		output= rotate(input,13)
		self.render_form(output)
	def get(self):
		self.render_form()

app = webapp2.WSGIApplication([('/', MainPage)], debug = True)