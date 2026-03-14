class DashboardPage:

    def __init__(self, page):
        self.page = page
        self.dashboard_text = "h6:has-text('Dashboard')"  # Update selector based on your site

    def verify_dashboard(self):
        self.page.wait_for_selector(self.dashboard_text, timeout=5000)
        return self.page.locator(self.dashboard_text).is_visible()