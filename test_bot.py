from selenium import webdriver
from time import sleep
from random import random
from secrets import password, email


class BadooBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        sleep(1)

        

    def login(self):
        self.driver.get('https://badoo.com')
        fb_btn = self.driver.find_element_by_xpath('//*[@id="page"]/div[2]/div[3]/div/div[3]/div/div[1]/div[2]/div/div/a')
        fb_btn.click()

        #Switch to login popup
        base_window = self.driver.window_handles[0]
        popup = self.driver.switch_to_window(self.driver.window_handles[1])


        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(email)

        pass_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pass_in.send_keys(password)        

        log_in_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        log_in_btn.click()

        self.driver.switch_to_window(base_window)

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[1]/div[1]')
        like_btn.click()
    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[2]/div[1]')
        dislike_btn.click()
    def auto_swape(self, n):
        right_count = 0
        left_count = 0
        for i in range(0,n) :
            sleep(random()+1)
            try:
                rand = random()
                if rand < .73:
                    self.like()
                    right_count += 1
                    print("Liczba polubien wynosi: ", right_count)
                    if (i%5 ==0): 
                        print("liczba operacji: ", i+1)
                else:
                    self.dislike()
                    left_count += 1 
                    print("Liczba odrzuczonych polubien wynosi: ", left_count)

            except Exception:
                try:
                    self.skip_exept()
                except Exception:
                    try:
                        self.its_a_match_exept()
                    except Exception:    
                        print("Wystapil wyjatek, przerywam dzialanie, Suma operacji: ", i)
                        break
            
    def skip_exept(self):
        popup1 = self.driver.find_element_by_xpath('/html/body/aside/section/div[1]/div/div[2]/div/div[2]')
        popup1.click()
    def email_exept(self):
        click = self.driver.find_element_by_xpath('//*[@id="simple-page"]/div[3]/section/div[3]/div/div[2]/a')
        click.click()
        #Tutaj dac exeption od skipa
    def its_a_match_exept(self):
        close_btn = self.driver.find_element_by_xpath('/html/body/aside/section/div[1]/div/div[1]/div[4]/i')
        close_btn.click()

    def message_all(self):
        pass
    def save_photo(self):
        bot.driver.save_screenshot("zdjecie-", self.save_descryption().name ,  ".png")
    def save_descryption(self):
        
        name = self.driver.find_element_by_xpath('//*[@id="mm_cc"]/div[1]/div/div/div[1]/div/div[1]/div/div[1]/div[2]/h1').text.replace('\n','')
        print("Swapowana osoba to", name)
        try:
            dec = self.driver.find_element_by_xpath('//*[@id="mm_cc"]/div[1]/div/div/div[1]/div/div[2]/div[1]/div').text.replace('\n',' ')
            print("Opis:", dec)
        except Exception:
            print('Brak opisu.')    
    def door(self):
        self.driver.close()
    def save_to_file(variable1, variable2):
        pass



bot = BadooBot()
bot.login()
