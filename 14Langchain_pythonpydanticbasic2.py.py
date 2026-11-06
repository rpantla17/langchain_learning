from pydantic import BaseModel,Field
class Product(BaseModel):
    name: str = Field(
        description= "Name of the Product"
        )
    model: str = Field(
        description= " the model of the product"
    )
    price: float = Field(
        description= "Proice of the Product"
    )
    in_stock : bool | None = Field(
        default= False, 
        description="whether the product is available or not"
        )
product = Product(name = "Iphone",model="Duo",price=1200.56)
print(product) ## pydantic objetc
print(product.name)  ## this is fuield
print(product.model_dump()) ##Python dictionary
print(type(product.model_dump()))
print(product.model_dump_json()) ## JSOn strign
print(type(product.model_dump_json()))