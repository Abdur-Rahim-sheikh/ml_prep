# Software Engineer Interview Questions

## Contents
1. [What are literals in Python?](#what-are-literals-in-python)
2. [Difference between CRUD and RESTful API](#difference-between-crud-and-restful-api)
3. [What is serialization and deserialization? How is it used in Python?](#what-is-serialization-and-deserialization-how-is-it-used-in-python)
4. [Principles to build a RESTful API](#principles-to-build-a-restful-api)
5. [Database sharding](#database-sharding)
6. [Getting 4th highest salary from a table](#getting-4th-highest-salary-from-a-table)

### What are literals in Python?
Literal's in Python is defined as a data which is given in a variable or constant. Python supports the following 5 types of literals:
- String literals -> `"abc"`
- Numeric literals -> `123`
- Boolean literals -> `True` or `False`
- Literal Collections -> `List`, `Tuple`, `Dictionary`, `Set`
- Special literals -> `None`

### Difference between CRUD and RESTful API
- CRUD stands for Create, Read, Update, and Delete. It is a set of operations that can be performed on a resource.
- RESTful API is an architectural style that uses HTTP requests to perform CRUD operations. It is based on the principles of REST (Representational State Transfer).
- CRUD operations are specific actions that can be performed on a resource, while RESTful API is a design pattern that uses HTTP methods to interact with resources.

### What is serialization and deserialization? How is it used in Python?
- Serialization is the process of converting a data structure or object into a format that can be stored or transmitted. It is used to save the state of an object or data structure to a file or memory buffer.
- Deserialization is opposite.
- In python, serializer converts complex data types like Django QuerySets and Models into native Python data types which can be easily rendered into JSON, XML, or other content types.

Extend base serializer

```python
from rest_framework import serializers
from .models import MyModel

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'
```

Use serializer

```python
from .models import MyModel
from .serializers import MyModelSerializer

queryset = MyModel.objects.all()

serializer = MyModelSerializer(queryset, many=True)
print(serializer.data)  
```

### Principles to build a RESTful API
There are several principles to keep in mind when building a RESTful API:
- Use HTTP methods (GET, POST, PUT, DELETE) to perform CRUD operations on resources.
- Client-server architecture: The client and server should be separate entities that communicate through a well-defined interface.
- Stateless: Each request from a client to the server must contain all the information necessary to understand the request, and the server should not store any client state between requests.
- Cacheable: Responses must be explicitly marked as cacheable or non-cacheable.
- Layered system: The client should not be able to tell whether it is connected directly to the end server or an intermediary.
- Uniform interface: This principle simplifies and decouples the architecture, which helps to improve the scalability of the system.
- Code on demand (optional): Servers can temporarily extend or customize the functionality of a client by transferring executable code.

### Database sharding
Database sharding is a method of horizontal partitioning in which rows of a database table are divided into multiple partitions or shards. Each shard is stored on a separate server instance, which allows for parallel processing and improved performance. Sharding is commonly used to distribute the load of a large database across multiple servers, thereby increasing scalability and reducing the risk of data loss. However, sharding can also introduce complexity and potential challenges, such as data consistency and maintenance issues.
complexities:
- Data distribution: Deciding how to distribute data across shards can be complex, especially when dealing with uneven data distribution or changing data access patterns.
- Data consistency: Ensuring data consistency across shards can be challenging, as updates to data may need to be propagated to multiple shards.

### Getting 4th highest salary from a table
```sql
SELECT name, salary FROM employee
WHERE salary = (
    SELECT DISTINCT salary 
    FROM employee 
    ORDER BY salary DESC 
    LIMIT 1 OFFSET 3
);
```

if it's postgresql, we can use rank() function

```sql
SELECT name, salary FROM (
    SELECT name, salary, rank() OVER (ORDER BY salary DESC) as r
    FROM employee
) as emp
WHERE r = 4;
```

postgresql also has more method on `OVER` clause like `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `PERCENT_RANK()`, `CUME_DIST()`, `NTILE()`, `LAG()`, `LEAD()`, `FIRST_VALUE()`, `LAST_VALUE()`, `NTH_VALUE()`