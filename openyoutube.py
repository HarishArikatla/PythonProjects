from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager 
 


driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.get('https://arikatlah.wixsite.com/python') 
print ("Opened javatpoint.com") 



print ("Done") 
input('Press anything to quit') 
driver.quit() 
print("Finished") 

