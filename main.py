import requests
import selectorlib



URL = "http://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def scrape(url):
    """
    Scrape the web page
    :param url:
    :return:
    """
    r = requests.get(URL, headers=HEADERS)

    data = r.text
    return data



def extract(data):
    extractor = selectorlib.Extractor.from_yaml_file("extractor.yaml")
    print(extractor.extract(data))
    value = extractor.extract(data)["tours"]
    return value

def send_email():
    print("Sending email...")

def store_extracted_data(data):
    with open("data.txt", "a", encoding="utf-8") as file:
        file.write(data + "\n")

def read_extracted_data():
    with open("data.txt", "r", encoding="utf-8") as file:
        return file.read()

if __name__ == "__main__":
    data = scrape(URL)
    print(data)
    tour = extract(data)
    print(tour)

    if tour != "No upcoming tours":
        content = read_extracted_data()
        if tour not in content:
            store_extracted_data(tour)
            send_email(tour)
    else:
        print("No email sent")

