class Locators:

    url="https://www.amazon.in/?language=en_in"
    # search_box="//input[@id='LocationSearch_input']"
    search_box = "//input[@id='twotabsearchtextbox']"
    search_result="//button[text()='Delhi']"
    tempature="(//span[@data-testid='TemperatureValue'])[1]"

    cowin_url="https://www.cowin.gov.in/home"
    cowin_signin_button="(//*[text()='Register / Sign In '])"
    mobile_no="//input[contains(@class,'mat-input-element mat-form-field-autofill-control')]"
    otp="//*[contains(text(),' GET OTP ')]"
    search_button="//*[contains(text(),'Search')]"
    filter_18="//label[text()='<text_replace>']"

    booking_date="(//div[@class='vaccine-box vaccine-box1 vaccine-padding'][1]/a)[2]"

    button="//*[@class='icp-button a-declarative']/span[text()='English']"
