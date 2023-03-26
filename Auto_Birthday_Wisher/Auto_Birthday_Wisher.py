#Automatic Birthday Wish To Auto-Wish
'''from numpy import append
import pandas as pd
import datetime
import smtplib 

# Enter your authentication details
GMAIL_ID = ''
GMAIL_PSWD = ''

def sendEmail(to,sub,msg):
    print(f"Email to {to} sent with subject {sub} and message {msg}")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PSWD)
    s.sendmail(GMAIL_ID, to, f"Subject: {sub}\n\n{msg}")
    s.quit()


if __name__=="__main__":
    df = pd.read_excel("C:\\Users\\Dell\\Desktop\\Python files\\Python Projects linked with the my_drive\\Birthday List.xlsx")
    #print(df)
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y") 
    #print(today)
    writeInd = []
    for index,item in df.iterrows():
        #print(index,item["Birthday"])
        bday = item["Birthday"].strftime("%d-%m")
        #print(bday)
        if (today == bday) and yearNow not in str(item["Year"]):
            sendEmail(item["Email.id"], "Happy Birthday",item["Dialogue"])
            writeInd.append(index)
    
    #print(writeInd)
    for i in writeInd:
        yr = df.loc[i,"Year"]
        #print(yr)
        df.loc[i,"Year"] = str(yr) + "," + str(yearNow)
        #print(df.loc[i,"Year"])

    df.to_excel('C:\\Users\\Dell\\Desktop\\Python files\\Python Projects linked with the my_drive\\Birthday List.xlsx',index=False)'''    

























































