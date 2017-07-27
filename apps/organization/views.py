from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.db.models import Q

from .models import CourseOrg, CityDict, Teacher

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .forms import  UserAskForm
from courses.models import Course
from operation.models import UserFavorite
from courses.models import Course

class OrgView(View):
    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        hot_orgs = all_orgs.order_by('-click_num')[:3]
        all_cities = CityDict.objects.all()

        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            all_orgs = all_orgs.filter(Q(name__icontains=search_keywords) | Q(desc__icontains=search_keywords))

        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        category = request.GET.get('ct', '')
        if category:
            all_orgs = all_orgs.filter(category=category)

        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_orgs = all_orgs.order_by('-students')
            elif sort == 'courses':
                all_orgs = all_orgs.order_by('-course_nums')
            else:
                all_orgs = all_orgs.order_by('id')

        org_nums = all_orgs.count()
        # Paginate for Organization
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs, 3, request=request)
        orgs = p.page(page)

        return render(request, 'org-list.html', {
            'all_orgs': orgs,
            'all_cities': all_cities,
            'org_nums': org_nums,
            'city_id': city_id,
            'category': category,
            'hot_orgs': hot_orgs,
            'sort': sort
        })


class AddUserAskView(View):
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            userask_form.save(commit=True)
            return HttpResponse("{'status':'success'}")
        else:
            return HttpResponse("{'status':'fail', 'msg':'errors!!'}")


class OrgHomeView(View):
    def get(self, request, org_id):
        current_page = 'home'
        course_org = CourseOrg.objects.get(id=int(org_id))
        course_org.click_num += 1
        course_org.save()
        # Verify liked or not
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True

        all_courses = course_org.course_set.all()[:3]
        all_teachers = course_org.teacher_set.all()[:1]
        return render(request, 'org-detail-homepage.html', {
            'all_courses': all_courses,
            'all_teachers': all_teachers,
            'course_org': course_org,
            'current_page': current_page,
            'has_fav': has_fav
        })


class OrgCourseView(View):
    def get(self, request, org_id):
        current_page = 'course'
        course_org = CourseOrg.objects.get(id=int(org_id))

        # Verify liked or not
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True

        all_courses = course_org.course_set.all()
        return render(request, 'org-detail-course.html', {
            'all_courses': all_courses,
            'course_org': course_org,
            'current_page': current_page,
            'has_fav': has_fav
        })


class OrgDescView(View):
    def get(self, request, org_id):
        current_page = 'desc'
        course_org = CourseOrg.objects.get(id=int(org_id))

        # Verify liked or not
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True

        return render(request, 'org-detail-desc.html', {
            'course_org': course_org,
            'current_page': current_page,
            'has_fav': has_fav
        })


class OrgTeacherView(View):
    def get(self, request, org_id):
        current_page = 'teacher'
        course_org = CourseOrg.objects.get(id=int(org_id))

        # Verify liked or not
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True

        all_teachers = course_org.teacher_set.all()
        return render(request, 'org-detail-teachers.html', {
            'all_teachers': all_teachers,
            'course_org': course_org,
            'current_page': current_page,
            'has_fav': has_fav
        })


class AddFavView(View):
    def post(self, request):
        fav_id = request.POST.get('fav_id', 0)
        fav_type = request.POST.get('fav_type', 0)

        if not request.user.is_authenticated():
            return HttpResponse("{'status':'fail', 'msg':'NotLogin'}")

        exist_record = UserFavorite.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
        if exist_record:
            exist_record.delete()
            if int(fav_type) == 1:
                course = Course.objects.get(id=int(fav_id))
                course.fav_nums -= 1
                if course.fav_nums < 0:
                    course.fav_nums = 0
                course.save()
            elif int(fav_type) == 2:
                course_org = CourseOrg.objects.get(id=int(fav_id))
                course_org.fav_nums -= 1
                if course_org.fav_nums < 0:
                    course_org.fav_nums = 0
                course_org.save()
            elif int(fav_type) == 3:
                teacher = Teacher.objects.get(id=int(fav_id))
                teacher.fav_nums -= 1
                if teacher.fav_nums < 0:
                    teacher.fav_nums = 0
                teacher.save()

            return HttpResponse("{'status':'success', 'msg':'like'}")
        else:
            user_fav = UserFavorite()
            if int(fav_id) > 0 and int(fav_type) > 0:
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.save()

                if int(fav_type) == 1:
                    course = Course.objects.get(id=int(fav_id))
                    course.fav_nums += 1
                    course.save()
                elif int(fav_type) == 2:
                    course_org = CourseOrg.objects.get(id=int(fav_id))
                    course_org.fav_nums += 1
                    course_org.save()
                elif int(fav_type) == 3:
                    teacher = Teacher.objects.get(id=int(fav_id))
                    teacher.fav_nums += 1
                    teacher.save()

                return HttpResponse("{'status':'success', 'msg':'dislike'}")
            else:
                return HttpResponse("{'status':'fail', 'msg':'like_error'}")


class TeacherListView(View):
    def get(self, request):
        all_teachers = Teacher.objects.all()

        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            all_teachers = all_teachers.filter(Q(name__icontains=search_keywords) |
                                               Q(work_company__icontains=search_keywords) |
                                               Q(work_position__icontains=search_keywords))

        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'hot':
                all_teachers = all_teachers.order_by('-click_num')

        sorted_teacher = Teacher.objects.all().order_by('-click_num')[:3]

        # Paginate for Teacher
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_teachers, 2, request=request)
        teachers = p.page(page)

        return render(request, 'teachers-list.html', {
            'all_teachers': teachers,
            'sorted_teacher': sorted_teacher,
            'sort': sort,
        })


class TeacherDetailView(View):
    def get(self,request, teacher_id):
        teacher = Teacher.objects.get(id=int(teacher_id))
        teacher.click_num += 1
        teacher.save()
        all_courses = Course.objects.filter(teacher=teacher)

        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_type=3, fav_id=teacher.id):
                has_teacher_fav = True
        else:
            has_teacher_fav = False

        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_type=2, fav_id=teacher.org.id):
                has_org_fav = True
        else:
            has_org_fav = False

        sorted_teacher = Teacher.objects.all().order_by('-click_num')[:3]
        return render(request, 'teacher-detail.html', {
            'teacher': teacher,
            'all_courses': all_courses,
            'sorted_teacher': sorted_teacher,
            'has_teacher_fav': has_teacher_fav,
            'has_org_fav': has_org_fav
        })
