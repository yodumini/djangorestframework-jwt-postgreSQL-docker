## API 簡單project

```bash
# 執行
docker compose up
```

### API文件

* GET TOKEN

| Method   |  POST|
|-------|:-----:|
| Path   |  /api/token/  |

* require body
```
{
    "username":"admin",
    "password":"admin1234"
}
```

* response body
```
{
    "refresh": "refresh token",
    "access": "TOKEN"
}
```

---
### 上傳文章
| Method   |  POST|
|-------|:-----:|
| Path   |  /api/news/  |

* require headers
```
{
  Authorization: Bearer {TOKEN},
  Content-Type: application/json
}
```

* require bodys
```
{
    "title": {"PUT TITLE"},
    "img": {"PUT IMG address"},
    "article": {"PUT AN ARTICLE"}
}
```

---
### 取得文章
| Method   |  GET|
|-------|:-----:|
| Path   |  /api/news/  |

* require headers
```
{
  Authorization: Bearer {TOKEN},
  Content-Type: application/json
}
```

* response body
```
[
    {
        "id": 1,
        "title": "t1",
        "img": "i1",
        "article": "i am article",
        "created": "2023-08-30T10:17:26.554952Z",
        "last_modify_date": "2023-08-30T10:17:26.554939Z"
    },
...
]
```

---
### 修改文章
| Method   |  PUT|
|-------|:-----:|
| Path   |  /api/news/{id}  |

* require headers
```
{
  Authorization: Bearer {TOKEN},
  Content-Type: application/json
}
```

* require bodys
```
{
    "title": {"PUT TITLE"},
    "img": {"PUT IMG address"},
    "article": {"PUT AN ARTICLE"}
}
```

---
### 刪除文章
| Method   |  DELETE|
|-------|:-----:|
| Path   |  /api/news/{id}  |

* require headers
```
{
  Authorization: Bearer {TOKEN},
  Content-Type: application/json
}
```

