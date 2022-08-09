
from .models import Post

def search(request):
    
    title = list(Post.objects.values_list('title',flat = True))
    b = list(Post.objects.all())
    body = [x.get_absolute_url() for x in b ]
    dic = dict(zip(title,body))
    
    return {'search':dic}