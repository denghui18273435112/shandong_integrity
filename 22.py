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
