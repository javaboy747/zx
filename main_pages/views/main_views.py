from django.shortcuts import render

# Create your views here.


def main(request):
    """
     메인 출력
    """
    #question = get_object_or_404()
    #context = {'question': question}
    return render(request, 'main_pages/main_page.html')
