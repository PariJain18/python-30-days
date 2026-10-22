def profile(**kwargs):
    print("My Profile")
    for key, value in kwargs.items():
        print(key,":", value)
profile(name="Pari", course="BCA")