from typing import Optional


class ProductClass():
    def __init__(self, **kwargs):
        self.pd_id = kwargs.get('pd_id')
        self.brand_name: Optional[str] = kwargs.get('brand_name')
        self.model_name: Optional[str] = kwargs.get('model_name')