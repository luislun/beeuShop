from categories.models import Category

def categories( request ):
    listCategories = Category.objects.filter( primary = True )

    contextData = {
        'listCategories': listCategories,
    }

    return contextData