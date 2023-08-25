from django.views import View
from django.http import JsonResponse

from rest_framework import status
from rest_framework.response import Response # Not woring with View
from rest_framework.views import APIView # Not woring properly : for get kwargs is {}

from .models import BenefitsModel
from . serializers import BenefitsModelSerializer
from ..program_module.models import ProgramModel


class BenefitView(View):
    def get(self, request, *args, **kwargs):
        _id = request.GET.get('id')
        if _id:
            try:
                benefit = BenefitsModel.objects.get(id=_id)
                serializer = BenefitsModelSerializer(benefit)
                context = {"success": True, "data": serializer.data}
                return JsonResponse(context, status=status.HTTP_200_OK)
            except:
                context = {"success": False, "msg": "Please give valid benefit id."}
                return JsonResponse(context, status=status.HTTP_404_NOT_FOUND)
            
        context = {"success": False, "msg": "Please give benefit id."}
        return JsonResponse(context, status=status.HTTP_400_BAD_REQUEST)


    def post(self, request, *args, **kwargs):
        serializer = BenefitsModelSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            context = {"success": True, "msg": "Benefit addedd successfully..!", "data": serializer.data}
            return JsonResponse(context, status=status.HTTP_201_CREATED)
        else:
            context = {"success": False, "msg": "Benefit addedd failed..!", "error": serializer.errors}
        return JsonResponse(context, status=status.HTTP_400_BAD_REQUEST)


class BenefitGetView(View):
    def get(self, request, *args, **kwargs):
        get_benefits_by = request.GET.get("get_benefits_by")
        benefits = None
        if get_benefits_by == 'all':
            benefits = BenefitsModel.objects.all()
        elif get_benefits_by == 'program' and request.GET.get('program_id'):
            program_id = request.GET.get('program_id')
            benefits = BenefitsModel.objects.filter(program_id=program_id)
        else:
            context = {"success": False,"msg": "Invalid get_benefits_by."}
            return JsonResponse(context, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = BenefitsModelSerializer(benefits, many=True)
        context = {"success": True, "data": serializer.data}
        return JsonResponse(context, status=status.HTTP_200_OK)
    

class BenefitRunView(View):
    def get(self, request, *args, **kwargs):
        # program_id = request.GET.get("program_id")
        # benefits_id = request.GET.get("benefits_id")

        # if program_id:
        #     program = ProgramModel.objects.filter(id=program_id).first()
        #     if program:
        #         prog_data = {
        #             "program_id": program.id,
        #             "short_code": program.short_code,
        #             "program_name": program.program_name
        #         }

        
        # program=ProgramModel.objects.filter(benefits__short_code='teleconsultation-benefit')
        # print("program by benefit short code", program)

        program=ProgramModel.objects.get(id=2)
        print("programs all benefits", program.benefits.all())

        # benefit = BenefitsModel()
        # benefit.short_code = "fourth-benefit"
        # benefit.label = "Fourth-Consultation"
        # benefit.benefit_type = "other"
        # benefit.benefit_category = "free"
        # benefit.program = ProgramModel.objects.get(id=2)
        # benefit.save()

        # print(benefit)


        return JsonResponse({"success": True}, status=status.HTTP_200_OK)



        
        
        # serializer = BenefitsModelSerializer(benefits, many=True)
        # context = {"success": True, "data": serializer.data}
        # return JsonResponse(context, status=status.HTTP_200_OK)
