from rest_framework import generics, mixins, permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions

from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer
from .permissions import IsStaffEditorPermission

class ProductRetrieveAPIView(generics.RetrieveAPIView):
    """
    RetrieveAPIView allows you to get one record from models.
    By default, the lookup field is called "pk" which is essentially
    the id of your model data.

    Client: GET
    URL: api/products/<int:pk>
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsStaffEditorPermission]


class ProductCreateAPIView(generics.CreateAPIView):
    """
    CreateAPIView allows you to post a data. It will expect a 
    JSON which contains the data needed for the model selected.
    Error handling is handles by the DRF itself.

    Client: POST
    URL: /api/products/
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content")
        if content is None:
            content = "-"

        serializer.save(content=content)


class ProductListAPIView(generics.ListAPIView):
    """
    ListAPIView will return all the records of the model.
    The lookup field is pk by default and it will expect
    a JSON file of the fields neede to be updated.

    Client: GET
    URL: /api/products/update/<int:pk>
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    """
    ListCreateAPIView is the combination of list and create view.
    It will perform list when the client sends a GET request or
    it will perform create then the client sends a POST request
    and also expecting a JSON data.

    Client: GET or POST
    URL: api/products/
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content")

        if content is None:
            content = "-"

        serializer.save(content=content)


class ProductUpdateAPIView(generics.UpdateAPIView):
    """
    UpdateAPIView will update the selected model instance.
    The lookup field is "pk" by default. It will expect
    a JSON data containing the fields to update as well.


    Client: GET
    URL: /api/products/update/<int:pk>
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content")

        if content is None:
            content = "-"

        serializer.save(content="-")


class ProductDeleteAPIView(generics.DestroyAPIView):
    """
    DeleteAPIView will delete the selected model instance.
    The lookup field is "pk" by default. 
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)


class ProductMixinView(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin,
                       generics.GenericAPIView):

    """
    Test of using generic api view along with mixins.
    Not recommended as the code gets convoluted. Just
    for demonstration purposes.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)

        if pk is None:
            return self.list(request, *args, **kwargs)
        else:
            return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


@api_view(["GET", "POST"])
def list_create_products(request, pk=None, *args, **kwargs):
    """
    Function-based version of ListCreateAPIView.
    Class-based views are much more prefered since they
    are declarative. Unlike function-based views that has
    all the logic piled up, making it imperative.

    Client: GET
    URL: /api/products/
    """

    method = request.method

    if method == "GET":
        if pk is not None:
            # Detail View
            queryset = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(queryset, many=False).data
        else:
            # List View.
            queryset = Product.objects.all()
            data = ProductSerializer(queryset, many=True).data

        return Response(data)

    elif method == "POST":
        # Create View.
        # Use request.POST for HttpRequest
        # Use request.data for JSON
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content") or None

            if content is None:
                content = "-"
            serializer.save(content=content)

            return Response(serializer.data)
        else:
            return Response({"Invalid", "Not good data."}, status=400)
