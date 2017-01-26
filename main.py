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
from helpers import encrypt
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

# TODO: use only the original files to implement the encryption function

# TODO: (optional) Make the page look nicer

def buildPage(textAreaText):
    formCreate = "<form method='post'>"
    cipherArea = """
        <label>Enter the text you'd like to encipher: </label>
        <br>
        <textarea name="plain_text"/>
        """
    textAreaEnd = "</textarea><br>"
    rotEntryArea = """
        <label>Enter the amount of characters to rotate by: </label>
        <br>
        <input type="text" name="rot_amount"/>
        <br>
        """
    submit = "<input type='submit'>"
    formEnd = "</form>"

    form = page_header + formCreate + cipherArea + textAreaText + textAreaEnd + rotEntryArea + submit + formEnd + page_footer

    return form

#addForm = """
#    <form method="post">
#        <label>
#            Enter the text you'd like to encipher: <textarea name="plain_text"/>" + escapedMess</textarea>
#        </label><br>
#        <label>
#            Enter the amount of characters to rotate by: <input type="text" name="rot_amount"/>
#        </label><br>
#        <input type="submit">
#    </form>
#    """

class Index(webapp2.RequestHandler):
    def get(self):
        content = buildPage("")
        self.response.write(content)

    def post(self):
        originalMessage = self.request.get("plain_text")
        rotAmount = self.request.get("rot_amount")

        rotAmount = int(rotAmount)

        encryptedMessage = encrypt(originalMessage, rotAmount)
        escapedMessage = cgi.escape(encryptedMessage)
        content = buildPage(escapedMessage)

        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
