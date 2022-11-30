from django.contrib import admin
from  .models import Categoria,Contato

# Modifica a exbição no admin com os camos que desejamos
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'sobrenome','telefone','email','data_criacao','categoria','mostrar')
    list_display_links = ('id',"nome",'sobrenome') #Cria um link para edição
    ## list_filter = ('nome','sobrenome')
    list_per_page = 10
    search_fields = ('nome','sobrenome','telefone')
    list_editable = ('telefone','mostrar')



# Para os model ser exibido no site admin
# precisa ser registrado
admin.site.register(Categoria)
admin.site.register(Contato,ContatoAdmin)
