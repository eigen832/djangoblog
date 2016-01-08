In our blog

Features
=========
Blog will have the following features

1. Post (Table in database)
2. Categories (Table in database)
3. Tag (Table in database)
4. Author (Table in database)

Ralations between tables
=========================
1. Post can have many categories, and a category can have many posts (Relation between Post and Category table) - ManyToMany relation

2. Tag can have many posts, and Post can have many tags (ManyToMany relation)

3. Author can have many posts and a post have a single author (OneToMany relation) [no post can be write by more than one author]

Attributes for tables
======================

Post
=====
1. title
2. created_date
3. body
4. tags
5. categories
6. author

Categories
===========
1. cat_name
2. cat_description

Author
=======
1. author name
2. author email (not mandatory)
3. author bio

Tag
====
1. tag_name
2. tag_description


