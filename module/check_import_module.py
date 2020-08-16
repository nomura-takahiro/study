
import sys

# 確認したいモジュールをインポート
import random

# 確認したいモジュール名を追加
module_list = ["random"]

for mod in module_list:
	if mod in sys.modules:
		print("random is in modules.")
	else:
		print("random is not in modules.")


