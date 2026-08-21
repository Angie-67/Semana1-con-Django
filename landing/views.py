from django.shortcuts import render


def home(request):
    contexto = {
        'titulo': 'TechNova Solutions',
        'eslogan': 'Transformamos ideas en soluciones digitales',
        'caracteristicas': [
            {
                'icono': '🚀',
                'titulo': 'Rendimiento',
                'descripcion': 'Aplicaciones rápidas y escalables que crecen con tu negocio.',
            },
            {
                'icono': '🔒',
                'titulo': 'Seguridad',
                'descripcion': 'Protección de datos con los más altos estándares de la industria.',
            },
            {
                'icono': '📱',
                'titulo': 'Responsive',
                'descripcion': 'Diseño adaptable a cualquier dispositivo: móvil, tablet y desktop.',
            },
            {
                'icono': '⚙️',
                'titulo': 'Integración',
                'descripcion': 'Conectamos tus sistemas existentes con nuestras plataformas.',
            },
        ],
        'estadisticas': [
            {'numero': '+150', 'etiqueta': 'Proyectos completados'},
            {'numero': '+80', 'etiqueta': 'Clientes satisfechos'},
            {'numero': '+10', 'etiqueta': 'Años de experiencia'},
        ],
    }
    return render(request, 'landing/index.html', contexto)
