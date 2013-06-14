# Create your views here.
import xzjmt
def global_context(request):
    c = {
         'wwwroot':xzjmt.settings.WWW_ROOT,
         'cssroot':xzjmt.settings.CSS_ROOT,
         'jsroot':xzjmt.settings.JS_ROOT,
         'imgroot':xzjmt.settings.IMG_ROOT,
        }
    return c