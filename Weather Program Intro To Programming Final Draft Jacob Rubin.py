#the following program is designed to allow a user to select to look for a weather forecast by either zip code or city name until they're finished.
import requests
import json
#imports necessary modules

def get_web_data(zip=None, city=None):
    baseURL = "https://api.openweathermap.org/data/2.5/weather?units=imperial"
    #the main URL to access API results in imperial units

    apiid = "806498720dab14528e3ff1595fad142a"
    #my individual API ID to allow access

    if zip is not None:

        baseURL += "&zip="+str(zip)+",us"
    else:
        baseURL += "&q="+str(city)+",us"

    baseURL += "&appid="+str(apiid)

    r = requests.get(baseURL)

    return r
#combines components depending on selection to create the right URL to access requested information

def display(resp):
    if resp.status_code == 200:
        data = resp.json()
        print("Your search results came through successfully and will appear below.")
        print()
        print(
f"""{data['name']} Weather Forecast:
Type: {data['weather'][0]['description']}
Wind speed : {data['wind']['speed']} miles/hr
Visibility : {data['visibility']} m
Min. Temp : {data['main']['temp_min']} F
Max Temp : {data['main']['temp_max']} F """)
        print()
        #extra prints to create space for the sake of appearance while running
    else:
        print("Your request has failed. Error: ", resp.status_code, "That request was invalid or not in our records. Please try something else.")
        #either prints the requested information or provides the user with the error associated with the reason for failure.

def main():
    #main function to ask users for their selection regarding searching by Zip or City Name
    while True:

        choice = int(
            input(
                "How would you like to search for a weather forecast? \n1 - By Zip Code\n2 - By City Name\n3 - Stop Searching\n"))
        if choice == 1:

            try:

                zCode = input("Enter a 5 digit zip code: ")

                resp = get_web_data(zCode, None)
                display(resp)
            except Exception as ex:
                print("Error: ", ex)
                #the first choice is to search by Zip
        elif choice == 2:
            try:
                cname = input("Enter a City Name: ")

                resp = get_web_data(None, cname)
                display(resp)
            except Exception as ex:
                print("Error: ", ex)
                #the second choice is to search by City Name
        elif choice == 3:
            break
        #the third choice is to stop searching
        else:
            print("That choice was invalid.\n")
            

if __name__ == "__main__":
    main()
