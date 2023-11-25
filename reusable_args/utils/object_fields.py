import graphene


class FieldWithArgs(graphene.Field):
    """
    Class with common (reusable) arguments.
    """

    def __init__(
            self,
            type_,
            args=None,
            resolver=None,
            source=None,
            deprecation_reason=None,
            name=None,
            description=None,
            required=False,
            _creation_counter=None,
            default_value=None,
            **extra_args
        ):
        """
        Field that adds the `search_keyword` argument to a query.
        """

        extra_args["search_keyword"] = graphene.String(
            required=False,
            default_value=None,
            description="Search phrase."
        )

        super().__init__(
            type_,
            args,
            resolver,
            source,
            deprecation_reason,
            name,
            description,
            required,
            _creation_counter,
            default_value,
            **extra_args
        )
