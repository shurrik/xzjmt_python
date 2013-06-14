# Create your views here.
import xzjmt
def global_context(request):
    return {'WWW_ROOT':xzjmt.settings.WWW_ROOT}