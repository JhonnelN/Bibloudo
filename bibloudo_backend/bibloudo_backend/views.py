from django.http import HttpResponse
from django.template import Template, Context


def carrera_materias(request):
    doc_externo = open("/home/ubuntu/proyectos/Bibloudo/mainsistemas.html")

    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context()

    documento = plt.render(ctx)

    return HttpResponse(documento)
