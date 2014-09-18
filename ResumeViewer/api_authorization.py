__author__ = 'Waz'
from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized


class AuthorizationByResume(Authorization):
    def read_list(self, object_list, bundle):
        author = bundle.request.user
        return object_list.filter(user=bundle.request.user)

    def read_detail(self, object_list, bundle):
        print('bananas')
        return bundle.obj.owner.author == bundle.request.user

    def create_list(self, object_list, bundle):
        raise Unauthorized()

    def create_detail(self, object_list, bundle):
        print('create det in progress')
        return bundle.obj.user == bundle.request.user

    def update_list(self, object_list, bundle):
        allowed = []

        # Since they may not all be saved, iterate over them.
        for obj in object_list:
            if obj.user == bundle.request.user:
                allowed.append(obj)

        return allowed


    def update_detail(self, object_list, bundle):
        print('updD')
        return bundle.obj.user == bundle.request.user

    def delete_list(self, object_list, bundle):
        print('aasdf')
        raise Unauthorized("Sorry, no deletes.")

    def delete_detail(self, object_list, bundle):
        print('deldet')
        raise Unauthorized("Sorry, no deletes.")
