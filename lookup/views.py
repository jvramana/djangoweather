from django.shortcuts import render

# Create your views here.
def home(request):
    #https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=FDF16C76-6FA4-458D-8CC6-A993DCF08776
    import json
    import requests
    
    if request.method == 'POST':
        zipCode = request.POST['zipcode']

        apiRequest = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zipCode+"&distance=5&API_KEY=FDF16C76-6FA4-458D-8CC6-A993DCF08776")

        try:
            api=json.loads(apiRequest.content)
        except Exception as e:
            api="Error..."

        return render(request,'home.html',{'api':api} )

    else:

        apiRequest = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=FDF16C76-6FA4-458D-8CC6-A993DCF08776")

        try:
            api=json.loads(apiRequest.content)
        except Exception as e:
            api="Error..."

        return render(request,'home.html',{'api':api} )


def about(request):
    return render(request,'about.html',{} )