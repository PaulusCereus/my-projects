# Базовые команды git

## Проверка работоспособности и версии git

```bash
git --version
```

## Настройка git с помощью настройки имени и почты

```bash
git config --global user.name "My Name"
git config --global user.email "myemail@example.com"
```

## Проверка настроек 

```bash
git config --list
```

## Проверка текущего статуса репозитория

```bash
git status
```

## Проверка всех логов (история коммитов)

```bash
git log
```

## Проверка удаленных подключений

```bash
git remote
```

## Добавление файла в отслеживаемое состояние

```bash
git add name_of_file
```

## Подтверждение изменений всех файлов в отслеживаемом состоянии

```bash
git commit -m "My message of this commit"
```

## Отправка локального репозитория на удаленный репозиторий

Отправка на удаленный репозиторий, который мы назвали `origin`, текущего репозитория по ветке `main`

```bash
git push -u origin main
```

### Задание 1
Изменить файл `README.md` и залить на репу

### Как делать?

```bash
git add README.md
git commit -m "Changed file README.md"
git push -u origin main
```

---

## Как проверить какие ветки существуют в текущем репозитории

```bash
git branch
```

## Как создать новую ветку

```bash
git branch new_branch
```

## Как поменять ветку

```bash
git checkout new_branch
```

---

## Установка и настройка

```bash
git --version # Проверяем есть ли git и смотрим его версию
git config --global user.name "Your Name" # Настроить имя пользователя
git config --global user.email "Your Email" # Настроить почту пользователя
git config --list # Проверить текущие настройки git
```

## Работа с репозиториями

```bash
git init # Создать пустой репозиторий в текщей папке для дальнейшего отслеживания
git clone URL # Скопировать .git репозиторий по ссылке URL
# Ссылка обычно представляет из себя
# https://github.com/username/repository.git

