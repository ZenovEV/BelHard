from crud import CRUDCategory


#print(CRUDCategory.get_articles(category_id=1))
"""
for category in CRUDCategory.get_all():
    print(category.name)
    print(category.__dict__)

"""

category = CRUDCategory.get(category_id=1)
print(category)
#category.parent_id = None
category.name = 'Food'
CRUDCategory.update(category=category)
print(CRUDCategory.get(category_id=1))
