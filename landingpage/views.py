from django.shortcuts import render
from .models import Image

def image_list(request):
    images = Image.objects.all()
    return render(request, 'image_list.html', {'images': images})

def add_image(request):
    # Cria um objeto Image
    image = Image()
    image.title = 'Minha Foto'
    image.description = 'Esta é uma foto que tirei em uma viagem.'
    image.image_file = 'imagens/minhafoto.jpg'
    
    # Salva o objeto no banco de dados
    image.save()
    
    # Renderiza um template com a mensagem de sucesso
    return render(request, 'sucesso.html', {'mensagem': 'Imagem adicionada com sucesso!'})

