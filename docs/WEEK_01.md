# Неделя 1 — фундамент Data Science

**Даты:** 28 сентября — 4 октября 2026  
**Нагрузка:** 10–12 часов  
**Цель:** уверенно загружать, исследовать и описывать данные; закрепить SQL и базовую статистику; сделать первый EDA энергетического временного ряда.

## Понедельник, 28 сентября — старт проекта и pandas
**1.5–2 часа**

**Теория, 25 минут:** list/dict/tuple/set, функции, comprehensions, try/except, CSV, отличие list / NumPy array / pandas Series.

**Практика, 60 минут:**
1. Создать venv и установить зависимости.
2. `python scripts/generate_sample_data.py`
3. Открыть CSV через pandas.
4. Выполнить `head`, `tail`, `shape`, `columns`, `dtypes`, `info`, `describe`, `isna().sum()`.
5. В notebook ответить: сколько строк, что такое одна строка, единица `load_mw`, есть ли пропуски, mean/median/min/max.

**Проверка себя:** объяснить `df["load_mw"]`, `df[["load_mw"]]`, `.loc`, `.iloc`.

Коммит: `day1: project setup and first pandas exploration`

## Вторник, 29 сентября — вероятность и описательная статистика
**1.5 часа**

**Теория, 45 минут:** случайная величина, матожидание, дисперсия, std, медиана, квантили, ковариация, корреляция. Для каждого понятия — интерпретация через электрическую нагрузку.

**Практика, 45 минут:** `mean`, `median`, `var`, `std`, `quantile`; сравнить будни/выходные и день/ночь; построить histogram, boxplot, линию нагрузки.

Мини-задача: ответить 3–5 предложениями, означает ли рост среднего рост нагрузки почти во все часы.

Коммит: `day2: descriptive statistics and load distributions`

## Среда, 30 сентября — SQL
**1.5 часа**

Повторить `SELECT`, `WHERE`, `ORDER BY`, `GROUP BY`, `HAVING`, агрегаты, `CASE WHEN`.

Импортировать CSV в SQLite и написать запросы:
1. Средняя нагрузка.
2. Средняя в выходные.
3. Средняя в будни.
4. 5 часов с максимальной нагрузкой.
5. Средняя нагрузка по часу суток.
6. Часы, где средняя нагрузка выше общего среднего.
7. `CASE WHEN` для night/morning/day/evening и средняя нагрузка по периоду.

Результат сохранить в `notebooks/02_sql_practice.sql`.

Коммит: `day3: SQL aggregations on energy load data`

## Четверг, 1 октября — распределения и корреляция
**1.5 часа**

**Теория:** Бернулли, биномиальное, нормальное, Пуассон; зачем модель распределения; почему correlation != causation.

**Практика:** scatter `temperature_c -> load_mw`, Pearson correlation по всем данным, отдельно будни/выходные; объяснить различия.

Мини-эксперимент: по 10 000 значений из normal/binomial/poisson, histogram и словесное описание формы.

Коммит: `day4: probability distributions and correlation analysis`

## Пятница, 2 октября — постановка задачи прогнозирования
**1–1.5 часа**

Создать `docs/FORECASTING_PROBLEM.md` по шаблону.

Сформулировать:
- target;
- prediction horizon;
- features: hour, weekday, weekend, temperature, lag 1h, lag 24h, lag 168h;
- baseline: например, `load(t) = load(t-24h)`;
- метрики MAE, RMSE, MAPE и какую из них проще объяснить диспетчеру.

Коммит: `day5: formulate energy load forecasting problem`

## Суббота, 3 октября — первый полноценный EDA
**2.5–3 часа**

Notebook как мини-отчёт:
1. Problem.
2. Data quality: размер, типы, пропуски, дубликаты, даты.
3. Descriptive statistics.
4. Time behaviour: график по времени, среднее по часу, среднее по дню недели.
5. Temperature vs load.
6. Weekends vs weekdays.
7. Минимум 5 содержательных выводов обычным языком.

Коммит: `day6: complete first energy load EDA`

## Воскресенье, 4 октября — закрепление
**1.5 часа**

Без подсказок ответить:
1. mean vs median;
2. variance;
3. std;
4. correlation;
5. correlation != causation;
6. WHERE vs HAVING;
7. GROUP BY;
8. target;
9. feature;
10. metric;
11. baseline;
12. почему нельзя оценивать модель только на train.

Запустить `pytest -q`, обновить README, создать `docs/WEEK_01_RESULTS.md` с блоками: что изучил / что получилось / что непонятно / ошибки / что дальше.

Коммит: `week1: finish data science foundations sprint`

## Definition of Done
- [ ] окружение запускается с нуля;
- [ ] тесты проходят;
- [ ] минимум 6 осмысленных коммитов;
- [ ] EDA notebook;
- [ ] SQL-задания;
- [ ] постановка задачи прогнозирования;
- [ ] минимум 5 содержательных выводов;
- [ ] устно объясняешь 10 из 12 контрольных вопросов.
