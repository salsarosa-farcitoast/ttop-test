from playwright.sync_api import sync_playwright
import time
import random

USERNAME = 'dummy'

with sync_playwright() as p:
    print("Launching browser...")
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    print("Navigating to the URL...")
    page.goto("https://tabletopia.com/players/id3674590/zdytgc")

    print("Waiting for 'Join' button...")
    page.wait_for_selector("#player-join-seat-btn", timeout=10000)
    print("Clicking 'Join' button...")
    page.click("#player-join-seat-btn")

    print("Waiting for username input field...")
    page.wait_for_selector("input.js-username", timeout=10000)
    print(f"Filling username: {USERNAME}")
    page.fill("input.js-username", USERNAME)

    print("Waiting for 'Play as Guest' button to be enabled...")
    page.wait_for_function(
        """() => {
            const btn = document.querySelector('button.button');
            return btn && !btn.classList.contains('disabled');
        }""",
        timeout=10000
    )
    print("Clicking 'Play as Guest' button...")
    page.click("button.button:has-text('Play as Guest')")

    print("Waiting for 'Continue' button...")
    page.wait_for_selector("#player-continue-btn", timeout=10000)
    print("Clicking 'Continue' button...")
    page.click("#player-continue-btn")

    print("Starting mouse movement simulation...")
    while True:
        print("Moving mouse in a rectangle pattern...")
        page.mouse.move(30, 30, steps=20)  # Start at top-left corner
        page.mouse.move(300, 30, steps=20)  # Move to top-right corner
        page.mouse.move(300, 300, steps=20)  # Move to bottom-right corner
        page.mouse.move(30, 300, steps=20)  # Move to bottom-left corner
        page.mouse.move(30, 30, steps=20)  # Move back to top-left corner

        sleep_time = random.uniform(2, 10)
        print(f"Sleeping for {sleep_time:.2f} seconds...")
        time.sleep(sleep_time)  # Wait for a random time between 2 and 10 seconds before repeating

    print("All actions completed. Browser will remain open.")
    input("Press Enter to close...")
