from playwright.sync_api import Page, expect


def test_lowtohigh(page: Page):
    """expected_titles = [
    "Pixel 2",
    "One Plus 6T",
    "iPhone XR",
    "One Plus 7",
    "iPhone XS",
    "iPhone 11",
    "Pixel 3",
    "One Plus 7T",
    "iPhone XS Max",
    "iPhone 12 Mini",
    "iPhone 11 Pro",
    "Galaxy S9",
    "iPhone 12",
    "One Plus 8",
    "Galaxy S10",
    "Pixel 4",
    "One Plus 8T",
    "One Plus 8 Pro",
    "iPhone 12 Pro",
    "Galaxy S20",
    "Galaxy Note 20",
    "iPhone 12 Pro Max",
    "Galaxy S20+",
    "Galaxy Note 20 Ultra",
    "Galaxy S20 Ultra"
]

    expected_prices = [
    "$399.00",
    "$429.00",
    "$499.00",
    "$499.00",
    "$549.00",
    "$599.00",
    "$599.00",
    "$599.00",
    "$649.00",
    "$699.00",
    "$699.00",
    "$699.00",
    "$799.00",
    "$799.00",
    "$899.00",
    "$899.00",
    "$899.00",
    "$899.00",
    "$999.00",
    "$999.00",
    "$999.00",
    "$1099.00",
    "$1199.00",
    "$1299.00",
    "$1399.00"
]
    page.goto("https://www.bstackdemo.com/")

    # Select "Lowest to highest"
    page.locator("select").select_option(value="lowestprice")

    page.wait_for_timeout(5000)

    expect(page.locator(".shelf-item__title")).to_have_text(expected_titles)
    expect(page.locator(".val")).to_have_text(expected_prices)

    expect(page.locator(".shelf-item__title").first).to_have_text("Pixel 2")
    expect(page.locator(".val").first).to_have_text("$399.00")

    # Last product title and price
    expect(page.locator(".shelf-item__title").last).to_have_text("Galaxy S20 Ultra")
    expect(page.locator(".val").last).to_have_text("$1399.00")


"""
    page.goto("https://www.bstackdemo.com/")
    page.locator("select").select_option(value="lowestprice")
    
    page.wait_for_timeout(5000)
    titles = page.locator(".shelf-item__title").all_text_contents()
    prices = page.locator(".val").all_text_contents()

    for name, price in zip(titles, prices):
        print(name, price)