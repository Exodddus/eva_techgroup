# 0. 来签到啦！- Git

答案是—— TECH

```python
# 明文固定4位，密钥为你的学号后4位
encrypt = lambda clear, key: "".join([hex(ord(clear[i]) * ord(key[i]))[2:] + '/' for i in range(4)])[:-1]

```
这行代码的功能是定义含有clear、key两个参量的encrypt函数，它将明文和密钥每一位转为ASCII码后相乘的结果转化为16进制，去除表示16进制的前两位字符，再连接成以'/'间隔的字符串，最后把结尾的'/'去掉。

一点聊胜于无的修改：
```python
# 明文固定4位，密钥为你的学号后4位
encrypt = lambda clear, key: "/".join([hex(ord(clear[i]) * ord(key[i]))[2:] for i in range(4)])

```
至少它更短了不是吗（