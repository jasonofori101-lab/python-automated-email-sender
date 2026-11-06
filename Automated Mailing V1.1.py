''' Generating customized email previews from reusable templates.'''

contacts = [
    {'name': 'Michael', 'email': 'michealsworld@gmail.com'},
    {'name': 'John', 'email': 'johndoe@gmail.com'},
    {'name': 'Jane', 'email': 'janedoe@gmail.com'}

]

company_list = {
    'company1': 'Stryker',
    'company2': 'Merck',
    'company3': 'Google'
}
templates = {
    'acceptance': '''
    ----------------------
    EMAIL PREVIEW
    ----------------------
    To: {email}

    Hello {name}, 

    Thank you so much for your interest in {company}!
    After reviewing your application, we've decided that
    you are a good fit for this position and thus we're extending 
    an offer for a full-time position. The offer is attached to this email.
    Please let us know if you have any questions.

    Best Regards,
    {company} Inc.'''

    ,
    'rejection': '''
    ----------------------
    EMAIL PREVIEW
    ----------------------
    To: {email}

    Hello {name}
    Thank you for your interest in {company}. After reviewing your application,
    we've decided to move forward with applicants for this position. Please know
    that this not reflect your abilities and that you are still open to applying 
    to other positions at this time.

    Best Regards,
    {company} Inc. '''

}


companies = list(company_list.values())

#Company Selection

def select_company(companies):
        company_options = []

        for number_option, company in enumerate(companies, 1):
            print(f'{number_option}. {company}')
            company_options.append(company.lower())

        while True:
            company_choice = input('\nWhat company would you like to choose?: ').strip().lower()

            if company_choice.isdigit() or company_choice.lstrip('-').isdigit():
                company_choice = str(int(company_choice))

                if int(company_choice) > len(companies):
                    print('Please enter a number or company from the list.')
                elif int(company_choice) == 0 :
                    print('Please enter a number or company from the list.')
                elif '-' in company_choice:
                    print('Please enter a number or company from the list.')
                else:
                    break
            elif company_choice not in company_options:
                print('I don\'t understand. Please enter a number or a company from the list.')
            else:
                break

        for number_option, company in enumerate(companies, 1):

            if company_choice == str(number_option):
                return company
            elif company_choice.lower() == company.lower():
                return company


#Recipient Selection

def select_recipient(contacts):
    #Building the list
        print('\nRecipient Selection\n')

        for number_option,contact in enumerate(contacts,1):
            print(f'{number_option}. {contact['name']}')

        print(f'{len(contacts) +  1}. Everyone')

        while True:
            contact_choice = input(
                '\nPlease select who you would like to contact(name/number): \n').lower().strip()

            if contact_choice.strip().lower() == 'everyone' or contact_choice == str(len(contacts) + 1):
                print('\nYou chose: Everyone\n')
                return contacts

            for number_option, contact in enumerate(contacts, 1):
                if contact_choice == contact['name'].lower() or contact_choice == str(number_option):

                    print(f'\nYou chose: {contact['name']}')
                    return [contact]


            else:
                print('\nPlease select from the options given\n')



#Email template section

def select_template(templates):
    while True:
        choose_template: str = input('''Select Template Type:
        1. Acceptance
        2. Rejection
        Type Response Here: 
        ''').strip().lower()


        if choose_template in ('acceptance','1', '1.'):
                return templates['acceptance']

        if choose_template in ('rejection','2' , '2.'):
               return templates['rejection']

        else:
            print('I don\'t understand. Please make sure that you choose one of the options above.')


#Printing message

def generate_emails(selected_contacts, chosen_template, chosen_company):

    for contact in selected_contacts:
        message = chosen_template.format(name = contact['name'], email = contact['email'] , company = chosen_company)
        print(message)

#Running the code
def main(): 
    while True:
        print('Welcome to Automated Email Preview Generator V1!.')
    
        chosen_company = select_company(companies)
        print(f'\nYou chose: {chosen_company}')
    
        selected_contacts = select_recipient(contacts)
    
        chosen_template = select_template(templates)
    
        generate_emails(selected_contacts, chosen_template, chosen_company)


        while True:
            more_emails = input(f'\nWould you like to print out more emails?(y/n)\n').strip().lower()
            if more_emails in ('yes', 'y','no', 'n'):
                break
            else:
                print('\nI don\'t understand. Please choose between (y/n).\n')
        if more_emails in ('no', 'n'):
            break

if __name__ == '__main__':
    main()
#Complete

