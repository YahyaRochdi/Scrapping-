from selenium import webdriver
import csv
from selenium.webdriver.common.by import By


# Définir le driver de Selenium
driver = webdriver.Chrome('chromedriver.exe')
urls = [
    
    'https://lematin.ma/express/2023/twitter-affiche-tweets-prives-cause-d-bug/388702.html',

    

]
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

csv_file_name = "Matin scraped.csv"
csv_columns = ["Author Name", "Article Title", "Content", "Time"]



for url in urls:
        driver.get(url)
        article_title = driver.find_element(By.CSS_SELECTOR, "#title").text
        author_name = driver.find_element(By.CSS_SELECTOR, "meta[itemprop='author']").get_attribute("content")
        content_element1 = driver.find_element(By.CSS_SELECTOR, 'article.card.p-1.mb-2').text
        time = driver.find_element(By.CSS_SELECTOR, "time").text

        # write the values of the scraped elements to the output file
        #print(article_title)
        #print(author_name)
        print(content_element1)
        #print(time)
driver.quit()  # Close the browser driver when done