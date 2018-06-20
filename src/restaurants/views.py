from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    html_="""<!-- A trilogy of books with numbered volumes. -->
<div>
  <p>
    The <strong>Lord of the Rings</strong> is an English-language fictional trilogy by J. R. R. Tolkien (1892-1973).
  </p>
  <p>
    The books in the trilogy are:
  </p>
  <ul>
    <li>Vol. 1: The Fellowship of the Ring</li>
    <li>Vol. 2: The Two Towers</li>
    <li>Vol. 3: The Return of the King</li>
  </ul>
</div> """
    return HttpResponse(html_)
    #return render(request, "home.html") 