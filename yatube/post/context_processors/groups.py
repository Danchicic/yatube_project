from ..models import Group


def get_groups(request):
    return {"groups": Group.objects.all()}
