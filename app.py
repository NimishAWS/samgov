from array import array
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import numpy as np
import pandas as pd

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scrap', methods = ['POST', 'GET'])
def scrap():
        output = request.form.to_dict()
        url = output['url']
        try:
            options = Options()
            options.headless = True
            driver = webdriver.Chrome()
            driver.minimize_window()
            driver.get(url)
            # driver.get('https://sam.gov/search/?index=opp&page=1&pageSize=25&sort=-modifiedDate&sfm%5Bstatus%5D%5Bis_active%5D=true')
            driver.implicitly_wait(0.8)
            content = driver.page_source

            #Getting head name 
            head = []
            try:
                for i in driver.find_elements(By.XPATH, '//*[@id="main-container"]/sam-frontend-search-home/div/div/div/div[2]/search-list-layout/div[2]/div/div/sds-search-result-list/div/div/app-opportunity-result/div/div[1]/div[1]/div/h3'):
                    checks = i.find_element(By.TAG_NAME, 'a')
                    head.append(checks.text)
            except:
                head = ["Null"]

            #Getting all urls for enter in tender page
            urls = []
            try:
                for i in driver.find_elements(By.XPATH, '//*[@id="main-container"]/sam-frontend-search-home/div/div/div/div[2]/search-list-layout/div[2]/div/div/sds-search-result-list/div/div/app-opportunity-result/div/div[1]/div[1]/div/h3'):
                    checks = i.find_element(By.TAG_NAME, 'a')
                    link = checks.get_attribute("href")
                    urls.append(link)
            except:
                urls.append("Null")

            noticeId = []
            relatedNotice = []
            contractLineItemNumber = [] 
            departmentAgency = []
            subtier = []
            majorCommand = []
            subCommand = []
            subCommand2 = []
            subCommand3 = []
            office = []
            contractAwardDate = []
            contractAwardNumber = []
            deliveryOrderNumber = []
            contractorAwardedUniqueid = []
            contractorAwardedName = []
            contractorAwardedAddress = []
            allOptionsValue = []
            contractOpportunityType = []
            allDatesTimes = []
            originalPublishedDate = []
            originalDateOffersDue = []
            inactivePolicy = []
            originalInactiveDate = []
            initiative = []
            originalSetAside = []
            productServiceCode = []
            nAICSCode = []
            placeofPerformance = []
            description = []
            contractingOfficeaddressStreet = []
            contractingOfficeaddressState = []
            contractingOfficeaddressCountry = []
            primaryPointofContactName = []
            primaryPointofContactEmail = []
            primaryPointofContactNumber = []
            secondaryPointofContactName = []
            secondaryPointofContactEmail = []
            secondaryPointofContactNumber = []
            currentHistory = []

            #Loop on all urls and get his data
            for i in urls:
                options = Options()
                options.headless = True   
                driver = webdriver.Chrome()
                driver.minimize_window()
                driver.get(i)
                driver.implicitly_wait(0.8)
                content = driver.page_source
                print(i)
                #For getting notification ID
                try:
                    notice_id = driver.find_element(By.CLASS_NAME,'description')
                    noticeId.append(notice_id.text)
                except:
                    noticeId.append("Null")

                #For getting Related Notice 
                try:
                    store_related_notice = ''
                    related_notice = driver.find_element(By.ID, 'header-related-notice')
                    store_related_notice = related_notice.text
                    store_related_notice_split = store_related_notice.split('\n')
                    relatedNotice.append(store_related_notice_split[1])
                except:
                    relatedNotice.append("Null")

                #For getting Contract Line Item Number  
                try:
                    contract_line_item_number = driver.find_element(By.ID, 'award-line-item-number')
                    id = contract_line_item_number.find_element(By.TAG_NAME,'span')
                    contractLineItemNumber.append(id.text)
                except:
                    contractLineItemNumber.append("Null")

                #for getting departments
                try:
                    department = ''
                    departments = driver.find_element(By.ID,'header-hierarchy-level')
                    department = departments.text
                    department_split = department.split('\n')
                    departmentAgency.append(department_split[1])
                except:
                    departmentAgency.append("Null")

                #for getting subiter
                try:
                    subtier_value = ''
                    subtiers = driver.find_element(By.ID, 'header-hierarchy-level')
                    subtier_value = subtiers.text
                    subtier_value_split = subtier_value.split('\n')
                    subtier.append(subtier_value_split[3])
                except:
                    subtier.append("Null")

                #for getting Major Command
                try:
                    major_command = ''
                    major_commands = driver.find_element(By.ID, 'header-hierarchy-level')
                    major_command = major_commands.text
                    major_command_split = major_command.split('\n')
                    majorCommand.append(major_command_split[5])
                except:
                    majorCommand.append("Null")

                #for getting Sub Commands
                try:
                    sub_command = ''
                    sub_command_value = driver.find_element(By.ID, 'header-hierarchy-level')
                    sub_command = sub_command_value.text
                    sub_command_split = sub_command.split('\n')
                    if sub_command_split[6] == 'Sub Command':
                            subCommand.append(sub_command_split[7])
                except:
                    subCommand.append("Null")

                #for getting Sub Command 2
                try:
                    sub_command2 = ''
                    sub_command2_value = driver.find_element(By.ID, 'header-hierarchy-level')
                    sub_command2=sub_command2_value.text
                    sub_command2_split = sub_command2.split('\n')
                    if sub_command2_split[8] == 'Sub Command 2':
                            subCommand2.append(sub_command2_split[9])
                    else:
                        subCommand2.append("Null")
                except:
                    subCommand2.append("Null")

                #for getting Sub Command 3
                try:
                    sub_command3 = ''
                    sub_command3_value = driver.find_element(By.ID, 'header-hierarchy-level')
                    sub_command3=sub_command3_value.text
                    sub_command3_split = sub_command3.split('\n')
                    if sub_command3_split[10] == 'Sub Command 3':
                            subCommand3.append(sub_command3_split[11])
                except:
                    subCommand3.append("Null")

                # for getting office
                try:
                    office_address = ''
                    office_address_value = driver.find_element(By.ID, 'header-hierarchy-level')
                    office_address=office_address_value.text
                    office_address_split = office_address.split('\n')
                    office.append(office_address_split[-1])
                except:
                    office.append("Null")

                #for getting contract award date
                try:
                    store_contract_award_date = ''
                    contract_award_date =  driver.find_element(By.ID, 'award-date')
                    store_contract_award_date = contract_award_date.text
                    contract_award_date_split = store_contract_award_date.split('\n')
                    contractAwardDate.append(contract_award_date_split[1])
                except:
                    contractAwardDate.append("Null")

                #for getting contract award number
                try:
                    contract_award_number =  driver.find_element(By.ID, 'award-number')
                    contractAwardNumber.append(contract_award_number.text)
                except:
                    contractAwardNumber.append("Null")

                #for getting Dilevery award number
                try:
                    delivery_order_number=  driver.find_element(By.ID, 'order-number')
                    deliveryOrderNumber.append(delivery_order_number.text)
                except:
                    deliveryOrderNumber.append("Null")

                #for getting contractor awarded unique entity id
                try:
                    contractor_awarded_unique_id =  driver.find_element(By.ID, 'awarded-uei')
                    contractorAwardedUniqueid.append(contractor_awarded_unique_id.text)
                except:
                    contractorAwardedUniqueid.append("Null")

                #for getting contractor awarded name
                try:
                    contractor_awarded_name =  driver.find_element(By.ID, 'awarded-name')
                    contractorAwardedName.append(contractor_awarded_name.text)
                except:
                    contractorAwardedName.append("Null")

                #for getting contractor awarded address
                try:
                    contractor_award_address =  driver.find_element(By.ID, 'awarded-address')
                    contractorAwardedAddress.append(contractor_award_address.text)
                except:
                    contractorAwardedAddress.append("Null")

                #for getting all options value
                try:
                    all_options_value =  driver.find_element(By.ID, 'award-amount')
                    allOptionsValue.append(all_options_value.text)
                except:
                    allOptionsValue.append("Null")

                #for getting Contract Opportunity Type
                try:
                    contract_opportunity_type =  driver.find_element(By.ID, 'general-type')
                    contractOpportunityType.append(contract_opportunity_type.text)
                except:
                    contractOpportunityType.append("Null")

                #for getting All Dates/Times are 
                try:
                    all_dates_times =  driver.find_element(By.ID, 'general-notice-timezone')
                    allDatesTimes.append(all_dates_times.text)
                except:
                    allDatesTimes.append("Null")

                #for getting Original Published Dates
                try:
                    original_published_date =  driver.find_element(By.ID, 'general-original-published-date')
                    originalPublishedDate.append(original_published_date.text)
                except:
                    originalPublishedDate.append("Null")

                #for getting Original Date Offers Due
                try:
                    original_date_Offers_due=  driver.find_element(By.ID, 'general-original-response-date')
                    originalDateOffersDue.append(original_date_Offers_due.text)
                except:
                    originalDateOffersDue.append("Null")


                #for getting Inactive Policy
                try:
                    inactive_policy = driver.find_element(By.ID, 'general-archiving-policy')
                    inactivePolicy.append(inactive_policy.text)
                except:
                    inactivePolicy.append("Null")

                #for getting Original Inactive Date
                try:
                    original_inactive_date = driver.find_element(By.ID, 'general-original-archive-date')
                    originalInactiveDate.append(original_inactive_date.text)
                except:
                    originalInactiveDate.append("Null")

                #for getting Initiative
                try:
                    initiative_value = driver.find_element(By.ID, 'general-special-legislation')
                    initiative.append(initiative_value.text)
                except:
                    initiative.append("Null")

                #for getting  Original Set Aside
                try:
                    original_set_aside = driver.find_element(By.ID, 'classification-original-set-aside')
                    originalSetAside.append(original_set_aside.text)
                except:
                    originalSetAside.append("Null")

                #for getting  Product Service Code
                try:
                    product_service_code = driver.find_element(By.ID, 'classification-classification-code')
                    productServiceCode.append(product_service_code.text)
                except:
                    productServiceCode.append("Null")

                #for getting  NAICS Code
                try:
                    nAICS_code = driver.find_element(By.ID, 'classification-naics-code')
                    nAICSCode.append(nAICS_code.text)
                except:
                    nAICSCode.append("Null")

                #for getting  Place of Performance
                try:
                    place_of_performance = driver.find_element(By.ID, 'classification-pop')
                    placeofPerformance.append(place_of_performance.text)   
                except:
                    placeofPerformance.append("Null")

                #for getting  Description
                try:
                    description_value = driver.find_element(By.ID, 'description')
                    description_value_tag = description_value.find_element(By.TAG_NAME, 'div')
                    description.append(description_value_tag.text)
                except:
                    description.append("Null")

                #for getting  Attachments/Links
            

                #for getting contracting office address Street
                try:
                    addressStreet = driver.find_element(By.ID,'contracting-office-contracting-office-street')
                    contractingOfficeaddressStreet.append(addressStreet.text)
                except:
                    contractingOfficeaddressStreet.append("Null")

                #for getting contracting office address State
                try:
                    addressState = driver.find_element(By.ID,'contracting-office-city-contracting-office-state')
                    contractingOfficeaddressState.append(addressState.text)
                except:
                    contractingOfficeaddressState.append("Null")

                #for getting contracting office address Country 
                try:
                    addressCountry = driver.find_element(By.ID,'contracting-office-contracting-office-country')
                    contractingOfficeaddressCountry.append(addressCountry.text)
                except:
                    contractingOfficeaddressCountry.append("Null")

                #for getting Primary Point of Contact full name
                try:
                    primary_point_of_contact_name =  driver.find_element(By.ID, 'contact-primary-poc-full-name')
                    primaryPointofContactName.append(primary_point_of_contact_name.text)
                except:
                    primaryPointofContactName.append("Null")

                #for getting Primary Point of Contact email
                try:
                    primary_point_of_contact_email =  driver.find_element(By.ID, 'contact-primary-poc-email')
                    primary_point_of_contact_email_tag = primary_point_of_contact_email.find_element(By.PARTIAL_LINK_TEXT, 'a')
                    primaryPointofContactEmail.append(primary_point_of_contact_email_tag.text)
                except:
                    primaryPointofContactEmail.append("Null")

                # for getting Secondary Point of Contact number
                try:
                    store_primary_point_of_contact_number = ''
                    store_primary_point_of_contact_number =  driver.find_element(By.ID, 'contact-primary-poc-phone')
                    store_primary_point_of_contact_number_value = store_primary_point_of_contact_number.text
                    primary_point_of_contact_number_split = store_primary_point_of_contact_number_value.split('\n')
                    primaryPointofContactNumber.append(primary_point_of_contact_number_split[1])
                except:
                    primaryPointofContactNumber.append("Null")


                #for getting Secondary Point of Contact  full name
                try:
                    secondary_point_of_contact_name = driver.find_element(By.ID, 'contact-secondary-poc-full-name')
                    secondaryPointofContactName .append(secondary_point_of_contact_name.text)
                except:
                    secondaryPointofContactName.append("Null")

                #for getting   Secondary Point of Contact email
                try:
                    secondary_point_of_contact_email =  driver.find_element(By.ID, 'contact-secondary-poc-email')
                    secondary_point_of_contact_email_tag = secondary_point_of_contact_email.find_element(By.PARTIAL_LINK_TEXT, 'a')
                    secondaryPointofContactEmail.append(secondary_point_of_contact_email_tag.text)
                except:
                    secondaryPointofContactEmail.append("Null")

                # for getting Secondary Point of Contact number
                try:
                    store_secondary_point_of_contact_number = ''
                    store_secondary_point_of_contact_number =  driver.find_element(By.ID, 'contact-secondary-poc-phone')
                    store_secondary_point_of_contact_number_value = store_secondary_point_of_contact_number.text
                    secondary_point_of_contact_number_split = store_secondary_point_of_contact_number_value.split('\n')
                    secondaryPointofContactNumber.append(secondary_point_of_contact_number_split[1])
                except:
                    secondaryPointofContactNumber.append("Null")

                #for getting current history
                try:
                    current_history = driver.find_element(By.ID,'history')
                    current_history_tag = current_history.find_element(By.TAG_NAME, 'li')
                    currentHistory.append(current_history_tag.text)
                    a = np.array(currentHistory)
                    history = a
                except:
                    currentHistory.append("Null")

            rowData =list(zip(head, urls, noticeId, relatedNotice, contractLineItemNumber, departmentAgency, subtier, majorCommand, subCommand,subCommand2, subCommand3,office,  contractAwardDate,contractAwardNumber, deliveryOrderNumber, contractorAwardedUniqueid, contractorAwardedName, contractorAwardedAddress, allOptionsValue, contractOpportunityType, allDatesTimes, originalPublishedDate, inactivePolicy, originalInactiveDate, initiative, originalSetAside, productServiceCode, nAICSCode, placeofPerformance, description, contractingOfficeaddressStreet, contractingOfficeaddressState,contractingOfficeaddressCountry, primaryPointofContactName, primaryPointofContactEmail,primaryPointofContactNumber, secondaryPointofContactName, secondaryPointofContactEmail,secondaryPointofContactNumber,history))

            df = pd.DataFrame(rowData,columns=['Head', 'Links', 'Notice ID', 'Related Notice', 'Contract Line Item Number ', 'Department/Ind. Agency','Sub-tier','Major Command', 'Sub Command', 'Sub command 2', 'Sub Command 3', 'Office', 'Contract Aware Date','Contract Aware Number', 'Delivery order number', 'Contract Awarded Unique Entity ID', 'Contractor Awarded Name' , 'Contractor Awarded Address', 'All Options Value', 'Contract Opportunity Type', 'All Dates/Times', 'Original Published Date', 'Inactive Policy', 'Original Inactive Date', 'Initiative', 'Original Set Aside', 'Product Service Code', 'NAICS Code', 'Place of Performance', 'Description', 'Contracting Office Address', 'State','Country', 'Primary Point of Contact full name', 'Primary Point of Contact Email','Primary Point of Contact number', 'Secondary Point of Contact Name', 'Secondary Point of Contact Email', 'Secondary Point of Contact number', 'History'])

            df.to_csv('lists.csv', encoding='UTF-8',index=False)
            return render_template('index.html', url = url)
        except:
            print()
        

if __name__ == '__main__':
    app.run(debug=True , port=3000)