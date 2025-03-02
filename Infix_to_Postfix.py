from stack import Stack


# Función para añadir el símbolo "$" como operador de concatenación
def addConcatenationSymbol(regEx):

    # Lista de operadores
    operators = {'+', '*', '|', '(', ')'}

    result = []

    for i in range(len(regEx)):
        current = regEx[i]
        # Agregar "$" cuando se encuentre una concatenación
        if current not in operators:
            result.append(current)
            if (i + 1 < len(regEx) and regEx[i + 1] not in
                    operators and regEx[i + 1] != ')'):
                result.append('$')
        elif current in operators:
            result.append(current)

    return ''.join(result)


def shuntingYard(regEx, alphabet):

    # Operadores con peso de prioridad
    precedence = {
        '*': 3,
        '+': 3,
        '$': 2,
        '|': 1,
        '(': 0,
        ')': 0
    }

    # Lista de operadores
    operators = list(precedence.keys())

    # Pila temporal para guardar operadores
    stack = Stack()

    # Arreglo para construir la notación postfija
    postFix = []

    # Arreglo con los elementos de la expresión regular
    regEx = addConcatenationSymbol(regEx)
    token = list(regEx)
    # Recorremos el token operandos y operadores
    for element in token:

        # Si el elemento es un operando dentro del alfabeto
        # válido se añade al postfijo
        if element in alphabet:
            postFix.append(element)

        elif element in operators:
            # Si el elemento es '(' se añade a la fila
            if element == '(':
                stack.push(element)

            # Si el elemento es un ')' se hace backtraking
            # para encontrar su respectivo '('
            elif element == ')':

                while not stack.empty() and stack.peek() != '(':
                    postFix.append(stack.pop())
                stack.pop()
            else:
                while (not stack.empty() and precedence[stack.peek()]
                       >= precedence[element]):
                    postFix.append(stack.pop())
                stack.push(element)

    while not stack.empty():
        postFix.append(stack.pop())

    return ''.join(postFix)
