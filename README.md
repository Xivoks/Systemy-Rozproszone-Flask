# Systemy-Rozproszone-Flask


Opis projektu i jego funkcjonalności.

## Wymagania

- Python 3.8.x
- Biblioteki: python-dotenv, flask-sqlalchemy, pymysql, cryptography, flask-migrate

## Instalacja

1. Zainstaluj Python 3.8.x na swoim systemie operacyjnym.
2. Sklonuj ten projekt na swój lokalny komputer.
3. Przejdź do katalogu projektu.

```shell
cd Systemy-Rozproszone-Flask
```

4. Zalecam utworzenie i aktywowanie wirtualnego środowiska Pythona.

```shell
python -m venv venv
source venv/bin/activate
```

5. Zainstaluj wymagane biblioteki, wykonując polecenie:

```shell
pip install -r requirements.txt
```

## Konfiguracja bazy danych

1. Skonfiguruj połączenie z bazą danych MySQL w pliku .env.

```
DATABASE_URI=mysql+pymysql://username:password@host:port/database_name
```

2. Wykonaj migrację bazy danych, wykonując polecenie:

```shell
flask db upgrade
```

## Uruchamianie aplikacji

1. Włącz wirtualne środowisko Pythona:

```shell
source venv/bin/activate
```

2. Uruchom aplikację:

```shell
flask run
```

3. Aplikacja jest teraz dostępna pod adresem: http://localhost:5000/

## Opis struktury projektu

- `application`: Katalog główny aplikacji.
  - `samples`: Przykładowy plik JSON z danymi użytkowników.
  - `static`: Katalog ze statycznymi zasobami, takimi jak obrazy i pliki CSS.
  - `templates`: Katalog z szablonami HTML używanymi w aplikacji.
  - `__init__.py`: Pusty plik inicjalizacyjny Python.
  - `db_manage_commands.py`: Moduł zawierający polecenia do zarządzania bazą danych.
  - `models.py`: Moduł zawierający definicje modeli.
  - `users.py`: Moduł zawierający funkcje i logikę obsługi użytkowników.
  - `utils.py`: Moduł zawierający pomocnicze funkcje i narzędzia.
  - `migrations`: Katalog zawierający pliki migracji bazy danych.
  - `app.py`: Główny plik aplikacji.
- `.flaskenv`: Plik zawierający zmienne środowiskowe dla aplikacji Flask.
- `.gitignore`: Plik konfiguracyjny dla Git, ignorujący niektóre pliki i katalogi.
- `.env`: Plik zawierający zmienne środowiskowe dla aplikacji.
- `config.py`: Plik konfiguracyjny aplikacji.
- `README.md`: Plik który aktualnie czytasz.

## Autorzy

``Don Alberto``
``Padre Juan``
