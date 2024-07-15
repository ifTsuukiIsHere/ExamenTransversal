from django.shortcuts import render, redirect
from django.contrib import messages
from ecommerce.db.models import Pedido

def guardar_direccion_envio(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        correo_electronico = request.POST.get('correo_electronico')
        numero_telefono = request.POST.get('numero_telefono')
        detalles_envio = request.POST.get('detalles_envio')

        if nombre and direccion and correo_electronico and numero_telefono:
            pedido = Pedido(
                nombre=nombre,
                direccion=direccion,
                correo_electronico=correo_electronico,
                numero_telefono=numero_telefono,
                detalles_envio=detalles_envio
            )
            pedido.save()
            messages.success(request, 'Datos almacenados.')
            return redirect('pago') 
        else:
            messages.error(request, 'Rellene los campos vacíos.')

    return render(request, 'Guardar_direccion_envio.html')
