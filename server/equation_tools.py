from sympy import *
from flask import jsonify

x = symbols('x')

# convert user typed expression to sympy expression
def _convert_to_sympy(expression):

    # remove all spaces
    expression = expression.replace(' ', '')

    # replace ^ with **
    expression = expression.replace('^', "**")

    # adding multiplication signs where needed
    b_sym = ['x', '(', 'l', 's', 'c', 't']
    for i in range(1, len(expression)):
        if expression[i] in b_sym and (expression[i-1] == 'x' or expression[i-1] == ')' or expression[i-1].isdigit()):
            expression = expression[:i] + '*' + expression[i:]
        

    # parsing the logs
    def convert_log(expression):
        pass
        

    return sympify(expression)

# compute first two derivatives of expression
def _compute_derivatives(expression):

    # convert expression to sympy expression
    expression = _convert_to_sympy(expression)

    # compute first derivative
    first_derivative = Derivative(expression, x)

    # compute second derivative
    second_derivative = Derivative(expression, x, x)

    return [expression, str(first_derivative.doit()), str(second_derivative.doit())]

# compute the roots of the expression
def _get_roots(expression):

    # convert to sympy expression
    expression = _convert_to_sympy(expression)

    # compute the roots
    roots = solve(expression, x)

    # return jsonify({
    #     "roots": roots
    # })

    return [str(root) for root in roots]


# find vertical asymptotes
def _get_vertical_asymptotes(expression):

    # convert to sympy expression
    expression = _convert_to_sympy(expression)

    vertical_asmyptotes = []

    # get undefined points
    singular_points = singularities(expression, x)

    # check left/right behaviour
    for point in singular_points:

        # get left and right limits
        left_limit = limit(expression, x, point, dir='-')
        right_limit = limit(expression, x, point, dir='+')

        # check if limits are plus/minus infinity
        if oo in [left_limit, right_limit] or -oo in [left_limit, right_limit]:
            vertical_asmyptotes.append(point)
    
    return vertical_asmyptotes

# get horizontal asymptotes
def _get_horizontal_asymptotes(expression):

    # convert to sympy expression
    expression = _convert_to_sympy(expression)

    horizontal_asmyptotes = []

    # get limits at infinity
    left_limit = limit(expression, x, -oo)
    right_limit = limit(expression, x, oo)

    return [str(left_limit), str(right_limit)]

# get the y-intercept
def _get_y_intercept(expression):

    # convert to sympy expression
    expression = _convert_to_sympy(expression)

    # get y-intercept
    y_intercept = expression.subs(x, 0)

    return str(y_intercept)

# get extrema 
def _get_extrema(expression):

    # convert to sympy expression
    expression = _convert_to_sympy(expression)

    # find the critical points
    critical_points = solve(Derivative(expression, x), x)

    # get the second derivative
    second_derivative = Derivative(expression, x, x)

    local_mins = []
    local_maxs = []

    # check the second derivative at the critical points
    for point in critical_points:
        if second_derivative.subs(x, point) > 0:
            local_mins.append(str(point))
        elif second_derivative.subs(x, point) < 0:
            local_maxs.append(str(point))

    return [local_mins, local_maxs]

# get points of inflection
def _get_points_of_inflection(expression):
 # convert to sympy expression
    expression = _convert_to_sympy(expression)

    # find the critical points
    critical_points = solve(Derivative(expression, x, x), x)

    # get the second derivative
    third_derivative = Derivative(expression, x, x, x)

    points_of_inflection = []

    # check the second derivative at the critical points
    for point in critical_points:
        if third_derivative.subs(x, point) != 0:
            points_of_inflection.append(str(point))
    
    return points_of_inflection



# return everything in a json
def get_function_information(expression):
    return jsonify({
        "firstDerivative": _compute_derivatives(expression)[1],
        "secondDerivative": _compute_derivatives(expression)[2],
        "yIntercept": _get_y_intercept(expression),
        "roots": _get_roots(expression),
        "extrema": _get_extrema(expression),
        "inflectionPoints": _get_points_of_inflection(expression),
        "verticalAsymptotes": _get_vertical_asymptotes(expression),
        "horizontalAsymptotes": _get_horizontal_asymptotes(expression)
    })