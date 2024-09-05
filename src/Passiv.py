from os import getenv
from time import sleep

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from pyotp import TOTP


def buy_passiv():
    load_dotenv("./.env.production")
    load_dotenv("./.env.local")
    if (
        not getenv("USER_EMAIL")
        or not getenv("USER_PASSWORD")
        or not getenv("TOTP_SECRET")
    ):
        raise Exception(
            "Please provide USER_EMAIL, USER_PASSWORD, and TOTP_SECRET in .env.production file"
        )
    user = {
        "email": getenv("USER_EMAIL"),
        "password": getenv("USER_PASSWORD"),
        "totp": TOTP(getenv("TOTP_SECRET") or ""),
    }

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False if getenv("ENV") == "local" else True
        )
        print("Browser launched")
        page = browser.new_page()
        page.goto("https://app.passiv.com/login")

        page.fill('input[name="email"]', user["email"] or "")
        page.fill('input[name="password"]', user["password"] or "")
        page.click("text=Sign in")
        print("Log in submitted")
        page.wait_for_load_state("domcontentloaded")

        page.fill('input[name="token"]', user["totp"].now())
        page.click("text=Submit")
        print("TOTP submitted")
        sleep(10)
        page.wait_for_url("https://app.passiv.com/dashboard", timeout=10)
        if page.url != "https://app.passiv.com/dashboard":
            raise Exception("Failed to login")

        accounts = page.query_selector_all("text=ALLOCATE")
        print(f"Found {len(accounts)} accounts to allocate")
        for account in accounts:
            account.click()
            sleep(2)
            page.click("text=Preview Orders")
            sleep(4)
            page.click("text=Confirm")
            print("Order submitted")

        sleep(10)
        browser.close()


if __name__ == "__main__":
    buy_passiv()
