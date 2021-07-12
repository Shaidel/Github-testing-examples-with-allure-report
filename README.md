https://docs.qameta.io/allure/#_about

Poniżej informacje jak zainstalować allure i uruchomić testy wygenerowane za pomocą tego narzędzia

Pobrać allure z:
https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.14.0/
dla Windows allure-commandline-2.14.0.zip

Dodać w zmiennych środowiskowych PATH do:
C:\allure-commandline-2.14.0\allure-2.14.0\bin

Instalacja allure jako biblioteki pythona z wykorzystaniem pytest:
https://pypi.org/project/allure-pytest/

Uruchomienie testu i zapisanie danych allure do katalogu results
python -m pytest (nazwa).py --alluredir ./results

Uruchomienie raportu w sesji przeglądarki
allure serve ./results

Zapisanie raportu na podstawie danych z katalogu results (domyślnie do katalogu allure-report)
allure generate ./results

Wyświetlenie raportu
allure open ./allure-report 
