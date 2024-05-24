
import requests

menu_list_url='http://127.0.0.1:8000/menu_list'
def menulist(request):
    # menu_list_request=requests.post(menu_list_url)
    # menu_list_response=menu_list_request.json()
    menu_list_response = request.session.get('menu_list')
    print('menu_list_response ',menu_list_response )
    return {'menu_list':menu_list_response}