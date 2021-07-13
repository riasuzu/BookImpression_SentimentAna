import statistics

import Books
import Analysis

book = Books.book_impression.BookImp()
nlu = Analysis.NLU.NLU()

# 文庫本のタイトルを取得する
paperbook_title = book.get_BookTitle()
# 文庫本のランキングの月
paperbook_rank_month = book.get_BookRank_M()
# 文庫本のリンク
paperbook_link = book.get_BookLink()

# リンクから感想を取得
paperbook_imp1 = book.get_BookImp_text(paperbook_link[0])
paperbook_imp2 = book.get_BookImp_text(paperbook_link[1])
paperbook_imp3 = book.get_BookImp_text(paperbook_link[2])
paperbook_imp4 = book.get_BookImp_text(paperbook_link[3])
paperbook_imp5 = book.get_BookImp_text(paperbook_link[4])
paperbook_imp6 = book.get_BookImp_text(paperbook_link[5])
paperbook_imp7 = book.get_BookImp_text(paperbook_link[6])
paperbook_imp8 = book.get_BookImp_text(paperbook_link[7])
paperbook_imp9 = book.get_BookImp_text(paperbook_link[8])
paperbook_imp10 = book.get_BookImp_text(paperbook_link[9])
paperbook_imp11 = book.get_BookImp_text(paperbook_link[10])
paperbook_imp12 = book.get_BookImp_text(paperbook_link[11])
paperbook_imp13 = book.get_BookImp_text(paperbook_link[12])
paperbook_imp14 = book.get_BookImp_text(paperbook_link[13])
paperbook_imp15 = book.get_BookImp_text(paperbook_link[14])
paperbook_imp16 = book.get_BookImp_text(paperbook_link[15])
paperbook_imp17 = book.get_BookImp_text(paperbook_link[16])
paperbook_imp18 = book.get_BookImp_text(paperbook_link[17])
paperbook_imp19 = book.get_BookImp_text(paperbook_link[18])
paperbook_imp20 = book.get_BookImp_text(paperbook_link[19])

# 感想をNLUの評判分析機能に通す
paperbookDoc1 = nlu.get_document(paperbook_imp1)
paperbookDoc2 = nlu.get_document(paperbook_imp2)
paperbookDoc3 = nlu.get_document(paperbook_imp3)
paperbookDoc4 = nlu.get_document(paperbook_imp4)
paperbookDoc5 = nlu.get_document(paperbook_imp5)
paperbookDoc6 = nlu.get_document(paperbook_imp6)
paperbookDoc7 = nlu.get_document(paperbook_imp7)
paperbookDoc8 = nlu.get_document(paperbook_imp8)
paperbookDoc9 = nlu.get_document(paperbook_imp9)
paperbookDoc10 = nlu.get_document(paperbook_imp10)
paperbookDoc11 = nlu.get_document(paperbook_imp11)
paperbookDoc12 = nlu.get_document(paperbook_imp12)
paperbookDoc13 = nlu.get_document(paperbook_imp13)
paperbookDoc14 = nlu.get_document(paperbook_imp14)
paperbookDoc15 = nlu.get_document(paperbook_imp15)
paperbookDoc16 = nlu.get_document(paperbook_imp16)
paperbookDoc17 = nlu.get_document(paperbook_imp17)
paperbookDoc18 = nlu.get_document(paperbook_imp18)
paperbookDoc19 = nlu.get_document(paperbook_imp19)
paperbookDoc20 = nlu.get_document(paperbook_imp20)


# documentからscoreの値を抜き出す
paperbookS1 = nlu.get_score(paperbookDoc1)
paperbookS2 = nlu.get_score(paperbookDoc2)
paperbookS3 = nlu.get_score(paperbookDoc3)
paperbookS4 = nlu.get_score(paperbookDoc4)
paperbookS5 = nlu.get_score(paperbookDoc5)
paperbookS6 = nlu.get_score(paperbookDoc6)
paperbookS7 = nlu.get_score(paperbookDoc7)
paperbookS8 = nlu.get_score(paperbookDoc8)
paperbookS9 = nlu.get_score(paperbookDoc9)
paperbookS10 = nlu.get_score(paperbookDoc10)
paperbookS11 = nlu.get_score(paperbookDoc11)
paperbookS12 = nlu.get_score(paperbookDoc12)
paperbookS13 = nlu.get_score(paperbookDoc13)
paperbookS14 = nlu.get_score(paperbookDoc14)
paperbookS15 = nlu.get_score(paperbookDoc15)
paperbookS16 = nlu.get_score(paperbookDoc16)
paperbookS17 = nlu.get_score(paperbookDoc17)
paperbookS18 = nlu.get_score(paperbookDoc18)
paperbookS19 = nlu.get_score(paperbookDoc19)
paperbookS20 = nlu.get_score(paperbookDoc20)

# str → float
paperbookScore1 = list(map(float, paperbookS1))
paperbookScore2 = list(map(float, paperbookS2))
paperbookScore3 = list(map(float, paperbookS3))
paperbookScore4 = list(map(float, paperbookS4))
paperbookScore5 = list(map(float, paperbookS5))
paperbookScore6 = list(map(float, paperbookS6))
paperbookScore7 = list(map(float, paperbookS7))
paperbookScore8 = list(map(float, paperbookS8))
paperbookScore9 = list(map(float, paperbookS9))
paperbookScore10 = list(map(float, paperbookS10))
paperbookScore11 = list(map(float, paperbookS11))
paperbookScore12 = list(map(float, paperbookS12))
paperbookScore13 = list(map(float, paperbookS13))
paperbookScore14 = list(map(float, paperbookS14))
paperbookScore15 = list(map(float, paperbookS15))
paperbookScore16 = list(map(float, paperbookS16))
paperbookScore17 = list(map(float, paperbookS17))
paperbookScore18 = list(map(float, paperbookS18))
paperbookScore19 = list(map(float, paperbookS19))
paperbookScore20 = list(map(float, paperbookS20))


paperbookScore_Ave = []

# scoreの平均値
paperbookScore_Ave.append(statistics.mean(paperbookScore1))
paperbookScore_Ave.append(statistics.mean(paperbookScore2))
paperbookScore_Ave.append(statistics.mean(paperbookScore3))
paperbookScore_Ave.append(statistics.mean(paperbookScore4))
paperbookScore_Ave.append(statistics.mean(paperbookScore5))
paperbookScore_Ave.append(statistics.mean(paperbookScore6))
paperbookScore_Ave.append(statistics.mean(paperbookScore7))
paperbookScore_Ave.append(statistics.mean(paperbookScore8))
paperbookScore_Ave.append(statistics.mean(paperbookScore9))
paperbookScore_Ave.append(statistics.mean(paperbookScore10))
paperbookScore_Ave.append(statistics.mean(paperbookScore11))
paperbookScore_Ave.append(statistics.mean(paperbookScore12))
paperbookScore_Ave.append(statistics.mean(paperbookScore13))
paperbookScore_Ave.append(statistics.mean(paperbookScore14))
paperbookScore_Ave.append(statistics.mean(paperbookScore15))
paperbookScore_Ave.append(statistics.mean(paperbookScore16))
paperbookScore_Ave.append(statistics.mean(paperbookScore17))
paperbookScore_Ave.append(statistics.mean(paperbookScore18))
paperbookScore_Ave.append(statistics.mean(paperbookScore19))
paperbookScore_Ave.append(statistics.mean(paperbookScore20))


# 文庫本
print()
print(paperbook_rank_month)
print()
print('本のタイトル  |  評判分析の平均値' + '\n')
print('scoreAveが1に近いほどpositiveな印象、-1に近いほどnegativeな印象' + '\n')
for i in range(20):

    print('第' + (str(i+1)) + '位:', end=' ')
    print(paperbook_title[i] + ': ', end=' scoreAve: ')
    print(paperbookScore_Ave[i])

print()
