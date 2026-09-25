# ml-lab

Учебный и портфолио-проект по Data Science / Machine Learning в энергетике.

## Главная цель

За 12 месяцев пройти путь от статистики, аналитики и классического ML до нейросетей, LLM и production ML — с упором на энергетические данные.

Первый большой проект: **прогнозирование электрической нагрузки**.

## Как устроен репозиторий

Подробное объяснение всех папок и файлов: [`docs/REPOSITORY_GUIDE.md`](docs/REPOSITORY_GUIDE.md).

## Неделя 1

Точный план находится в [`docs/WEEK_01.md`](docs/WEEK_01.md).

К концу первой недели здесь должны быть:

- настроенное Python-окружение;
- базовая работа с NumPy и pandas;
- SQL-практика;
- статистика: среднее, дисперсия, квантили, корреляция, распределения;
- первый EDA энергопотребления;
- осмысленные коммиты в Git.

## Быстрый старт

### Windows PowerShell

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python scripts/generate_sample_data.py
jupyter lab
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python scripts/generate_sample_data.py
jupyter lab
```

Открыть `notebooks/01_eda.ipynb`.

Тесты:

```bash
pytest -q
```

## Реальные данные

После знакомства с пайплайном будем переходить на открытые энергетические данные. Один из хороших источников — Open Power System Data:
https://data.open-power-system-data.org/time_series/

На первой неделе используется маленький синтетический датасет, чтобы быстро отработать инструменты и статистическое мышление.

## Правило проекта

Каждый новый метод должен отвечать на вопрос:

> какую реальную задачу он решает и как мы поймём по метрике, что решение стало лучше?
