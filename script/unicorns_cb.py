import requests
import pandas as pd 

def baixar_data():
    url = "https://www.cbinsights.com/research-unicorn-companies.json"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data)
    df.to_csv("data/cbinsights_unicorns.csv", index=False, encoding="utf-8")

# so roda diretamente 
if __name__ == "__main__":
    baixar_data()
