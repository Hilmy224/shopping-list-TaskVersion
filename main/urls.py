from django.urls import path
from main.views import show_main, create_product, show_xml,show_json,show_xml_by_id, show_json_by_id 
from main.views import register,login_user,logout_user,add_amount,lessen_ammount,delete_product,edit_product
from main.views import get_product_json,add_product_ajax,delete_item_ajax
from main.views import create_product_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('addAmount/<int:id>/',add_amount,name='add_amount'),
    path('lessenAmount/<int:id>/',lessen_ammount,name='lessen_amount'),
    path('deleteProduct/<int:id>/',delete_product,name='delete_product'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('get-product/', get_product_json, name='get_product_json'),
   path('create-ajax/', add_product_ajax, name='add_product_ajax'),
   path('delete-ajax/<int:id>/',delete_item_ajax,name='delete_product_ajax'),
   path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]