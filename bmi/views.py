from django.shortcuts import render


# Create your views here.
def bmi_calculate(request):
    contex = {}
    
    if request.method == 'POST':

        height = request.POST.get('height')
        weight = request.POST.get('weight')
        
        if height and weight:

            height = float(height)
            weight = float(weight)
            bmi = weight / ((height / 100) ** 2)

            if bmi < 18.5:

                status = "Vazn yetishmovchiligi"
                advice = "Sizda vazn yetishmovchiligi bor. Ratsioningizni boyitish tavsiya etiladi."

            elif bmi >= 18.5 and bmi <= 24.9:

                status = "Me'yoriy vazn"
                advice = "Ajoyib! Vazningiz me'yorda. Shu tarzda davom eting!"

            elif bmi >= 25 and bmi <= 29.9:

                status = "Ortiqcha vazn"
                advice = "Sizda biroz ortiqcha vazn bor. Jismoniy faollikni oshirish tavsiya etiladi."

            else:

                status = "Semizlik"
                advice = "Sizda semizlik darajasi mavjud. Mutaxassis bilan maslahatlashish tavsiya etiladi."

            contex = {'bmi': round(bmi, 1),
                      'status': status,
                      'advice': advice
                      }
            
    return render(request, 'index.html', contex)