from django.contrib.auth.backends import ModelBackend
from study07.models import MyUser


class MyBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # 找用户
        #  做验证密码

        # 找人
        user = None
        try:
            user = MyUser.objects.get(username=username)
            print(user)
        except:
            try:
                user = MyUser.objects.get(phone=username)
            except:
                try:
                    user = MyUser.objects.get(email=username)
                except:
                    return None
        if user.check_password(password):
            print(user)
            return user
        else:
            return None