def kgv(numbers):
    """Berechnet das kleinste gemeinsame Vielfache (kgV) für eine Liste von Zahlen"""

    # Funktion zur Berechnung des kgV für zwei Zahlen
    def kgv_two_numbers(a, b):
        return abs(a * b) // ggt([a, b])

    # Überprüfe, ob die Liste mindestens zwei Zahlen enthält
    if len(numbers) < 2:
        raise ValueError("Die Liste sollte mindestens zwei Zahlen enthalten.")

    # Berechne das kgV iterativ für alle Zahlen in der Liste
    result = numbers[0]
    for num in numbers[1:]:
        result = kgv_two_numbers(result, num)
    return result


def ggt(numbers):
    """Berechnet den größten gemeinsamen Teiler (ggT) für eine Liste von Zahlen"""
    def ggt_two_numbers(x, y):
        while y:
            x, y = y, x % y
        return x

    # Überprüfe, ob die Liste mindestens zwei Zahlen enthält
    if len(numbers) < 2:
        raise ValueError("Die Liste sollte mindestens zwei Zahlen enthalten.")

    # Berechne den ggT iterativ für alle Zahlen in der Liste
    result = numbers[0]
    for num in numbers[1:]:
        result = ggt_two_numbers(result, num)
    return result