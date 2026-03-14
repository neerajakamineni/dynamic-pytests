import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    # Force headless mode in CI
    return {**browser_context_args, "headless": True}