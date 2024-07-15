import requests

url = "https://aladhan.p.rapidapi.com/timingsByCity"

querystring = {"country":"Uzbekistan","city":"Jizzax","school":"1"}

headers = {
	"X-RapidAPI-Key": "c04aa4972bmsh1e00bfe24d579e0p1e9e3ejsn9fe4308f1431",
	"X-RapidAPI-Host": "aladhan.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

city = "Toshkent"
url = f"https://islomapi.uz/api/present/day?region={city}"

r = requests.get(url).json()['times']
morning = r.get('tong_saharlik')
sun = r.get('quyosh')
noon = r.get('peshin')
century = r.get('asr')
evening = r.get('shom_iftor')
huft = r.get('hufton')

print(morning)