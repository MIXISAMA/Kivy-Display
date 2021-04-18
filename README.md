# 环境配置

帮学长写的，据说可以拿补助，美滋滋。

## 依赖

```bash
pip install kivy
pip install PyMySQL
```

## 配置

* 数据库配置: `gallery/database.py`

## 思路

借鉴的另一个人的代码，我这里抛砖引[玉](https://github.com/hackebrot/kivy-gallery)。

这个项目是要连接数据库，获取并展示文物信息，那么就让单独一个`database.py`文件获取到后，一直保留着就可以了。咱也不知道数据量有多大，炸了再说。

那没数据库也不是跑不了，`database.py`里面有假数据，可以用着看效果。

## 需要明确的事情

* rep_data(文物资料信息表)提供图片/obj/mtl的位置有歧义，具体应该请求哪个一个url，最好给一个Sample。
* rep_data表中部分元组中obj或mtl缺失，如何处理。
* 部署系统？屏幕分辨率？
* 展示数据量有多大

## Todo

* 图片滚动✅
* 图片列表❎
* 数据清洗❎
* 三维展示❎
