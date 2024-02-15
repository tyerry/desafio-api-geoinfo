import requests

def findCountry(region, keyword):
    response = []
    currentPage = 1
    maxPages = 1
    
    while currentPage <= maxPages:
        url = f"http://127.0.0.1:8000/countries?region={region}&keyword={keyword}&page={currentPage}"
        r = requests.get(url)

        if r.status_code == 200:
            success = r.json()
            maxPages = success['totalPages']
            
            for data in success['data']:
                country={
                    'name':data['name'],
                    'population':data['population']
                }
                
                response.append(country)
                
            currentPage += 1
        else:
            print("Falha na requisição: ",r.status_code)
            break
    
    return response
    
if __name__ == '__main__':
    findCountry(1,'BBB')