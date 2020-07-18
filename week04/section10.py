'''
jieba分词和关键字提取

'''

import jieba
# 1.分词
# strings = ['我来自极客大学', 'Python进阶训练营真好玩']
# jieba.add_word('极客大学')
# jieba.load_userdict('user_dict.txt')
# for string in strings:
#     res = jieba.cut(string, cut_all = False)  # 精确模式
#     print(list(res))
# for string in strings:
#     res = jieba.cut(string, cut_all = True)   # 全模式
#     print(list(res))


# 2.关键词提取
import jieba.analyse as analyse
# text = text = '机器学习，需要一定的数学基础，需要掌握的数学基础知识特别多，如果从头到尾开始学，估计大部分人来不及，我建议先学习最基础的数学知识'
# tfidf = analyse.extract_tags(text,
#                             topK = 5,  # 取出权重最大的前五个
#                             withWeight = True  # 带权重值
#                             )

# 屏蔽不想匹配的关键词
# analyse.set_stop_words('stop_words.txt')
# tfidf = analyse.extract_tags(text,
#                             topK = 5,  # 取出权重最大的前五个
#                             withWeight = False  # 不带权重值
#                             )
# print(tfidf)


# 调整分词，合并为一个词
string2 = '我们中出了一个叛徒'
jieba.suggest_freq('中出', True)

result = jieba.cut(string2, HMM=False)
print('分词合并: ' + '/'.join(list(result)))
# 调整分词，，分为两个词
string2 = '我们中出了一个叛徒'
jieba.suggest_freq(('中','出'), True)

result = jieba.cut(string2, HMM=False)
print('分词合并: ' + '/'.join(list(result)))
