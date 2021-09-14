#Joel

interest = 1.1
savings = int(input("Hur mycket vill du spara?"))
years = int(input("Hur länge vill du spara?"))

result = savings*years**interest

print("Du kommer ha",result,"kr efter",years,"år")