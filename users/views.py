from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView

from methodical_material.models import EduMaterial
from steamcentre.settings import BASE_DIR, MEDIA_ROOT
from .models import Profile, Comment, SubComment


def user_info(request, username):
    if not request.user.is_active or username != request.user.username:
        return redirect('index')

    profile = list(Profile.objects.filter(user_id=request.user.id))
    if profile:
        profile = profile[0]
    else:
        profile = None

    massages = []
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.save()
        if request.FILES:
            if profile:
                try:
                    path_img = profile.img.url.split('/')[-1]
                    BASE_DIR.joinpath(MEDIA_ROOT).joinpath('user_photos').joinpath(path_img).unlink()
                except:
                    pass
                profile.img = request.FILES['img']
                profile.save()

            else:
                Profile.objects.create(user=request.user, img=request.FILES['img'])
            # massages.append('Фото завантажується. Перезавантажте сторінку')

        url_photo = ''
        if profile:
            url_photo = profile.img.url

        massages.append('Дані збережено')
        return render(request, 'users/user_info.html', context={'url_photo': url_photo, 'massages': massages})

    url_photo = None
    try:
        url_photo = profile.img.url
    except:
        url_photo = ''

    return render(request, 'users/user_info.html', context={'url_photo': url_photo, 'massages': massages})


class CommentsAPIView(APIView):
    """
    url: api/v1/edumaterials/<pk_material>/comments/
    method get: get comments of edumaterial pk=pk_material

    url: api/v1/edumaterials/<pk_material>/comments/<pk_comment>
    method get: get comment pk=pk_comment and all its sub_comments
    method post: add into db new comment of material with id=pk_material
    method put: update comment of material with id=pk_material
    body: {"text": "comment text"}
    method delete: delete comment

    url: api/v1/edumaterials/<pk_material>/comments/<pk_comment>/<pk_sub_comment>
    method get: get sub_comment pk=pk_comment
    method post: add into db new sub_comment of comment with id=pk_comment
    method put: update sub_comment of comment with id=pk_comment
    body: {"text": "comment text"}
    method delete: delete sub_comment
    """

    @staticmethod
    def __get_sub_comment(obj, user=None):
        sub_url_img = '/static/img/default/user.jpg'

        try:
            sub_url_img = obj.user.profile.img.url
        except:
            pass

        date = f'{obj.date.day}|{obj.date.month}|{obj.date.year}'

        my_comment = False
        if user:
            my_comment = obj.user.pk == user.pk

        return {
            'id_sub_comments': obj.pk,
            'full_name': obj.user.username + ' ' + obj.user.last_name,
            'url_img': sub_url_img,
            'date': date,
            'text': obj.text,
            'my_comment': my_comment,
        }

    def __get_comment(self, obj, user=None):
        url_img = '/static/img/default/user.jpg'

        try:
            url_img = obj.user.profile.img.url
        except:
            pass

        sub_comments = []
        for sub_comment in SubComment.objects.filter(comment_id=obj.pk):
            sub_comments.append(
                self.__get_sub_comment(sub_comment, user)
            )

        date = f'{obj.date.day}|{obj.date.month}|{obj.date.year}'
        return {
            'id_comments': obj.pk,
            'full_name': obj.user.username + ' ' + obj.user.last_name,
            'url_img': url_img,
            'date': date,
            'text': obj.text,
            'sub_comments': sub_comments,
            'my_comment': obj.user.pk == user.pk,
        }

    def get(self, request, pk_material, pk_comment=None, pk_sub_comment=None):
        if pk_sub_comment:
            try:
                obj = SubComment.objects.get(pk=pk_sub_comment)
                return Response(self.__get_sub_comment(obj, request.user))
            except:
                return Response({'error': 'not fined sub_comment'})

        if pk_comment:
            try:
                obj = Comment.objects.get(pk=pk_comment)
                return Response(self.__get_comment(obj, request.user))
            except:
                return Response({'error': 'not fined comment'})

        lst = []
        for obj in Comment.objects.filter(edu_material_id=pk_material).order_by('-date'):
            lst.append(self.__get_comment(obj, request.user))
        return Response({'comments': lst})

    def post(self, request, pk_material, pk_comment=None):
        if request.user.is_anonymous:
            return Response({'error': 'is_anonymous'})

        # {"text": "comment text"}
        data = request.data
        user = request.user
        text = data.get('text', None)

        if pk_comment:
            try:
                comment = Comment.objects.get(pk=pk_comment)
            except:
                return Response({"error": "Comment pk=pk_comment"})

            SubComment.objects.create(
                text=text,
                user=user,
                comment=comment,
            )
            comment.edu_material.count_comments += 1
            comment.edu_material.save()
            return Response(data)

        try:
            edu_material = EduMaterial.objects.get(pk=pk_material)
        except:
            return Response({"error": "edu_material pk=pk_material"})

        Comment.objects.create(
            edu_material=edu_material,
            user=user,
            text=text
        )
        edu_material.count_comments += 1
        edu_material.save()
        return Response(data)

    def put(self, request, pk_material, pk_comment=None, pk_sub_comment=None):
        # {"text": "comment text"}
        if request.user.is_anonymous:
            return Response({'error': 'is_anonymous'})

        data = request.data
        text = data.get("text", None)
        if pk_sub_comment:
            try:
                sub_comment = SubComment.objects.get(pk=pk_sub_comment)
                if sub_comment.user != request.user:
                    return Response({"error": "user don't have rights"})
                sub_comment.text = text
                sub_comment.save()
                return Response(data)
            except:
                return Response({'error': 'Comment.objects.get(pk=pk_comment)'})
        try:
            comment = Comment.objects.get(pk=pk_comment)
            if comment.user != request.user:
                return Response({"error": "user don't have rights"})
            comment.text = text
            comment.save()
            return Response(data)
        except:
            return Response({'error': 'Comment.objects.get(pk=pk_comment)'})

    def delete(self, request, pk_material, pk_comment, pk_sub_comment=None):
        if request.user.is_anonymous:
            return Response({'error': 'is_anonymous'})

        if pk_sub_comment:
            try:
                sub_comment = SubComment.objects.get(pk=pk_sub_comment)
                if sub_comment.user != request.user:
                    return Response({"error": "user don't have rights"})
                sub_comment.comment.edu_material.count_comments -= 1
                sub_comment.comment.edu_material.save()
                sub_comment.delete()
                return Response({'sub_comment': 'deleted_comment'})
            except:
                return Response({'error': 'Comment.objects.get(pk=pk_comment)'})
        try:
            comment = Comment.objects.get(pk=pk_comment)
            if comment.user != request.user:
                return Response({"error": "user don't have rights"})
            comment.edu_material.count_comments -= 1 + comment.subcomment_set.count()
            comment.edu_material.save()
            comment.delete()
            return Response({'comment': 'deleted_comment'})
        except:
            return Response({'error': 'Comment.objects.get(pk=pk_comment)'})


class ProfileAPIView(APIView):
    def get(self, request):
        query_profile = Profile.objects.filter(user_id=request.user.id)
        if query_profile:
            profile = query_profile[0]
            query_collection_material = profile.collection_material.filter()
            context = {
                'collection_materials_id': [obj.pk for obj in query_collection_material]
            }

            return Response(context)
        return Response({'error': 'is not authorization'})

    def put(self, request):
        if request.user.is_anonymous:
            return Response({'error': 'is_anonymous'})

        if not hasattr(request.user, 'profile'):
            Profile.objects.create(user=request.user)

        def add_or_remove(material, all_material, profile_property):
            if material in all_material:
                profile_property.remove(material)
                return False
            profile_property.add(material)
            return True

        profile = request.user.profile

        pk = request.data.get('favorite_id', None)
        key_d = 'favorite_id'
        if not pk:
            pk = request.data.get('like_id', None)
            key_d = 'like_id'

        try:
            material = EduMaterial.objects.get(pk=pk)
        except:
            return Response({'error': 'error pk'})

        all_material = profile.collection_material.all() if key_d == 'favorite_id' else profile.liked.all()
        profile_property = profile.collection_material if key_d == 'favorite_id' else profile.liked
        is_add = add_or_remove(material, all_material, profile_property)
        if key_d == 'like_id':
            if is_add:
                material.like += 1
            else:
                material.like -= 1
            material.save()

        return Response({'response': 'good'})
