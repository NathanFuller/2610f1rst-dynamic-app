from django.shortcuts import render
from django.http import HttpResponse


#It would be really cool if this page were a dynamic list of the pages on my site.
#Maybe figure that out.
def index(request):
    document = """
<h3>This is the homepage to Nate's dynamic django web project.</h3>
<p>Links to the sites hosted here:</p>
<ul>

    <li><a href='f1rst'>F1rst</a></li>
</ul>
    """
    
    return HttpResponse(document)