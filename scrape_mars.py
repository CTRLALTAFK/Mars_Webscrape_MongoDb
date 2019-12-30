from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd

def scrape():
    executable_path = {"executable_path": "chromedriver.exe"}
    browser = Browser("chrome",**executable_path, headless=False)
    news_title, news_par = mars_news(browser)
    mars_data = {"news_title": news_title, 
                 "news_paragraph": news_par,
                 "featured_image": featured_img_url(browser),
                 "weather":twitter_weather (browser),
                 "facts": mars_facts(),
                 "hemispheres":hemispheres(browser)}      
    browser.quit()
    return mars_data


def mars_news (browser):
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
    html = browser.html
    soup_news = bs(html, "html.parser")

    news_element = soup_news.select_one("ul.item_list li.slide")
    news_title = news_element.find("div",class_="content_title").get_text()
    
    news_par = news_element.find("div",class_="article_teaser_body").get_text()
        
    return news_title, news_par

def featured_img_url(browser):
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    browser.is_element_present_by_id("full_image", wait_time=1)
    #clicking on "full image"
    full_img_el = browser.find_by_id("full_image")
    full_img_el.click()

    #finding then clicking on "more info"
    browser.is_element_present_by_text("more info", wait_time=1)
    more_info_elem = browser.find_link_by_partial_text('more info')
    more_info_elem.click()

    html = browser.html
    soup_img = bs(html, "html.parser")
    #print(soup_img.prettify())

    #getting source URL for img
    img_url_rel = soup_img.select_one('figure.lede a img').get("src")
    img_url_rel

    featured_image_url = "https://www.jpl.nasa.gov" + img_url_rel
    return featured_image_url

def twitter_weather (browser):
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    html = browser.html
    soup_weather = bs(html, "html.parser")
    # Find a Tweet with the data-name `Mars Weather`
    mars_weather_tweet = soup_weather.find("div", 
                                    attrs={
                                        "class": "tweet", 
                                        "data-name": "Mars Weather" })
    # Search Within Tweet for <p> Tag Containing Tweet Text
    mars_weather = mars_weather_tweet.find("p", "tweet-text").get_text()
    mars_weather = mars_weather.replace("pic.twitter.com/LF8bj3SF22", " ")
    return mars_weather

def mars_facts ():
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url) #comes back as a list with a length of 3
    df = tables[0] #access dataframe
    data_string = df.to_html()
    return data_string

def hemispheres(browser):
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    hemisphere_image_urls = []
    links = browser.find_by_css("a.product-item h3")               

    for i in enumerate (links):
        
        hemisphere = {}    
        browser.find_by_css("a.product-item h3")[i].click()
        #title
        hemisphere["title"] = browser.find_by_css("h2.title").text
        hemisphere_image_urls.append(hemisphere)
        #img url
        img_element = browser.find_link_by_text('Sample')
        hemisphere["img_url"] = img_element["href"]
        
        
        browser.back()
    return hemisphere_image_urls



if __name__ == "__main__":
    print(scrape())

