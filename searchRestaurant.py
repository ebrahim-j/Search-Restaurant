import urllib2
import json
 
 
def locu_search(query):
    url = 'https://api.locu.com/v1_0/venue/search/?api_key=9fb8cd70cb34cab8e83690473133f51943b5c93f'
    locality = query.replace(' ', '%20')
    final_url = url + "&locality=" + locality + "&category=restaurant"
    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)
   
    for item in data['objects']:
        print item['name'], item['phone']
