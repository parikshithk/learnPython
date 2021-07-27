import smtplib, imapclient

conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()  # this starts encryption
conn.login('parikshith@writer.com', 'epytbdozjmjmojla')  # Using the google app password
conn.sendmail('parikshith@writer.com', 'testuser@writer.com',
              'Subject: Test email.. \n\n Dear testuser, \nThis is the body of the email. \n\n-PK')
conn.quit()

# conn = imapclient.IMAPClient('smtp.gmail.com', ssl=True)
# conn.login('parikshith@writer.com', 'epytbdozjmjmojla')
# UIDs = conn.search(['SINCE 26-Jul-2021'])
# print(UIDs)
