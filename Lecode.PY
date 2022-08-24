#Ce programe va permettre de resortir les valeurs de stoks pour un ou des utilisateurs
#Il permettra aussi de tenir un regisrtre d'utilisateurs
from tempfile import TemporaryDirectory


start_date="2022-07-15"
end_date="2022-07-22"
from ast import Break
import yfinance as yf


userlist=[]
usernam=input("Hello ! Thanks your for using my programe. Lets start by telling me your Username: ")
    

listeofstock=["TSLA","ADM","GOOGL","GOOG","AMZN","ADBE","AXP","AAPL","ATO","BAC","EBAY","FDX","ETSY","GS","IBM","JNJ","JPM","MCHP","MU","NFLX","NKE"]


if usernam in userlist:
    print("Glad to see you again "+usernam)
else:
    print("First time I see you around. Glad to meet you "+usernam)
    userlist.append(usernam)

print("--------------------------------------")


print(listeofstock)

request=input("What stock are you interrested in today ?: ")

def lecal(x):
    vehi=yf.Ticker(str(x))
    print(vehi.history(start=start_date, end=end_date))
    print("")
    print("Tap in END to end the program " + 
        "/To change user tape CHANGE")
    print("-----------------------------------------------------------------")
    print(listeofstock)
    



while request != "END":
    if request in listeofstock:
        lecal(request)
        request=input()
    elif request =="CHANGE":
        newuser=input("Who am I talking to right now ?: ")
        if newuser in usernam:
            print("Glad to see you again "+newuser)
            print(listeofstock)
            newrequest=input("What stock value you want to see today?: ")
            if newrequest in listeofstock:
                lecal(newrequest)
            elif request=="END":
                print("Thank you for using my program today see you soon LOVEyou")
        else:
            userlist.append(newuser)
            print("First time We meet "+newuser)
            print("-----------------------------------------------------------------")
            print(listeofstock)
        request=input("What stock value you want to see today?: ")
    else:
        print("Please make sur the stock you want is in upper case and in the list provided")
        break
request=input()
if request in listeofstock:
    lecal(request)
print("Thank you" +str(userlist)+ "for using my program today! See you soon LOVE you") 

