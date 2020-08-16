
# ファイル名をインポートしているモジュール名と同じにしてしまうと、
# AttributeErrorになるかもしれない
# ⇒先にカレントディレクトリのファイルが読み込まれるため、正規のモジュールファイルが読み込まれない

import random

#引数に指定する範囲で乱数生成
print(random.randint(0,100))
#print(random.randrange(0,100))

