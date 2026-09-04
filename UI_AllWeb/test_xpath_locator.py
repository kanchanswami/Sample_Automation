from playwright.sync_api import Page, expect

def test_xpath_location(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    #absolute xpath
    logo=page.locator("//html/body/div[4]/div[1]/div[1]/div[1]/a/img")
    expect(logo).to_be_visible()

    #relative xpath
    expect(page.locator("//img[@alt='Tricentis Demo Web Shop']")).to_be_visible()
    page.wait_for_timeout(500)


    #xpath with contains
    products = page.locator("//h2/a[contains(@href, 'computer')]")
    products_count=products.count()
    print("Product count:", products_count)
    expect(products).to_have_count(products_count)

    #First product information
    print("First product content:-", products.first.text_content())

    #Last product information
    print("Last product content:-", products.last.text_content())

     #Middle product information
    print("2nd product content:-", products.nth(2).text_content())

    print("Printing product title using looping statement:- ")
    product_title = products.all_text_contents()
    for i in product_title:
        print(i)

     #xpath with start-with()
    build_product=page.locator("//h2//a[starts-with(@href,'/build')]")
    print("count the building product:", build_product.count())
    expect(build_product).to_have_count(build_product.count())

    #xpath with text() function
    registrator = page.locator("//a[text()='Register']")
    expect(registrator).to_be_visible()

    #xpath with last() function
    google_plus_link = page.locator("//div[@class='column follow-us']//li[last()]")
    expect(google_plus_link).to_have_text("Google+")
    #page.locator("//div[@class='column follow-us']//li(5)]")

    twitter = page.locator("//div[@class='column follow-us']//li[position()=2]")
    expect(twitter).to_have_text("Twitter")

