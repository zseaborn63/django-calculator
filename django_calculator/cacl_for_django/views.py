from django.shortcuts import render, render_to_response


# Create your views here.

def make_op(operator):
    pass


def new_view(request):
    first_num = request.GET.get("first_num")
    second_num = request.GET.get("second_num")
    operator = request.GET.get("operator")
    op_dict = {
        "Add": "+",
        "Subtract": "-",
        "Divide": "/",
        "Multiply": "*"
    }
    if operator == None:
        context = {
            "calculation": "0",
            "equation": " "
        }
    else:
        try:
            equation = first_num + op_dict[operator] + second_num
            answer = float(eval(equation))
            context = {
                "calculation": answer,
                "equation": equation +  " = {}".format(answer)
            }
        except:
            context = {
                "calculation": "This cannot be computed",
                "equation": "Try again!"
            }
    return render_to_response(template_name="math.html", context=context)

def math_view(request):
    first_num = request.GET.get("first_num")
    second_num = request.GET.get("second_num")
    operator = request.GET.get("operator")
    if first_num and second_num:
        if operator == "Divide":
            if int(second_num) == 0:
                calc = "You clearly don't understand math"
                op = None
            else:
                calc = int(first_num) / int(second_num)
                op = "/"
        elif operator == "Multiply":
            calc = int(first_num) * int(second_num)
            op = "*"
        elif operator == "Subtract":
            calc = int(first_num) - int(second_num)
            op = "-"
        else:
            calc = int(first_num) + int(second_num)
            op = "+"
    else:
        calc = None
        op = None
    context =  {
        "calculation": "{}".format(calc),
        "first_number": first_num,
        "second_number": second_num,
        "operator": operator,
        "equation": "{} = {} {} {}".format(calc, first_num, op, second_num)
                }
    return render_to_response(template_name="math.html", context=context)