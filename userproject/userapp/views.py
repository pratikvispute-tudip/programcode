from django.shortcuts import render
from userapp.forms import UserForm,UserLogin
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from userapp.models import UserProfile
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.base import TemplateView

# Create your views here.
class UserFormView(View):
	form_class = UserForm
	template_name = 'registrationform.html'
	registered=False
	

	def get(self, request, *args, **kwargs):
		form = self.form_class()
		registered=False
		return render(request, self.template_name, {'form': form,'registered':registered})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		registered=False
		alreadyregistered=False
		if form.is_valid():
			uname = request.POST['username']
			emailid = request.POST['emailid']


			try:
				user = UserProfile.objects.get(username=uname, emailid=emailid)
				if user:
					# return HttpResponse("Already registered")
					alreadyregistered=True
					registered= False
			except ObjectDoesNotExist:
				form.save()
				registered=True
				alreadyregistered=False



		return render(request,self.template_name,{'form':form,'registered':registered,'alreadyregistered':alreadyregistered})

class UserLoginView(View):
	form_class = UserLogin
	template_name = 'userlogin.html'
	

	def get(self,request,*args,**kwargs):
		print"--------Session-------",request.session.__dict__

		if request.session.has_key("u_id"):
			self.template_name = "dashboard.html" , 
			print request.session["u_id"], "++++++++++++==="
		else:
			print "------NBO SESSION FOUND------", 

		form = self.form_class()
		return render(request,self.template_name,{'form':form})

	def post(self,request,*args,**kwargs):
		form = self.form_class(request.POST)
		print "-------", request.POST['password']
		uname = request.POST['username']
		pword = request.POST['password']

		u=UserProfile.objects.get(username=request.POST['username'])


		# user = authenticate(username=uname, password=pword)
		try:
			user = UserProfile.objects.get(username=uname, password=pword)
		except ObjectDoesNotExist:
			return HttpResponse("Login Failed")



		print user, "!!!!!!!!!!!!!!!!"

		if user:
			# if user.is_active:
			# 	login(request, user)
			# return HttpResponse("Login successful")
			if u.password==request.POST['password']:
				 request.session['u_id'] = u.id
				 print "@@@@@@@@@@@@@@@@",request.session['u_id']
				 return HttpResponseRedirect("/dashboard/")
			# else:
			# 	return HttpResponse("Your account is disabled.")
		else:
			# print "Invalid login details: {0}, {1}".format(uname, pword)
			return HttpResponse("Invalid login details supplied.")
		return render(request,self.template_name,{'form':form})

class DashboardView(TemplateView):
	template_name="dashboard.html"

class logoutView(View):
	template_name="logout.html"
	def get(self, request, *args, **kwargs):
		try:
			del request.session['u_id']
		except KeyError:
			pass
		return render(request, self.template_name, {})

