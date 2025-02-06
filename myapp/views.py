from django.shortcuts import render
from myapp.forms import Product_form
from django.views import View
from myapp.models import Product



# lh:8000/create/

class ProductCreateView(View):
    def get(self, request):
        form = Product_form

        return render(request, 'index.html', {'form': form})

    def post(self, request):
        form = Product_form(request.POST)  
        
        if form.is_valid():
            
            print(form.cleaned_data)

            Product.objects.create(**form.cleaned_data)

        else:
            print(form.errors)

        form=Product_form
        
        return render(request, 'index.html',{'form':form}) 
    

    
# lh:8000/read/

class Product_Read(View):

    def get(self,request):

        data=Product.objects.all()
        
        return render(request,"read.html",{"data":data})
    


# lh:8000/update/

class Product_update(View):

    def get(self,request,**kwargs):

        id=kwargs.get("pk")

        data=Product.objects.get(id=id)

        form=Product_form(instance=data)

        return render(request,"update.html",{"form":form})
    

    def post(self,request,**kwargs):
        
        id=kwargs.get("pk")

        data=Product.objects.get(id=id)

        form=Product_form(request.POST,instance=data)

        if form.is_valid():

            form.save()

        form=Product_form

        return render(request,"update.html",{"form":form})
    


# lh:8000/delete/

class Product_delete(View):

    def get(self,request,**kwargs):
        
        id=kwargs.get("pk")

        Product.objects.get(id=id).delete()

        return render(request,"delete.html")
    

    
     


