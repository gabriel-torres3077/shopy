# shopy
API preview: 
![projectpreview](/preview/api_preview.png)</br>
Guide:
- [Install](#install)
- [shopy API](#shopy-api)
    - [Product](#product)
        - [Create Product](#create-product)
            - [Create Product Request](#create-product-request)
            - [Create Product Response](#create-product-response)
        - [Get Product](#get-product)
            - [Get Product Request](#get-product-request)
            - [Get Product Response](#get-product-response)
        - [Update Product](#update-product)
            - [Update Product Request](#update-product-request)
            - [Update Product Response](#update-product-response)
        - [Delete Product](#delete-product)
            - [Delete Product Request](#delete-product-request)
            - [Delete Product Response](#delete-product-response)
    - [Order](#order)
        - [Create Order](#create-order)
            - [Create Order Request](#create-order-request)
            - [Create Order Response](#create-order-response)
        - [Get Order](#get-order)
            - [Get Order Request](#get-order-request)
            - [Get Order Response](#get-order-response)
        - [Update Order](#update-order)
            - [Update Order Request](#update-order-request)
            - [Update Order Response](#update-order-response)
        - [Delete Order](#delete-order)
            - [Delete Order Request](#delete-order-request)
            - [Delete Order Response](#delete-order-response)

# Install
## Requirements
* [Docker](https://docs.docker.com)

## Instalation guide

- after setup your environment run 
```shell
docker-compose up -d
```
- create a super user with docker
```shell
docker-compose run --rm app sh -c "python manage.py createsuperuser"
username: (your username)
Email address: (your email)
Password: (your password)
Password (again): (Confirm password)
```
- access the api with the docker desktop app-1 port or by the direct link [here](http://localhost:8000/api/product/)
![Docker container](/preview/docker_preview.png)

# User
## Create Product

### Create Product Request

```js
POST /api/product
```

```json
{
    "name": "God of war 2018",
    "price": "250.00",
    "score": 89,
    "image": "img.jpg" // file
}
```

### Create Product Response

```js
201 Created
```

## Get Product

### Get Product Request

```js
GET /api/product/{{id}}
```

### Get Product Response

```js
200 Ok
```

```json
{
    "id": 1,
    "name": "God of war 2018",
    "price": "250.00",
    "score": 89,
    "image": "/games/img.jpg"
}
```

## Update Product

### Update Product Request

```js
PUT /api/product/{{id}}
```

```json
{
    "id": 1,
    "name": "God of war 2020", // change
    "price": "250.00",
    "score": 89,
    "image": "img.jpg" // file
}
```

### Update Product Response

```js
200 OK
```

```yml
Location: {{host}}api/product/{{id}}
```

## Delete Product

### Delete Product Request

```js
DELETE /api/product/{{id}}
```

### Delete Product Response

```js
204 No Content
```

# Order
## Create Order

### Create Order Request

```js
POST /api/orders/  
```

```json
{
    "user": 1,
    "checkout": false,
    "products": [
        4,
        5
    ],
}
```

### Create Order Response

```js
201 Created
```

## Get Role

### Get Role Request

```js
GET /api/order/{{id}}
```

### Get Order Response

```js
200 Ok
```

```json
{
    "id": 1,
    "user": 1,
    "checkout": false,
    "products": [
        4,
        5
    ],
    "freight": "20.00",
    "total": "234.00"
}
```

## Update Order

### Update Order Request

```js
PUT /api/order/{{id}}
```

```json
{
    "id": 6,
    "user": 1,
    "checkout": false,
    "products": [
        4,
    ]
}
```

### Update Order Response

```js
200 OK
```

```yml
Location: {{host}}api/order/{{id}}
```

## Delete Order

### Delete Order Request

```js
DELETE /api/order/{{id}}
```

### Delete Order Response

```js
204 No Content
```
