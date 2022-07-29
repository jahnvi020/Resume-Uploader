from django.shortcuts import render
from .forms import ResumeForm
from .models import resume
from django.views import View

class HomeView(View):  #class based view
    def get(self,request):
        form=ResumeForm()
        candidates=resume.objects.all()
        return render(request,'resume/index.html',{'candidates':candidates,'form':form})
        
    # submission of data-post method
    def post(self,request):
        form=ResumeForm(request.POST,request.FILES)  #request.FILES - because files are also submitted
        if form.is_valid():
            form.save()
            return render(request, 'resume/index.html', {'form':form})

class CandidateView(View):
    def get(self,request,pk):
        candidate= resume.objects.get(pk=pk)
        return render(request,'resume/candidate.html',{'candidate':candidate})

