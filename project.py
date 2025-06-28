from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = Chrome(executable_path= "chromedriver.exe")
driver.get("https://www.google.com/")
search_bar = driver.find_element('name' , 'q')

singer =  input("What's the singer's name? ")
music = input("What's the name of song? ")
search_bar.send_keys(f"{singer} {music} Lyrics")
search_bar.send_keys(Keys.ENTER)

soup = BeautifulSoup(driver.page_source , 'html.parser')
soup = soup.find_all('div' , attrs= {"jsname" : "WbKHeb"})

for soup1 in soup:
    soup1 = soup1.find_all('div' , attrs={"jsname" : "U8S5sf"})
    for div in soup1:
        div = div.find_all('span' , attrs={"jsname" : "YS01Ge"})
        with open(f"{singer}-{music} Lyrics.txt" , 'a') as file:
            for span in div:
                print(span.text)
                file.write(span.text + '\n')
