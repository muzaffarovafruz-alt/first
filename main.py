# 1. Davlatlar ro'yxati
davlatlar = ["O'zbekiston", "Turkiya", "AQSh", "Germaniya", "Yaponiya"]

print("Davlatlar:", davlatlar)

# 2. Ro'yxat uzunligi
print("Ro'yxat uzunligi:", len(davlatlar))

# 3. Tartiblangan holda
print("Alifbo tartibida:", sorted(davlatlar))

# 4. Teskari tartibda
print("Teskari alifbo:", sorted(davlatlar, reverse=True))

# 5. Asl ro'yxatni qayta chiqarish
print("Asl ro'yxat:", davlatlar)

# 6. reverse() yordamida
davlatlar.reverse()
print("reverse() dan keyin:", davlatlar)

# Asl holatiga qaytarish
davlatlar.reverse()

# 7. sort() yordamida avval alifbo, keyin teskari
davlatlar.sort()
print("sort() alifbo:", davlatlar)

davlatlar.sort(reverse=True)
print("sort() teskari:", davlatlar)


# 8. 120 dan 1200 gacha bo'lgan juft sonlar
juft_sonlar = list(range(120, 1201, 2))
print("Juft sonlar:", juft_sonlar)


# 9. Ro'yxatdagi sonlar yig'indisi
print("Yig'indi:", sum(juft_sonlar))


# 10. Eng katta va eng kichik son orasidagi ayirma
ayirma = max(juft_sonlar) - min(juft_sonlar)
print("Eng katta va eng kichik son ayirmasi:", ayirma)


# 11. Ro'yxatdagi elementlar soni
print("Elementlar soni:", len(juft_sonlar))


# 12. Boshidan, o'rtasidan va oxiridan 20 ta qiymat
print("Boshidan 20 ta:", juft_sonlar[:20])
print("O'rtasidan 20 ta:", juft_sonlar[len(juft_sonlar)//2-10:len(juft_sonlar)//2+10])
print("Oxiridan 20 ta:", juft_sonlar[-20:])


# 13. taomlar ro'yxati
taomlar = ["osh", "manti", "somsa", "shashlik", "lag'mon"]

print("Taomlar:", taomlar)


# 14. nonushta ro'yxatiga taomlar va nusxa olish
nonushta = taomlar.copy()

# 15. Faqat nonushtaga yeyiladigan taomlarni qoldirish
nonushta = ["non", "tuxum", "qaymoq"]

# Qo'shimcha 2 ta taom
nonushta.extend(["asal", "pishloq"])

print("Nonushta:", nonushta)


# 16. Ikkala ro'yxatni konsolga chiqarish
print("Taomlar:", taomlar)
print("Nonushta:", nonushta)


# 17. nonushta ro'yxatini o'zgarmas ro'yxatga (tuple) aylantirish
nonushta = tuple(nonushta)

print("Tuple ko'rinishida:", nonushta)


# 18. nonushta[0] ga yangi qiymat berish
# Tuple ichidagi qiymatni to'g'ridan-to'g'ri o'zgartirib bo'lmaydi.
# Shuning uchun yangi tuple yaratamiz.

nonushta = ("qaymoq va non",) + nonushta[1:]

print("Yangi nonushta:", nonushta)







