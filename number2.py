"""
問題文には書かれていないが、
一人のユーザーしか一つのレシピを作れない
一つのレシピしか一つの材料を使えない
というのはありえないので、
ユーザー：レシピ、レシピ：材料
共に多対多の関係を持っているはず。
なのでそれぞれに対して中間テーブルを作成する
"""

# ユーザーテーブル
CREATE TABLE  users(
  id INT NOT NULL,
  name varchar(32) NOT NULL,
  PRIMARY KEY (id),
  INDEX id_index (id)
)

# ユーザー：レシピ中間テーブル
# 問題文には、ユーザー→レシピの関係性だったので、その順番でインデックスを貼る
CREATE TABLE  user_recipe(
  user_id INT NOT NULL,
  recipe_id INT NOT NULL,
  PRIMARY KEY(user_id, recipe_id),
  INDEX id_index (user_id, recipe_id)
)

# レシピテーブル
CREATE TABLE recipes(
  id INT NOT NULL,
  name varchar(32) NOT NULL,
  PRIMARY KEY (id),
  INDEX id_index (id)
)

# レシピ：材料　中間テーブル
# 問題文には、レシピ→材料の関係性だったので、その順番でインデックスを貼る
CREATE TABLE  recipe_material(
  recipe_id INT NOT NULL,
  material_id INT NOT NULL,
  PRIMARY KEY(recipe_id, material_id),
  INDEX id_index (recipe_id, material_id)
)

# 材料テーブル
CREATE TABLE  materials(
  id INT NOT NULL,
  name varchar(32) NOT NULL,
  PRIMARY KEY (id),
  INDEX id_index (id)
)