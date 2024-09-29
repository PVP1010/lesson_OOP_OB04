# Рассмотрим пример кода без использования данного принципа Чтобы понять разницу в кодах,
# для начала рассмотрим пример без использования принципа единственной ответственности.

class UserManager():
    def __init__(self, user):
        self.user = user
    def change_user_name(self, user_name):
        self.user = user_name
    def save_user(self) :
        file = open("users.txt", "a")
        file.write(self.user)
        file.close()

# Теперь сделаем это правильно, с соблюдением принципа единственной ответственности:

class User():
    def __init__(self, user):
        self.user = user

class UserNameChanger():
    def __init__(self, user):
        self.user = user
    def change_name(self, new_name):
        self. user = new_name

class SaveUser():
    def __init(self, user):
        self.user = user
    def save(self):
        file = open("users.txt", "a")
        file.write(self.user)
        file.close()


# В итоге у нас получилось несколько отдельных классов, каждый из которых занимается тем,
# чем ему нужно. Это один из самых простых принципов, который мы можем внедрить с самого начала
# работы над программами. Вообще все эти принципы направлены на то, чтобы обеспечить возможность
# дальнейшего развития, модернизации и расширения кода в будущем.