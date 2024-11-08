print("\nBilangan dari 1 hingga 6:")
#Bilangan 1-6
i = 1
while i <= 6:
    if i % 2 == 0:
        print(f"{i} adalah bilangan genap")
    else:
        print(f"{i} adalah bilangan ganjil")
    i += 1


print("\nHanya Bilangan Genap dari 1 hingga 6:")
#Bilangan genap 1-6
i = 1
while i <= 6:
    if i % 2 == 0:
        print(f"{i} adalah bilangan genap")
    i += 1


print("\nHanya Bilangan Ganjil dari 1 hingga 6:")
#Bilangan ganjil 1-6
i = 1
while i <= 6:
    if i % 2 != 0:
        print(f"{i} adalah bilangan ganjil")
    i += 1
