#!/usr/bin/env python3

import json,os
import cgi
import cgitb
import secret
cgitb.enable()

# In case you want to report full env var in JSON this is the script for question 1 and some task for question 2
# print("Content-Type: application/json\n\n")
# print(json.dumps(dict(os.environ)))

env_var = os.environ
form = cgi.FieldStorage()
username = form['username'].value
password = form['password'].value

if username == secret.username and secret.password:
	print(f"Set-Cookie: {username}+{password}")
print("Content-Type: text/html\n\n")

print(f"""
	<html>
	<head><title>Lab 3: CGI</title></head>
	<body>
		<h1>Question 1</h1><h2>environment variables</h2><p>{env_var}</p>
		<h1>Question 2</h1><h2>QUERY_STRING</h2><p>{env_var.get('QUERY_STRING')}</p>
		<h1>Question 3</h1><h2>User's Browser</h2><p>{env_var.get('HTTP_USER_AGENT')}</p>
		<h1>Question 4</h1><h2>Login Form</h2>    
		<form method="POST" action="/hello.py">
        	<label> <span>Username:</span> <input autofocus type="text" name="username"></label> <br>
        	<label> <span>Password:</span> <input type="password" name="password"></label>
        	<button type="submit"> Login! </button>
    	</form>
    	<p>username:{username} / password:{password}</p>
	</body>
	</html>
""")

