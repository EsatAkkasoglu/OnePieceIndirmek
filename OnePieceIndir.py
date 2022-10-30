#Çalıştırmanız yeterlidir.
#Üzerinde oynamalar yapılarak diğer indirme veweb işlemleri için bilgi sahibi olabilmeniz için kodlar kolay olanlar ile hazırlanmıştır.
#Diğer animeler için de link düzenlenerek ve XPATH kısımları değiştirilerek yapılabilir.
from selenium import webdriver
from time import sleep 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


from webdriver_manager.chrome import ChromeDriverManager
chromeOp = webdriver.ChromeOptions()
chromeOp.add_argument("--incognito")

#Bazı importlar üzerinde oynama yapılması için import edilmiştir.
#Kodlarda karşılatığımız hataları düzeltmek için yardım istiye bilirsiniz.

print("Bölüm aralığı girmeniz gerekmektedir.")
x=int(input("İstediğiniz Son Bölümü Giriniz: ",))
y=int(input("İstediğiniz Son Bölümü Giriniz: ",))
for i in range(x,(y+1)):
    
    driver= webdriver.Chrome(ChromeDriverManager().install()) 
    
    #driver.maximize_window()
    driver.delete_all_cookies()
    url="https://anizm.net/one-piece-"+str(i)+"-bolum"
    driver.get(url)
    
    driver.implicitly_wait(5)
    
    
     
    fanButton= driver.find_element(By.XPATH,'/html/body/main/div[2]/div/div[2]/div[1]/div[1]/div/div/a/div').click()
    
    sleep(2)
    drive_button=driver.find_element(By.XPATH,'/html/body/main/div[2]/div/div[2]/div[1]/div[4]/div/a[7]').click()
    
    driver.switch_to.default_content()
    sleep(2)
    driverLink=driver.find_elements(By.XPATH,'/html/body/main/div[2]/div/div[2]/div[1]/div[3]/iframe')[0].get_attribute("src")
    
    driverLink2=driverLink.replace("preview","view")
    sleep(2)
    driver.get(driverLink2)
    sleep(10)
    
    
    actions = ActionChains(driver) 
    actions.send_keys(Keys.TAB * 2)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    sleep(4)
    
    driver.switch_to.window(driver.window_handles[1])
    sonLink=driver.current_url
    print(sonLink)
    driver.get(sonLink)
    sleep(2)
    
    actions = ActionChains(driver) 
    actions.send_keys(Keys.TAB * 2)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    
    #fanButton= driver.find_element(By.XPATH,'/html/body/div[5]/div[1]')
    
    print(driver.window_handles[1])
    print(drive_button)
    

    print(driverLink)
#internet hızınıza göre buradaki süreyi uzatınız.   
    sleep(20)
    driver.quit()
    
    
    sleep(5)
