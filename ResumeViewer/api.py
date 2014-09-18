__author__ = 'admin'
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from ResumeViewer.models import Job
from tastypie.authentication import SessionAuthentication
from tastypie.authorization import Authorization
from django.contrib.auth.models import User
from tastypie import fields
from ResumeViewer.api_authorization import AuthorizationByResume


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']

class JobResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
    def obj_create(self, bundle, **kwargs):
        """
        Assign created notes to the current user
        """
        return super(JobResource, self).obj_create(bundle, user=bundle.request.user)
    class Meta:
        authentication = SessionAuthentication()
        authorization = AuthorizationByResume()
        # authorization = Authorization()
        queryset = Job.objects.all()
        resource_name = 'job'
        allowed_methods = ['post', 'get', 'put']
        excludes = ['meta']
        always_return_data = True

