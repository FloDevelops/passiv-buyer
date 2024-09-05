# Passiv Buyer

This is a simple project to automatically allocate available funds in a brokerage account to a pre-defined accounts and corresponding potfolio models in Passiv.

This project only **executes the one-click trades that Passiv provides**.

According to Passiv, this manual step is a legal requirement to ensure that the user is aware of the trades that are being executed.

I personnaly executed these one-click trades manually many times, however I often did it with mutiple days of delay as it needs to be done during market hours.

Bored of doing this manually and loosing on a few days of market performance each time, I decided to automate the process of executing these one-click trades.

Now, since this script runs on a daily schedule with GitHub Actions, every time I have available funds in my brokerage account (dividends or deposits), these are automatically allocated within the same day or the next market day.

## How it works

- Retrieve the username, password and one-time password secret (two-factor authentication) from the environment variables.
- Open a browser window.
- Log in with the username and password, and generate a one-time password to pass the two-factor authentication.
- Navigate to the Passiv dashboard.
- Find if they are any "Allocate" call to action buttons, and if so click them, and then click on "Preview orders" and "Confirm" buttons.
- Close the browser window.

## Prerequisites

- A Passiv account linked to a brokerage account with active protfolio models.
- The Python version indicated in the `.python-version` file (preferrably installed with `pyenv`).

## Installation

1. Fork and clone the repository.
2. Open a terminal and navigate to the repository folder.
3. Make sure the current Python version is the one indicated in the `.python-version` file by running `python --version`.
4. Create a virtual environment by running `python -m venv .venv`.
5. Activate the virtual environment by running `source .venv/bin/activate`.
6. Install the dependencies by running `pip install -r requirements.txt`.
7. Copy and rename the `.env.production.example` file to `.env.production`, and edit the values with your Passiv credentials (the TOTP secret can be found in your Passiv settings).
8. Copy and rename the `.env.local.example` file to `.env.local` (the `ENV` variable is set to `local` to ease the development process by showing the browser window instead of running in headless mode).
9. Run the script by running `python src/Passiv.py` (you should see a browser window opening, logging in, executing trades if some are available, and then closing).
10. If it does not work, you might have to tweak the `src/Passiv.py` script to a specific use case or website update and can submit a pull request to share the fix.
11. If it works, you can now schedule the script to run daily by using GitHub Actions (see the `.github/workflows/run-passiv.yml` file).
12. In your GitHub repository, go to the "Settings" tab, then "Secrets", and "Actions", and add the following secrets like you did in the `.env.production` file:
    - `USER_EMAIL`: Your Passiv username.
    - `USER_PASSWORD`: Your Passiv password.
    - `TOTP_SECRET`: Your Passiv TOTP secret.
13. Commit and push the changes to your repository.
14. Go to the "Actions" tab in your GitHub repository, and you should see the scheduled workflow running daily, or you can run it manually by clicking on the "Run workflow" button.

## Comments

The `src/app.py` file is a simple FastAPI application that can be used to run the script in a web server. This can be useful to run the script in a serverless environment like AWS Lambda, Google Cloud Run Functions, or Azure Functions.

The `Dockerfile` and `docker-compose-dev.yml` files are provided to run the web server in a Docker container. This can be useful to test the web server locally and deploy it without environment dependencies.

## Disclaimer

This project is not affiliated with Passiv and requires your full attention and understanding of the code before running it to avoid executing unwanted trades.

If Passiv updates their website or adds bot detection, this script might not work anymore and will need to be updated.
