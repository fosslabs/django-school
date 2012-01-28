from django import template

register = template.Library()

@register.filter
def list_to_int(value):
    ans = []
    for i in value:
        ans.append(int(i))
    return ans

@register.filter
def to_int(value):
    return int(value)

@register.filter
def get_item0(value, arg):
    return value[arg-1]

@register.filter
def get_item(value, arg):
    return value[arg]

@register.filter
def get_radio_item(value, arg):
    ans = value.get("q"+str(arg), -1)
    return int(ans)

@register.filter
def get_checkbox_item(value, arg):
    ans = value.getlist("q"+str(arg))
    ans1 = []
    for i in ans:
        ans1.append(int(i))
    return ans1

@register.filter
def get_text_item(value, arg):
    ans = value.get("q"+str(arg), "")
    return ans

@register.filter
def get_last_item(queryset):
    return queryset[queryset.count()-1]

@register.filter
def lines(value):
    return value.splitlines()

@register.filter
def split(value, sep):
    return value.split(sep)

@register.filter
def material(value):
    file_type = value[-3:]
    if file_type == "pdf":
        return file_type
    elif file_type == "ppt":
        return "pptx"
    elif file_type == "ptx":
        if value[-4:] == "pptx":
            return "pptx" 
    else:
        return "file"
