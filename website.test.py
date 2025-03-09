"""
This script uses Playwright to automate browser interactions for testing a website.

Steps performed by the script:
1. Start Playwright and launch a Chromium browser instance.
2. Open a new browser page with JavaScript enabled.
3. Navigate to the specified URL and wait for the page to load.
4. Locate the dropdown toggle button using XPath and wait for it to be attached and visible.
5. Scroll the dropdown toggle button into view if it is off-screen.
6. Click the dropdown toggle button to open the dropdown menu.
7. Wait for the dropdown menu to become visible.
8. Locate the Media link within the dropdown menu using XPath.
9. Wait for the Media link to be visible and clickable.
10. Click the Media link.
11. Print a confirmation message.
12. Pause for 5 seconds for debugging purposes.
13. Close the browser page and the browser instance.
14. Stop Playwright.

Note: The script assumes that the local server is running at http://127.0.0.1:8080/.
"""

import time
from playwright.sync_api import sync_playwright

XPATH_PREFIX = "xpath="
URL = "http://127.0.0.1:8080/"

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
page = browser.new_page(java_script_enabled=True)

# Go to the URL and wait for the page to load
page.goto(URL, wait_until="domcontentloaded")

# XPath for the dropdown toggle (button that opens the menu)
DROPDOWN_TOGGLE_XPATH = XPATH_PREFIX + "//a[contains(@class, 'dropdown-toggle')]"
DROPDOWN_TOGGLE = page.locator(DROPDOWN_TOGGLE_XPATH)

# Wait for the toggle button to be attached and visible
DROPDOWN_TOGGLE.wait_for(state="attached", timeout=20000)  # Increased timeout to 20 seconds
DROPDOWN_TOGGLE.wait_for(state="visible", timeout=20000)

# Scroll the element into view if it's off-screen
DROPDOWN_TOGGLE.scroll_into_view_if_needed()

# Try clicking the dropdown toggle with force=True if not interactable
DROPDOWN_TOGGLE.click(force=True)

# Wait for the dropdown menu to become visible
DROPDOWN_MENU_XPATH = XPATH_PREFIX + "//div[contains(@class, 'dropdown-menu')]"
page.wait_for_selector(DROPDOWN_MENU_XPATH, state="visible", timeout=5000)

# XPath for the Media link
MEDIA_XPATH = XPATH_PREFIX + "//a[contains(@class, 'dropdown-item') and contains(@href, '/story')]"
media_link = page.locator(MEDIA_XPATH)

# Wait for the Media link to be visible and clickable
media_link.wait_for(state="visible", timeout=5000)
media_link.click()

print("Clicked on Media link!")
time.sleep(5)

# Debugging Pause (Uncomment if needed)
# page.pause()

# Close the page and browser
page.close()
browser.close()
playwright.stop()
