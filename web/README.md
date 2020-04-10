# WEB APP

This is web app.

You can use it by normal method, but notice that when you change the model in [app](../app) , you should do the follow stuff to re-generate the <code>Track</code> model in this [app](./app).

By doing this:
```
sqlacodegen mysql+pymysql://root:password@localhost/kanai?charset=utf8mb4 --flask
```

You can get a new model which defined by yourself. Just copy that to the <code>models.py</code>, and have fun!