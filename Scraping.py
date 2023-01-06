from requests import Session
from bs4 import BeautifulSoup as bs
import json

class Scraping:

    login_page = None
    login_user = None
    login_pass = None
    login_session = None

    def __init__(self, input_loging_page, input_login_user, input_login_pass) -> None:
        self.login_page = input_loging_page
        self.login_user = input_login_user
        self.login_pass = input_login_pass
        self.login_session = Session()

    def login(self):
        site = self.login_session.get(self.login_page)
        login_data = {"username": self.login_user, "password": self.login_pass, "pos_no":"0"}
        self.login_session.post(self.login_page, login_data)

    def getContent(self, url):
        r = self.login_session.get(url)
        soup = bs(r.content, "html.parser")
        soup = soup.encode("utf-8")
        soup = json.loads(soup)
        return soup
