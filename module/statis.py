
import statistics

# mean(平均値)
nums = [1,65,4,3,29,90,3]
print(statistics.mean(nums))

# median(中央値)
print(statistics.median(nums))

# mode(最頻値)
# ※どれも1つしかない場合例外(StatisticsError)となる
print(statistics.mode(nums))



