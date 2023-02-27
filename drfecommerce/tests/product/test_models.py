import pytest
from django.core.exceptions import ValidationError

pytestmark = pytest.mark.django_db


class TestCategroyModels:
    def test_str_method(self, category_factory):
        # Arrange
        # Act
        x = category_factory(name="test_cat")
        # Assert
        assert x.__str__() == "test_cat"


class TestBrandModels:
    def test_str_method(self, brand_factory):
        # Arrange
        # Act
        x = brand_factory(name="test_brand")
        # Assert
        assert x.__str__() == "test_brand"


class TestProductModels:
    def test_str_method(self, product_factory):
        # Arrange
        # Act
        obj = product_factory(name="test_product")
        # Assert
        assert obj.__str__() == "test_product"


class TestProductLineModels:
    def test_str_method(self, product_line_factory):
        obj = product_line_factory(sku="12345")
        assert obj.__str__() == "12345"

    def test_duplicate_order_values(self, product_line_factory, product_factory):
        obj = product_factory()
        product_line_factory(order=1, product=obj)
        with pytest.raises(ValidationError):
            product_line_factory(order=1, product=obj).clean()
