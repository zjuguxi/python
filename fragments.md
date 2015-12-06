# 零散的知识点

## 0, None, 空字符串"", 空列表[], 空元组(), 空字典{} 的布尔值都是False

## 函数可以做为变量,参数用(x)写在后面
    def find_city:
        pass
    cities['_find'] = find_city
     # 向字典cities插入键值
    city_found = cities['_find'](cities, state)
     # 从字典cities中提取'_find'的键值即函数find_city，函数参数是(cities, state)
	