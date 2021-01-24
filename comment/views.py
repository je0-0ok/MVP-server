import json
from .models        import Comment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CommentSerializer

# @method_decorator(csrf_exempt, name='dispatch')
class CommentView(APIView):
    def post(self, request):
        comment_serializer = CommentSerializer(data=request.data)

        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response(comment_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def get(self, request, **kwargs):
        comment_queryset = Comment.objects.all()
        comment_serializer = CommentSerializer(comment_queryset, many=True)
        return Response(comment_serializer.data, status=status.HTTP_200_OK)