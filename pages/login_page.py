class LoginPage:

    def __init__(self, page):
        self.page = page
        self.username = 'input[name="username"]'
        self.password = 'input[name="password"]'
        self.login_btn = 'button[type="submit"]'

    def login(self, user, pwd):
        self.page.fill(self.username, user)
        self.page.fill(self.password, pwd)
        self.page.click(self.login_btn)