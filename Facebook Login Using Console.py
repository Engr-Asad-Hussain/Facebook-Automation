from selenium import webdriver

def main():
      driver_path = "C:\\Users\\*********\\chromedriver.exe"
      driver = webdriver.Chrome()
      driver.get('https://www.facebook.com/')

      # Get the Data from the User to Print etc
      name = input('EMAIL ADDRESS  :  ')
      print()      
      message = input('PASSWORD       :  ')
      print()
      
      User = driver.find_element_by_id("email")
      User.send_keys(name)
      
      Password = driver.find_element_by_id("pass")
      Password.send_keys(message)

      Button = driver.find_element_by_id("loginbutton")
      Button.click()

if __name__=="__main__":
      main()

