GrapQL Concepts




In order to make queries to our Django project, we are going to need few things:

*Schema with defined object types
*A view, taking queries as input and returning the result


GraphQL presents your objects to the world as a **graph** structure rather than a more hierarchical structure in REST. 
In order to create this representation, Graphene needs to know about each **type of object** which will appear in the graph.


This graph also has a **root type** through which all access begins. This is the Query class.


To create GraphQL types for each of our Django models, we are going to *subclass the DjangoObjectType class* which will automatically define GraphQL fields that correspond to the fields on the Django models, much similar to serializers in DRF.


After we’ve done that, we will list those types as fields in the Query class.


Getting Relationships

````

query {
  categoryByName(name: "Dairy") {
    id
    name
    ingredients {
      id
      name
    }
  }
}

´´´
