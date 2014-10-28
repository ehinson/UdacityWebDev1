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

# create textarea 

form = """
<form method = "post" onsubmit= "rotate('text', 13)">
	  
	  <p>Enter some text to encode: </p>
	  
	  <textarea placeholder ="Enter some text to encode..." name = "text" rows = "10" cols= "50" ></textarea>
	  <p><input type = "submit"></p>
</form>
"""

# takes as input a lowercase letter and an integer n 
# returns a letter n steps in the alphabet after the letter
# wraps around at 'z'

def shift_n_letters(letter, n):
     offset=ord(letter)-ord('a')
     offset= offset+n
     offset=offset%26
     offset= ord('a')+ offset
     value= chr(offset)
     return value

# takes as input an Uppercase letter and an integer m 
# returns a letter m steps in the alphabet after the letter
# wraps around at 'Z'	 
	 
def shift_m_letters(letter, m):
     offset=ord(letter)-ord('A')
     offset= offset+m
     offset=offset%26
     offset= ord('A')+ offset
     value= chr(offset)
     return value

# takes in a string s and int n
# returns a string of letters 
# where each letter is n steps after each letter in s

def rotate(s, n):
    p=""
    for letter in text:
         if ord(letter)>= ord('a') and ord(letter)<= ord('z'):
             p = p + shift_n_letters(letter, n)
         elif ord(letter) >= ord('A') and ord(letter)<= ord('Z'):
              p = p + shift_m_letters(letter, n)
         else:
             p = p + letter
    return p

class MainPage(webapp2.RequestHandler):

    def post(self):
	    text_rotate = rotate(self.request.get('text'), 13)
        self.response.out.write(text_rotate)
		
    def get(self):
	    self.response.out.write(form)
	
	
		
app = webapp2.WSGIApplication([('/', MainPage)], debug = True