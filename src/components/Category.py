class Category:
    """
    Class Category is where we categorize our products.

    Args:
        category_id (str): is used for identifying category.
        category_name (str): is the name of the category.

    Attributes:
        _category_id: where we store category_id.
        _category_name: where we store category_name.
    """

    def __init__(self, category_id, category_name):
        if category_id is None:
            raise TypeError("Argument 'category_id' is required!")
        if category_name is None:
            raise TypeError("Argument 'category_name' is required!")

        self._category_id = category_id
        self._category_name = category_name
