# ----------------------------------Pliki i moduły----------------------------------------

# Otwórz plik
# fo = open("text.txt", "r")                  # otwiera plik r jako read
# print("Nazwa pliku: ", fo.name)             # wydrukuję nazwę pliku
#
# line = fo.readline()                        # do zmiennej line odczytaj linijkę tekstu
# print("Czytaj linię: >" + line + "<")       # kursor wyląduje w kolejnej lini
#
# # Ponownie ustaw wskaźnik na początek
# fo.seek(0, 0)                               # seek ustalony względem początku
# line = fo.readline()
# print("Czytaj linię: >" + line + "<")
#
# # Zamknij otwarty plik
# fo.close()                                  # zamykamy plik


# ----------------------------------Tell-------------------------------------------------
# Otwórz plik
# fo = open("text.txt", "r")
# print("Nazwa pliku: ", fo.name)
#
# # Uzyskaj aktualną pozycję pliku.
# pos = fo.tell()
# print("Aktualna pozycja: " + str(pos))
#
# line = fo.readline()
# print("Czytaj linię: >" + line + "<")
#
# # Uzyskaj aktualną pozycję pliku.
# pos = fo.tell()
# print("Aktualna pozycja: " + str(pos))
#
# # Zamknij otwarty plik
# fo.close()


# ----------------------------------Cwiczenie1---------------------------------------------
# Napisz program w Pythonie, aby odczytać i wyświetlić cały plik tekstowy.

# x = open("text.txt")
# print(x.read())

# to samo inaczej


# ----------------------------------Cwiczenie2---------------------------------------------
# Napisz program w Pythonie, który odczyta plik tekstowy wiersz po wierszu i zapisze
# go na liście content_list.
# content_list to lista zawierająca przeczytane wiersze.
# Możesz skorzystać z podpowiedzi (podanej dalej).
# Podpowiedź
# Instrukcja with w Pythonie jest używana w obsłudze wyjątków,
# aby kod był czystszy i bardziej czytelny. Upraszcza zarządzanie wspólnymi zasobami,
# takimi jak strumienie plików. Zwróć uwagę na następujący przykład kodu,
# w jaki sposób użycie instrukcji with sprawia, że kod jest czystszy.

# 1) bez użycia instrukcji with
# file = open('file_path', 'w')
# file.write('hello world !')
# file.close()
#
# # 2) bez użycia instrukcji with
# file = open('file_path', 'w')
# try:
#     file.write('hello world')
# finally:
#     file.close()
#
# # używanie instrukcji with
# with open('file_path', 'w') as file:
#     file.write('hello world !')

# Zauważ, że w przeciwieństwie do pierwszych dwóch implementacji,
# nie ma potrzeby wywoływania file.close() podczas używania instrukcji with.
# Sama instrukcja with zapewnia właściwe pozyskiwanie i uwalnianie zasobów.
# Wyjątek podczas wywołania file w pierwszej implementacji może uniemożliwić
# poprawne zamknięcie pliku, co może wprowadzić kilka błędów w kodzie,
# np. wiele zmian w plikach nie będzie obowiązywać,
# dopóki plik nie zostanie poprawnie zamknięty.

# Drugie podejście w powyższym przykładzie zajmuje się wszystkimi wyjątkami,
# ale użycie instrukcji with sprawia, że kod jest zwarty i znacznie bardziej czytelny.
# W ten sposób instrukcja with pomaga uniknąć błędów i wycieków, zapewniając,
# że zasób zostanie prawidłowo wydany, gdy kod korzystający z zasobu zostanie całkowicie wykonany.
# Instrukcja with jest powszechnie używana ze strumieniami plików,
# jak pokazano powyżej oraz z blokadami, gniazdami, podprocesami i telnetami itp.

# Tutaj zaczynam to zadanie xD

with open("text.txt") as plik:
    content_list = plik.readlines()
    print(content_list)
    type(content_list)
    print(type(content_list))
