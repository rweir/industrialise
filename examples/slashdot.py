from industrialise import browser

username = 'YOURUSERNAME'
password = 'YOURPASSWORD'

b = browser.Browser()
b.go("http://slashdot.org/")
b.follow("Log In")
form = b.forms[2]
form.fields['unickname'] = username
form.fields['upasswd'] = password
b.submit(form, extra_values={'userlogin': 'Log in'})
print b.contents
assert username in b.contents
