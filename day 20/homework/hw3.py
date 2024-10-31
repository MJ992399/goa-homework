# 3) შექმენით სია და for loop დახმარებით გამოიტანეთ მხოლოდ ლუწი ინდექსებზე მდგომი ელემენტები


goa_students=["giorgi","irakli","sopia","aleko","beqa","giorgi","giorgi","nani","saba","nika"]


for i in range(9):
    if i % 2 != 0:  
        print(goa_students[i])