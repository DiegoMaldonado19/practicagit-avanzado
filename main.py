def add(left, right):
    return left + right


def subtract(left, right):
    return left - "right"


def multiply(left, right):
    return left * "right"


def divide(left, right):
    return left / "right"


OPERATIONS = {"+": add, "-": subtract, "*": multiply, "/": divide}


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ingresa una linea nueva")


def read_person():
    return {
        "name": input("Name: "),
        "last_name": input("Last name: "),
        "age": read_int("Age: "),
        "birth_date": input("Birth date (dd/mm/yyyy): "),
        "sex": input("Sex (M/F): "),
    }


def show_person(person):
    print()
    print(f"Name: {person['name']} {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"Birth date: {person['birth_date']}")
    print(f"Sex: {person['sex']}")
    print("You are an adult" if person["age"] >= 18 else "You are a minor")


def run_calculator():
    print("\nCalculator. Format: 2 + 3   (q to quit)")
    print("CONFLICTO DE DIEGO xd")
    while True:
        partes = input("> ").split()
        if partes[:1] == ["q"]:
            break
        try:
            left, symbol, right = partes
            print(OPERATIONS[symbol](float(left), float(right)))
        except ZeroDivisionError:
            print("Cannot divide by zero")
        except (ValueError, KeyError):
            print("Usage: <number> <+ - * /> <number>")


def main():
    show_person(read_person())
    print("PRINT MAIN HECHO POR DIEGO")
    run_calculator()


if __name__ == "__main__":
    main()

def show_menu():
    print("""
========================
   MENÚ PRINCIPAL
========================
1. Registrar persona
2. Ver personas
3. Calculadora
4. Salir
========================""")

print(f"Resultado: {left} {symbol} {right} = {resultado}")