from products.models import Category

def create_items():
    # Code to create initial items
    # Example: YourModel.objects.create(...)
    category_cloths = Category.objects.create(
    name='New Category',
    description='This is a new category',
)
    category_electronics = Category.objects.create(
        name='New Category',
        description='This is a new category',
    )
    category_cloths.save()
    category_electronics.save()