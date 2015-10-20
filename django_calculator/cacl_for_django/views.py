from django.shortcuts import render, render_to_response


# Create your views here.


def math_view(request):
    first_num = int(request.GET.get("first_num"))
    second_num = int(request.GET.get("second_num"))
    operator = request.GET.get("operator")
    if operator == "Divide":
        if second_num == 0:
            calc = "You clearly don't understand math"
        else:
            calc = first_num / second_num
    elif operator == "Multiply":
        calc = first_num * second_num
    elif operator == "Subtract":
        calc = first_num - second_num
    else:
        calc = first_num + second_num
    context =  {
        "calculation": "{}".format(calc),
        "first_number": first_num,
        "second_number": second_num,
        "operator": operator
                }
    return render_to_response(template_name="math.html", context=context)