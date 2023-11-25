import graphene

from .utils import FieldWithArgs

FRUITS = [
    {"id": 1, "name": "Guava"},
    {"id": 2, "name": "Peach"},
    {"id": 3, "name": "Orange"},
    {"id": 4, "name": "Papaya"},
    {"id": 5, "name": "Pineapple"},
]

class FruitType(graphene.ObjectType):
    """
    `FruitType`
    """

    id = graphene.Int()
    name = graphene.String()

    def resolve_id(self, info):
        return self.get("id")
    
    def resolve_name(self, info):
        return self.get("name")


class GreetingsQuery(graphene.ObjectType):
    """
    Test the GraphQL service by saying hello.
    """

    hello = graphene.String(
        name=graphene.String(default_value="World"),
        description="Optional recipient of the greetings.",
    )
    ping = graphene.String()

    def resolve_hello(self, info, name):
        """
        Say hello.
        -------
        Parameters:
        name : Optional recipient of the greetings. Default: "World".
        """

        return "Hello, " + name

    def resolve_ping(self, info):
        """
        Ping pong.
        """

        return "pong"


class QueryWithReusableArgs(graphene.ObjectType):
    records_reusable = FieldWithArgs(
        graphene.List(FruitType),
    )

    def resolve_records_reusable(self, info, search_keyword):
        records = FRUITS

        if search_keyword:
            records = [
                fruit
                for fruit in FRUITS
                if search_keyword.lower() in fruit.get("name").lower()
                or search_keyword.lower() == fruit.get("name").lower()
            ]
        
        return records

class ApiQuery(
    GreetingsQuery,
    QueryWithReusableArgs,
):
    """
    Class that "houses" all queries defined in the application.
    To add your query to the schema, inherit it in this class declaration.
    For example:

    ```
    class ApiQuery(YourQueryClass):
        pass
    ```
    """

    pass

demo_schema = graphene.Schema(query=ApiQuery)
