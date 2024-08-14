from django.shortcuts import render

# Create your views here.


def home(request):
    a = [
       {
           "img":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTbCZAyI-AGsucfeIHBwDqxF0OYtgVhYSm9Eg&s",
           "title":"Shoe",
           "description":"This is the best shoe in the world"
       },{
           "img":"https://assets.myntassets.com/dpr_1.5,q_60,w_400,c_limit,fl_progressive/assets/images/27989168/2024/3/2/5ef86fa4-73e3-4266-8d81-d9921dded8751709348581018SidhidataWomensPrintedReadyToWearSareeWithUnstitchedBlousePi1.jpg",
           "title":"Saree",
           "description":"This is the best saree in the world"
       },{
            "img":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyW7l-lLoY4nBYEnqA9ydYbUU56CgDtaq-rQ&s",

           "title":"Camera",
           "description":"This is the best camera in the world"

       }
    ]
    context = {
        'cards':a
    }
    return render(request,"index.html",context)