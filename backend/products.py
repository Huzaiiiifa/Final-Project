products = ["Sennheiser 600", 
            "Sony WH-1000XM6", 
            "Sony WH-1000XM4 Wireless", 
            "Anker Soundcore Space Q45 Wireless", 
            "Anker Soundcore Life Q20 2024", 
            "Focal Bathys Wireless"]

prices = [149, 
          199, 
          89,
          129,
          159,
          79]

print("اختر رقم المنتج:")
for x in range(len(products)):
    print(x + 1, "-", products[x])

while True:
    choice = input("\nاكتب الرقم: ")
    if not choice.isdigit():
        print("الرجاء إدخال رقم صحيح.")
        continue
    choice = int(choice)
    if 1 <= choice <= len(products):
        break
    else:
        print("لا يوجد منتج بهذا الرقم، حاول مرة أخرى.")

index = choice - 1
name = products[index]
price = prices[index]
tax = price * 0.15
total = price + tax

print("\nلقد اخترت:", name)
print("سعر المنتج شامل الضريبة:", round(total, 2), "ريال")