from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.data_reader import get_test_data

def test_login(page):

    data = get_test_data()

    login = LoginPage(page)
    dashboard = DashboardPage(page)

    page.goto("https://opensource-demo.orangehrmlive.com")
    page.wait_for_load_state("networkidle")

    login.login(
        data["admin_user"]["username"],
        data["admin_user"]["password"]
    )

    assert dashboard.verify_dashboard()