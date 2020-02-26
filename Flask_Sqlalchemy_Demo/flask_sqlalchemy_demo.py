# ！/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/1/23 15:18
# @Author   : guanqiao
# TODO(guanqiao): flask_sqlalhemy_demo数据库曾删改查 wtf_form表单验证

from flask import Flask, render_template, flash, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import validators, StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy


# 实例化flask
app = Flask(__name__)
app.secret_key = '666'

# 配置MySQL数据库，关联数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345@127.0.0.1/flask_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# 作者模型
class Authors(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    bks = db.relationship('Books', backref='bks')

    def __repr__(self):
        return 'Authors: %s' % self.name


# 书籍模型
class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

    def __repr__(self):
        return 'Books: %s %s' % (self.name, self.author_id)


# 提交
class User(FlaskForm):
    author = StringField('作者', validators=[DataRequired()])
    book = StringField('书籍', validators=[DataRequired()])
    submit = SubmitField('提交')

    '''
    1. 调用WTF的函数实现验证
    2. 验证通过获取数据
    3. 判断作者是否存在
    4. 如果作者存在,判断书籍是否存在,没有重复数据就添加数据,如果错误就提示错误
    5. 如果作者不存在,添加作者和书籍
    6. 验证不通过，提示错误
    '''

# 增加作者和书籍
@app.route('/', methods=['get', 'post'])
def run():
    user = User()
    authors = Authors.query.all()

    # 1. 调用WTF的函数实现验证
    if user.validate_on_submit():

        # 2. 验证通过获取数据
        author_name = user.author.data
        book_name = user.book.data

        # 3. 判断作者是否存在
        author = Authors.query.filter_by(name=author_name).first()

        # 4. 如果作者存在
        if author:
            # 判断书籍是否存在
            book = Books.query.filter_by(name=book_name).first()

            # 如果错误就提示错误
            if book:
                flash('同名书籍已存在')

            # 没有重复数据就添加数据
            else:
                try:
                    new_book = Books(name=book_name, author_id=author.id)
                    db.session.add(new_book)
                    db.session.commit()
                except Exception as e:
                    print(e)
                    flash('添加书籍失败')
                    db.session.rollback()

        # 5. 如果作者不存在,添加作者和书籍
        else:
            try:
                # 添加作者和书籍
                new_author = Authors(name=author_name)
                db.session.add(new_author)
                db.session.commit()

                new_book = Books(name=book_name, author_id=new_author.id)
                db.session.add(new_book)
                db.session.commit()
            except Exception as e:
                print(e)
                flash('添加作者和书籍失败')
                db.session.rollback()

    # 6. 验证不通过，提示错误
    else:
        if request.method == 'post':
            flash('参数错误')

    return render_template('index.html', form=user, authors=authors)


# 删除书籍
@app.route('/delete_book/<book_id>')
def delete_book(book_id):

    # 查询数据库，是否有该id的书籍，有就删除，没有就提示错误
    book = Books.query.get(book_id)

    # 如果有，就删除
    if book:
        try:
            db.session.delete(book)
            db.session.commit()
        except Exception as e:
            print(e)
            flash('删除书籍失败')
            db.session.rollback()

    # 如果没有，就提示错误
    else:
        flash('找不到该书籍')

    return redirect(url_for('run'))


# 删除作者
@app.route('/delete_author/<author_id>')
def delete_author(author_id):
    # 查询数据库，是否有该id的作者，如果有，就删除(先删书籍，再删作者)，如果没有，就提示错误

    # 查询数据库
    author = Authors.query.get(author_id)
    book = Books.query.filter_by(author_id=author.id).first()

    # 如果有，就删除(先删书籍，再删作者)
    if author:
        try:
            db.session.delete(book)
            db.session.commit()

            db.session.delete(author)
            db.session.commit()
        except Exception as e:
            print(e)
            flash('删除作者失败')
            db.session.rollback()

    # 如果没有，就提示错误
    else:
        flash('找不到该作者')

    return redirect(url_for('run'))



if __name__ == '__main__':
    # 删除表
    db.drop_all()
    # 创建表
    db.create_all()

    # 测试插入数据
    author1 = Authors(name='张三')
    author2 = Authors(name='李四')
    db.session.add_all([author1, author2])
    db.session.commit()

    book1 = Books(name='flask', author_id=author1.id)
    book2 = Books(name='高级flask', author_id=author1.id)
    book3 = Books(name='python', author_id=author2.id)
    book4 = Books(name='高级python', author_id=author2.id)
    db.session.add_all([book1, book2, book3, book4])
    db.session.commit()


    app.run(debug=True)
