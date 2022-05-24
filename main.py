import instaloader

profile_name = input("Введите ник: ")

print("Загружаю контент....")

instaloader.Instaloader().download_profile(profile_name)

print("Загрузка завершена")