
import keyword

# Pythonでキーワード(予約語)となっているかをチェック

# 予約語ならTrue
print(keyword.iskeyword("for"))

# 違うならFalse
print(keyword.iskeyword("name"))


