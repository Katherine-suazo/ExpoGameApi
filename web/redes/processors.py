from .models import LinkRed

def ctx_dict(request):
    ctx = {}
    link = LinkRed.objects.all()
    
    for l in link:
        ctx[l.key] = l.url
    return ctx
