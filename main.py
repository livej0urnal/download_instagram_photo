import instaloader

profile_name = input("Input nickname: ")

print("Load content....")

instaloader.Instaloader().download_profile(profile_name)

print("Load complete!")