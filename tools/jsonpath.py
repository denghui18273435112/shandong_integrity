import  jsonpath

book={
"store": {
    "book": [
      { "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95,
        "age":"x"
      },
      { "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99,
        "age":"x"
      },
      { "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99,
        "age":"x"
      },
      { "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99,
        "age":"x"
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}

# print(jsonpath.jsonpath(book,"$.store.book[*].author"))
# print(jsonpath.jsonpath(book,"$..color"))
# print(jsonpath.jsonpath(book,"$.store.bicycle.price"))
# print(jsonpath.jsonpath(book,"$..age"))
# #print(jsonpath.jsonpath(data,"$.msg"))

print(jsonpath.jsonpath(book,"$.store.book[*]"))



# -*- coding:utf-8 -*-
"""
============================
Author : wen
Time : 2021/1/7 12:20
Email : 976076733@qq.com
============================
"""

from jsonpath import jsonpath

"""
jsonpath方法需要两个参数:
参数1:数据
参数2:jsonpath表达式

注意点:
    1.如果没有匹配不到数据返回的是False
    2.匹配到数据返回的是包含数据的列表

jsonpath语法:
$               ----------->根节点
.               ----------->选择子节点
..               ----------->选择子孙节点(不考虑层级)
[]              ----------->选择子节点/选择数组索引
[,]             ----------->选择多个字段
@               ----------->代表当前选中的节点(和条件过滤一起使用)
[?(过滤条件)]    ------------> 通过条件过滤数据
"""

data = {'code': 200,
        'data': [
            {'photo': 'https://static-image.xfz.cn/1454046552_487.png', 'create_time': '2016-01-29 13:49:13',
             'link': 'http://www.ehoutai.com/', 'uid': 7, 'name': '易后台'},
            {'photo': 'https://static-image.xfz.cn/1454046135_474.png', 'create_time': '2016-01-29 13:42:15',
             'link': 'http://www.sanjieke.com/', 'uid': 4, 'name': '三节课'},
            {'photo': 'https://static-image.xfz.cn/1454046053_122.png', 'create_time': '2016-01-29 13:40:53',
             'link': 'https://www.aliyun.com/', 'uid': 1, 'name': '阿里云'},
            {'photo': 'https://static-image.xfz.cn/1454047318_361.png', 'create_time': '2016-01-29 14:01:59',
             'link': 'http://xmanlegal.com/', 'uid': 8, 'name': '未来法律'}]}

data2 = {'code': 0,
         'msg': 'OK',
         'data':
             {'id': 10006043,
              'leave_amount': -422500.0,
              'mobile_phone': '13449960188',
              'reg_name': '小可爱',
              'reg_time': '2021-01-01 22:03:39.0',
              'type': 1,
              'token_info':
                  {'token_type': 'Bearer',
                   'expires_in': '2021-01-07 12:32:52',
                   'token': 'eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjEwMDA2MDQzLCJleHAiOjE2MDk5OTM5NzJ9.W_wi-NFjJMa3NZF9BOv_j0DvdSRhP7ncMrLfDdpM7HPpW01Afh7Gn6MAQXAFsS0Wge2BUlXAxLNTEv2RO3w-Ow'}},
         'copyright': 'Copyright 哈哈 © 2017-2020 xx技术有限公司 All Rights Reserved'
         }
token = jsonpath(data2, "$..token")
print(token)

# 选择子节点
code = jsonpath(data2, "$.code")  # ==  jsonpath(data2, "$[code]")
print(code)

# 通过索引选择列表中的数据
code = jsonpath(data, "$.data[0]")  # ==  jsonpath(data, "$[data][0]")
print(code)
code1 = jsonpath(data, "$.data[1].name")  # == jsonpath(data, "$.data[1][name]")
print(code1)

# 选择多个字段
code2 = jsonpath(data, "$.data[1][name,link,]")  # ==  jsonpath(data, "$.data[1].name,link")
print(code2)
code3 = jsonpath(data2, "$.data[id,mobile_phone,type]")  # == jsonpath(data2, "$.data.[id,mobile_phone,type]")
print(code3)

# 通过过滤条件
res1 = jsonpath(data, "$.data[?(@.uid==4)]")   # == jsonpath(data, "$[data][?(@.uid==4)].name")
print(res1)
res2 = jsonpath(data, "$.data[?(@.uid==4)][name]")  # == jsonpath(data, "$.data[?(@.uid==4)].name")
print(res2)