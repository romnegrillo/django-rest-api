from django.urls import path

from .views import              \
    ProductListAPIView,         \
    ProductCreateAPIView,       \
    ProductRetrieveAPIView,     \
    ProductListAPIView,         \
    ProductListCreateAPIView,   \
    ProductUpdateAPIView,       \
    ProductDeleteAPIView,       \
    ProductMixinView,           \
    list_create_products
    

urlpatterns = [
    #path("", ProductCreateAPIView.as_view(), name="product-create"), # Replaced by ListCreateAPIView
    #path("all/", ProductListAPIView.as_view()), # Replaced by ListCreateView
   
    path("", ProductListCreateAPIView.as_view()),
    path("<int:pk>/", ProductRetrieveAPIView.as_view()),
    path("update/<int:pk>", ProductUpdateAPIView.as_view()),
    path("delete/<int:pk>", ProductDeleteAPIView.as_view()),
    
    # Testing of function-based equivalent views for:
    # CreateView
    # DetailView
    # ListView
    # path("<int:pk>/", list_create_products, name="product-retrieve"),
    # path("", list_create_products, name="product-list-create"),

    # Testing of mixins using generic api view.
    #path("", ProductMixinView.as_view()),
    #path("<int:pk>/", ProductMixinView.as_view()),
]
