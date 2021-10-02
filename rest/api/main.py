from fastapi import FastAPI
from fastapi.responses import JSONResponse

from utils.docs import DESCRIPTION, TAGS_METADATA
from models.message import Message
from models.product import Product


app = FastAPI(
    title="ProdutosApp",
    description=DESCRIPTION,
    version="0.0.1",
    openapi_tags=TAGS_METADATA,
    docs_url="/",
)

products = {}
last_id = None


@app.get(
    "/products/{product_id}",
    tags=["produtos"],
    response_model=Product,
    responses={404: {"model": Message}},
)
def get_product(product_id: int):
    if product_id not in products:
        return JSONResponse(
            status_code=404,
            content={"message": f"Product with ID {product_id} not found"},
        )
    else:
        return products.get(product_id)


@app.get(
    "/products",
    tags=["produtos"],
    response_model=dict,
    responses={404: {"model": Message}},
)
def get_all_product():
    return products


@app.post(
    "/products/",
    tags=["produtos"],
    response_model=Product,
    responses={400: {"model": Message}},
)
def create_product(product: Product):
    global last_id
    if last_id is None:
        last_id = 1
    else:
        last_id += 1

    products[last_id] = product
    return product


@app.put(
    "/products/{product_id}",
    tags=["produtos"],
    response_model=Product,
    responses={404: {"model": Message}},
)
def update_product(product_id: int, product: Product):
    if product_id not in products:
        return JSONResponse(
            status_code=404,
            content={"message": f"Product with ID {product_id} not found"},
        )

    products[product_id] = product
    return product


@app.delete(
    "/products/{product_id}",
    tags=["produtos"],
    response_model=Message,
    responses={404: {"model": Message}},
)
def delete_product(product_id: int):
    if product_id not in products:
        return JSONResponse(
            status_code=404,
            content={"message": f"Product with ID {product_id} not found"},
        )

    del products[product_id]
    return JSONResponse(
        status_code=202,
        content={"message": f"Product with ID {product_id} was removed sucessfully"},
    )
