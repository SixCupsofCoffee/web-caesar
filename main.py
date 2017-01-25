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
from helpers import alphabet_position, rotate_character, encrypt
import cgi

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Web Caesar</title>
</head>
<body>
    <h1>Web Caesar</h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Index(webapp2.RequestHandler):
    def get(self):
        addForm = """
        <form action="/rotate" method="post">
            <label>
                Enter the text you'd like to encipher: <input type="textarea" name="plain_text"/>
            </label><br>
            <label>
                Enter the amount of characters to rotate by: <input type="text" name="rot_amount"/>
            </label><br>
            <input type="submit" value="Encipher"/>
        </form>
        """

        content = page_header + addForm + page_footer

        self.response.write(content)

class Rotate(webapp2.RequestHandler):
    def post(self):
        originalMessage = self.request.get("plain_text")
        rotAmount = self.request.get("rot_amount")

        rotAmount = int(rotAmount)

        encryptedMessage = encrypt(originalMessage, rotAmount)
        escapedMessage = cgi.escape(encryptedMessage)

        message = page_header + "<h3>Encryption Completed</h3>" + "<em><b>Your message is: </b></em>" + escapedMessage + page_footer

        self.response.write(message)


app = webapp2.WSGIApplication([
    ('/', Index),
    ('/rotate', Rotate)
], debug=True)
